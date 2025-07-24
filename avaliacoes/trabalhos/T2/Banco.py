import os
import mysql.connector
import redis
import time

class BancoConector():

    def __init__(self):
        try:
            while True:
                try:
                    print("Conectando ao MySQL")
                    db_config = {
                        'host': os.getenv("DB_HOST_SQL"),
                        'port': int(os.getenv("DB_PORT")),
                        'user': os.getenv("DB_USER"),
                        'password': os.getenv("DB_PASSWORD"),
                        'database': os.getenv("DB_NAME", "ConexaoChat"),        
                    }
                    self.conexao = mysql.connector.connect(**db_config)
                    self.cursor = self.conexao.cursor()
                    print("Conectado no MySQL com sucesso!\n")
                    break
                except Exception as e:
                    time.sleep(5)
                    print(f"Erro ao tentar conectar: {e}")
        except Exception as e:
            print(f"Erro ao conectar no banco MySQL: {e}")

        try:
            while True:
                print("Conectando ao redis")
                self.r = redis.Redis(
                    host=os.getenv("DB_HOST_REDIS"),
                    port=6379,
                    decode_responses=True 
                )
                print("Conectado no Redis com sucesso!\n")
                break
        except Exception as e:
            print(f"Erro ao conectar no banco Redis: {e}")
        
        
        try:
            print("Ajustando configurações do banco SQL")
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS mensagens (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100),
                    texto VARCHAR(1000)
                )
            """)
            self.conexao.commit()
            
            self.cursor.execute("SET SQL_SAFE_UPDATES = 0")
            self.conexao.commit()
        except mysql.connector.Error as err:
            self.conexao = None
            self.cursor = None
            print(f"Erro ao tentar conectar: {err}")

        
        print("\n!!Conexões de banco de dados feitas com sucesso!!\n")
    
    
    def adicionaMensagem(self, nome, texto):
        try:
            self.cursor.execute("INSERT INTO mensagens (nome, texto) VALUES (%s, %s)", (nome, texto))
            self.conexao.commit()
            id = self.cursor.lastrowid
            self.r.publish('canal_mensagens', f'Add:{id}~{nome}~{texto}')
            print("mensagem enviada com sucesso!")
        except Exception as e:
            print(f"erro ao adicionar mensagem!: {e}")

    def pegarMensagemPorID(self, id):
        try:
            self.cursor.execute("SELECT * FROM mensagens WHERE id = %s", (id,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar mensagem: {e}")
            return None
            
    def excluirMensagem(self, id):
        try:
            dados = self.pegarMensagemPorID(id)
            self.cursor.execute("DELETE FROM mensagens WHERE id = (%s)", (id,))
            self.conexao.commit()
            self.r.publish('canal_mensagens', f'Del:{id}~{dados[1]}~{dados[2]}')
            print("mensagem excluída com sucesso!")
        except Exception as e:
            print("erro ao excluir mensagem!")
            print(e)

   
    def pegarMensagens(self):
        try:
            self.cursor.execute("SELECT * FROM mensagens")
            resultados = self.cursor.fetchall()

            return resultados
        except Exception as e:
            print("erro ao pegar mensagens!")
            print(e)

    def desconecta(self):
        self.cursor.close()
        self.conexao.close()
