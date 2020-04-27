import doctest

from src.manager.insurance_manager import InsuranceManager
from src.model.danger_type import DangerType
from src.model.immunity_level import ImmunityLevel
from src.model.abstract_insurance import AbstractInsurance
from src.model.health_insurance import HealthInsurance
from src.model.insurance_type import InsuranceType
from src.model.life_insurance import LifeInsurance
from src.model.property_insurance import PropertyInsurance


def main():
    first_health_insurance = HealthInsurance(10, 4000, 20, "Volodymyr's Health", ImmunityLevel.HIGH)
    print(first_health_insurance)

    second_health_insurance = HealthInsurance(12, 4400, 30, "Volodymyr's Health", ImmunityLevel.MIDDLE)
    print(second_health_insurance)

    first_life_insurance = LifeInsurance(37, 54575, 31, "Volodymyr's Life", emergency_savings=75000,
                                         number_of_dependents=4)
    print(first_life_insurance)

    second_life_insurance = LifeInsurance(20, 50000, 30, "Volodymyr's Life", emergency_savings=40000,
                                          number_of_dependents=4)
    print(second_life_insurance)

    first_property_insurance = PropertyInsurance(25, 52000, 30, "Volodymyr's Property",
                                                 danger_type=DangerType.NO_DANGER,
                                                 accidents_for_twenty_years=2)
    print(first_property_insurance)

    second_property_insurance = PropertyInsurance(15, 30000, 30, "Volodymyr's Property",
                                                  danger_type=DangerType.NEAR_AIRPORT,
                                                  accidents_for_twenty_years=10)
    print(second_property_insurance)

    print("\n")
    print(second_health_insurance.__repr__())
    print(first_property_insurance.__repr__())
    print("\n")

    insurances = [first_health_insurance, second_health_insurance, first_life_insurance, second_life_insurance,
                  first_property_insurance, second_property_insurance]

    manager = InsuranceManager(insurances)
    manager.find_by_risk_level(1.1)
    manager.find_by_insurance_type(InsuranceType.HealthInsurance)
    manager.find_by_customer_payment_uah(30)


if __name__ == '__main__':
    main()
doctest.testmod(verbose=True, extraglobs={'obj': AbstractInsurance()})
