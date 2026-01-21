from sklearn.ensemble import RandomForestClassifier
from my_data import X_train, X_test, y_train, y_test

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Train model with new features
model_final = RandomForestClassifier(n_estimators=100, random_state=42)
model_final.fit(X_train, y_train)

# Compare performance
baseline_score = model.score(X_test, y_test)
final_score = model_final.score(X_test, y_test)

print(f"Baseline accuracy: {baseline_score:.4f}")
print(f"Final accuracy: {final_score:.4f}")
print(f"Improvement: {(final_score - baseline_score):.4f}")

# Baseline accuracy: 0.9100
# Final accuracy: 0.9100
# Improvement: 0.0000
