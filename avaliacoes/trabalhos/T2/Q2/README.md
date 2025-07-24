# Utilização do Redis

Utilizei a imagem **redis:alpine** para fazer o envio de notificações entre computadores da mesma rede. O **Redis** é um banco de dados me memória cache, portanto é extremamente rápido. Além disso ele usa a estrutura **NoSQL**.

A utilização está na pasta anterior à essa, no docker-compose.yml e o acesso está sendo feito em Python com a biblioteca redis.

A seguir segue os trechos em que o redis aparece:

## Criando conexão
```
redis:
image: redis:alpine 
container_name: redis
networks:
    - rede_chat 
ports:
    - "6379:6379"
```

```
self.r = redis.Redis(
                    host=os.getenv("DB_HOST_REDIS"),
                    port=6379,
                    decode_responses=True 
                )
```

## Enviando notificações

```
self.r.publish('canal_mensagens', f'Add {id}~{nome}~{texto}')

```


## Fazendo ouvinte

```
pubsub = bancoGer.r.pubsub()
pubsub.subscribe('canal_mensagens')

print("Esperando mensagens")

for msg in pubsub.listen():
    if msg['type'] == 'message':
        if msg['data'].startswith('Add:'):
            dados = msg['data'][4:]
            id, nome, mensagem = dados.split("~")
            page.run_thread(adicionar_mensagem, id, nome, mensagem)
        elif msg['data'].startswith('Del:'):
            dados = msg['data'][4:]
            id, nome, mensagem = dados.split("~")
            page.run_thread(remover_mensagem, id, nome, mensagem)
```