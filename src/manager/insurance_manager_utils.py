import doctest

from src.model.danger_type import DangerType
from src.model.health_insurance import HealthInsurance
from src.model.immunity_level import ImmunityLevel
from src.model.life_insurance import LifeInsurance
from src.model.property_insurance import PropertyInsurance
from src.model.sort_type import SortType


class InsuranceManagerUtils:
    def __init__(self):
        pass

    def __del__(self):
        pass

    @staticmethod
    def sort_by_risk_level(insurances, sort_type: SortType):
        """
        returns a sorted list of insurances with given

        >>> InsuranceManagerUtils.sort_by_risk_level(insurances, SortType.ASCENDING)
        [customer_payment_uah= 20 insurance_type= InsuranceType.HealthInsurance risk_level= 0.1, \
customer_payment_uah= 31 insurance_type= InsuranceType.HealthInsurance risk_level= 1.1, \
customer_payment_uah= 30 insurance_type= InsuranceType.PropertyInsurance risk_level= 1.1, \
customer_payment_uah= 31 insurance_type= InsuranceType.LifeInsurance risk_level= 3.0, \
customer_payment_uah= 30 insurance_type= InsuranceType.LifeInsurance risk_level= 4.0, \
customer_payment_uah= 30 insurance_type= InsuranceType.PropertyInsurance risk_level= 5.5]

        """
        if sort_type == SortType.ASCENDING:
            sorted_insurances = sorted(insurances, key=lambda insurance: insurance.get_risk_level())
        elif sort_type == SortType.DESCENDING:
            sorted_insurances = sorted(insurances, key=lambda insurance: insurance.get_risk_level(), reverse=True)
        elif sort_type not in SortType:
            raise Exception
        return sorted_insurances

    @staticmethod
    def sort_by_insurance_type(insurances, sort_type: SortType):
        """
        returns a sorted list of insurances with given insurance_type

        >>> InsuranceManagerUtils.sort_by_insurance_type(insurances, SortType.DESCENDING)
        [customer_payment_uah= 30 insurance_type= InsuranceType.PropertyInsurance risk_level= 1.1, \
customer_payment_uah= 30 insurance_type= InsuranceType.PropertyInsurance risk_level= 5.5, \
customer_payment_uah= 31 insurance_type= InsuranceType.LifeInsurance risk_level= 3.0, \
customer_payment_uah= 30 insurance_type= InsuranceType.LifeInsurance risk_level= 4.0, \
customer_payment_uah= 20 insurance_type= InsuranceType.HealthInsurance risk_level= 0.1, \
customer_payment_uah= 31 insurance_type= InsuranceType.HealthInsurance risk_level= 1.1]
        """
        if sort_type == SortType.ASCENDING:
            sorted_insurances = sorted(insurances, key=lambda insurance: str(insurance.insurance_type))
        elif sort_type == SortType.DESCENDING:
            sorted_insurances = sorted(insurances, key=lambda insurance: str(insurance.insurance_type), reverse=True)
        elif sort_type not in SortType:
            raise Exception
        return sorted_insurances

    @staticmethod
    def sort_by_customer_payment_uah(insurances, sort_type: SortType):
        """
        returns a sorted list of insurances with given customer_payment_uah

        >>> InsuranceManagerUtils.sort_by_customer_payment_uah(insurances, SortType.DESCENDING)
        [customer_payment_uah= 31 insurance_type= InsuranceType.HealthInsurance risk_level= 1.1, \
customer_payment_uah= 31 insurance_type= InsuranceType.LifeInsurance risk_level= 3.0, \
customer_payment_uah= 30 insurance_type= InsuranceType.LifeInsurance risk_level= 4.0, \
customer_payment_uah= 30 insurance_type= InsuranceType.PropertyInsurance risk_level= 1.1, \
customer_payment_uah= 30 insurance_type= InsuranceType.PropertyInsurance risk_level= 5.5, \
customer_payment_uah= 20 insurance_type= InsuranceType.HealthInsurance risk_level= 0.1]
        """
        if sort_type == SortType.ASCENDING:
            sorted_insurances = sorted(insurances, key=lambda insurance: insurance.customer_payment_uah)
        elif sort_type == SortType.DESCENDING:
            sorted_insurances = sorted(insurances, key=lambda insurance: insurance.customer_payment_uah, reverse=True)
        elif sort_type not in SortType:
            raise Exception
        return sorted_insurances


if __name__ == '__main__':
    doctest.testmod(verbose=True, extraglobs={"insurances": [HealthInsurance(10, 4000, 20, "Volodymyr's Health", ImmunityLevel.HIGH), \
HealthInsurance(12, 4400, 31, "Volodymyr's Health", ImmunityLevel.MIDDLE), \
LifeInsurance(37, 54575, 31, "Volodymyr's Life", emergency_savings=75000, number_of_dependents=4), \
LifeInsurance(20, 50000, 30, "Volodymyr's Life", emergency_savings=40000, number_of_dependents=4), \
PropertyInsurance(25, 52000, 30, "Volodymyr's Property", danger_type=DangerType.NO_DANGER, accidents_for_twenty_years=2), \
PropertyInsurance(15, 30000, 30, "Volodymyr's Property", danger_type=DangerType.NEAR_AIRPORT, accidents_for_twenty_years=10)]})

