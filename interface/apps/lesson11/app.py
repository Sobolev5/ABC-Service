import pprint
import os
import sys
import socketserver
from simple_print import sprint
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
from wsgiref.handlers import BaseHandler
from io import BytesIO


def main(request):
    sprint("main request={request}", c="green")
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]  
    DEBUG = os.getenv("DEBUG")
    response = request * 5
    response += f"Hello from LESSON11 DEBUG={DEBUG}"
    return status, headers, response.encode()


def django_wsgi(environ, start_response):
    sprint("django_wsgi", c="green")

    # https://stackoverflow.com/questions/1783383/how-do-i-copy-wsgi-input-if-i-want-to-process-post-data-more-than-once 
    request = ""
    try:
        length = int(environ.get('CONTENT_LENGTH', '0'))
        byte_obj = BytesIO(environ['wsgi.input'].read(length))  
        request = byte_obj.getvalue().decode()
    except Exception as e:
        print(e)
    setup_testing_defaults(environ)

    status, headers, response = main(request)
    start_response(status, headers)
    return [response]


with make_server('', 10000, django_wsgi) as server:
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()


# class MyTCPHandler(socketserver.BaseRequestHandler):

#     def handle(self):
#         # self.request is the TCP socket connected to the client
#         self.data = self.request.recv(1024).strip()
#         print("{} wrote:".format(self.client_address[0]))
#         print(self.data)
          
#         response = b'HTTP/1.0 200 OK\n\nHello World'
#         self.request.sendall(response)

# if __name__ == "__main__":
#     with socketserver.TCPServer(("0.0.0.0", 10004), MyTCPHandler) as server:
#         server.serve_forever()    