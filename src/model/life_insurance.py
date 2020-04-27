from src.model.abstract_insurance import AbstractInsurance
from src.model.insurance_type import InsuranceType


class LifeInsurance(AbstractInsurance):
    __insurance_type = InsuranceType.LifeInsurance

    def __init__(self, duration_in_years=0, compensation=0, customer_payment_uah=0, client=None, emergency_savings=0,
                 number_of_dependents=0):
        super().__init__(duration_in_years, compensation, customer_payment_uah, client)
        self.emergency_savings = emergency_savings
        self.number_of_dependents = number_of_dependents

    def __del__(self):
        pass

    def __str__(self):
        return super().__str__() + " insurance_type= " + str(self.__insurance_type) + " emergency_savings= " + str(
            self.emergency_savings) + " number_of_dependents= " + str(
            self.number_of_dependents) + " risk_level= " + str(
            self.get_risk_level())

    def __repr__(self):
        return "customer_payment_uah= " + str(self.customer_payment_uah) + " insurance_type= " + str(
            self.__insurance_type) + " risk_level= " + str(self.get_risk_level())

    def get_risk_level(self):
        risk_level = self.number_of_dependents * 0.5
        if self.emergency_savings < 10000:
            risk_level += 3
            return risk_level
        elif self.emergency_savings < 50000:
            risk_level += 2
            return risk_level
        elif self.emergency_savings < 80000:
            risk_level += 1
            return risk_level
        else:
            risk_level += 0.1
            return risk_level

    @property
    def insurance_type(self):
        return self.__insurance_type
