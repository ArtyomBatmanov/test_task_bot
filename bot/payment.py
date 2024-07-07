import uuid
from yookassa import Configuration, Payment
from .config import SHOP_ID, SECRET_KEY

Configuration.account_id = SHOP_ID
Configuration.secret_key = SECRET_KEY


def create_payment(amount, currency="RUB", description="Payment Description"):
    payment = Payment.create(
        {
            "amount": {"value": str(amount), "currency": currency},
            "confirmation": {
                "type": "redirect",
                "return_url": "https://your-website.com/return_url",
            },
            "capture": True,
            "description": description,
            "metadata": {"order_id": str(uuid.uuid4())},
        }
    )
    return payment.confirmation.confirmation_url
