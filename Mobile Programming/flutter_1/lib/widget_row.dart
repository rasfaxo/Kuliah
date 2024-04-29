import 'package:flutter/material.dart';

class WidgetColumn extends StatelessWidget {
  const WidgetColumn({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('Widget Row'),
        ),
        body: const Row(
          children: [
            Text('Kolom 1'),
            Text('Kolom 2'),
            Text('Kolom 3'),
            Text('Kolom 4'),
          ],
        ));
  }
}
