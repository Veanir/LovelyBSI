import json
import google.generativeai as genai
from dotenv import load_dotenv
import os
import multiprocessing
import re
import argparse
import time
import random

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def load_academic_content(file_path):
    """Load the academic content from the markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def generate_explanation(question, academic_content, model):
    """Generate explanation for a question using academic content as context."""
    prompt = f"""
    You are an expert in cybersecurity education. Your task is to analyze and explain a multiple-choice question.
    Use the provided academic content as background knowledge, but your explanation should stand on its own.

    Here is the academic content for your background knowledge:

    <academic_content>
    {academic_content}
    </academic_content>

    Here is the question to analyze and explain:

    <question_data>
    {{
        "questionId": {question['questionId']},
        "title": "{question['title']}",
        "answers": [
    """
    for answer in question['answers']:
        prompt += f"""
            {{
                "text": "{answer['text']}",
                "isCorrect": {str(answer['isCorrect']).lower()}
            }},
         """
    prompt += """
        ]
    }}
    </question_data>

    First, analyze the question in English (wrap in <analysis> tags):
    - What core cybersecurity concept is being tested?
    - What knowledge and understanding is required to answer this correctly?
    - Are there any technical terms, commands, or tools that need explanation?
    - What common misconceptions might students have about this topic?
    - What real-world implications or scenarios are relevant?
    - How do the incorrect answers relate to the correct one(s)?
    - What's the pedagogical value of this question?

    Then, provide a comprehensive explanation in Polish (wrap in <explanation> tags). Your explanation MUST:

    1. Start DIRECTLY with the core technical concept explanation - NO introductory meta-text about what the question tests
       - Jump straight into explaining the technical concept, tool, or command
       - Define any technical terms as you use them
       - Explain configurations or parameters when they appear

    2. For each answer option:
       - Explain why it is correct or incorrect
       - For commands/tools, explain their effects
       - For concepts, explain their applicability
       - Include practical implications

    3. Use concrete examples that show real-world application
       - Demonstrate cause-and-effect
       - Show practical implications

    Your explanation must:
    - Be self-contained
    - Be detailed but concise
    - Use clear, precise language
    - Focus on practical understanding
    - Help build a mental model
    - AVOID meta-commentary about the question itself
    """

    max_retries = 5
    base_delay = 1
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            if "429" in str(e):
                delay = (base_delay * (2 ** attempt) + random.uniform(0, 1))
                print(f"Rate limit hit. Retrying in {delay:.2f} seconds... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(delay)
            else:
                print(f"Error generating explanation: {e}")
                return None
    print(f"Failed to generate explanation after {max_retries} retries.")
    return None

def process_question(args):
    """Process a single question with academic content."""
    question, academic_content, model = args
    
    with lock:
        print(f"Processing question {question['questionId']}: {question['title']}")
    
    explanation = generate_explanation(question, academic_content, model)
    
    if explanation:
        # Extract only the explanation, ignore analysis
        explanation_match = re.search(r"<explanation>(.*?)</explanation>", explanation, re.DOTALL)
        question['explanation'] = explanation_match.group(1).strip() if explanation_match else "Nie udało się wygenerować wyjaśnienia."
        
        with lock:
            print(f"Completed question {question['questionId']}")
    else:
        question['explanation'] = "Nie udało się wygenerować wyjaśnienia."
    
    return question

def init_lock(l):
    """Initialize the lock for multiprocessing."""
    global lock
    lock = l

def analyze_questions(questions_file, academic_file, output_file, question_id=None, num_workers=None, verbose=False):
    """Analyze questions using academic content with multiprocessing."""
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in .env file.")

    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    
    # Load academic content
    academic_content = load_academic_content(academic_file)
    if verbose:
        print("Loaded academic content")
    
    # Load questions
    with open(questions_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    # Filter for specific question if ID provided
    if question_id is not None:
        questions = [q for q in questions if q['questionId'] == question_id]
        if not questions:
            raise ValueError(f"Question with ID {question_id} not found in the questions file")
    
    if verbose:
        print(f"Processing {len(questions)} question{'s' if len(questions) > 1 else ''}")
    
    # Initialize multiprocessing
    lock = multiprocessing.Lock()
    
    # Determine number of workers with proper type handling
    cpu_count = os.cpu_count() or 1  # Default to 1 if cpu_count returns None
    if num_workers is None:
        num_workers = cpu_count
    else:
        num_workers = min(num_workers, cpu_count)
    
    if verbose:
        print(f"Using {num_workers} worker processes")
    
    # Process questions in parallel
    with multiprocessing.Pool(processes=num_workers, initializer=init_lock, initargs=(lock,)) as pool:
        # Create arguments for each question
        args = [(question, academic_content, model) for question in questions]
        # Process questions in parallel
        results = pool.map(process_question, args)
    
    # Save results
    with open(output_file, 'w', encoding='utf-8') as f:
        # If processing single question, save just that question
        if question_id is not None:
            json.dump(results[0], f, indent=4, ensure_ascii=False)
        else:
            json.dump(results, f, indent=4, ensure_ascii=False)
    
    if verbose:
        print(f"Results saved to {output_file}")
    return results

def parse_args():
    parser = argparse.ArgumentParser(description='Analyze cybersecurity questions and generate explanations using AI.')
    parser.add_argument('-q', '--questions', 
                        default='data/questions.json',
                        help='Path to the JSON file containing questions (default: data/questions.json)')
    parser.add_argument('-a', '--academic', 
                        default='data/filtered_output.md',
                        help='Path to the markdown file containing academic content (default: data/filtered_output.md)')
    parser.add_argument('-o', '--output', 
                        default='data/explained_questions.json',
                        help='Path where to save the output JSON (default: data/explained_questions.json)')
    parser.add_argument('-i', '--id',
                        type=int,
                        help='Process only the question with this ID')
    parser.add_argument('-w', '--workers', 
                        type=int,
                        help='Number of worker processes (default: CPU count)')
    parser.add_argument('-v', '--verbose', 
                        action='store_true',
                        help='Enable verbose output')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    analyze_questions(
        questions_file=args.questions,
        academic_file=args.academic,
        output_file=args.output,
        question_id=args.id,
        num_workers=args.workers,
        verbose=args.verbose
    )
