<center><h1> Redes de Computadores 2025</h1></center>

<center><h2>Federal Institute of Parana (IFPR) Professor Darlon Vassata</h2></center>
<br>
<center><h2>Felipe Barradas Sebastião, 2025</center>

Aqui apresento os conteúdos e resumos das aulas de redes que tive em 2025 com o professor Darlon no IFPR. Tudo que está descrito nesse readme é baseado nas aulas que tivemos ao decorrer do ano letivo, parte no livro "Redes De Computadores E A Internet - Uma Abordagem TOP-DOWN" e no site https://materiais.darlon.com.br/RC.

# 2° Bimestre

## Aula 19/05/2025

- Pilha de Protocolos

```
TCP/IP

    -Aplicação (conteúdo e endereço)
    -Transporte
    -Rede (IP)
    -Enlace (placa da rede)
    -Física
```

- Redes da Máquina
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



## Aula 26/05/2025

- "Criar" Servidor

```
    docker run -p porta:subporta httpd
```

- Conceitos Básicos Docker

```
imagem: modelo ou projeto que tem informações para executar
containter: uma imagem em execução
```


- Comandos Docker

```
docker stop -> para um container e pode despausar dps
docker rm -> remove um container sem poder reiniciá-lo
docker ps -> mostra info sobre containers em execução
docker build
```


- Dockerfile

```
FROM onde_executará

COPY arquivo_pasta

CMD ["como executar", "caminho arquivo"]

```


## Aula 02/06/2025

- Login no DockerHub e Push na imagem

```
    doker login -u nome_usuario

    docker push nomeImagem

    docker pull nomeImagem
```


- Criando uma imagem e a executando

```bash
    docker build -t nome_imagem . // cria uma imagem a partir d que está escrito no Dockerfile e coloca o nome


    docker run nome_imagem // roda a imagem


.:obs no Dockerfile deve se colocar o FROM o COPY e o CMD
```

- Listar, Remover ... Containers e Imagens

```
    docker rmi <ID_img ou Nome>
    docker images -> mostra as imagens locais

    docker image (system - tudo) prune -a -> remove imagens não utilizadas

```

## Aula 10/06/2025

Note que para cada container precisamos realizar um processo com diversos parâmetros ... por isso existe o orquestrador, que irá manipular diversos containers, esse é o compose.yaml

Dentro do compose:

docker composer [comando] 
ex: docker compose up -> executa o compose

```
services: // lista de containers
    counter: // diz o nome da imagem
        build: . // fala que para contruir irá utilizar o dockerfile da pasta atual
    contador: // nome da imagem
        image: isadoraizlou/counter // diz para pegar a imagem no dockerhub
        environment: // para falar coisas do ambiente do container
            VARIAVEL = X // para adicionar uma variável ao ambiente

```

.: obs: variáveis de ambiente, ex: PATH tem todos os caminhos de executáveis importantes, faça um echo ${PATH} e verá. shellshock -> bug nas variáveis do ambiente

### Banco de dados com docker:
Podemos utilizar banco de dados mysql por exemplo mesmo sem ter o mysql baixado com o seguinte:

```
  banco_dados:
    image: mysql
    environment:
      - MYSQL_ROOT_PASSWORD=aluno
      - MYSQL_USER=aluno
      - MYSQL_PASSWORD=aluno
    ports:
      - O primeiro numero vai para o docker : O segundo vai para o container
```


## Aula 17/06/2025

### CI/CD (Coninuous Integration/Continuous Deliver)

CI/CD significa atualizar o software enquanto ele executa, utilizaremos para isso o containrrr/watchtower -> torre de observação que irá verificar quando atualizou

```
    watchtower:
        image: containrrr/watchtower // imagem desenvolvida para isso
        container_name: watchtower // alterando nome
        volumes: // para compartilhar: o arquivo antes dos ":" é disponivel com o nome apos os ":"
        - /var/run/docker.sock:/var/run/docker.sock // dá o caminho para o whatchtower executar nosso docker no kernel
        environment:
        - WATCHTOWER_POLL_INTERVAL = 15 //  a cada quanto tempo ele irá verificar
        command: contador // passa o container que irá verificar
```

note que só funcionará para as máquinas que executam com o watchtower

## Aula 24/06/2025

Iniciamos um servidor com apache e colocamos ele com o docker, o trabalho está no repositorio FelipeBarradasCICD

## Aula 08/07/2025

Dev Containers -> ambientes de desenvolvimento para não precisar ficar instalando as dependências..

## Trabalho Livre 2° Bimestre

Dentro da pasta avaliações/trabalho/T2 há um chat de comunicação em computadores da rede local as instruções de como usar estão disponíveis no readme dentro do trabalho. Além disso, dentro de Q2 na mesma pasta há uma explicação básica da utilização do redis, um banco de dados em memória cache.


# 3° Bimestre

A seguir há um resumo dos conteúdos do terceiro bimestre.

## Camadas de Protocolos TCP/IP

## Estrutura Geral

* **Aplicação**
* **Transporte**
* **Rede (ou Internet)**
* **Enlace (ou Vínculo de Dados)**
* **Física**

## Camada de Aplicação

