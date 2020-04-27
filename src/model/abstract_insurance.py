from typing import Any
from abc import ABC, abstractmethod


class AbstractInsurance(ABC):

    def __init__(self, duration_in_years=0, compensation=0, customer_payment_uah=0, client=None):
        self.duration_in_years = duration_in_years
        self.compensation = compensation
        self.customer_payment_uah = customer_payment_uah
        self.client = client

    def __str__(self):
        return "duration_in_years= " + str(self.duration_in_years) + " compensation= " + str(
            self.compensation) + " customer_payment_uah= " + str(self.customer_payment_uah) + " client= " + str(
            self.client)

    def __del__(self):
        print('Destructor called, insurance deleted.')

    @abstractmethod
    def get_risk_level(self):
        raise NotImplementedError

    @abstractmethod
    def insurance_type(self):
        raise NotImplementedError
