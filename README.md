# Projeto Python Loja Virtual! :department_store:
Projeto desenvolvido por mim durante o curso de Desenvolvimento Web na Trybe. Divulgado aqui como portfólio de aprendizado.

<details>
<summary><strong>Objetivos do projeto:</strong></summary>
 
  * Criar um programa que simula uma loja virtual elaborando códigos que façam o uso de tipagem estática em Python.
  * Verificar se sou capaz de:
    * Elaborar códigos que façam o uso de tipagem estática em Python.
    * Elaborar códigos utilizando a linguagem Python que utilizam Classes, Construtores, Instâncias, Atributos e Métodos.
    * Examinar um projeto em Python que utiliza o paradigma de Programação Orientada a Objetos.
    * Escrever código Python que passa em testes de integração.
</details>
<details>
<summary><strong> Requisitos do projeto:</strong></summary>

  * Desenvolver a classe Produto.
  * Desenvolver a classe Estoque.
  * Testar o construtor/inicializador da classe Livro.
  * Testar a descrição do Livro.

</details>
  
## Rodando o projeto localmente

Para rodar o projeto em sua máquina, abra seu terminal, crie um diretório no local de sua preferência com o comando `mkdir` e acesse o diretório criado com o comando `cd`:

```bash
mkdir meu-diretorio &&
cd meu-diretorio
```

Clone o projeto com o comando `git clone`:

```bash
git clone https://github.com/marcosadrianoti/tb-python-poo-pythonico
```

Acesse o diretório do projeto com o comando `cd`:

```bash
cd tb-python-poo-pythonico
```

crie o ambiente virtual:
```bash
python3 -m venv .venv
```

Ative o ambiente virtual:
```bash
source .venv/bin/activate
```

Instale as dependências no ambiente virtual:
```bash
python3 -m pip install -r dev-requirements.txt
```

Execute os testes:
```bash
python3 -m pytest
```
