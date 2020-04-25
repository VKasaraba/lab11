from enum import Enum


class DangerType(Enum):
    HURRICANE_ZONE = 1
    EARTHQUAKE_ZONE = 2
    FLOODING_ZONE = 3
    NEAR_ACTIVE_VOLCANO = 4
    NEAR_AIRPORT = 5
    NO_DANGER = 6
