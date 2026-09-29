from http.server import HTTPServer, SimpleHTTPRequestHandler

server = HTTPServer(("127.0.0.1", 8000), SimpleHTTPRequestHandler)

print("Server running at http://127.0.0.1:8000")
print("Register No: 26001912")
print("Name: Faheema")

server.serve_forever()