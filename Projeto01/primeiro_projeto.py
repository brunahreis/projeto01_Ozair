# =====================================
# Persistência / Repositório
# =====================================

REPOSITORIO_CLIENTE = []
REPOSITORIO_ENDERECO = []
REPOSITORIO_PRODUTO = []

def persistencia_cliente_salvar(novo_cliente):
    codigo_novo_cliente = len(REPOSITORIO_CLIENTE) + 1
    # Ajuste da persistência
    novo_cliente["codigo"] = codigo_novo_cliente
    # Salvei na persistência/repositório.
    REPOSITORIO_CLIENTE.append(novo_cliente)
    return novo_cliente

def persistencia_cliente_pesquisar_todos():
    lista_clientes = list(REPOSITORIO_CLIENTE)
    return lista_clientes

def persistencia_pesquisar_pelo_codigo(codigo):
    cliente_procurado = None
    for cliente in REPOSITORIO_CLIENTE:
        if cliente["codigo"] == codigo:
            cliente_procurado = cliente
            break
    return cliente_procurado

def persistencia_endereco_salvar(novo_endereco):
    codigo_novo_endereco = len(REPOSITORIO_ENDERECO) + 1
    # Ajuste da persistência
    novo_endereco["codigo"] = codigo_novo_endereco
    # Salvei na persistência/repositório.
    REPOSITORIO_ENDERECO.append(novo_endereco)
    return novo_endereco

def persistencia_endereco_pesquisar_todos():
    lista_enderecos = list(REPOSITORIO_ENDERECO)
    return lista_enderecos

def persistencia_pesquisar_pelo_codigo_endereco(codigo):
    endereco_procurado = None
    for endereco in REPOSITORIO_ENDERECO:
        if endereco["codigo"] == endereco:
            endereco_procurado = endereco
            break
    return endereco_procurado

def persistencia_produto_salvar(novo_produto):
    codigo_novo_produto = len(REPOSITORIO_PRODUTO) + 1
    # Ajuste da persistência
    novo_produto["codigo"] = codigo_novo_produto
    # Salvei na persistência/repositório.
    REPOSITORIO_PRODUTO.append(novo_produto)
    return novo_produto

def persistencia_produto_pesquisar_todos():
    lista_produtos = list(REPOSITORIO_PRODUTO)
    return lista_produtos

def persistencia_pesquisar_pelo_codigo_produto(codigo):
    produto_procurado = None
    for produto in REPOSITORIO_PRODUTO:
        if produto["codigo"] == produto:
            produto_procurado = produto
            break
    return produto_procurado

# =====================================
# Regras / Casos de Uso / BO
# =====================================

def regra_cadastrar_novo_cliente(novo_cliente):
    # TODO Validar o novo cliente
    novo_cliente = persistencia_cliente_salvar(novo_cliente)
    return novo_cliente

def regras_pesquisar_todos_clientes():
    return persistencia_cliente_pesquisar_todos()

def regras_cliente_pesquisar_pelo_codigo(codigo):
    return persistencia_pesquisar_pelo_codigo(codigo)

def regra_cadastrar_novo_endereco(novo_endereco):
    # TODO Validar o novo endereco
    novo_endereco = persistencia_endereco_salvar(novo_endereco)
    return novo_endereco

def regras_pesquisar_todos_enderecos():
    return persistencia_endereco_pesquisar_todos()

def regras_produto_pesquisar_pelo_codigo(codigo):
    return persistencia_pesquisar_pelo_codigo_produto(codigo)

def regra_cadastrar_novo_produto(novo_produto):
    # TODO Validar o novo endereco
    novo_produto = persistencia_produto_salvar(novo_produto)
    return novo_produto

def regras_pesquisar_todos_produtos():
    return persistencia_produto_pesquisar_todos()

def regras_produto_pesquisar_pelo_codigo(codigo):
    return persistencia_pesquisar_pelo_codigo_produto(codigo)



# =====================================
# API Rest / Controlador
# =====================================
# para o Projeto01 cliente

from fastapi import FastAPI
import pydantic
from pydantic import BaseModel
from typing import List


app = FastAPI()

