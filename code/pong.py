import socket

def start_pong_server(host, port):
    print(f"Pong-Service läuft auf {host}:{port}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
            server_socket.bind((host, port))
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
    HOST = input("Gib die Adresse des Servers ein: ")
    PORT = int(input("Gib den Port des Servers ein: "))
    start_pong_server(HOST, PORT)
