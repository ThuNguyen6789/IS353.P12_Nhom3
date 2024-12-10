from sklearn.ensemble import RandomForestClassifier

def create_model(params):
    return RandomForestClassifier(**params, random_state=42)
