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