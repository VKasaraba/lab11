import doctest
from typing import List
from src.model.insurance_type import InsuranceType
from src.model.abstract_insurance import LifeInsurance
from src.model.danger_type import DangerType
from src.model.health_insurance import HealthInsurance
from src.model.immunity_level import ImmunityLevel
from src.model.life_insurance import LifeInsurance
from src.model.property_insurance import PropertyInsurance


class InsuranceManager:

    def __init__(self, insurances=[]):
        self.insurances = insurances

    def __del__(self):
        pass

    def find_by_risk_level(self, expected_risk_level):
        """
        returns a list of insurances with given risk_level

        >>> manager.find_by_risk_level(1.1)
        [customer_payment_uah= 31 insurance_type= InsuranceType.HealthInsurance risk_level= 1.1, \
customer_payment_uah= 30 insurance_type= InsuranceType.PropertyInsurance risk_level= 1.1]
        """
        found_insurances: List[LifeInsurance] = []
        for insurance in self.insurances:
            if insurance.get_risk_level() == expected_risk_level:
                found_insurances.append(insurance)
        return found_insurances

    def find_by_insurance_type(self, expected_insurance_type):
        """
        returns a list of insurances with given insurance_type

        >>> manager.find_by_insurance_type(InsuranceType.PropertyInsurance)
        [customer_payment_uah= 30 insurance_type= InsuranceType.PropertyInsurance risk_level= 1.1, \
customer_payment_uah= 30 insurance_type= InsuranceType.PropertyInsurance risk_level= 5.5]

        """
        found_insurances: List[LifeInsurance] = []
        for insurance in self.insurances:
            if insurance.insurance_type == expected_insurance_type:
                found_insurances.append(insurance)
        return found_insurances

    def find_by_customer_payment_uah(self, expected_customer_payment):
        """
        returns a list of insurances with given customer_payment_uah

        >>> manager.find_by_customer_payment_uah(30)
        [customer_payment_uah= 30 insurance_type= InsuranceType.LifeInsurance risk_level= 4.0, \
customer_payment_uah= 30 insurance_type= InsuranceType.PropertyInsurance risk_level= 1.1, \
customer_payment_uah= 30 insurance_type= InsuranceType.PropertyInsurance risk_level= 5.5]
        """
        found_insurances: List[LifeInsurance] = []
        for insurance in self.insurances:
            if insurance.customer_payment_uah == expected_customer_payment:
                found_insurances.append(insurance)
        return found_insurances


if __name__ == '__main__':
    first_health_insurance = HealthInsurance(10, 4000, 20, "Volodymyr's Health", ImmunityLevel.HIGH)
    second_health_insurance = HealthInsurance(12, 4400, 31, "Volodymyr's Health", ImmunityLevel.MIDDLE)

    first_life_insurance = LifeInsurance(37, 54575, 31, "Volodymyr's Life", emergency_savings=75000,
                                         number_of_dependents=4)
    second_life_insurance = LifeInsurance(20, 50000, 30, "Volodymyr's Life", emergency_savings=40000,
                                          number_of_dependents=4)

    first_property_insurance = PropertyInsurance(25, 52000, 30, "Volodymyr's Property",
                                                 danger_type=DangerType.NO_DANGER,
                                                 accidents_for_twenty_years=2)
    second_property_insurance = PropertyInsurance(15, 30000, 30, "Volodymyr's Property",
                                                  danger_type=DangerType.NEAR_AIRPORT,
                                                  accidents_for_twenty_years=10)

    insurances = [first_health_insurance, second_health_insurance, first_life_insurance, second_life_insurance,
                  first_property_insurance, second_property_insurance]
    my_dict = {"one":1, "two":2}
    doctest.testmod(verbose=True, extraglobs={"manager": InsuranceManager(insurances)})

