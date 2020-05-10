from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from src.model.life_insurance import LifeInsurance
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class InsuranceContract(LifeInsurance, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    duration_in_years = db.Column(db.Integer, unique=False)
    compensation = db.Column(db.Integer, unique=False)
    customer_payment_uah = db.Column(db.Integer, unique=False)
    client = db.Column(db.String(32), unique=False)
    emergency_savings = db.Column(db.Integer, unique=False)
    number_of_dependents = db.Column(db.Integer, unique=False)

    def __init__(self, duration_in_years, compensation, customer_payment_uah, client, emergency_savings,
                 number_of_dependents):
        super().__init__(duration_in_years, compensation, customer_payment_uah, client, emergency_savings,
                         number_of_dependents)


class InsuranceContractSchema(ma.Schema):
    class Meta:
        fields = ('duration_in_years', 'compensation', 'customer_payment_uah', 'client', 'emergency_savings',
                  'number_of_dependents')


insurance_contract_schema = InsuranceContractSchema()
insurance_all_contracts_schema = InsuranceContractSchema(many=True)


@app.route("/insurance_contract", methods=["POST"])
def add_insurance_contract():
    duration_in_years = request.json['duration_in_years']
    compensation = request.json['compensation']
    customer_payment_uah = request.json['customer_payment_uah']
    client = request.json['client']
    emergency_savings = request.json['emergency_savings']
    number_of_dependents = request.json['number_of_dependents']
    insurance_contract = InsuranceContract(duration_in_years, compensation, customer_payment_uah, client,
                                           emergency_savings, number_of_dependents)
    db.session.add(insurance_contract)
    db.session.commit()
    return insurance_contract_schema.jsonify(insurance_contract)


@app.route("/insurance_contract", methods=["GET"])
def get_insurance_contracts():
    all_insurance_contracts = InsuranceContract.query.all()
    result = insurance_contract_schema.dump(all_insurance_contracts)
    return jsonify({'insurance_contracts': result})


@app.route("/insurance_contract/<id>", methods=["GET"])
def get_insurance_contract_by_id(id):
    insurance_contract = InsuranceContract.query.get(id)
    if not insurance_contract:
        abort(404)
    return insurance_contract_schema.jsonify(insurance_contract)


@app.route("/insurance_contract/<id>", methods=["PUT"])
def insurance_contract_update(id):
    insurance_contract = InsuranceContract.query.get(id)
    if not insurance_contract:
        abort(404)
    old_insurance_contract = copy.deepcopy(insurance_contract)
    insurance_contract.duration_in_years = request.json['duration_in_years']
    insurance_contract.compensation = request.json['compensation']
    insurance_contract.customer_payment_uah = request.json['customer_payment_uah']
    insurance_contract.client = request.json['client']
    insurance_contract.emergency_savings = request.json['emergency_savings']
    insurance_contract.number_of_dependents = request.json['number_of_dependents']
    db.session.commit()
    return insurance_contract_schema.jsonify(old_insurance_contract)


@app.route("/insurance_contract/<id>", methods=["DELETE"])
def insurance_appliance_delete(id):
    insurance_contract = InsuranceContract.query.get(id)
    if not insurance_contract:
        abort(404)
    db.session.delete(insurance_contract)
    db.session.commit()
    return insurance_contract_schema.jsonify(insurance_contract)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
