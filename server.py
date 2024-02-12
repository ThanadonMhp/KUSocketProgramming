import socket,random,time

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8080)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print('Server is listening for connections...')

# Accept a connection
connection, client_address = server_socket.accept()
print('Connection from', client_address)

def process_request(request):
    # Dummy processing, just append "Server Processed: " to the request
    processed_request = "Server Processed: " + request
    return processed_request

def send_response_message(message):
    response = f"{message}"
    connection.send(response.encode('utf-8'))

def send_response(status_code, status_phrase, message):
    response = f"RES {status_code} {status_phrase} {message}"
    connection.send(response.encode('utf-8'))
    
datas = ['data1','data2','data3','data4','data5','data6','data7','data8','data9','data10']
lockers = ['1','2','3','4','5','6','7','8','9','10']
passwords = ['1234','1234','1234','1234','1234','1234','1234','1234','1234','1234']
# rand_num = random.randint(1,100)
# print(rand_num)
# send_response_message(rand_num)
# Receive and process messages from the client
while True:
    data = connection.recv(1024).decode('utf-8')
    if not data:
        break

    # Check if the received data follows the protocol
    if data.startswith(""):
        # Extract the message from the request
        message = data
        print('Client Selected :', message)
        if(message in lockers) :
            send_response_message("Enter locker %s password : " % message)
            password_input = connection.recv(1024).decode('utf-8')
            print('Client Entered Password :', password_input)
            while(password_input != passwords[int(message)-1]) :
                send_response_message("Try again")

            send_response_message('Correct Password!\n')
                    
            choice = connection.recv(1024).decode('utf-8')
            if(choice == 'a') :
                print (int(message)-1)
                send_response_message('Message : %s' % datas[int(message)-1])
            elif(choice == 'b') :
                new_message = connection.recv(1024).decode('utf-8')
                datas[int(message)-1] = new_message
                send_response_message('Message updated successfully')
            elif(choice == 'c') :
                new_password = connection.recv(1024).decode('utf-8')
                passwords[int(message)-1] = new_password
                send_response_message('Password updated successfully')
            elif(choice == 'd') :
                send_response_message('Exiting...')
                break
        
        else :
            send_response_message("Invalid locker number")
            