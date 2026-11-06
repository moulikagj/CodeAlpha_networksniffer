from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def packet_callback(packet):
    if IP in packet:
        print("\n----- Packet Details -----")
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

        if TCP in packet:
            print("Protocol: TCP")
            print("Source Port:", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        elif UDP in packet:
            print("Protocol: UDP")
            print("Source Port:", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

        elif ICMP in packet:
            print("Protocol: ICMP")

        else:
            print("Protocol: Other")

        if Raw in packet:
            print("Payload Size:", len(bytes(packet[Raw].load)), "bytes")
        else:
            print("Payload Size: 0 bytes")

        print("-------------------------")

print("Network Sniffer Started...")
print("Capturing 10 IP packets...")

sniff(filter="ip", prn=packet_callback, count=10, store=False)

print("\nPacket capturing completed!")