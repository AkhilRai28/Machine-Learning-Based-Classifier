import 'package:flutter/material.dart';

class AppTheme {
  // Primary purple
  static const Color primaryPurple = Color(0xFF6A1B9A);
  // A slightly lighter accent
  static const Color accentPurple = Color(0xFF8E24AA);
  // A darker purple for backgrounds
  static const Color darkPurple = Color(0xFF4A148C);

  static final TextTheme textTheme = TextTheme(
    // headlineLarge replaces headline1
    headlineLarge: TextStyle(
      fontSize: 28,
      fontWeight: FontWeight.bold,
      color: Colors.white,
    ),
    // bodyLarge replaces bodyText1
    bodyLarge: TextStyle(
      fontSize: 16,
      color: Colors.white70,
    ),
  );

  static ThemeData get themeData => ThemeData(
    brightness: Brightness.dark,
    // Use a ColorScheme instead of primaryColor/accentColor
    colorScheme: ColorScheme.dark(
      primary: primaryPurple,
      secondary: accentPurple,
      background: darkPurple,
    ),
    scaffoldBackgroundColor: darkPurple,
    textTheme: textTheme,
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: accentPurple,  // backgroundColor replaces primary
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
        padding: EdgeInsets.symmetric(vertical: 14, horizontal: 24),
      ),
    ),
  );
}
