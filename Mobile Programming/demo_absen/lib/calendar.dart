import 'package:flutter/cupertino.dart';
import 'package:table_calendar/table_calendar.dart';
import 'package:intl/intl.dart';

class CalenderScreen extends StatefulWidget {
  const CalenderScreen({Key? key}) : super(key: key);

  @override
  State<CalenderScreen> createState() => _CalendarScreenState();
}

class _CalendarScreenState extends State<CalenderScreen> {
  DateTime today = DateTime.now();

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        TableCalendar(
          headerStyle: const HeaderStyle(
            formatButtonVisible: false,
            titleCentered: true,
          ),
          availableGestures: AvailableGestures.all,
          focusedDay: today,
          firstDay: DateTime(2010, 10, 16),
          lastDay: DateTime(2050, 10, 16),
        ),
        const SizedBox(height: 10),
        const Align(
          alignment: Alignment.centerLeft,
          child: Row(
            mainAxisAlignment: MainAxisAlignment
                .center, // Untuk menampilkan ikon dan jam di tengah layar
            children: [
              Icon(
                CupertinoIcons.time_solid,
                size: 18,
              ),
              SizedBox(
                  width:
                      5), // Memberikan sedikit jarak antara ikon dan jam digital
              DigitalClockWidget(),
            ],
          ),
        ),
      ],
    );
  }
}

class DigitalClockWidget extends StatefulWidget {
  const DigitalClockWidget({super.key});

  @override
  State<DigitalClockWidget> createState() => _DigitalClockWidgetState();
}

class _DigitalClockWidgetState extends State<DigitalClockWidget> {
  String _formattedTime = '';

  @override
  void initState() {
    super.initState();
    // Atur timer untuk memperbarui waktu setiap detik
    _updateTime();
  }

  void _updateTime() {
    final String formattedTime = DateFormat.jm().format(DateTime.now());
    setState(() {
      _formattedTime = formattedTime;
    });

    // Perbarui waktu setiap detik
    Future.delayed(const Duration(seconds: 1), _updateTime);
  }

  @override
  Widget build(BuildContext context) {
    return Text(
      _formattedTime,
      style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
    );
  }
}
