#!/usr/bin/python3
#LAURA TRABAS CLAVERO

import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind(('localhost', 1234))

mySocket.listen(5)

primero = 0

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        peticion = recvSocket.recv(2048).decode("utf-8", "strict")
        print(peticion)

        try:
            numero = peticion.split()[1][1:]
            print (numero)
            if numero == "favicon.ico":
                recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + "Ni caso\r\n", 'utf-8'))
                recvSocket.close()
                continue
            print('Answering back...')

            if (primero == 0):
                primero = numero
                resultado = "Me has dado " + str(primero) + " .Dame otro mas"
            else:
                segundo = numero
                resultado = int(primero) + int(segundo)
                resultado = "Me has dado " + str(primero) + " . Ahora " + str(segundo) + ". El resultado es: " + str(resultado)
                primero = 0

            recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><h1>" + resultado + "</h1></body></html>" +
                            "\r\n", 'utf-8'))
            recvSocket.close()
        except ValueError:
            print ('Me has dado un numero erroneo')

except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
