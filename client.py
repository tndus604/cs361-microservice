import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
PORT = "tcp://127.0.0.1:5555"
socket.connect(PORT)

while True:
    # Send a request
    request_message = input("Enter your request: ")
    socket.send_string(request_message)

    # Receive the response
    response = socket.recv_string()
    print(f"Received response: {response}")