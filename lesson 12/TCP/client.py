import json
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)
# response = json.dumps({'username': 'Tom', 'age': 16})
# # Отправляем сообщение, предварительно закодировав его в машинный код
# client_socket.send(response.encode('utf-8'))

# Новое

try:
    while True:
        print('Welcome')
        username = input('username -->')
        password = input('password -->')
        nick = input('nickname -->')
        data = {'action': 'register',
                'username': username,
                'password': password,
                'nick': nick}
        client_socket.send(json.dumps(data).encode('utf-8'))
        data = client_socket.recv(1024)
        print(json.loads(data.decode('utf-8'))['message'])
        client_socket.close()
        break
except:
    client_socket.close()


