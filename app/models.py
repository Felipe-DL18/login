from init import db
from werkzeug.security import  generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__='resumos_conta'
    id= db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome= db.Column(db.String(100), nullable=False)
    email= db.Column(db.String(100), nullable=False, unique=True)
    senha= db.Column(db.String(100), nullable=False, unique=True)

    def  __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)
    def verify_senha(self, senha):
        return check_password_hash(self.senha, senha)