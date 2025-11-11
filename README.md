
<center><h1> Computer Networks 2025</h1></center>

<center><h2>Federal Institute of Parana (IFPR) Professor Darlon Vassata</h2></center>
<br>
<center><h2>Felipe Barradas Sebastião, 2025</h2></center>

Versão em porguês abaixo

Here I present the summaries and class notes from my 2025 Computer Networks course with Professor Darlon at IFPR.
All content described here is based on our classes throughout the academic year, partially using the book *"Computer Networking: A Top-Down Approach"* and the website [materiais.darlon.com.br/RC](https://materiais.darlon.com.br/RC).

---

# 2nd Term

## Class 05/19/2025

* **Protocol Stack**

```
TCP/IP

    - Application
    - Transport
    - Network (IP)
    - Link
    - Physical
```

* **Machine Networks**

```
lo -> virtual network (localhost)
enum 1 -> network card
```

Commands:

```
nc -l port
nc ip port
ifconfig -> check IP settings
```

---

## Class 05/26/2025

Creating a simple web server using Docker:

```
docker run -p port:subport httpd
```

**Basic Docker Concepts**

* Image → model with execution instructions
* Container → a running image

**Useful Commands**

```
docker stop
docker rm
docker ps
docker build
```

**Dockerfile Example**

```
FROM base_image
COPY file_folder
CMD ["how to execute", "file path"]
```

---

## Class 06/02/2025

**DockerHub Login & Push**

```
docker login -u username
docker push imageName
docker pull imageName
```

**Build and Run Image**

```bash
docker build -t image_name .
docker run image_name
```

---

## Class 06/10/2025

Introduction to **Docker Compose** – a container orchestrator.

```
services:
  counter:
    build: .
  contador:
    image: isadoraizlou/counter
    environment:
      VARIABLE = X
```

### Database with Docker

```
database:
  image: mysql
  environment:
    - MYSQL_ROOT_PASSWORD=aluno
    - MYSQL_USER=aluno
    - MYSQL_PASSWORD=aluno
  ports:
    - 3306:3306
```

---

## Class 06/17/2025

### CI/CD (Continuous Integration / Continuous Delivery)

```
watchtower:
  image: containrrr/watchtower
  container_name: watchtower
  volumes:
    - /var/run/docker.sock:/var/run/docker.sock
  environment:
    - WATCHTOWER_POLL_INTERVAL=15
  command: contador
```

---

## Class 06/24/2025

Started an Apache server with Docker.
Project available in repository **FelipeBarradasCICD**.

---

## Class 07/08/2025

**Dev Containers** – development environments that avoid dependency installation on the host system.

---

## Free Project – 2nd Term

In `avaliacoes/trabalho/T2`, there is a **local network chat application**.
In `Q2`, there’s a basic explanation of **Redis**, an in-memory cache database.

---

# 3rd Term

## TCP/IP Protocol Layers

### General Structure

* Application
* Transport
* Network (Internet)
* Link (Data Link)
* Physical

---

## Application Layer

Provides direct services to user processes.

Examples:

* HTTP → for web browsers
* SMTP → for email clients

**PDU:** Message / Data

---

## Transport Layer

Manages communication **from process to process** and ensures reliable delivery.

* **TCP:** reliable and ordered
* **UDP:** faster, no verification

**PDU:** Segment

---

## Network Layer

Handles **logical addressing (IP)** and **routing**.

**PDU:** Packet

---

## Data Link Layer

Responsible for **local delivery** within the same network.

* Adds **MAC addresses**
* Controls **frame transmission**

**PDU:** Frame

---

## Physical Layer

Transmits **raw bits (0s and 1s)** through the medium.

Examples:

* Ethernet – electrical signals
* Wi-Fi – radio waves
* Fiber optics – light pulses

**PDU:** Bits

---

## Encapsulation Example

HTTP Request → TCP → IP → Frame → Bits

---

## FAQ

**Does the Data Link layer translate text into binary?**
No. Text-to-binary conversion happens at higher layers (Application layer).

**Why is DNS part of the Application layer?**
Because it provides services directly to user applications, translating domain names (e.g., `google.com`) into IP addresses.

---

## Summary Table

| Layer       | Main Function                        | Data Unit |
| ----------- | ------------------------------------ | --------- |
| Application | Services to applications             | Data      |
| Transport   | Process-to-process communication     | Segment   |
| Network     | Addressing and routing               | Packet    |
| Link        | Local communication, physical access | Frame     |
| Physical    | Transmission of bits                 | Bits      |
---

# Network Layer Class

We use IP addresses to address a network and a machine. For this address, 32 bits are reserved, which are divided into 4 groups of 8 bits, resulting in something like:

| 1 1 1 1 1 1 1 1 | 1 1 1 1 1 1 1 1 | 1 1 1 1 1 1 1 1 | 1 1 1 1 1 1 1 1 |

| 255 | 255 | 255 | 255 |

There are 3 standard classes, which are A, B, and C, and they respectively allocate 8, 16, and 24 bits reserved for the network, with the rest for the hosts. That is, class C offers only 8 bits for the host portion, limiting it to 2⁸ = 255 hosts. However, the addresses require one address for the network (in which all bits after the first x bits, according to the class, are 0) and one address for the broadcast (in which all bits are 1 and it sends to all hosts).

Note that there is a very large difference between the number of hosts offered by class B and class C. For example, class B offers 2¹⁶ - 2 hosts = 65,533, while class C offers only 253 hosts. Therefore, the following were created:

## CIDR (CLASSLESS INTER DOMAIN ROUTING)

Classless IPs, which are defined through masks and allow a better distribution between the number of networks and hosts. Note:

ADDRESS / BITS RESERVED FOR NETWORK

192.168.248.0 / 26 -> there are 26 bits for the network and 6 for hosts, which equals 2⁶ - 2 hosts

### Network addresses

They are defined as follows: the bits reserved for the network remain as they are, and the rest are filled with 0s.

### Broadcast addresses

They are defined as follows: the bits reserved for the network remain as they are, and the rest are filled with 1s.

From this content, exercises were practiced and are available in aulas/exercicios/CIDR.md


## DHCP (Dynamic Host Configuration Protocol)

* 1 - The DHCP client connects to the network and sends a *Discover* message to the server (it sends a broadcast because it doesn’t yet know who the server is).
* 2 - The server responds with an *Offer* message to the client, proposing an available IP address.
* 3 - The client sends a *Request* message confirming its choice.
* 4 - The server sends an *Acknowledgement* (*ACK*) to finalize the assignment.

It also provides the default gateway, which is the router’s address — that is, the device responsible for communicating outside the local network.

---

## NAT (Network Address Translation)

> Note: NAT is not a protocol, but rather a function performed by the router.

There is an issue with the number of available IP addresses — they are limited to around 6 billion, yet there are tens of billions of devices that connect to the Internet every day.
Therefore, NAT was created. It keeps track of the **Source Address**, **Source Port**, **Destination Address**, and **Destination Port**.
Through this, a computer with a local IP address (e.g., 192.168.250.160) can communicate outside its own network, with the router handling the translation between private and public addresses.


# Versão em Português

Aqui apresento os conteúdos e resumos das aulas de redes que tive em 2025 com o professor Darlon no IFPR.
Tudo que está descrito nesse readme é baseado nas aulas que tivemos ao decorrer do ano letivo, parte no livro *"Redes De Computadores E A Internet - Uma Abordagem TOP-DOWN"* e no site [materiais.darlon.com.br/RC](https://materiais.darlon.com.br/RC).

---

# 2° Bimestre

## Aula 19/05/2025

* Pilha de Protocolos

```
TCP/IP

    - Aplicação (conteúdo e endereço)
    - Transporte
    - Rede (IP)
    - Enlace (placa da rede)
    - Física
```

* Redes da Máquina

```
lo -> rede imaginária (localhost)
enum 1 -> placa de rede
```

```
nc -l porta
nc ip porta

nc -> comando para conexões (l = listening)
ifconfig -> ver configurações de ip da maquina
```

---

## Aula 26/05/2025

* "Criar" Servidor

```
docker run -p porta:subporta httpd
```

* Conceitos Básicos Docker

```
imagem: modelo ou projeto que tem informações para executar
container: uma imagem em execução
```

* Comandos Docker

```
docker stop -> para um container e pode despausar dps
docker rm -> remove um container sem poder reiniciá-lo
docker ps -> mostra info sobre containers em execução
docker build
```

* Dockerfile

```
FROM onde_executará
COPY arquivo_pasta
CMD ["como executar", "caminho arquivo"]
```

---

## Aula 02/06/2025

* Login no DockerHub e Push na imagem

```
docker login -u nome_usuario
docker push nomeImagem
docker pull nomeImagem
```

* Criando uma imagem e a executando

```bash
docker build -t nome_imagem .
docker run nome_imagem
```

> Obs: no Dockerfile deve-se colocar o FROM, COPY e CMD

* Listar, Remover ... Containers e Imagens

```
docker rmi <ID_img ou Nome>
docker images
docker image prune -a
```

---

## Aula 10/06/2025

Explicação sobre **Docker Compose**, um orquestrador de containers.

```
services:
  counter:
    build: .
  contador:
    image: isadoraizlou/counter
    environment:
      VARIAVEL = X
```

> Variáveis de ambiente como PATH armazenam diretórios importantes.
> O comando `echo ${PATH}` exibe seu conteúdo.

### Banco de Dados com Docker:

```
banco_dados:
  image: mysql
  environment:
    - MYSQL_ROOT_PASSWORD=aluno
    - MYSQL_USER=aluno
    - MYSQL_PASSWORD=aluno
  ports:
    - 3306:3306
```

---

## Aula 17/06/2025

### CI/CD (Continuous Integration / Continuous Delivery)

```
watchtower:
  image: containrrr/watchtower
  container_name: watchtower
  volumes:
    - /var/run/docker.sock:/var/run/docker.sock
  environment:
    - WATCHTOWER_POLL_INTERVAL=15
  command: contador
```

---

## Aula 24/06/2025

Configuração de servidor Apache em container Docker.
Trabalho disponível no repositório **FelipeBarradasCICD**.

---

## Aula 08/07/2025

**Dev Containers** – ambientes de desenvolvimento prontos sem precisar instalar dependências localmente.

---

## Trabalho Livre 2° Bimestre

Na pasta `avaliacoes/trabalho/T2` há um **chat de comunicação em rede local**.
Também há, em `Q2`, uma explicação básica sobre o uso do **Redis**, um banco de dados em memória cache.

---

# 3° Bimestre

A seguir há um resumo dos conteúdos do terceiro bimestre.

## Camadas de Protocolos TCP/IP

### Estrutura Geral

* **Aplicação**
* **Transporte**
* **Rede (ou Internet)**
* **Enlace (ou Vínculo de Dados)**
* **Física**

---

## Camada de Aplicação

Responsável por fornecer serviços de rede diretamente aos processos do utilizador.

Exemplos:

* HTTP (navegadores)
* SMTP (e-mails)

**PDU:** Mensagem/Dados

---

## Camada de Transporte

Estabelece comunicação **de processo a processo**, garantindo entrega e ordem.

* **TCP:** confiável
* **UDP:** rápido, sem verificação

**PDU:** Segmento

---

## Camada de Rede

Gerencia **endereçamento IP** e **roteamento** entre redes.

**PDU:** Pacote

---

## Camada de Enlace

Entrega local e controle de acesso físico.

* Adiciona endereços **MAC**
* Define **quadros (frames)**

**PDU:** Quadro

---

## Camada Física

Transmissão de **bits (0 e 1)** através de meios físicos.

* Ethernet (elétrica)
* Wi-Fi (rádio)
* Fibra ótica (luz)

**PDU:** Bits

---

## Exemplo de Encapsulamento

Pedido HTTP → TCP → IP → Frame → Bits

---

## FAQ

**Por que o DNS é camada de aplicação?**
Porque fornece serviços diretos às aplicações (tradução de nomes de domínio em IPs).

---

## Resumo das Camadas

| Camada     | Função Principal                         | Unidade de Dados |
| ---------- | ---------------------------------------- | ---------------- |
| Aplicação  | Serviços às aplicações                   | Dados            |
| Transporte | Comunicação entre processos              | Segmento         |
| Rede       | Endereçamento e roteamento               | Pacote           |
| Enlace     | Comunicação local e endereçamento físico | Quadro           |
| Física     | Transmissão de bits                      | Bits             |

---


# Aula Camada de Redes

Utilizamos os endereços IPs para endereçar uma rede e uma máquina. Para esse endereço são reservados 32 bits os quais são divididos em 4 grupamentos de 8 bits tendo algo parecido com:

| 1 1 1 1 1 1 1 1 | 1 1 1 1 1 1 1 1 |1 1 1 1 1 1 1 1 | 1 1 1 1 1 1 1 |

| 255 | 255 | 255 | 255 |

Existem 3 classes padrões as quais são A, B e C as quais respectivamente ofertam 8, 16 e 24 bits reservados para a rede e o resto para máquinas, ou seja, a classe C oferece apenas 8 bits para máquina limitando a apenas 2⁸=255 máquinas. Porém os endereços precisam de um endereço para a rede (o qual todos os bits são 0 após os x primeiros de acordo com a classe) e um endereço para o broadcast (o qual todos os bits são 1 e envia para todas as máquinas).

Note que há uma diferença muito grande entre a quantidade de máquinas da classe B e da classe C, por exemplo a B oferta 2¹⁶ - 2 máquinas = 65533, mas a classe C oferta apenas 253 máquinas. Logo foi criado os:

## CIDR (CLASSLESS INTER DOMAIN ROUTING)

Os IPs sem classe, que são definidos a partir de máscaras e permitem uma distribuição melhor entre quantidade de rede e máquinas, note:

ENDERECO / BITS RESERVADOS PARA REDE

192.168.248.0 / 26 -> há 26 bits para as redes e 6 para máquinas o que valem a 2⁶ - 2 máquinas

### Endereços de rede
São definidos de acordo com: os bits reservados para rede são normais e o resto preenchido por 0

### Endereços de broadcast
São definidos de acordo com: os bits reservados para rede são normais e o resto é preenchido por 1

Desse conteúdo foram praticados exercícios que estão em aulas/exercicios/CIDR.md

## DHCP (DINAMIC HOST CONTROL PROTOCOL)

 - 1 - Cliente DHCP se conecta à rede e manda um Discover para o servidor (manda broadcast pois ainda não sabe quem é o servidor).
 - 2 - O servidor responde uma solicitação apenas para o cliente com um IP possível
 - 3 - O cliente envia um request confirmando
 - 4 - O servidor faz um "acknowledgement"

Informa o gateway padrão que é o endereço do roteador, ou seja, aquele que tem a função de conversar fora da rede.

## NAT (Network Address Translation)

Note: NAT não é um protocolo mas sim parte do roteador

 Há um erro nas quantidades de endereços ips, correto? Eles são limitados a apenas 6 bilhões, mas existem dezenas de bilhoes de dispositivos que se conectam na internte todos os dias. Portanto foi criado o NAT que salva o END Origem, A Porta Origem, O End Destino e a Porta Destino, através disso um computador com IP local (192.168.250.160, v.g.) e então auxilia o roteador na comunicação fora da rede dele próprio.