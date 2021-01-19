from cardvalidator import luhn
from pydantic import BaseModel, Field, validator, SecretStr, ValidationError
import datetime


class ProcessPaymentRequest(BaseModel):
    CreditCardNumber: SecretStr = Field(..., alias="credit_card_number",
                                        description="credit card number associated with "
                                                    "the account that needs to be debited")
    CardHolder: str = Field(..., alias="card_holder",
                            description="name associated with the credit card")
    ExpirationDate: datetime.datetime = Field(...,
                                              alias="expiration_date",
                                              description="expiry date/thru date/validity")
    SecurityCode: SecretStr = Field(alias="security_code",
                                    default=None,
                                    description="security code/CVV",
                                    max_length=3,
                                    min_length=3)
    Amount: float = Field(..., alias="amount", description="amount to be debited", gt=0)

    @validator("CreditCardNumber")
    def validate_credit_card(cls, card_num):
        if not luhn.is_valid("".join([character for character in card_num.get_secret_value() if character.isalnum()])):
            raise ValueError("entered card number is not valid.")
        else:
            return card_num

    @validator("ExpirationDate")
    def validate_expiration_date(cls, date):
        if date < datetime.datetime.now():
            raise ValueError("the card has expired.")
        else:
            return date

