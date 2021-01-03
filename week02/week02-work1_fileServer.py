import socket

host = 'localhost'
port = 9999
# 创建socket对象，绑定端口，并监听 ，接收客户端发过来的流
def file_Server(recfile):
    recText = ''
    with  socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((host,port))
        s.listen(1)

        conn,addr = s.accept()
        with conn:
            #print('Connected by',addr)
            while True:
                data = conn.recv(4096)
                #recText = recText + data.decode()
                with open(recfile,'a') as f:
                    f.write(data.decode())
                
                if not data:
                    break
                #conn.sendall(data)
        #print(recText)




if __name__ == '__main__':
    file_Server('G:\\tmp\\stracelog_server.txt')
