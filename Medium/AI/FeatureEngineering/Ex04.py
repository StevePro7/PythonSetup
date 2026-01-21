import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from my_data import X_train, y_train, X_test, y_test


# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Create SHAP explainer
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# Global importance
shap.summary_plot(shap_values, X_test, plot_type="bar")
plt.title("SHAP")
plt.show()

# Local explanation for one prediction
shap.force_plot(explainer.expected_value[1],
                shap_values[1][0], X_test.iloc[0])

# shap.utils._exceptions.DimensionError: Length of features is not equal to the length of shap_values!
