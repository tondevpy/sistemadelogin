from model import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib


def retornarSession():
    CONN = "sqlite:///projeto2.db"
    engine = create_engine(CONN, echo=False)
    Session = sessionmaker(bind=engine)

    return Session()


class Cadastro():

    @classmethod
    def verificarDados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 3:
            return 2

        if len(email) > 50 or len(email) < 10:
            return 3

        if len(senha) > 50 or len(senha) < 6:
            return 4

        return 1

    @classmethod
    def cadastrar(cls, nome, email, senha):

        session = retornarSession()
        usuario = session.query(Pessoa).filter(Pessoa.email == email).all()

        if len(usuario) > 0:
            return 5

        dados_verificados = cls.verificarDados(nome, email, senha)

        if dados_verificados != 1:
            return dados_verificados

        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            p1 = Pessoa(nome=nome, email=email, senha=senha)
            session.add(p1)
            session.commit()

            return 1


        except:
            return 3

class Login:
    
    @classmethod
    def login(cls, email, senha):
        session = retornarSession()
        senha = hashlib.sha256(senha.encode()).hexdigest()

        logar = session.query(Pessoa).filter(Pessoa.email == email).filter(Pessoa.senha == senha).all()
        if len(logar) == 1:
            return {'logado': True, 'id': logar[0].id}
        else:
            return False
        
