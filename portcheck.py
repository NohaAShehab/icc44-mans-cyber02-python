import socket


def port_scan(target_host, start_port, end_port):
    # print(target_host, start_port, end_port)
    # scan related ports in the target host
    for port in range(start_port, end_port+1):
        # open socket for each port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        # check if the current port connected to the socket is opened or not
        result = sock.connect_ex((target_host, port))
        if result == 0:
            print(f"Port {port} is open")
        # else:
        #     print(f"Port {port} is closed")
        sock.close()




if __name__ == '__main__':
    port_scan('127.0.0.1',4999, 5001)