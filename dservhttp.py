import http.server
import socketserver
import os
import sys

# Define a porta
PORTA = 8048

# Garante que o servidor vai rodar na pasta onde o .exe estiver
pasta_atual = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
os.chdir(pasta_atual)

Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORTA), Handler) as httpd:
        print(f"Servidor rodando! Acesse http://localhost:{PORTA}")
        print("Para encerrar, feche esta janela.")
        httpd.serve_forever()
except OSError as e:
    print(f"Erro: A porta {PORTA} pode já estar em uso.")
    input("Pressione ENTER para sair...")