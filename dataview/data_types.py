import enum


class DataTypes(enum.Enum):
    ALL = 0
    NUMERIC = 1
    CATEGORICAL = 2
    ORDINAL = 3
    NOMINAL = 4
    TEXT = 5


class Processing(enum.Enum):
    IMPUTE = 0
    STANDARDIZE = 1
    ONEHOT = 2
