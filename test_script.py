#test_script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

from io import BytesIO
import gdown

# Replace 'FILE_ID' with the actual ID of your Google Drive file
file_id = '1m73Ot3M2O2YPPH1urzuTejOaOEQuDi2P'

# Google Drive API endpoint to download the file
url = f'https://drive.google.com/uc?id={file_id}'



file = gdown.download(url,output="wildfire_base_clean.zip")

# Convert the downloaded file bytes to a BytesIO object
# file_in_memory = BytesIO(file_bytes)

df=pd.read_csv(file,compression='zip')

with open('head.pkl','wb') as f : 
    pickle.dump(df.head(),f)

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='annee')
plt.savefig('plot.png')


if __name__ == "__main__" : 
    None