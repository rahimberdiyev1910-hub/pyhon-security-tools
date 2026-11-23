import socket
from datetime import datetime

class NetworkScanner:
    def __init__(self, target_host):
        self.target_host = target_host
        self.open_ports = []

    def scan_ports(self, port_list):
        print(f"[*] Scanning target: {self.target_host}")
        print(f"[*] Time started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        for port in port_list:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((self.target_host, port))
            if result == 0:
                print(f"[+] Port {port}: OPEN")
                self.open_ports.append(port)
            sock.close()
        
        return self.open_ports

if __name__ == "__main__":
    # Localhost tekshiruvi uchun namuna
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]
    scanner = NetworkScanner("127.0.0.1")
    scanner.scan_ports(common_ports)
