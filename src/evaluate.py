from sklearn.metrics import classification_report, confusion_matrix
import joblib

def evaluate_model(model_path, X_test, y_test):
    model = joblib.load(model_path)
    y_pred = model.predict(X_test)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
