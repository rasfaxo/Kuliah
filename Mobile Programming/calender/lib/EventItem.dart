import 'package:flutter/material.dart';

class EventItem extends StatelessWidget {
  final String eventContent;

  EventItem({required this.eventContent});

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.symmetric(
        horizontal: 12,
        vertical: 4,
      ),
      color: Colors.blue[300],
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12),
      ),
      elevation: 4,
      child: ListTile(
        onTap: () {
          showDialog(
            context: context,
            builder: (context) {
              return AlertDialog(
                title: const Text("Detail Acara"),
                content: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(eventContent),
                  ],
                ),
              );
            },
          );
        },
        title: Text(
          eventContent,
          style: const TextStyle(fontWeight: FontWeight.bold),
          selectionColor: Colors.red,
        ),
      ),
    );
  }
}
