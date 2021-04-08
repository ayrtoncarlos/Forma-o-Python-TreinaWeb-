import sys, os
path = '/'.join((os.path.abspath('3 - Sênior/Fundamentos de Kivy/main.py').replace('\\', '/')).split('/')[:-1])
sys.path.insert(0, path)

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import partial

from entidades import cliente
from repositorios import cliente_repositorio


class ExclusaoPopup(Popup):
    Popup.title = 'Aviso'

class MensagemPopup(Popup):
    pass

class BotaoListagem(ToggleButton):
    def __init__(self, cliente_id, cliente_nome, cliente_idade, **kwargs):
        super(BotaoListagem, self).__init__(**kwargs)
        self.id_cliente = cliente_id
        self.nome_cliente = cliente_nome
        self.idade_cliente = cliente_idade
        self.text = f'Nome: {self.nome_cliente} - Idade: {self.idade_cliente}'
        self.group = 'clientes'
    
    def _do_release(self, *args):
        Principal().cliente_selecionado(self.id_cliente)

class Principal(BoxLayout):
    id_cliente = 0

    def __init__(self, **kwargs):
        super(Principal, self).__init__(**kwargs)
        self.listar_clientes()
    
    def cliente_selecionado(self, id):
        Principal.id_cliente = id
    
    def listar_clientes(self):
        self.ids.clientes.clear_widgets()
        clientes = cliente_repositorio.ClienteRepositorio.listar_clientes()
        for c in clientes:
            id = str(c[0])
            nome = c[1]
            idade = str(c[2])
            self.ids.clientes.add_widget(BotaoListagem(id, nome, idade))
    
    def cadastrar_cliente(self):
        nome = self.ids.nome.text
        idade = self.ids.idade.text

        if nome == '' or idade == '':
            MensagemPopup().open()
        else:
            cli = cliente.Cliente(nome, idade)
            cliente_repositorio.ClienteRepositorio.inserir_cliente(cli)
            self.ids.nome.text = ''
            self.ids.idade.text = ''
            self.listar_clientes()
    
    def editar_cliente(self):
        id = Principal.id_cliente
        nome = self.ids.nome.text
        idade = self.ids.idade.text

        if nome == '' or idade == '':
            MensagemPopup().open()
        else:
            cli = cliente.Cliente(nome, idade)
            cliente_repositorio.ClienteRepositorio.editar_cliente(id, cli)
            self.ids.nome.text = ''
            self.ids.idade.text = ''
            self.listar_clientes()
    
    def remover_cliente(self):
        id = Principal.id_cliente
        popup = ExclusaoPopup()
        popup.funcao = partial(self.remover, id)
        popup.open()
    
    def remover(self, id):
        cliente_repositorio.ClienteRepositorio.remover_cliente(id)
        self.listar_clientes()

class Crud(App):
    def build(self):
        return Principal()

Crud().run()
