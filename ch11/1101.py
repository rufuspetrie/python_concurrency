import asyncio

class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info("peername")
        print("Connection from {}".format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print("Data received: {!r}".format(message))

loop = asyncio.get_event_loop()
coro = loop.create_server(EchoServerClientProtocol, "127.0.0.1", 8888)
server = loop.run_until_complete(coro)

# Serve requests until keyboard interrupt (ctrl-c)
print("Serving on {}".format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()