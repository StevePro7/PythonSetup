import lime
import lime.lime_tabular
from sklearn.ensemble import RandomForestClassifier
from my_data import X_train, y_train, X_test


# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Create LIME explainer
explainer = lime.lime_tabular.LimeTabularExplainer(
    X_train.values,
    feature_names=X_train.columns,
    class_names=["Class_0", "Class_1"],
    mode="classification"
)

# Explain single prediction
exp = explainer.explain_instance(
    X_test.iloc[0].values,
    model.predict_proba,
    num_features=10
)
exp.show_in_notebook()
