import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8080))
server_socket.listen(5)
print("Server listening on 0.0.0.0:8080")

while True:
    client_socket, client_address = server_socket.accept()
    print("Client connected from {}".format(client_address))

    image_name=str(input("Enter image file name: "))
    client_socket.sendall(image_name.encode("utf-8"))

    with open(image_name, "rb") as f:
        image = f.read()
        client_socket.sendall(image)
    print("Image transferred")

    client_socket.close()
