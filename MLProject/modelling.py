import mlflow
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import os

data = np.load('telco_customer_churn_preprocessing/train.npz')
X, y = data['X_train'], data['y_train']
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"Training: {X_train.shape[0]} | Validation: {X_val.shape[0]}")

with mlflow.start_run(run_name="CI_RandomForest"):
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    
    acc = accuracy_score(y_val, y_pred)
    f1 = f1_score(y_val, y_pred, average='weighted')
    print(f"Accuracy: {acc:.4f} | F1: {f1:.4f}")
    
    run_id = mlflow.active_run().info.run_id
    with open('run_id.txt', 'w') as f:
        f.write(run_id)
    
    mlflow.sklearn.log_model(model, "model")
    print(f"Run ID: {run_id}")