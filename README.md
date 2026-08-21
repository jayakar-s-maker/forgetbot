ForgetBot

A smart mirror that makes sure you never forget your stuff when you leave the house.
<img width="597" height="335" alt="images" src="https://github.com/user-attachments/assets/7ebe43dc-0d31-4c41-94df-db32459e9778" />


A Image of what ForgetBot will like


What It Does

Smart Departure Reminders: Walk up to the mirror, and it recognizes your face and asks where you're headed. Say "I'm going shopping," and it tells you exactly what to bring.

MagicMirror Dashboard: Displays live weather, news, and plays your music through USB speakers while you get ready.

Hands-Free Control: Speak directly to the mirror to trigger checklists or manage music using the built-in mic and speaker.

Hardware Setup

Brain: Raspberry Pi 5

Camera: Raspberry Pi AI Camera (handles face detection so the Pi 5 doesn't have to do all the heavy lifting)

Audio: USB Microphone + Mini USB Speaker

Enclosure: 3" Deep Shadow Box (built deep enough so the Pi 5, active cooler, screen, and cables fit with plenty of breathing room)

How It Works
Offloading face detection directly to the AI Camera’s processor keeps the Raspberry Pi 5 free to run the MagicMirror UI. This keeps the dashboard smooth and lag-free even while background audio and voice detection are running.
