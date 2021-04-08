import MySQLdb, configparser, os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class FabricaConexao():
    def conectar(self):
        config = configparser.ConfigParser()
        path = '/'.join((os.path.abspath('3 - Sênior/SQLAlchemy ORM/main.py').replace('\\', '/')).split('/')[:-1])
        config.read(os.path.join(path,'config.ini'))

        user = config['DATABASE']['user']
        passwd = config['DATABASE']['passwd']
        db = config['DATABASE']['db']
        host = config['DATABASE']['host']
        port = int(config['DATABASE']['port'])
        
        engine = create_engine(f'mysql://{user}:{passwd}@{host}:{port}/{db}')
        
        print('Conexão realizada com sucesso')
        return engine

    def desconectar_engine(self, engine):
        engine.dispose()
        print('Conexão finalizada com sucesso')
    
    def desconectar(self, sessao):
        sessao.close()
        print('Conexão finalizada com sucesso')
    
    def criar_sessao(self):
        conexao = self.conectar()

        Session = sessionmaker()
        Session.configure(bind=conexao)
        session = Session()

        return session
