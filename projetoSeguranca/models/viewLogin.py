from flet import *

class ViewLogin(UserControl):
    def __init__(self):
        super().__init__()
        self.login=TextField(label="Login")
        self.senha=TextField(label="Senha",password=True)
        self.btnEntrar=ElevatedButton(text="Entrar")

    def build(self):
        coluna=Column(controls=[
            self.login,
            self.senha,
            self.btnEntrar
        ])

        return coluna