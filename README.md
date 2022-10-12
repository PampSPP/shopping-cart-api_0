<div align=center>

</div>
<img style="center;" src="./extras/banner_PyToys.gif">
</div>
	
# PyToys- Desafio final]

</div>


<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"/>
  <img src=https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white/>
</p>


## <img style="left;" src="./extras/robo_t.png"> Objetivo do projeto

Esse projeto tem como objetivo a criação de um serviço de carrinho de compras com o tema brinquedo utilizando arquitetura REST API, a partir do framework fastAPI, onde os registros são salvos no banco de dados MongoDB. 


<p align="center">
  <a href="#heavy_check_mark-requisitos-funcionais">Requisitos funcionais</a>&nbsp;&nbsp;|&nbsp;
  <a href="#-squad-sparck-girls">Colaboradoras</a>
</p>


## <img style="left;" src="./extras/cabeca.png"> Requisitos funcionais

API com as seguintes funcionalidades:

- Gerenciamento de clientes: Cadastro, busca, atualização de senha e remoção;
- Gerenciamento de endereços: Cadastro e busca;
- Gerenciamento de produtos: Cadastro, pesquisa, atualização e remoção;
- Gerenciamento de carrinho de compras: Criação, inclusão/remoção de produtos e remoção do carrinho;
- Exibição de pedidos já finalizados.

## <img style="left;" src="./extras/pingu_t.png"> Regras de negócio


- Cada cliente terá seu próprio cadastro, validado pelo e-mail;
- Para atualização de senha o cliente precisa fornecer o e-mail junto a nova senha;
- Cada cliente poderá cadastrar quantos endereços quiser;
- Para atualização de produtos é necessário fornecer o código correspondente e a informação que ele deseja atualizar;
- Cada cliente poderá conter apenas UM carrinho de compras aberto, validado pelo e-mail;
- A quantidade de carrinhos fechados por cliente é ilimitada;
- Um carrinho de compras aberto não precisa necessariante possuir produtos;
- A partir do momento que o usuário passa para o carrinho aberto o parametro pay como True, os produtos que estavam dentro dele vão para um carrinho fechado e esse carrinho aberto é excluído.
- No carrinho de compras fechado não será possível fazer alteração de produtos, pois ele é um pedido que o usuário finalizou anteriormente.


## <img style="left;" src="./extras/piao_t.png"> Rodando o projeto na sua máquina


Passo a passo para execução do projeto:

1) Criar um arquivo .env na raiz do projeto para configuração das variáveis de ambiente do banco de dados.

2) Criar ambiente virtual

```
Windows: python3 -m venv venv
Linux: virtualenv venv
```

3) Ativar ambiente virtual

```
Windows: venv\Scripts\activate.bat
Linux: source venv/bin/activate
```



1) Instalar as dependências
```
pip install -r requirements.txt
pip install -r requirements-test.txt
```

5) Subir o servidor FastApi
```
uvicorn --reload main:app
```


## <img style="left;" src="./extras/blocos_t.png"> Documentação Swagger

## <img style="left;" src="./extras/dino_t.png">Banco de dados

## Testes

## <img style="left;" src="./extras/girls2.png"> Tribo PyToys

<p align="center">
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/HozaniaB">
        <img src="https://github.com/HozaniaB.png" width="100px;" alt="Foto de Hozania"/><br>
        <sub>
          <b>Hozania Barnabé</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/liviamrocha">
        <img src="https://github.com/liviamrocha.png" width="100px;" alt="Foto de Livia"/><br>
        <sub>
          <b>Livia Rocha</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/palomasantos">
        <img src="https://github.com/palomasantos.png" width="100px;" alt="Foto de Paloma"/><br>
        <sub>
          <b>Paloma Santos</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/PampSPP">
        <img src="https://github.com/PampSPP.png" width="100px;" alt="Foto de Pâmela Czyziw"/><br>
        <sub>
          <b>Pâmela Czyziw</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
<p>



## <img style="left;" src="./extras/boneca_t.png">Links úteis:
[Python](https://docs.python.org/3/)
[FastAPI](https://fastapi.tiangolo.com/)
[MongoDB](https://www.mongodb.com/docs/)
[Swagger](https://swagger.io/docs/)
