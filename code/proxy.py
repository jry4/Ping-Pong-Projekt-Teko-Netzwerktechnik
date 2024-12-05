import socket

def start_proxy(proxy_host, proxy_port, server_host, server_port):
    print(f"Proxy läuft auf {proxy_host}:{proxy_port} und leitet weiter an {server_host}:{server_port}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as proxy_socket:
            try:
                proxy_socket.bind((proxy_host, proxy_port))
            except OSError as e:
                print(f"Fehler: Port {proxy_port} ist bereits belegt. Bitte einen anderen Port verwenden.")
                return

            while True:
                try:
                    # Empfang vom Ping-Client
                    data, client_addr = proxy_socket.recvfrom(1024)
                    print(f"Empfangen vom Ping-Client {client_addr}: {data.decode()}")

                    # Weiterleitung an Pong-Server
                    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as forward_socket:
                        forward_socket.sendto(data, (server_host, server_port))
                        print(f"Weitergeleitet an Pong-Server {server_host}:{server_port}: {data.decode()}")

                        # Antwort vom Pong-Server empfangen
                        server_response, server_addr = forward_socket.recvfrom(1024)
                        print(f"Antwort vom Pong-Server {server_addr}: {server_response.decode()}")

                    # Weiterleitung an Ping-Client
                    proxy_socket.sendto(server_response, client_addr)
                    print(f"Antwort an Ping-Client {client_addr} weitergeleitet: {server_response.decode()}")

                except socket.error as e:
                    print(f"Netzwerkfehler im Proxy: {e}")

    except KeyboardInterrupt:
        print("\nProxy wurde beendet.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    PROXY_HOST = "127.0.0.1"
    PROXY_PORT = input("Gib den Port des Proxys ein (Standard: 12346): ") or "12346"
    SERVER_HOST = input("Gib die Adresse des Pong-Servers ein (Standard: 127.0.0.1): ") or "127.0.0.1"
    SERVER_PORT = input("Gib den Port des Pong-Servers ein (Standard: 12345): ") or "12345"
    start_proxy(PROXY_HOST, int(PROXY_PORT), SERVER_HOST, int(SERVER_PORT))
