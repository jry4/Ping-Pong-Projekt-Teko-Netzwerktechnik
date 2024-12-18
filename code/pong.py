import socket

def start_pong_server(host, port):
    print(f"Pong-Service läuft auf {host}:{port}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
            try:
                server_socket.bind((host, port))
            except OSError as e:
                print(f"Fehler: Port {port} ist bereits belegt. Bitte einen anderen Port verwenden.")
                return

            while True:
                try:
                    data, addr = server_socket.recvfrom(1024)  # Empfangene Daten
                    if not data:
                        print(f"Leere Daten von {addr} erhalten. Überspringe...")
                        continue
                    
                    try:
                        n = int(data.decode())  # Konvertiere die empfangene Zahl
                        print(f"Empfangen von {addr}: {n}")
                        response = str(n + 1)  # Berechne n + 1
                        server_socket.sendto(response.encode(), addr)  # Sende Antwort
                        print(f"Gesendet an {addr}: {response}")
                    except ValueError:
                        print(f"Fehler: Ungültige Daten von {addr} erhalten: {data.decode()}")

                except socket.error as e:
                    print(f"Netzwerkfehler: {e}")

    except KeyboardInterrupt:
        print("\nPong-Server wurde beendet.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    HOST = input("Gib die Adresse des Servers ein (Standard: 127.0.0.1): ") or "127.0.0.1"
    PORT = input("Gib den Port des Servers ein (Standard: 12345): ") or "12345"
    start_pong_server(HOST, int(PORT))
