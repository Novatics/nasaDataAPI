# Microserviço de Extração
Extração e distribuição de dados de satélites da NASA

# Getting started

Antes de tudo, você precisa instalar [docker](https://docs.docker.com/install/) e [docker-compose](https://docs.docker.com/compose/install/)

# Rodando a aplicação

Clone o repositório
```bash
$ git clone https://github.com/Novatics/nasaDataAPI
```

Acesse o diretório principal da aplicação
```bash
$ cd nasaData
```
Crie o arquivo .env
```bash
$ touch .env
```

Copie e cole as linhas abaixo no .env
```
POSTGRES_USER=extractapi
POSTGRES_PASSWORD=extractapi123
POSTGRES_DB=extractapi
POSTGRES_HOST=db-extract
PORT=8000
```

Rode a aplicação

```bash
$ (sudo) docker-compose up
```

And you are good to go! o/
