import asyncio
import pickle
import random
import time


async def tcp_echo_client():
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    while True:
        out_data = [random.randint(1,100) for i in range(3)]
        print(f'Send: {out_data!r}')
        message = pickle.dumps(out_data)
        writer.write(message)

        inc_data = await reader.read(100)
        message = pickle.loads(inc_data)
        print(f'Received: {inc_data!r}')
        time.sleep(2)

    print('Close the connection')
    writer.close()

asyncio.run(tcp_echo_client())