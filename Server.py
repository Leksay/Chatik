import socket
import sys
import time
class MyHTTPServer:

    def __init__(self, host, port, server_name):
        self.host = host
        self.port = port
        self.server_name = server_name

    def serve_forever(self):
        serv_sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            proto=0
        )
        try:
            serv_sock.bind((self.host,self.port))
            print("server has been started")
            serv_sock.listen()
            print("server waiting for connection")
            while True:
                conn,addr = serv_sock.accept()
                try:
                    self.serve_client(conn,addr)
                except Exception as e:
                    print("Client servin failed", e)
        finally:
            serv_sock.close()

    def serve_client(self,conn,addr):
        try:
            data = conn.recv(1024)
            print("Connection: ",addr)
            print("---------------------")
            print("Request Data from Browser")
            answr = bytes("<-Answer->",'utf-8')
            print(data)
            conn.send(data + answr)
            conn.close()
            time.speep(0.1)
        except ConnectionResetError:
            conn = None
        except Exception as e:
            self.send_error(conn,e)

        if conn:
            conn.close()

    def parse_request(self,conn):
        pass #TODO:

    def handle_request(self,conn):
        pass #TODO:

    def send_response(self,conn,resp):
        pass #TODO:

    def send_error(self,conn,err):
        pass #TODO

if __name__ == '__main__':
    print("main")
    print("main")
    print("main")

    host = "172.105.88.159"
    port = 8081
    name = "Chatik"

    serv = MyHTTPServer(host,port,name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass


