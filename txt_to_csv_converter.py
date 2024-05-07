import pandas as pd

# Read the data
data = pd.read_csv("english_italian.txt", sep="\t", header=None, names=["English", "Italian"])

# Save directly to a CSV file
data.to_csv("english_italian.csv", index=False)