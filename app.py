from flask import Flask
from flask_restful import Api
from services.cliente import Cliente, Clientes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
api = Api(app)

@app.before_first_request
def cria_banco():
    db.create_all()

api.add_resource(Clientes, '/clientes')
api.add_resource(Cliente, '/clientes/<int:id>')

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)