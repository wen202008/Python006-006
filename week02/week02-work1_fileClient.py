import socket,sys
from pathlib import Path

def file_Client(sdfile):
    if not Path(sdfile).is_file() :
        print(f'argu {sdfile} 不是一个文件')
        sys.exit(1)
    
    host = 'localhost'
    port = 9999

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))

    with open(sdfile,'r') as f:
        sendtext = f.read()
        s.sendall(sendtext.encode())


    s.close()


if __name__ == '__main__':
    file_Client('G:\\tmp\\stracelog.txt')