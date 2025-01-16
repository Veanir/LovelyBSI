import 'dart:convert';
import 'package:http/http.dart' as http;

class NetworkService {
  final String _questionsUrl = 'https://gist.githubusercontent.com/Veanir/69461bc1e4c67f0f6721b448e0cf1cec/raw/e8034c8b40fc659daac777220bf13f6a27b98c68/questions.json'; // Replace with your direct download link

  Future<List<dynamic>> fetchQuestions() async {
    try {
      final response = await http.get(Uri.parse(_questionsUrl));

      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Failed to load questions: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Failed to load questions: $e');
    }
  }
} 