from src.model.abstract_insurance import AbstractInsurance
from src.model.immunity_level import ImmunityLevel
from src.model.insurance_type import InsuranceType


class HealthInsurance(AbstractInsurance):
    __insurance_type = InsuranceType.HealthInsurance

    def __init__(self, duration_in_years=0, compensation=0, customer_payment_uah=0, client=None,
                 immunity_level=ImmunityLevel.MIDDLE):
        super().__init__(duration_in_years, compensation, customer_payment_uah, client)
        self.immunity_level = immunity_level

    def __del__(self):
        print('Destructor called, health_insurance deleted.')

    def __str__(self):
        return super().__str__() + " immunity_level = " + str(self.immunity_level) + " risk_level= " + str(
            self.get_risk_level())

    def get_risk_level(self):
        if self.immunity_level == ImmunityLevel.HIGH:
            return 0.1
        elif self.immunity_level == ImmunityLevel.MIDDLE:
            return 1.1
        else:
            return 2.1

    @property
    def immunity_level(self):
        return self._immunity_level

    @immunity_level.setter
    def immunity_level(self, immunity_level: ImmunityLevel):
        if immunity_level not in ImmunityLevel:
            raise Exception
        self._immunity_level = immunity_level

    @property
    def insurance_type(self):
        return self.__insurance_type
