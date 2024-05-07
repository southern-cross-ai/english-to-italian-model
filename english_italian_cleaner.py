import pandas as pd

# Read the data
data = pd.read_csv("english_italian.txt", sep="\t", header=None, names=["English", "Italian", "License"])

# Select English and Italian columns
english_italian_data = data[["English", "Italian"]]

# Save to a text file with tab separation
with open("english_italian.txt", "w", encoding="utf-8") as f:
    f.write(english_italian_data.to_csv(sep="\t", index=False, header=False))