#!/usr/bin/env python3
"""
Module to send commands to a Global Caché iTach device.

Parameters: host port command [response_timeout]

Some examples:

* Send IR command ('1:3' targets the 3rd IR output socket):
    python3 ip2ir.py 192.168.84.42 4998 'sendir,1:3,2,38226,1, ... ,4892' 0.1
* Learn IR command (15 second timeout permits multiple capture attempts):
    python3 ip2ir.py 192.168.84.42 4998 'get_IRL' 15
* Stop learning mode (also stops on receipt of non-learning command):
    python3 ip2ir.py 192.168.84.42 4998 'stop_IRL'
* Get device network configuration (first with default timeout, then 0.1 sec):
    python3 ip2ir.py 192.168.84.42 4998 'get_NET,0:1'
    python3 ip2ir.py 192.168.84.42 4998 'get_NET,0:1' 0.1
* List device capabilities:
    python3 ip2ir.py 192.168.84.42 4998 'get_devices'

API Guide   : https://www.globalcache.com/files/docs/API-iTach.pdf
Tested with : https://www.globalcache.com/products/itach/ip2ir-pspecs/
"""
import socket
import sys
import textwrap


def send_command(host, port, command, timeout):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        ba = bytearray(command.encode())
        ba.extend(b'\x0D')  # command must end with Carriage Return ('\r')
        print(f'command={repr(ba)}')
        print(f'Sending command with {timeout} second response timeout...')
        s.connect((host, port))
        s.sendall(ba)
        output = ''
        s.settimeout(timeout)
        try:
            chunk = s.recv(1024)
            while len(chunk) > 0:
                output += chunk.decode('utf-8')
                chunk = s.recv(1024)
        except BlockingIOError as e:
            print(e)
        except socket.timeout:
            print('Assuming complete (timed out waiting for more data)')

    print(f'\nRaw Output\n----------')
    print(repr(output))

    print(f'\nOutput\n------')
    print(output.replace('\r', '\n'))


if __name__ == '__main__':
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        raise ValueError(textwrap.dedent('''
            Parameters : host port command [response_timeout]
            API Guide  : https://www.globalcache.com/files/docs/API-iTach.pdf
            
            Examples
            --------
            python3 ip2ir.py 192.168.84.42 4998 'get_devices'
            python3 ip2ir.py 192.168.84.42 4998 'get_NET,0:1'
            python3 ip2ir.py 192.168.84.42 4998 'get_IRL' 15
            python3 ip2ir.py 192.168.84.42 4998 'stop_IRL'
            python3 ip2ir.py 192.168.84.42 4998 'sendir,1:3,2,38226,1, ... ,4892' 0.1
        '''))

    default_timeout = 3 if len(sys.argv) < 5 else float(sys.argv[4])
    send_command(sys.argv[1], int(sys.argv[2]), sys.argv[3], default_timeout)
