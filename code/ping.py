import socket
import time

def start_ping_client(server_ip, server_port, initial_spin=0):
    print(f"Verbinde zu Proxy/Pong-Service auf {server_ip}:{server_port}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
            spin = initial_spin
            client_socket.settimeout(5)  # Timeout für den Empfang
            while True:
                try:
                    # Nachricht senden
                    client_socket.sendto(str(spin).encode(), (server_ip, server_port))
                    print(f"Gesendet: {spin}")

                    # Antwort empfangen
                    data, addr = client_socket.recvfrom(1024)
                    try:
                        response = int(data.decode())
                        print(f"Antwort erhalten von {addr}: {response}")
                        spin = response  # Spin-Wert aktualisieren
                    except ValueError:
                        print(f"Fehler: Ungültige Antwort vom Server: {data.decode()}")

                except socket.timeout:
                    print("Zeitüberschreitung beim Warten auf Server-Antwort. Neuer Versuch...")
                except socket.error as e:
                    print(f"Netzwerkfehler: {e}. Verbindung wird erneut versucht.")
                    time.sleep(1)

    except KeyboardInterrupt:
        print("\nPing-Client wurde beendet.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    SERVER_IP = input("Gib die IP-Adresse des Servers/Proxys ein: ")
    SERVER_PORT = int(input("Gib den Port des Servers/Proxys ein: "))
    start_ping_client(SERVER_IP, SERVER_PORT)
