from flet import *
from models.viewLogin import ViewLogin
from models.viewCadastro import ViewCadastro
from models.modelUsuario import listarUsuarios
from modelCadastro import insertProduto

def main(page:Page):
    page.title="Controle De Sistema"
    telaLogin=ViewLogin()
    telaCadastro=ViewCadastro()
    # Funções
    def entrarSistema(e):
        # Pegar valor da tela login
        login=telaLogin.login.value
        senha=telaLogin.senha.value
        for usuario in listarUsuarios():
            if login==usuario[1]:
                if senha==usuario[2]:
                    page.go("/cadastro")
                else:
                    telaLogin.senha.error_text="Senha invalida!"
                    telaLogin.senha.update()
            else:
                telaLogin.login.error_text="nome não cadastrado"
                telaLogin.login.update()

    # Eventos de Buttons
    telaLogin.btnEntrar.on_click=entrarSistema

    def cadastrarProduto(e):
        nome=telaCadastro.nome.value
        marca=telaCadastro.marca.value
        valor=float(telaCadastro.valor.value)
        insertProduto(nome,marca,valor)

    telaCadastro.btnCadastrar.on_click=cadastrarProduto



    def changeRoute(route):
        page.views.clear()
        page.views.append(
            View(
               route="/",
                controls=[
                    telaLogin
                ]
            )
        )
        if page.route=="/cadastro":
            page.views.append(
                View(
                    route="/cadastro",
                    controls=[telaCadastro]
                )
            )

        page.update()

    page.on_route_change=changeRoute
    page.go(page.route)


app(target=main)