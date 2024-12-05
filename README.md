# Ping-Pong-Proxy Projekt Teko Netzwerktechnik

Ein einfaches Netzwerkprojekt in Python, das aus einem Ping-Client, einem Pong-Server und einem Proxy-Server besteht. Der Client sendet eine Nachricht ("Ping" oder Zahlen) an den Proxy, der sie an den Server weiterleitet. Der Server verarbeitet die Nachricht und sendet eine Antwort zurück.

## **Projektstruktur**

- `ping.py`: Der Client sendet Nachrichten und wartet auf Antworten.
- `pong.py`: Der Server verarbeitet Nachrichten und gibt die Antwort zurück.
- `proxy.py`: Der Proxy vermittelt zwischen Client und Server.

---

## **Voraussetzungen**

- Python 3.x installiert (Prüfen Sie mit `python3 --version`).
- Netzwerkinfrastruktur, die UDP-Kommunikation erlaubt.

---

## **Installation**

1. Klonen oder laden Sie das Projekt herunter:
   ```bash
   git clone https://github.com/username/ping-pong-proxy.git
   cd ping-pong-proxy

