import pandas as pd
import os

DATA_DIR = "./data"
DATA_PATH = os.path.join(DATA_DIR, "cleaned_data/v1.csv")

data = pd.read_csv(DATA_PATH)

# Statistics
def get_startups_founded_per_year():
    return data["Founded"].value_counts()

if __name__ == "__main__":
    print(get_startups_founded_per_year())
