"""
Simple model training script for Hello World Azure ML service.
This creates a basic scikit-learn model that can be deployed to Azure ML.
"""
import json
import pickle
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os


def create_sample_data():
    """Create sample data for training simple regression model"""
    np.random.seed(42)

    # Create synthetic data: predict greeting sentiment score based on name length and vowel count
    names = [
        "Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah",
        "Ivan", "Julia", "Kevin", "Laura", "Michael", "Nancy", "Oliver", "Paula",
        "Quinn", "Rachel", "Steve", "Tina", "Uma", "Victor", "Wendy", "Xavier",
        "Yvonne", "Zachary", "AI", "ML", "Azure", "Python", "Data", "Science"
    ]

    features = []
    targets = []

    for name in names:
        # Features: name length, vowel count, consonant count
        name_length = len(name)
        vowel_count = sum(1 for char in name.lower() if char in 'aeiou')
        consonant_count = name_length - vowel_count

        # Target: synthetic "greeting enthusiasm score"
        enthusiasm_score = (
            name_length * 0.3 +
            vowel_count * 2.0 +
            consonant_count * 0.5 +
            np.random.normal(0, .5)     # Add some noise
        )

        features.append([name_length, vowel_count, consonant_count])
        targets.append(enthusiasm_score)

    return np.array(features), np.array(targets)


def train_model():
    """Train simple regression model"""
    print("Training Hello World greeting model")

    # Create sample data
    X, y = create_sample_data()

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create and train the model pipeline
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Model performance")
    print(f"  MSE: {mse:.4f}")
    print(f"  Rsq: {r2:.4f}")

    return model, scaler


def save_model(model, scaler, model_dir="./model"):
    """Save the trained model and preprocessing components"""
    os.makedirs(model_dir, exist_ok=True)

    # Save the model and scaler
    joblib.dump(model, os.path.join(model_dir, "greeting_model.pkl"))
    joblib.dump(scaler, os.path.join(model_dir, "scaler.pkl"))

    # Create model metadata
    model_info = {
        "model_name": "greeting_enthusiasm_predictor",
        "model_type": "LinearRegression",
        "version": "1.0.0",
        "created_data": datetime.now().isoformat(),
        "description": "Predicts greeting enthusiasm score based on name characteristics",
        "features": [
            "name_length",
            "vowel_count",
            "consonant_count"
        ],
        "target": "enthusiasm_score",
        "framework": "scikit-learn",
        "preprocessing": "StandardScaler"
    }

    with open(os.path.join(model_dir, "model_info.json"), "w") as f:
        json.dump(model_info, f, indent=2)

    print(f"Model saved to {model_dir}/")
    print("     - greeting_model.pkl")
    print("     - scaler.pkl")
    print("     - model_info.json")


def main():
    """Main training function"""
    print("Hello World")

    # Train the model
    model, scaler = train_model()

    # Save the model
    save_model(model, scaler)

    # Test the model with sample names
    print()
    test_names = ["Alice", "Bob", "AI", "Azure", "Python"]

    for name in test_names:
        name_length = len(name)
        vowel_count = sum(1 for char in name.lower() if char in 'aeiou')
        consonant_count = name_length - vowel_count

        features = np.array([[name_length, vowel_count, consonant_count]])
        features_scaled = scaler.transform(features)
        enthusiasm = model.predict(features_scaled)[0]

        print(f"    {name}: enthusiasm score = {enthusiasm:.2f}")

    print("the end")


if __name__ == '__main__':
    main()