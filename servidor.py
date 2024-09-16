import os
import threading
import time
import random
# Pipes para números e strings
NUM_REQ_PIPE = '/tmp/num_req_pipe'
NUM_RESP_PIPE = '/tmp/num_resp_pipe'
STR_REQ_PIPE = '/tmp/str_req_pipe'
STR_RESP_PIPE = '/tmp/str_resp_pipe'

# Criar pipes (FIFO) de requisição e resposta para números
if not os.path.exists(NUM_REQ_PIPE):
    os.mkfifo(NUM_REQ_PIPE)

if not os.path.exists(NUM_RESP_PIPE):
    os.mkfifo(NUM_RESP_PIPE)

# Criar pipes (FIFO) de requisição e resposta para strings
if not os.path.exists(STR_REQ_PIPE):
    os.mkfifo(STR_REQ_PIPE)

if not os.path.exists(STR_RESP_PIPE):
    os.mkfifo(STR_RESP_PIPE)

# Função para responder requisições de números
def handle_number_requests():
    while True:
        with open(NUM_REQ_PIPE, 'r') as num_pipe:
            request = num_pipe.read().strip()
            if request:
                print(f"Servidor: Recebida solicitação de número: {request}")
                # Gera um número aleatório entre 1 e 100
                response = f"Número gerado: {random.randint(1, 100)}\n"
                time.sleep(1)  # Simula o processamento
                with open(NUM_RESP_PIPE, 'w') as num_pipe_w:
                    num_pipe_w.write(response)
                print("Servidor: Resposta de número enviada.")

# Função para responder requisições de strings
def handle_string_requests():
    while True:
        with open(STR_REQ_PIPE, 'r') as str_pipe:
            request = str_pipe.read().strip()
            if request:
                print(f"Servidor: Recebida solicitação de string: {request}")
                response = f"String resposta: 'Olá Cliente!'\n"  # Exemplo de string
                time.sleep(1)  # Simula o processamento
                with open(STR_RESP_PIPE, 'w') as str_pipe_w:
                    str_pipe_w.write(response)
                print("Servidor: Resposta de string enviada.")

# Função principal do servidor que cria o pool de threads
def start_server():
    print("Servidor iniciado...")
    
    # Criar pool de threads
    threads = []
    
    # Criar thread para requisições de números
    t_number = threading.Thread(target=handle_number_requests)
    threads.append(t_number)
    
    # Criar thread para requisições de strings
    t_string = threading.Thread(target=handle_string_requests)
    threads.append(t_string)

    # Iniciar threads
    for t in threads:
        t.start()

    # Manter o servidor rodando
    for t in threads:
        t.join()

if __name__ == "__main__":
    start_server()