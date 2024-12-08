from xgboost import XGBClassifier

def create_model(params):
    return XGBClassifier(**params, random_state=42)