import dataview as dv
from sklearn.cross_validation import train_test_split


all_types = [dv.DataTypes.NUMERIC, dv.DataTypes.CATEGORICAL]

diabetes = dv.fetch_view('DiabetesView')

df = (diabetes.select([dv.DataTypes.NUMERIC, dv.DataTypes.CATEGORICAL])
              .view(partition_method=train_test_split,
                  ((dv.DataTypes.ALL, dv.Processing.IMPUTE),
                   (dv.DataTypes.NUMERIC, dv.Processing.STANDARDIZE),
                   (dv.DataTypes.CATEGORICAL, dv.Processing.ONEHOT)))
              .data)
print(df)
