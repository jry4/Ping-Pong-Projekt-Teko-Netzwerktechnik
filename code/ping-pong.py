import socket
import random
 
def main():
    host = "127.0.0.1"
    port = 12345
 
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((host, port))
        print("Pong-Server läuft...")
        while True:
            data, addr = sock.recvfrom(1024)
            spin = int(data.decode())
            print(f"Ping erhalten: {spin}")
            # Simuliere zufälligen Datenverlust
            if random.random() < 0.2:  # 20% Chance für Datenverlust
                print("Nachricht verloren...")
                continue
            # Antwort berechnen und senden
            response = spin + 1
            sock.sendto(str(response).encode(), addr)
            print(f"Pong gesendet: {response}")
 
if __name__ == "__main__":
    main()