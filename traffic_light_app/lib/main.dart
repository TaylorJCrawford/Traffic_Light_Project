import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:http/http.dart' as http;

void main() => runApp(MaterialApp(
      home: Home(),
    ));

class Home extends StatefulWidget {
  @override
  _Home createState() => _Home();
}

class _Home extends State<Home> {
  final inMeetingColour = Colors.red[300];
  final notInMeetingColour = Color.fromRGBO(173, 216, 230, 1);

  String imageAddress = 'assets/images/free.jpg';
  bool inMeeting = false;
  String titleBarText = 'Not In Meeting!';
  String buttonText = 'Start';
  TextEditingController txtController = TextEditingController();
  String defaultIPAddress  = "192.168.1.81";

  void loadAndUpdateIpAddress() async {
    // Method to update IP Address Stored In local Storage.

    final SharedPreferences _prefs = await SharedPreferences.getInstance();
    final String? IPAddress = _prefs.getString("IPAddress");

    if (IPAddress != null && IPAddress != '') {
      // Load into textbox.

      if (txtController.text == '') {
        txtController.text = IPAddress;
      } else if (txtController.text != IPAddress) {
        // Update IPAddress With Value in txtController
        await _prefs.setString('IPAddress', txtController.text);
      }

    } else {
      // Used Default Value.

      // Set in local storage.
      await _prefs.setString('IPAddress', defaultIPAddress);
      // Then Load into textbox.
      txtController.text = defaultIPAddress;
    }
  }

  @override
  Widget build(BuildContext context) {

  loadAndUpdateIpAddress();

    return Scaffold(
      appBar: AppBar(
        title: Text(titleBarText),
        centerTitle: true,
        // backgroundColor: Colors.red[300],
        backgroundColor: (() {
          if (inMeeting)
            return inMeetingColour;
          else
            return notInMeetingColour;
        })(),
      ),
      body: Container(
        color: Colors.grey[300],
        child: Column(
          children: <Widget>[
            Container(
              padding: EdgeInsets.all(20.0),
              color: Colors.grey[300],
              child: TextField(
                controller: txtController,
                textAlign: TextAlign.center,
                decoration: InputDecoration(
                  border: UnderlineInputBorder(),
                  hintText: 'Enter IP Address',
                ),
              ),
            ),
            Container(
              padding: EdgeInsets.fromLTRB(20, 0, 20, 35),
              color: Colors.grey[300],
              child: Center(
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(20), // Image border
                  child: SizedBox.fromSize(
                    // Image radius
                    size: Size.square(450.0),
                    child: Image.asset(imageAddress, fit: BoxFit.cover),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: Change,
        child: Text(buttonText),
        backgroundColor: (() {
          if (inMeeting)
            return inMeetingColour;
          else
            return notInMeetingColour;
        })(),
      ),
    );
  }

  void Change() {
    setState(() {
      // Once Called This Triggers The Build Function Above.

      if (inMeeting == true) {
        // Change To Not In Meeting
        inMeeting = false;
        titleBarText = 'Not In Meeting!';
        imageAddress = 'assets/images/free.jpg';
        buttonText = 'Start';
        sendRequest("0");
      } else {
        inMeeting = true;
        titleBarText = 'In Meeting!';
        imageAddress = 'assets/images/inMeeting.jpg';
        buttonText = 'Finish';
        sendRequest("1");
      }
    });
  }

  void sendRequest(String inMeeting) async { //   1 = inMeeting     0 = notInMeeting
    print("Request has been sent.");
    String ipAddress = txtController.text;
    final response = await http.get(Uri.parse("http://" + ipAddress + "/" + inMeeting));

    // Use For Testing:
    String responseData = utf8.decode(response.bodyBytes);
    print(json.decode(responseData));
  }
}