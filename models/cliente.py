from sql_alchemy import db
from datetime import datetime


class Cliente(db.Model):

    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(55), nullable=False)
    cep = db.Column(db.String(55), nullable=True)
    rua = db.Column(db.String(55), nullable=True)    
    bairro = db.Column(db.String(55), nullable=True)
    cidade = db.Column(db.String(55), nullable=True)
    uf = db.Column(db.String(55), nullable=True)
    telefone = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, data=None):
        self.created_at = datetime.now()
        if data:
            self.cpf = data['cpf']
            self.nome = data['nome']
            self.cep = data['cep']
            self.rua = data['rua']
            self.bairro = data['bairro']
            self.cidade = data['cidade']
            self.uf = data['uf']
            self.telefone = data['telefone']
            self.ativo = True

    @staticmethod
    def create(cliente):
        db.session.add(cliente)
        db.session.commit()

    @property
    def serialize(self):
        return {
            'id': self.id,
            'cpf': self.cpf,
            'nome': self.nome,
            'telefone': self.telefone,
            'created_at': datetime.timestamp(self.created_at),
            'ativo': self.ativo,
            'cep': self.cep,
            'logradouro': self.rua,
            'bairro': self.bairro,
            'localidade': self.cidade,
            'uf': self.uf}
            