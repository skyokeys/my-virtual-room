import socket
server_host = '0.0.0.0'
server_port = 1234

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print(f'connectet to server')
    command = input()
    client_socket.send(command.encode('utf-8'))
    output = client_socket.recv(1024).decode('utf-8')
    print(f'command output: {output}')
    client_socket.close()
connect_to_server()