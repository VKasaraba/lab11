from src.model.abstract_insurance import LifeInsurance
from src.model.danger_type import DangerType
from src.model.insurance_type import InsuranceType


class PropertyInsurance(LifeInsurance):
    __insurance_type = InsuranceType.PropertyInsurance

    def __init__(self, duration_in_years=0, compensation=0, customer_payment_uah=0, client=None, address=None,
                 property_value_in_uan=0, accidents_for_twenty_years=0, danger_type=DangerType.NO_DANGER):
        super().__init__(duration_in_years, compensation, customer_payment_uah, client)
        self.address = address
        self.property_value_in_uan = property_value_in_uan
        self.accidents_for_twenty_years = accidents_for_twenty_years
        self.danger_type = danger_type

    def __del__(self):
        pass

    def __str__(self):
        return str(__name__) + super().__str__() + " insurance_type= " + str(self.__insurance_type) + " address= " + str(
            self.address) + " property_value_in_uan= " + str(
            self.property_value_in_uan) + " accidents_for_twenty_years= " + str(
            self.accidents_for_twenty_years) + " danger_type= " + str(self.danger_type) + " risk_level= " + str(
            self.get_risk_level())

    def __repr__(self):
        return "customer_payment_uah= " + str(self.customer_payment_uah) + " insurance_type= " + str(
            self.__insurance_type) + " risk_level= " + str(self.get_risk_level())

    def get_risk_level(self):
        risk_level = self.accidents_for_twenty_years * 0.5
        if self.danger_type == DangerType.HURRICANE_ZONE:
            risk_level += 2
        elif self.danger_type == DangerType.EARTHQUAKE_ZONE:
            risk_level += 2
        elif self.danger_type == DangerType.FLOODING_ZONE:
            risk_level += 1.5
        elif self.danger_type == DangerType.NEAR_ACTIVE_VOLCANO:
            risk_level += 2.8
        elif self.danger_type == DangerType.NEAR_AIRPORT:
            risk_level += 0.5
        else:
            risk_level += 0.1
        return risk_level

    @property
    def insurance_type(self):
        return self.__insurance_type

    @property
    def danger_type(self):
        return self._danger_type

    @danger_type.setter
    def danger_type(self, danger_type: DangerType):
        if danger_type not in DangerType:
            raise Exception
        self._danger_type = danger_type
