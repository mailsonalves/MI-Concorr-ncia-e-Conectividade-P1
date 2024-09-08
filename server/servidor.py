import socket
import threading
import pickle
import json
from entidades import *

class Servidor():
    def __init__(self, port, host) -> None:
        self._port = port
        self._host = host
        self.__allclients = {}
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)