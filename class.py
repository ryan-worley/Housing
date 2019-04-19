bianary = [
    'MSSubClass',
    'MSZoning',
    'Street',
    'Alley',
    'LotShape',
    'LandContour',
    'Utilities',
    'LotConfig',
    'LandSlope',
    'Neighborhood',
    'BldType',
    'HouseStyle',
    'RoofStyle',
    'RoofMat1',
    'MassVnrType',
    'ExterQual',
    'ExterCond',
    'Foundation',
    'BsmtQual',
    'BsmtCond',
    'BsmtExposure',
    'BsmtFinType1',

    ]

continuous = [
    'LotFrontage',
    'OverallQual',
    'OverallCond',
    'LotArea',
    'OverallQual',
    'OverallCond',
    'MassVnrArea',
    ]

unique = [
    'YearRemodAdd',  # Stuff
    ]

dependent = [
    ('Condition1', 'Condition2'),
    ('Exterior1st', 'Exterior2nd')
]