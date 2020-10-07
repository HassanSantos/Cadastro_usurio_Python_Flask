from flask_restful import Resource, reqparse
from models.cliente import Cliente as ClienteModel
import requests
from flask import jsonify


class Clientes(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('cpf', type=int, required=False)
    parser.add_argument('nome', type=str, required=False)
    parser.add_argument('telefone', type=int, required=False)
    parser.add_argument('cep', type=str, required=False)

    def post(self):
        cliente_data = self.parser.parse_args()
        cep_input = cliente_data['cep']
        request = requests.get('https://viacep.com.br/ws/{}/json/'.format(
            cep_input))
        address_data = request.json() 
        cliente_data['cep'] = address_data['cep']
        cliente_data['rua'] = address_data['logradouro']
        cliente_data['bairro'] = address_data['bairro']
        cliente_data['cidade'] = address_data['localidade']
        cliente_data['uf'] = address_data['uf']
        cliente_model = ClienteModel(cliente_data)
        ClienteModel.create(cliente_model)
        return cliente_data, 201

    def get(self):
        cliente = ClienteModel.query.filter_by(
            ).all()
        return jsonify([i.serialize for i in cliente])


class Cliente(Resource):

    def get(self, id):
        cliente = ClienteModel.query.filter_by(id=id).first()
        if cliente:
            return cliente.serialize

        return {}

    def post(self, id):
        cliente_data = Clientes.parser.parse_args()
        clienteBd = ClienteModel.query.filter_by(id=id).first()
        if clienteBd:
            clienteBd.nome = cliente_data['nome']
            clienteBd.cpf = cliente_data['cpf']
            clienteBd.telefone = cliente_data['telefone']
            clienteBd.endereco = cliente_data['endereco']
            clienteBd.ativo = cliente_data['ativo']
            clienteBd.create(clienteBd)
            return clienteBd.serialize, 202
        else:
            print("ERRO")
            # TODO validar erro