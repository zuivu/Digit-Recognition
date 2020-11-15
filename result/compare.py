from numpy.core.numeric import count_nonzero
import pandas as pd


RESULT_FILE = ["result.csv", "result_2.csv", "last_submission.csv", "submission_kaggle_test.csv"]
DF = {}

for filename in RESULT_FILE:
    df = pd.read_csv(filename, sep=',', header=0, index_col=0)
    DF[filename] = df["Category"]

df1 = DF[RESULT_FILE[2]]
df2 = DF["result_2.csv"]

print("Total is", df1.shape[0])

print(sum(df1 != df2))
