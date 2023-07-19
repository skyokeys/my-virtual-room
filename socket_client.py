import socket
server_host = '0.0.0.0'
server_port = 3141

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    server_open = False
    while not server_open:
        print('Password:')
        password = input()
        if password == '3141592Pi':
            print('correct :')
            print('welcome skyoker')
            server_open = True
        else:
            print('wrong password')
    print("---------------Server---------------")
    print('    - server host = 0.0.0.0')
    print('    - server port = 3141')
    print('ready to send commands!')
    exit = False
    while not exit:
        command = input()
        client_socket.send(command.encode('utf-8'))
        output = client_socket.recv(1024).decode('utf-8')
        print(output)
        if command == 'close server':
            client_socket.close
            exit = True
connect_to_server()