OK = "OK"
FALHA = "FALHA"

# ----- rotas / caminhos / salas

# ** Rotas **
    
@app.get("/")
async def bem_vinda():
    site = "Seja bem vinda"
    return site.replace('\n', '')
   
class NovoCliente(BaseModel):
    codigo: int
    nome: str
    email: str
    senha: str

@app.post("/clientes")
async def criar_novo_cliente(novo_cliente: NovoCliente):
    if novo_cliente.codigo in novo_cliente:
        return FALHA
    novo_cliente = regra_cadastrar_novo_cliente(novo_cliente.dict())
    return OK


@app.get("/clientes/{nome}")
async def retornar_usuario_com_nome(nome: str):
    return FALHA

@app.get("/clientes/{codigo}")
async def retornar_pesquisa_cliente_pelo_codigo(codigo: int):
    if codigo in persistencia_pesquisar_pelo_codigo:
        return persistencia_pesquisar_pelo_codigo[codigo]
    return FALHA

@app.delete("/clientes")
async def deletar_cliente(codigo: int):
    if codigo in persistencia_pesquisar_pelo_codigo:
        return OK
    return FALHA

# **************************************************************

class Endereco(BaseModel):
    rua: str
    cep: str
    cidade: str
    estado: str
    
class ListaDeEnderecosDoUsuario(BaseModel):
    cliente: NovoCliente
    enderecos: List[Endereco] = []
    
@app.post("/clientes/{codigo}/endereco")
async def criar_novo_endereco(novo_endereco: Endereco):
    if novo_endereco.codigo in criar_novo_endereco:
        return FALHA
    novo_endereco = regra_cadastrar_novo_endereco(novo_endereco.dict())
    return OK

@app.get("/clientes/{codigo}/endereco")
async def retornar_endereco_completo(nome: str):
    return FALHA

@app.get("/clientes/{codigo}/endereco{codigo}")
async def retornar_pesquisa_endereco_pelo_codigo(codigo: int):
    if codigo in persistencia_pesquisar_pelo_codigo_endereco:
        return persistencia_pesquisar_pelo_codigo_endereco[codigo]
    return FALHA

@app.delete("/clientes/{codigo}/endereco")
async def deletar_endereco(codigo: int):
    if codigo in persistencia_pesquisar_pelo_codigo_endereco:
        return OK
    return FALHA

# *************************************************************

class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    
@app.post("/produtos")
async def criar_novo_produto(novo_produto: Produto):
    if novo_produto.codigo in criar_novo_produto:
        return FALHA
    novo_produto = regra_cadastrar_novo_produto(novo_produto.dict())
    return OK

@app.get("/produtos")
async def retornar_nome_produto(nome: str):
    return FALHA

@app.get("/produtos/{codigo}")
async def retornar_pesquisa_produto_pelo_codigo(codigo: int):
    if codigo in persistencia_pesquisar_pelo_codigo_produto:
        return persistencia_pesquisar_pelo_codigo_produto[codigo]
    return FALHA

@app.delete("/produtos/{codigo}")
async def deletar_produto(codigo: int):
    if codigo in persistencia_pesquisar_pelo_codigo_produto:
        return OK
    return FALHA

# *************************************************************

class CarrinhoDeCompras(BaseModel):
    id_cliente: int
    id_produto: List[Produto] = []
    preco_total: float
    quantidade_de_produtos: int
    
preco_total = sum()
quantidade_de_produtos = sum()

@app.post("/carrinho/{id_cliente}/{id_produto}/")
async def adicionar_carrinho(id_cliente: int, id_produto: int):
    return OK


@app.get("/carrinho/{id_cliente}")
async def retornar_carrinho(id_cliente: int):
    return CarrinhoDeCompras


@app.get("/carrinho/{id_cliente}")
async def retornar_total_carrinho(id_cliente: int):
    if retornar_total_carrinho in id_cliente:
        return quantidade_de_produtos, preco_total
    return FALHA


@app.delete("/carrinho/{id_cliente}")
async def deletar_carrinho(id_cliente: int):
    if id_cliente in persistencia_pesquisar_pelo_codigo:
        return OK
    return FALHA