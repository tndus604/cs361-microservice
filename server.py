import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
PORT = "tcp://127.0.0.1:5555"
socket.bind(PORT) 


while True:
    message = socket.recv_string()
    print(f"Received request: {message}")

    random_number = random.randint(0, 36)

    # send back
    socket.send_string(str(random_number))
