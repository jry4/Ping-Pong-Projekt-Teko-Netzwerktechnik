import socket

def start_proxy(proxy_host, proxy_port, pong_host, pong_port):
    """
    Startet den Proxy, der Nachrichten vom Ping-Client entgegennimmt, an den Pong-Server weiterleitet
    und Antworten zurück zum Ping-Client sendet.
    """
    print(f"Proxy läuft auf {proxy_host}:{proxy_port} und verbindet zu Pong auf {pong_host}:{pong_port}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as proxy_socket:
            proxy_socket.bind((proxy_host, proxy_port))  # Proxy wartet auf eingehende Nachrichten
            while True:
                try:
                    # Nachricht vom Ping-Client empfangen
                    data, client_address = proxy_socket.recvfrom(1024)
                    print(f"Empfangen von Ping-Client {client_address}: {data.decode()}")

                    # Nachricht an den Pong-Server weiterleiten
                    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as forward_socket:
                        forward_socket.sendto(data, (pong_host, pong_port))
                        pong_response, _ = forward_socket.recvfrom(1024)  # Antwort vom Pong-Server empfangen
                        print(f"Antwort vom Pong-Server: {pong_response.decode()}")

                    # Antwort zurück an den Ping-Client senden
                    proxy_socket.sendto(pong_response, client_address)
                    print(f"Antwort an Ping-Client {client_address} gesendet: {pong_response.decode()}")

                except socket.error as e:
                    print(f"Netzwerkfehler: {e}")

    except KeyboardInterrupt:
        print("\nProxy wurde beendet.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    # Feste Konfiguration für Proxy und Pong-Server
    PROXY_HOST = "localhost"  # Adresse des Proxys
    PROXY_PORT = 12345        # Port des Proxys
    PONG_HOST = "localhost"   # Adresse des Pong-Servers
    PONG_PORT = 12346         # Port des Pong-Servers

    start_proxy(PROXY_HOST, PROXY_PORT, PONG_HOST, PONG_PORT)
