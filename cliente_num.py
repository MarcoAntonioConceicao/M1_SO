import os
import time

NUM_REQ_PIPE = '/tmp/num_req_pipe'
NUM_RESP_PIPE = '/tmp/num_resp_pipe'

def request_number():
    # Enviar solicitação de número
    with open(NUM_REQ_PIPE, 'w') as num_pipe:
        num_pipe.write("Request number\n")
    
    # Ler resposta
    with open(NUM_RESP_PIPE, 'r') as num_pipe:
        response = num_pipe.read().strip()
        print(f"Cliente: Resposta recebida -> {response}")

if __name__ == "__main__":
    while True:
        request_number()
        time.sleep(2)  # Intervalo entre requisições