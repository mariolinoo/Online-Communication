import asyncio
import pickle #für das versenden von listen und dicts mit dumps() und loads()
import sqlite3


async def handle_echo(reader, writer):
    while True:
        inc_mess = await reader.read(100)
        inc_data = pickle.loads(inc_mess)
        addr = writer.get_extra_info('peername')
        data_list.append(inc_data)

        print(f"Received {inc_data!r} from {addr!r}") #!r ist ein raw string ... \n hat kein Funktion mehr


        print(f"Send: {inc_data!r}")
        writer.write(inc_mess)
        await writer.drain()


    print("Close the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    conn = sqlite3.connect("sensor.db")
    print("created database")
    asyncio.run(main())

