import socket
import time

def start_ping_client(server_ip, server_port, initial_spin=0):
    """
    Startet den Ping-Service, der eine Zahl n (spin) an den Pong-Service sendet
    und auf n + 1 antwortet.
    """
    print(f"Verbinde zu Pong-Service auf {server_ip}:{server_port}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
            spin = initial_spin
            while True:
                try:
                    client_socket.sendto(str(spin).encode(), (server_ip, server_port))  # Sende Ping
                    print(f"Gesendet: {spin}")
                    
                    data, addr = client_socket.recvfrom(1024)  # Empfange Antwort (n + 1)
                    
                    try:
                        response = int(data.decode())  # Konvertiere Antwort zu int
                        print(f"Antwort erhalten von {addr}: {response}")
                        spin = response  # Aktualisiere den spin-Wert
                    except ValueError:
                        print(f"Fehler: Ungültige Antwort vom Server: {data.decode()}")
                        continue

                except socket.timeout:
                    print("Zeitüberschreitung beim Warten auf Server-Antwort.")
                except socket.error as e:
                    print(f"Netzwerkfehler: {e}")
                
                time.sleep(1)  # Warte 1 Sekunde vor dem nächsten Ping

    except KeyboardInterrupt:
        print("\nPing-Client wurde beendet.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    SERVER_IP = input("Gib die IP-Adresse des Servers ein: ")  # Userinput für IP des Servers
    SERVER_PORT = int(input("Gib den Port des Servers ein (Standard: 12345): "))
    start_ping_client(SERVER_IP, SERVER_PORT)