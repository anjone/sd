import paramiko
import socket
import base64

#proxy = paramiko.ProxyCommand("CONNECT {}:{} HTTP/1.1\r\nProxy-Authorization: Basic <credentials>\r\n\r\n".format(*target))

'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
proxy = ("10.228.110.21", 8002)
sock.connect(proxy)
proxy_auth = b'jiangqizhou:Cpic123456'
proxy_cred = base64.b64encode(proxy_auth)

cmd_connect = "CONNECT {}:{} HTTP/1.1\r\nProxy-Authorization: Basic {}\r\n\r\n".format("58.250.152.93", "27386", proxy_cred)

sock.sendall(cmd_connect.encode("utf8"))

print(sock.recv(1024))

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="58.250.152.93",port=27386,username='sftp',password='sftp_tai@2017#',sock=sock)
sftp_client = client.open_sftp()
print(sftp_client.listdir())
'''

# another method
import urllib
import http.client

proxy_uri = "http://jiangqizhou:Cpic123456@10.228.110.21:8002"
url = urllib.parse.urlparse(proxy_uri)
http_con = http.client.HTTPConnection(url.hostname,url.port)

headers = {}
if url.username and url.password:
    auth = '%s:%s' % (url.username, url.password)
    headers['Proxy-Authorization'] = "Basic {}".format(base64.b64encode(auth.encode("ascii")))
    print(headers)

http_con.set_tunnel("58.250.152.93", 27386, headers)
http_con.connect()
sock = http_con.sock

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="58.250.152.93",port=27386,username='sftp',password='sftp_tai@2017#',sock=sock)
sftp_client = client.open_sftp()
print(sftp_client.listdir())