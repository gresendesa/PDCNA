# CPDCNA - Programa de Detecção de Crise Nervosa Autista

Este software implementa a aplicação que armazena e processa dos dados transmitidos através dos leitores de dados. 

## Instância em produção
Você pode acessar a istância deste projeto 

## Como instalar

## Instalação (uma única vez) e execução
Depois que baixar o repositório, faça o seguinte para instalar o ambiente na sua máquina (Exemplo aplica-se a sistemas linux baseados em Debian). Note que `venvcc` é um nome de exemplo. Você pode substituir pelo nome que quiser, sem prejuízo funcional.
 1. Primeiro instale o virtualenv
 ~~~shell
 apt install virtualenv
 ~~~
 2. Crie um ambiente virtual 
 ~~~shell
 virtualenv -p python3 venvcc
 ~~~
 3. Inicie o ambiente virtual
 ~~~shell
 source venvcc/bin/activate
 ~~~
 4. Instale as dependências
 ~~~shell
 pip install -r requirements.txt
 ~~~
 5. Lide com as migrations (isso criará o seu banco de dados).
 ~~~shell
 cd pdcna/
 python manage.py makemigrations
 python manage.py migrate
 ~~~
 6. Execute. Isso criará um servidor em sua porta 8080
 ~~~shell
 python manage.py runserver
 ~~~

## Descrição da API


### Participante

- Inserir um registro na base de dados
```http
PUT /dados/participante HTTP/1.1
Content-Type: application/json
Host: 127.0.0.1:8000
Content-Length: 51

{
	"nome":"nome",
	"data_nascimento": "YYYY-MM-DD"
}	
```

- Pegar todos os registros da base de dados
```http
GET /dados/participante HTTP/1.1
Host: 127.0.0.1:8000
```

### Levantamento

- Inserir um registro na base de dados
```http
PUT /dados/levantamento HTTP/1.1
Content-Type: application/json
Host: 127.0.0.1:8000
Content-Length: 45

{
	"data":"YYYY-MM-DD",
	"participante": 1
}	
```

- Pegar todos os registros da base de dados
```http
GET /dados/levantamento HTTP/1.1
Host: 127.0.0.1:8000
```

### Levantamento_dados

- Inserir um registro na base de dados
```http
PUT /dados/levantamento_dados HTTP/1.1
Content-Type: application/json
Host: 127.0.0.1:8000
Content-Length: 65

{
	"levantamento":1,
	"variavel": "varname",
	"valor": 3141592
}	
```

- Pegar todos os registros da base de dados
```http
GET /dados/levantamento_dados HTTP/1.1
Host: 127.0.0.1:8000
```
