API de Vendas

API desenvolvida em **FastAPI** para gerenciar informações de vendas de produtos.  
Permite consultar a quantidade total de vendas e os detalhes de cada venda pelo seu ID, servindo como exemplo de uma API local rodando em `http://127.0.0.1:8000/`.

---

##  Como executar o projeto

### Pré-requisitos

- Python instalado
- FastAPI
- Uvicorn

Você pode instalar as dependências necessárias com:

```bash
pip install fastapi uvicorn

# Clone este repositório
git clone https://github.com/seu-usuario/nome-do-repo.git

# Entre na pasta
cd nome-do-repo

# Inicie o servidor FastAPI com Uvicorn
uvicorn main:app --reload

O projeto estará disponível em:
http://127.0.0.1:8000
