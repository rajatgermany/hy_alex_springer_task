import pandas as pd
import os
import re
import numpy as np

DATA_DIR = "./data"
SAMPLED_DATA_PATH = os.path.join(DATA_DIR, "base_data/sampled_data.csv")
CLEANED_DATA_PATH = os.path.join(DATA_DIR, "cleaned_data/v1.csv")

data = pd.read_csv(SAMPLED_DATA_PATH)

def extract_year(item):
    """Extracts year 
        Note - Scrapper fails to extract some startup's founded year info so used error handling
    """
    try:
        return re.findall("(?:20|19)\d+", item)[0]  # function returns list, so extracting first value
    except:
        return np.nan

# Extracted the year
data["Founded"] = data["Founded"].apply(extract_year)

# Arrange Colums order
col =['startup',
    'title',
    'Location',
    'Founded',
    'Investment',
    'Management', 
    'Segment', 
    'description', 
    'Website',
    'facebook',
    'instagram',
    'linkedin',
    'twitter',
    'xing',
    'youtube'
   ]

data = data[col]
data.to_csv(CLEANED_DATA_PATH, index=False)
