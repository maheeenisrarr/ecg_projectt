import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

np.random.seed(42)
n_samples = 500

heart_rate = np.random.randint(60, 120, n_samples)
qrs_width = np.random.uniform(0.06, 0.12, n_samples)
st_level = np.random.uniform(-0.5, 0.5, n_samples)
qt_interval = np.random.uniform(0.35, 0.45, n_samples)

X = np.column_stack([heart_rate, qrs_width, st_level, qt_interval])
y = np.where((heart_rate > 100) | (st_level > 0.3), 1, 0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "ecg_model.pkl")
print("✅ Demo ECG model saved as ecg_model.pkl")
print("Test prediction (0=Normal, 1=Abnormal):", model.predict([[85, 0.09, 0.1, 0.4]]))
