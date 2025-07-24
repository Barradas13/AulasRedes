# 🗨️ ConexaoChat

ConexaoChat é um projeto de chat local que permite a troca de mensagens entre pessoas conectadas na **mesma rede**, com persistência de dados via **MySQL** e atualizações em tempo real utilizando **Redis**. A interface web foi construída com **Flet**, proporcionando uma aplicação leve e interativa acessível pelo navegador.

---

## 🧰 Tecnologias e Ferramentas Utilizadas

- 🐳 **Docker + Docker Compose** – Orquestração e isolamento dos serviços.
- 🐬 **MySQL** – Armazenamento persistente das mensagens.
- 🔁 **Redis** – Comunicação em tempo real via pub/sub.
- 🌐 **Flet** – Criação da interface web reativa.
- 🐍 **Python** – Lógica da aplicação e manipulação de dados.

---

## 🏗️ Arquitetura da Aplicação

A arquitetura do ConexaoChat é composta por três serviços principais:

- Banco de Dados (Armazena os dados)
- Servidor (Gere os clientes, mensagens e interface)
- Cliente (notifica com Redis)

Além disso dois atores principais:

- Host: responsável por subir a infraestrutura completa via Docker Compose e manter o servidor aberto.
- Cliente: Ele apenas executa o container do chat apontando para o IP do host para conectar no servidor.


Banco de Dados ---MySQL---> Servidor <---Redis--- Cliente


- O **host** atua como servidor (responsável por subir os containers MySQL, Redis e App) e também pode enviar mensagens.
- Os **clientes** acessam a aplicação via navegador conectando-se ao IP do host, e interagem em tempo real.
- **Mensagens são salvas no MySQL**, e **notificações são enviadas pelo Redis** para atualizar dinamicamente a interface dos usuários.

---

## 🚀 Instruções de Uso

### 📌 1. Configuração do Host (Servidor)

#### Passo 1: Criar o arquivo `.env` na raiz do projeto com as variáveis:

```env
DB_ROOT_PASSWORD=senhadocomputador
DB_USER=root
DB_PASSWORD=senhadocomputador
DB_HOST_SQL=banco_dados
DB_HOST_REDIS=redis
DB_PORT=3306
DB_NAME=ConexaoChat
```

#### Passo 2: Subir os containers

```
    docker compose up
```

#### A aplicação estará disponível em:
```
    http://localhost:8550
```

### 📌 2. Execução do Cliente (Usuários na mesma rede)

#### Comando para execução (em uma linha):
```
    docker run -it -e DB_HOST_SQL=192.168.X.X -e DB_HOST_REDIS=192.168.X.X -e DB_PORT=33306 -e DB_USER=root -e DB_PASSWORD=senhadocomputador -e DB_NAME=ConexaoChat -p 8550:8550 barradas13/chat

    Substitua 192.168.X.X pelo IP local do host.
    Substitua senhadocomputador pela senha do banco.
```

## Observações

- Certifique-se de que todos os dispositivos estejam na mesma rede local.

- Redis é utilizado apenas para notificações em tempo real (Pub/Sub).

- MySQL armazena de forma persistente todas as mensagens do chat.