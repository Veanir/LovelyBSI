import 'dart:convert';
import 'dart:io';
import 'package:flutter/services.dart' show rootBundle;
import 'package:path_provider/path_provider.dart';
import '../models/question.dart';
import '../services/network_service.dart';

class QuestionRepository {
  final NetworkService _networkService = NetworkService();

  Future<List<Question>> loadQuestions() async {
    try {
      final file = await _getLocalFile();
      if (await file.exists()) {
        final jsonString = await file.readAsString();
        final jsonData = json.decode(jsonString);
        return _parseQuestions(jsonData);
      } else {
        return await _loadFromAssets();
      }
    } catch (e) {
      print('Error loading questions from local file: $e');
      return await _loadFromAssets();
    }
  }

  Future<List<Question>> _loadFromAssets() async {
    final jsonString = await rootBundle.loadString('assets/questions.json');
    final jsonData = json.decode(jsonString);
    return _parseQuestions(jsonData);
  }

  List<Question> _parseQuestions(dynamic jsonData) {
    final questions = (jsonData as List)
        .map((question) => Question.fromJson(question))
        .toList();
    for (var question in questions) {
      question.answers.shuffle();
    }
    return questions;
  }

  Future<void> saveStarredQuestions(List<Question> questions) async {
    final starredQuestionIds =
        questions.where((q) => q.isStarred).map((q) => q.questionId).toList();
    final file = await _getLocalFile('starred_questions.json');
    await file.writeAsString(json.encode(starredQuestionIds));
  }

  Future<List<int>> _loadStarredQuestions() async {
    try {
      final file = await _getLocalFile('starred_questions.json');
      if (await file.exists()) {
        final jsonString = await file.readAsString();
        return (json.decode(jsonString) as List).cast<int>();
      }
    } catch (e) {
      print('Error loading starred questions: $e');
    }
    return [];
  }

  Future<File> _getLocalFile([String fileName = 'questions.json']) async {
    final directory = await getApplicationDocumentsDirectory();
    return File('${directory.path}/$fileName');
  }

  Future<void> syncQuestions() async {
    try {
      final jsonData = await _networkService.fetchQuestions();
      final file = await _getLocalFile();
      await file.writeAsString(json.encode(jsonData));
      print('Questions synced successfully');
    } catch (e) {
      print('Error syncing questions: $e');
    }
  }
}
