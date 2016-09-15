#!/bin/sh

#capture by webkit2png output to /tmp/ folder
python /root/Desktop/websit2png/python-webkit2png/webkit2png/scripts.py $1 -o /tmp/webcapture.png --debug --log=/tmp/capture.log

sleep 15

#send email to monitor team
#python /root/Desktop/website_capture/sendmail.py "Web Capture Script" "/tmp/webcapture.png"

#send to Line Group Web Capture Monitoring
python /root/Desktop/website_capture/sendToline.py
