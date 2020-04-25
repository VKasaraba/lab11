from typing import List

from src.model.abstract_insurance import AbstractInsurance


class InsuranceManager:

    def __init__(self, insurances=[]):
        self.insurances = insurances

    def __del__(self):
        print('Destructor called, insurance_manager deleted.')

    def find_by_risk_level(self, expected_risk_level):
        found_insurances: List[AbstractInsurance] = []
        for insurance in self.insurances:
            if insurance.get_risk_level() == expected_risk_level:
                found_insurances.append(insurance)
        return found_insurances

    def find_by_insurance_type(self, expected_insurance_type):
        found_insurances: List[AbstractInsurance] = []
        for insurance in self.insurances:
            if insurance.insurance_type == expected_insurance_type:
                found_insurances.append(insurance)
        return found_insurances

    def find_by_customer_payment_uah(self, expected_customer_payment):
        found_insurances: List[AbstractInsurance] = []
        for insurance in self.insurances:
            if insurance.customer_payment_uah == expected_customer_payment:
                found_insurances.append(insurance)
        return found_insurances

