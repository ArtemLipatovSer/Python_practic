import json
import socket

# Создаем сервер
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # Выше означает что используем стек ТСП
# server_address = ('localhost', 12345)
# # 12345 это порт через ктороый будет переваваться информация в сеть
# server_socket.bind(server_address)
# # Выше утсановка конфигурация, слияние сервера и адреса
# server_socket.listen(99)

# # Выше сколько устройств мы будем поддерживать, сколько будет пользователей на сервере
# print('Ожидаем подключение')
# client_socket, client_address = server_socket.accept()
# print('client address - ', client_address)
#
# while True:
#     data = client_socket.recv(1024)
#     # Выше 1024 Кб мы будем получать
#     if not data:
#         break
#     # # Выводим отправленное сообщение, предварительно декодировав в нормальные буквы
#     # print(data.decode('utf-8'))
#     data = data.decode('utf-8')
#     data = json.loads(data)
#     print(data)
#     print(data['username'])

# Новое

def save_users_to_file():
    with open('users.json', 'w') as file:
        json.dump(users, file)

def registration(data):
    username = data['username']
    password = data['password']
    nick = data['nick']
    if username not in users:
        users[username] = {"password":password, 'nick': nick}
        save_users_to_file()
        return {'status': 'success', 'message': 'Регистрация прошла успешно'}
    else:
        return {'status': 'Error', 'message': 'Invalid username or password'}

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        data = json.loads(data.decode('utf-8'))

        if data['action'] == 'register':
            response = registration(data)
        else:
            response = {'status': 'Error', 'message': 'Invalid action'}
        client_socket.send(json.dumps(response).encode('utf-8'))

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    users = {}
    try:
        with open("user.json", 'r') as file:
            users = json.load(file)
    except:
        with open('users.json', 'w') as file:
            json.dump(users, file)

    print(registration({'username': 'Tom', 'password': 1234, 'nick': 'TESTTOM'}))
    server_socket.listen(99)
    print('Ожидаем подключение')
    # Разрешаем подключение
    client_socket, client_address = server_socket.accept()
    print('Accepting - ', {client_address})

    handle_client(client_socket)
