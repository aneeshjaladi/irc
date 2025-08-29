import socket
import threading

clients = []

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"Received: {message.decode('utf-8')}")
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            break

    client_socket.close()

def start_server(host='127.0.0.1', port=3000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"IRC server running on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        clients.append(client_socket)
        client_socket.send(b"Welcome to the IRC server!\n")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()

print("Server started locally")
print("salman is a good boy")
