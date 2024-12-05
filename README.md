# Ping-Pong-Proxy Projekt Teko Netzwerktechnik

Ein einfaches Netzwerkprojekt in Python, das aus einem Ping-Client, einem Pong-Server und einem Proxy-Server besteht. Der Client sendet eine Nachricht ("Ping")an den Proxy, der sie an den Server weiterleitet. Der Server verarbeitet die Nachricht und sendet eine Antwort zurück.

## **Projektstruktur**

- `ping.py`: Der Client sendet Nachrichten und wartet auf Antworten.
- `pong.py`: Der Server verarbeitet Nachrichten und gibt die Antwort zurück.
- `proxy.py`: Der Proxy vermittelt zwischen Client und Server.

---

## **Voraussetzungen**

- Python 3.x installiert (Prüfen Sie mit `python3 --version`).
- Prüfen der Installation mit:
    ```bash
    python3 --version
    ```

---

## **Installation**
Die drei Files (pong.py/proxy.py/ping.py) müssen alle in einer separaten Konsole gestartet werden

1. Klonen oder laden Sie das Projekt herunter:
   ```bash
   git clone https://github.com/jry4/Ping-Pong-Projekt-Teko-Netzwerktechnik
   cd Ping-Pong-Proxy Projekt Teko Netzwerktechnik

2. In der Konsole mit cd (Pfad) ins richtige Verzeichnis gelangen ( Eintrag (Pfad) durch Pfad des gespeciherten Projekts ersetzten)

3. Starten des Pong-Servers:
    ```bash
    python3 pong.py
    ```
4. Befolgen der Anweisungen in der Konsole bis der Pong-Server gestartet ist.
5. Starten des Proxy-Servers:
    ```bash
    python3 proxy.py
    ```
6. Befolgen der Anweisungen in der Konsole bis der Proxy-Server gestartet ist.
7. Starten des Ping-Servers:
    ```bash
    python3 ping.py
    ```
8. Befolgen der Anweisungen in der Konsole bis der Ping-Server gestartet ist.




   
    

