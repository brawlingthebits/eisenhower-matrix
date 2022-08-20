# eisenhower-matrix
API da matriz de Eisenhower, que auxilia a priorização de tarefas de acordo com o grau de urgência e importância.

## Como rodar esta aplicação?

### 1. Primeiramente, clone este repositório na sua máquina e acesse o mesmo pelo terminal. 

### 2. Será necessário ter o Python a partir da terceira versão instalado. Então, crie um ambiente virtual com o Python:

```shell
python -m venv venv
```

### 3. Entre no ambiente virtual criado:

```shell
. venv/bin/activate
```

### 4. Instale todas as dependências necessárias para que a aplicação rode.

```shell
pip install -r requirements.txt
```

### 5. Crie um arquivo .env e o preencha com seus dados a partir do .env.example

### 6. Rode as migrations após criar uma database num banco de dados SQL da sua preferência

```shell
flask db run
```

### 7. Agora você tem acesso às rotas na sua máquina.
