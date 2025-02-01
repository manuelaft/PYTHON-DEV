import flet as ft

# função principal
def main(pagina): 

    # Título da página e adicionar o título
    titulo=ft.Text('É O TAL DO ZAPIZAPI')
    pagina.add(titulo) 
    pagina.update()

    chat=ft.Column()

    # função do canal de comunicação
    def tunel(mensagem):
        texto=ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(tunel)

    # função do botão Iniciar chat (vai abrir o popup)
    def abrir_popup(evento):
        pagina.overlay.append(popup)
        popup.open=True
        pagina.update()
        print('clicou no botão')

    # Botão Iniciar chat
    botao=ft.ElevatedButton('Iniciar chat',on_click=abrir_popup)
    pagina.add(botao)
    pagina.update()

    # função do botão enviar (no chat)
    def enviar_mensagem(evento):
        print('enviou mensagem')
        mensagem=(f'{nome.value}: {campo_mensagem.value}')
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value=''
        pagina.update()

    # Variavel da mensagem, botão e a linha (para alinhar os 2)
    campo_mensagem=ft.TextField(label='Escreva sua mensagem aqui',on_submit=enviar_mensagem)
    botao_enviar=ft.ElevatedButton('Enviar',on_click=enviar_mensagem)
    linha=ft.Row([campo_mensagem,botao_enviar])

    # função do botão entrar (no popup), remover tudo da página
    def entrar(evento):
        popup.open=False
        pagina.remove(botao,titulo)

        usuario_entrou_no_chat=(f'{nome.value} entrou no chat')

        pagina.controls.clear() # limpa tudo
        pagina.add(ft.Text(usuario_entrou_no_chat))
        pagina.add(chat)
        pagina.add(linha)
        pagina.update()

    # Título, campo de preencher o nome e botão entrar da popup
    nome=ft.TextField(label='Digite seu nome aqui',on_submit=entrar)
    popup=ft.AlertDialog(title=ft.Text(f'Bem vindo ao zapizapi!'),content=nome,actions=[ft.ElevatedButton('Entrar',on_click=entrar)])

ft.app(main,view=ft.WEB_BROWSER) # formato de site
