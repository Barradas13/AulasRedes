<center><h1> Redes de Computadores 2025</h1></center>

<center><h2>Federal Institute of Parana (IFPR) Professor Darlon Vassata</h2></center>
<br>
<center><h2>Felipe Barradas Sebastião, 2025</center>


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
