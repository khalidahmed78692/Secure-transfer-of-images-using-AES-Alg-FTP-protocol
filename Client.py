import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipaddress=str(input("Enter Sender/ Server ip address: "))
client_socket.connect((ipaddress, 8080))

image_name = client_socket.recv(1024).decode("utf-8")


image = b''
while True:
    chunk = client_socket.recv(4096)
    if not chunk:
        break
    image += chunk

with open(image_name, "wb") as f:
    f.write(image)

print("Image received")

client_socket.close()
