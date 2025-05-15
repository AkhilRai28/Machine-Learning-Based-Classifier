import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

import 'theme.dart';
import 'screens/home_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Example of secure init flag — you can store user prefs here.
  final storage = FlutterSecureStorage();
  await storage.write(key: 'app_initialized', value: 'true');

  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Music Genre Classifier',
      theme: AppTheme.themeData,
      home: HomeScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}
