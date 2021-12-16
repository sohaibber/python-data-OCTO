from flask import Blueprint, request
from src.constants import AGGREGATOR_MODEL_PATH
from src.models.aggregator_model import AggregatorModel
import numpy as np
from flask import jsonify
import json
# from bson import json_util

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
        dictio = {}
        i=1
        for tr in transactions:
                dictio[str(i)]=json.loads(str(tr))
                i+=1
        
        return dictio

