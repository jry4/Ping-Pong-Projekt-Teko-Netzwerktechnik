import socket

def start_pong_server(host="192.168.101.13", port=12345):
    """
    Startet den Pong-Service, der auf eingehende UDP-Pings wartet und
    mit n + 1 antwortet.
    """
    print(f"Pong-Service läuft auf {host}:{port}...")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        while True:
            data, addr = server_socket.recvfrom(1024)  # Empfangene Daten (n)
            if not data:
                continue
            
            n = int(data.decode())  # Konvertiere die empfangene Zahl
            print(f"Empfangen von {addr}: {n}")
            response = str(n + 1)  # Berechne n + 1
            server_socket.sendto(response.encode(), addr)  # Sende Antwort
            print(f"Gesendet an {addr}: {response}")

if __name__ == "__main__":
    start_pong_server()
