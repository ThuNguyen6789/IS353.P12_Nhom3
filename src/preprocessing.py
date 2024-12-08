import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(filepath):
    df = pd.read_csv(filepath)
    print(df.columns)
    feature_names = ['dtbhk_truoc', 'drltl', 'sotchk', 'namhoc']
    scaler = StandardScaler()
    X = scaler.fit_transform(df[feature_names])
    y = df['xeploai']
    return X, y
