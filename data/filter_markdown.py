def filter_navigation_sections(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content into sections
    sections = content.split('## Menu nawigacyjne')
    
    # Take only the content parts (even indices, as odd indices are navigation sections)
    filtered_content = sections[0]  # First part before any navigation
    for section in sections[1:]:
        # Find the next heading or separator after navigation section
        content_start = section.find('##')
        if content_start == -1:
            content_start = section.find('---')
        
        if content_start != -1:
            filtered_content += section[content_start:]
    
    # Write filtered content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(filtered_content)

if __name__ == "__main__":
    input_file = "data/output.md"
    output_file = "data/filtered_output.md"
    filter_navigation_sections(input_file, output_file)
    print(f"Filtered content saved to {output_file}") 