Essencialmente, esta camada pega nos dados gerados por uma aplicação (como um pedido para aceder a uma página web) e formata-os de acordo com um protocolo específico (como o **HTTP**) para que a aplicação correspondente no dispositivo de destino (o servidor web) possa compreendê-los e responder.

### Função Principal

Fornecer serviços de rede diretamente aos processos do utilizador.

* Quando o navegador quer obter uma página web, ele usa o protocolo **HTTP**.
* Quando envia um e-mail, o cliente de e-mail usa o **SMTP**.

### PDU (Unidade de Dados de Protocolo)

A unidade de dados é chamada **mensagem** ou **dados** — o conteúdo bruto que a aplicação quer enviar.

> **Resumo:** A camada de Aplicação define *o que* está a ser comunicado — como escolher a língua e o assunto antes de uma conversa.


## Camada de Transporte

A Camada de Transporte (Camada 4) atua como **gestora de tráfego** para os dados.
Ela estabelece comunicação **de processo a processo** — garantindo que os dados cheguem ao **programa certo** dentro do computador.

### Funções Principais

1. **Segmentação e Remontagem**
   Divide mensagens grandes em **segmentos** menores, numerados para remontagem no destino.

2. **Controlo de Fluxo e Fiabilidade**

   * **TCP (Transmission Control Protocol):** serviço fiável e ordenado.
     Usado para e-mail, web e transferência de ficheiros.
   * **UDP (User Datagram Protocol):** serviço rápido e sem verificação.
     Usado para streaming, jogos e chamadas VoIP.

> **Resumo:** A camada de Transporte pega os dados da aplicação, adiciona números de porta e entrega-os à próxima camada.


## Camada de Rede (ou Internet)

Responsável por **endereçamento lógico** e **roteamento** — é o *sistema postal global* da internet.

### Funções

* **Endereçamento IP:**
  Cada dispositivo tem um endereço IP.
  A camada adiciona cabeçalhos com IP de origem e destino.
  → Unidade de dados: **Pacote**
* **Roteamento:**
  Determina o melhor caminho de roteadores até o destino — como um GPS para dados.

> **Resumo:** A camada de Rede encapsula os segmentos em pacotes e os envia pela internet.


## Camada de Enlace (ou Vínculo de Dados)

Responsável pela **entrega local** dentro da mesma rede.

### Funções

* **Endereçamento Físico:**
  Coloca os pacotes em quadros (**frames**) e adiciona endereços **MAC**.
* **Controlo de Acesso ao Meio:**
  Evita colisões entre dispositivos na mesma rede.

### Endereço MAC

* **Formato:** `00:1A:2B:3C:4D:5E`
* **Função:** Identifica dispositivos dentro da rede local.

> **Resumo:** A Camada de Rede usa IP para roteamento global, e a Enlace usa MAC para entrega local.


## Camada Física

Responsável por transmitir e receber **bits brutos (0s e 1s)** através do meio físico.

### Exemplos

* **Ethernet:** define voltagem elétrica.
* **Wi-Fi:** define ondas de rádio.
* **Fibra ótica:** define pulsos de luz.

> **Resumo:** A camada Física é a engenharia da transmissão — converte quadros em sinais e vice-versa.


## Exemplo de Encapsulamento

**Cenário:** Pedido HTTP para `pudim.com`

### Camada de Aplicação

* Cria a mensagem:

  ```
  GET / HTTP/1.1
  Host: pudim.com
  ```
* **PDU:** Dados / Mensagem

### Camada de Transporte

* Usa **TCP** (porta 80 para HTTP)
* Adiciona cabeçalho TCP (porta de origem, destino, sequência)
* **PDU:** Segmento

### Camada de Rede (Internet)

* Adiciona cabeçalho IP (origem e destino)
* Exemplo:

  * Origem: `200.150.10.5`
  * Destino: `177.54.148.81`
* **PDU:** Pacote

### Camada de Enlace

* Adiciona cabeçalho e trailer com MACs

  * MAC Origem: placa do computador
  * MAC Destino: router local
  * Trailer: código CRC
* **PDU:** Quadro (Frame)

### Camada Física

* Converte o quadro em bits e sinais (elétricos, rádio ou luz)
* **PDU:** Bits

> O processo inverso (desencapsulamento) ocorre no servidor, camada por camada.



## Perguntas Frequentes

### A camada de enlace traduz um arquivo de texto para binário?

Não.
A tradução de texto para binário ocorre nas **camadas superiores**, geralmente na **Aplicação**.

> A camada de Enlace apenas *transporta* o envelope digital, sem se importar com o conteúdo.



### Por que o DNS é camada de aplicação?

Porque ele fornece serviços diretamente às aplicações dos usuários, **traduzindo nomes de domínio** (ex: `google.com`) para **endereços IP** (ex: `172.217.160.142`).



## Resumo das Camadas

| Camada     | Função Principal                         | Unidade de Dados |
| ---------- | ---------------------------------------- | ---------------- |
| Aplicação  | Serviços às aplicações                   | Dados            |
| Transporte | Comunicação entre processos              | Segmento         |
| Rede       | Endereçamento e roteamento               | Pacote           |
| Enlace     | Comunicação local e endereçamento físico | Quadro           |
| Física     | Transmissão de bits                      | Bits             |


