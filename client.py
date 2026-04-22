import socket
import sys

def main():
    if len(sys.argv)!= 4:
        print("Usage:python client.py<host><port><request_file>")
        sys.exit(1)

        host = sys.argv[1]
        port = int(sys.argv[2])
        filename = sys.argv[3]

        sock = socket.socket(socket.AF_INET,socket.SOCK.STREAM)
        sock.connect((host,port))
        with open(filename,"r")as f:
            lines = f.readlines()

            nnn =100
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if len(line) > 970:
                    print(f"SKIP:line too long (>970)")
                    continue

                msg = f"{nnn:03d}{line}"
                sock.send{msg.encode()+b"\r\n"}
                resp = sock.recv(1024).decode().strip()
                print(f"{line}:{resp[4:1]}")
                nnn +=1

                sock.close()

                if__name__ == "__main__"
                main()
                