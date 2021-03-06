import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.56.1"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            connection = self.client.recv(2048).decode()
            print('connection:', connection)
            return connection
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            _send = pickle.loads(self.client.recv(2048 * 2))
            print(_send)
            return _send
        except socket.error as e:
            print(e)

