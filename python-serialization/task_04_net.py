#!/usr/bin/env python3
import socket
import json


def start_server(host='127.0.0.1', port=65432):
    """
    Starts a TCP server that listens for one connection, receives JSON data,
    deserializes it, and prints the dictionary.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            data = b""
            while True:
                packet = conn.recv(1024)
                if not packet:
                    break
                data += packet

            try:
                decoded_data = data.decode('utf-8')
                dictionary = json.loads(decoded_data)
                print("Received Dictionary from Client:")
                print(dictionary)
            except (json.JSONDecodeError, UnicodeDecodeError):
                print("Failed to decode or deserialize the received data")


def send_data(data, host='127.0.0.1', port=65432):
    """
    Connects to the server, serializes the dictionary to JSON, and sends it.
    """
    try:
        serialized_data = json.dumps(data).encode('utf-8')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            client_socket.sendall(serialized_data)
    except ConnectionRefusedError:
        print("Connection failed. Is the server running?")
    except Exception as e:
        print(f"An error occurred: {e}")
