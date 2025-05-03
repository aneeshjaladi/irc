# 📡 Basic IRC Server in Python (Socket Programming)

This is a minimal IRC-style **chat server** built using Python's `socket` and `threading` modules. It accepts multiple client connections and **broadcasts messages** to all connected clients in real-time.

---

## 📦 Features

- Handles multiple clients simultaneously
- Broadcasts messages sent by any client to all others
- Built with only Python standard libraries
- Simple and clean structure

---

## 🚀 Getting Started

### 🧰 Requirements

- Python 3.9+
- A terminal-based TCP client (like `telnet` or `nc`) to connect to the server

### 🔧 Running the Server

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cpushalman/irc.git
   ```
2. **Run the Server**
  ```bash
python server.py
```
3. **Connect clients using telnet or netcat:
Open separate terminals and run:**
```bash
telnet 127.0.0.1:3000
```


## Note:This script runs on your local machine,if the server establishes connection with multiple terminals using tcp client on your local machine you'll be able to visualize the socket handling concept within your localhost,you can tunnel this onto the internet using any tunnel of your choice like `ngrok` and be able to connect irc s with your buddies for  Ephemeral, Non-Surveilled, or Privacy-Focused Chat 
### nowhere your chat data is to be found after you send it also the other receives it

