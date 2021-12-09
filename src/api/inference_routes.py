from flask import Blueprint, request
from src.constants import AGGREGATOR_MODEL_PATH
from src.models.aggregator_model import AggregatorModel
import numpy as np
from flask import jsonify

model = AggregatorModel()
model.load(AGGREGATOR_MODEL_PATH)
blueprint = Blueprint('api', __name__, url_prefix='/api')

@blueprint.route('/')
@blueprint.route('/index')
def index():
    return "CARD FRAUD DETECTION API - INFERENCE BLUEPRINT"


@blueprint.route('/inference', methods=['GET', 'POST'])
def run_inference():
    from src.api.app import Transaction
    from src.api.db import db
    if request.method == 'POST':
        features = np.array(request.json).reshape(1, -1)
        prediction = model.predict(features)
        target=prediction[0]
        #store data on SQLite Table
        print(features)
        features = [str(x) for x in features[0]]
        trans = Transaction(features=features, prediction=str(target))
        db.session.add(trans)
        db.session.commit()
        return str(prediction[0])
    elif request.method == 'GET':
        transactions = Transaction.query.all()
        return str([{"v0": transaction.v0, "v1": transaction.v1, "v2": transaction.v2, "v3": transaction.v3, "prediction": transaction.prediction} for transaction in transactions])

