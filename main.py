from fastapi import FastAPI 

vendas = {
    1: {"item": "livro", "preco": 29.99, "quantidade": 10},
    2: {"item": "mouse", "preco": 24.99, "quantidade": 20},
    3: {"item": "teclado", "preco": 49.99, "quantidade": 15},
    4: {"item": "monitor", "preco": 499.99, "quantidade": 5},
    5: {"item": "cabo HDMI", "preco": 34.99, "quantidade": 50},
    6: {"item": "webcam", "preco": 99.99, "quantidade": 8},
    7: {"item": "fone de ouvido", "preco": 79.99, "quantidade": 12},
}

app = FastAPI()
@app.get("/")

def home():
    return {" Quantidade de vendas: ": len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
    return vendas[id_venda]
else:
    return {"Erro": "ID venda inexistente."}