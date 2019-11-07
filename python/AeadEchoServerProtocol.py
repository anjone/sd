from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend
import asyncio, os

PW = b'password'

class AeadEchoServerProtocol(asyncio.Protocol):
    def __init__(self, password):
        key_material = HKDF(
            algorithm=hashes.SHA256(),
            length=64, salt=None, info=None,
            backend=default_backend()
        ).derive(password)
        self._server_read_key = key_material[0:32]
        self._server_write_key = key_material[32:64]

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        nonce, ciphertext = data[:12], data[12:]
        plaintext = ChaCha20Poly1305(self._server_read_key).decrypt(nonce, ciphertext, b'')
        message = plaintext.decode()
        print('Decrypted message from client: {!r}'.format(message))

        print('Echo back message: {!r}'.format(message))
        reply_nonce = os.urandom(12)
        ciphertext = ChaCha20Poly1305(self._server_write_key).encrypt(reply_nonce, plaintext, b'')
        self.transport.write(reply_nonce + ciphertext)

        print('Close the client socket')
        self.transport.close()

loop = asyncio.get_event_loop()
coro = loop.create_server(lambda: AeadEchoServerProtocol(PW), '127.0.0.1', 8888)
server = loop.run_until_complete(coro)

print('Serving on {}'.format(server.sockets[0].getsockname()))

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()