import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:permission_handler/permission_handler.dart';
import 'package:tflite_flutter/tflite_flutter.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  Interpreter? _interpreter;
  String _genre = 'Unknown';
  bool _loading = true;

  @override
  void initState() {
    super.initState();
    _loadModel();
  }

  Future<void> _loadModel() async {
    _interpreter = await Interpreter.fromAsset('model/genre_classifier.tflite');
    setState(() => _loading = false);
  }

  Future<void> _pickAudioAndClassify() async {
    if (!await Permission.storage.request().isGranted) return;
    final picker = ImagePicker();
    final file = await picker.pickImage(source: ImageSource.gallery);
    if (file == null) return;

    // TODO: Extract audio features and run _interpreter!
    setState(() => _genre = 'Rock');
  }

  @override
  Widget build(BuildContext context) {
    final colors = Theme.of(context).colorScheme;
    return Scaffold(
      body: _loading
          ? Center(child: CircularProgressIndicator())
          : Stack(
        fit: StackFit.expand,
        children: [
          Image.asset(
            'assets/images/purple_music_bg.jpg',
            fit: BoxFit.cover,
          ),
          // semi-transparent overlay for better contrast:
          Container(color: Colors.black38),
          Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'Detected Genre',
                style: Theme.of(context).textTheme.headlineLarge,
              ),
              SizedBox(height: 8),
              Text(
                _genre,
                style: Theme.of(context).textTheme.bodyLarge,
              ),
              SizedBox(height: 32),
              ElevatedButton.icon(
                icon: Icon(Icons.music_note, color: colors.onSecondary),
                label: Text('Select Audio'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: colors.secondary,
                ),
                onPressed: _pickAudioAndClassify,
              ),
            ],
          ),
        ],
      ),
    );
  }
}
