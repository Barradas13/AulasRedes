import flet as ft
from Banco import BancoConector
import threading

def criarPagina():

    def main(page: ft.Page):
        bancoGer = BancoConector()

        page.title = "Chat"

        campo_nome = ft.TextField(label="Digite seu username")
        campo_texto = ft.TextField(label="Digite sua mensagem")

        mensagens_container = ft.ListView(
            expand=True,
            auto_scroll=True,
            spacing=10,
            padding=10
        )

        async def carregar_mensagens():
            print("Carregando mensagens...")
            mensagens_container.controls.clear()
            for i in bancoGer.pegarMensagens():
                id, nome, mensagem = i
                adicionar_mensagem(id, nome, mensagem)
            page.update()

        def adicionar_mensagem(id, nome, texto):
            mensagens_container.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text(nome, size=20, weight="bold"),
                        ft.Text(texto, size=14),
                        ft.ElevatedButton(
                            "Excluir",
                            on_click=lambda e, id=id: botao_excluir(e, id)
                        )
                    ]),
                    bgcolor=ft.Colors.GREY,
                    border_radius=10,
                    padding=10,
                    margin=5
                )
            )
            page.update()

        def remover_mensagem(id, nome, mensagem):
            for control in mensagens_container.controls[:]:
                if (control.content.controls[0].value == nome and control.content.controls[1].value == mensagem):
                    mensagens_container.controls.remove(control)
                    page.update()
                    break

        def ouvinte(page):
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


        threading.Thread(target=ouvinte, args=(page,), daemon=True).start()

        def botao_enviar(e):
            nome = campo_nome.value.strip()
            texto = campo_texto.value.strip()
            if nome and texto:
                bancoGer.adicionaMensagem(nome, texto)
                campo_texto.value = ""

        def botao_excluir(e, id):
            bancoGer.excluirMensagem(id)

        page.add(
            campo_nome,
            campo_texto,
            ft.ElevatedButton("Enviar", on_click=botao_enviar),
            mensagens_container
        )

        #carregar msg é async pq se não dá erro aq
        page.run_task(carregar_mensagens)

    print("Rodando com Flet em: http://0.0.0.0:8550 ou http://localhost:8550")
    ft.app(target=main, view=ft.WEB_BROWSER, port=8550, host="0.0.0.0")
