import random
import socket
import pickle
import string
import uuid
import json
from entidades import *
import threading

class Cliente:
    def __init__(self, port, host) -> None:
        self._port = port
        self._host = host
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def start_client(self):
        self._s.connect((self._host, self._port))
        self._login()
        
    def __request(self, typeOperation, data):
        data_serialized = pickle.dumps((typeOperation, data))
        self._s.send(data_serialized)


        response = self._s.recv(4096)
        if not response:
            return False

        try:
            # Tenta desserializar os dados
            deserialized_data = pickle.loads(response)
            return deserialized_data
        except pickle.UnpicklingError:
            print("Erro ao desserializar os dados recebidos.")
            return None