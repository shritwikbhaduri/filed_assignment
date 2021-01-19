from typing import Dict

from flask import make_response, jsonify
import logging


class PaymentGateway:
    """
    this class is responsible for all payment related operations
    """

    def __init__(self, details: Dict):
        self.details = details
        self.transaction_result = False

    def perform(self):
        if self.details["Amount"] < 20:
            result = self.cheap_payment_gateway()
        elif 20 < self.details["Amount"] < 500:
            result = self.expensive_payment_gateway()
            if not result:
                result = self.cheap_payment_gateway()
        else:
            result = self.premium_payment_gateway(retry_count=3)

        if result:
            data = {'message': 'transaction successful', 'code': 'SUCCESS'}
            return make_response(jsonify(data), 200)
        else:
            data = {'message': 'transaction un-successful', 'code': 'FAILED'}
            return make_response(jsonify(data), 500)

    def cheap_payment_gateway(self, retry_count: int = 0):
        """
        handles payment through CheapPaymentGateway
        :param retry_count: number of retries if the payment fails
        :return: success/failure
        """
        while True:
            logging.info(f"processing payment request on {self.details['CardHolder']} using CheapPaymentGateWay")

            # will contains all the code for the payment to process, since it's a dummy function codes are missing

            if not self.transaction_result and retry_count > 0:
                retry_count = retry_count - 1
            else:
                return self.transaction_result

    def expensive_payment_gateway(self, retry_count: int = 0):
        """
        handles payment through CheapPaymentGateway
        :param retry_count: number of retries if the payment fails
        :return: success/failure
        """
        while True:
            logging.info(f"processing payment request on {self.details['CardHolder']} using ExpensivePaymentGateWay")

            # will contains all the code for the payment to process, since it's a dummy function codes are missing

            if not self.transaction_result and retry_count > 0:
                retry_count = retry_count - 1
            else:
                return self.transaction_result

    def premium_payment_gateway(self, retry_count: int = 0):
        """
        handles payment through CheapPaymentGateway
        :param retry_count: number of retries if the payment fails
        :return: success/failure
        """
        while True:
            logging.info(f"processing payment request on {self.details['CardHolder']} using PremiumPaymentGateWay")

            # will contains all the code for the payment to process, since it's a dummy function codes are missing

            # this statement checks if transaction
            if not self.transaction_result and retry_count:
                retry_count = retry_count - 1
            else:
                return self.transaction_result
