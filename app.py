from http.client import BAD_REQUEST
from flask import Flask, request, abort
from pydantic import ValidationError
from paymentGateWays import PaymentGateway

from models import ProcessPaymentRequest

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>this is working</h1>"


@app.route('/ProcessPayment', methods=['POST'])
def process_payment():
    """
    this API handles payments
    :return: json
    """

    try:
        body = ProcessPaymentRequest.validate(request.get_json())
        return PaymentGateway(details=body.dict()).perform()

    except ValidationError as err:
        abort(BAD_REQUEST, err)


app.run(port=8000)
