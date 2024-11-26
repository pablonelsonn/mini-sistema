from flet import *

class ViewCadastro(UserControl):

    def __init__(self):
        super().__init__()
        self.nome=TextField(label="Nome")
        self.valor=TextField(label="Valor")
        self.marca=TextField(label="Marca")
        self.btnCadastrar=ElevatedButton(text="Cadastrar")
        self.tabela=DataTable(
            columns=[
                DataColumn(Text("id")),
                DataColumn(Text("Nome")),
                DataColumn(Text("Marca")),
                DataColumn(Text("Valor")),
            ],
            rows=[
                DataRow(
                    cells=[
                        DataCell(
                            content=Text("1")
                        ),
                        DataCell(
                            content=Text("arroz")
                        ),
                        DataCell(
                            content=Text("Tio joão")
                        ),
                        DataCell(
                            content=Text("25.00")
                        ),
                    ]
                )
            ]
        )
    def build(self):
        # Vou retornar minha tela por esse metodo
        linhaNav=Row(
           controls=[self.nome,self.valor,
                     self.marca,self.btnCadastrar]
        )
        linhaTabela=Row(
            controls=[self.tabela]
        )

        return Column(
            controls=[linhaNav,linhaTabela]
            )