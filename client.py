import socket,time

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server's address and port
server_address = ('localhost', 8080)
client_socket.connect(server_address)
print('Connected to server')

# # Recive ans for checkout
# response = client_socket.recv(1024).decode('utf-8')
# print('Server response Answer.')

def send_request(message):
    request = f"{message}"
    client_socket.send(request.encode('utf-8'))
    # print('Sent to server : ', message)

    # Receive and print the server's response
    response = client_socket.recv(1024).decode('utf-8')
    print(response)

# Send messages to the server

while True :
    print("type \"exit\" for exit")
    message_input = input("Enter locker number : ")
    if(message_input == "exit" ) :
        break
    else :
        send_request(message_input)

        while True :
            password_input = input("Enter password : ")
            client_socket.send(password_input.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            if(response == 'Correct Password!\n') :
                break
            else :
                print(response)

        print('-*-*-*-*-*-*-*-*-*-*- Menu -*-*-*-*-*-*-*-*-*-*-')
        print('a) View Message')
        print('b) Edit Message')
        print('c) Change Password')
        print('d) Exit')

        print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        choice = input("Enter choice : ")
        client_socket.send(choice.encode('utf-8'))

        if(choice == 'a') :
            response = client_socket.recv(1024).decode('utf-8')
            print(response)
        elif(choice == 'b') :
            message = input("Enter new message : ")
            send_request(message)
        elif(choice == 'c') :
            password = input("Enter new password : ")
            send_request(password)
        elif(choice == 'd') :
            break
        else :
            print('Invalid choice')

        print('-------------------------------------------------')

# Close the connection
client_socket.close()