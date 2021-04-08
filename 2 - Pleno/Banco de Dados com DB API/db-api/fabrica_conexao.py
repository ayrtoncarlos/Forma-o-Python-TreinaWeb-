import MySQLdb, configparser, os

class FabricaConexao():
    @staticmethod
    def conectar():
        config = configparser.ConfigParser()
        path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
        config.read(os.path.join(path,'config.ini'))
        db = MySQLdb.connect(user=config['DATABASE']['user'], 
                             passwd=config['DATABASE']['passwd'], 
                             db=config['DATABASE']['db'], 
                             host=config['DATABASE']['host'], 
                             port=int(config['DATABASE']['port']), 
                             autocommit=config['DATABASE']['autocommit'])
        print('Conexão realizada com sucesso')
        return db

    @staticmethod
    def desconectar(db):
        db.close()
        print('Conexão finalizada com sucesso')