import os
import joblib
from src.preprocessing import preprocess_data
from src.model import create_model
from imblearn.combine import SMOTEENN
from sklearn.model_selection import train_test_split

def train_model(data_path='data/processed.csv', save_path='src/model.pkl'):
    print("Starting model training process...")

    X, y = preprocess_data(data_path)
    print(f"Data preprocessing complete. X shape: {X.shape}, y shape: {y.shape}")
    
    print("Resampling data using SMOTEENN...")
    resampler = SMOTEENN(sampling_strategy="auto", random_state=42)
    X_resampled, y_resampled = resampler.fit_resample(X, y)
    print(f"Resampling complete. X_resampled shape: {X_resampled.shape}, y_resampled shape: {y_resampled.shape}")
    
    print("Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X_resampled, y_resampled, test_size=0.2, random_state=42, stratify=y_resampled
    )
    print(f"Training data shape: X_train: {X_train.shape}, y_train: {y_train.shape}")
    print(f"Test data shape: X_test: {X_test.shape}, y_test: {y_test.shape}")
    
    params = {
        'max_depth': 7,
        'n_estimators': 200,
        'colsample_bytree': 1.0,
        'subsample': 0.9,
    }
    print(f"Model hyperparameters: {params}")

    print("Creating and training the model...")
    model = create_model(params)
    model.fit(X_train, y_train)
    print("Model training complete.")
    
    save_dir = os.path.dirname(save_path)
    if save_dir and not os.path.exists(save_dir):
        os.makedirs(save_dir)
        print(f"Created directory {save_dir}")

    print(f"Saving the model to {save_path}...")
    joblib.dump(model, save_path)
    print(f"Model saved to {os.path.abspath(save_path)}")

# Run the training process
if __name__ == "__main__":
    train_model()
