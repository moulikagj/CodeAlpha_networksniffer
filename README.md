Basic Network Sniffer Using Python

Project Overview

The Basic Network Sniffer is a Python-based cybersecurity project developed as part of the CodeAlpha Cyber Security Internship.

It captures network packets and analyzes their basic information using the Scapy library.

Features

- Captures live network packets.
- Displays source and destination IP addresses.
- Identifies network protocols such as TCP, UDP and ICMP.
- Displays source and destination port numbers.
- Shows packet payload size.
- Uses Scapy for packet capturing and analysis.

Technologies Used

- Python 3
- Scapy
- Npcap
- Visual Studio Code

Requirements

- Windows 10 or Windows 11
- Python installed
- Scapy library
- Npcap installed

Installation

1. Install Python.
2. Install Npcap from https://npcap.com/
3. Open the project folder in VS Code.
4. Install the required library:

pip install -r requirements.txt

How to Run

Open the terminal in the project folder and execute:

python network_sniffer.py

Run with the necessary permissions for packet capture.

Output

The program displays:

- Source IP address
- Destination IP address
- Protocol
- Source port
- Destination port
- Payload size

Security Note

Use this tool only on your own network or networks where you have explicit permission to capture traffic.

Internship

CodeAlpha Cyber Security Internship

Author

Moulika