from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt
from my_data import X_train, y_train

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Get feature importances
importances = model.feature_importances_
data: dict = {
    "feature": X_train.columns,
    "importance": importances
}
feature_importance_df = pd.DataFrame(data).sort_values("importance", ascending=False)
print(feature_importance_df)

# Visualize
plt.barh(feature_importance_df['feature'], feature_importance_df['importance'])
plt.xlabel('Importance')
plt.title('Feature Importance - Random Forest')
plt.show()


#        feature  importance
# 14  feature_14    0.131266
# 11  feature_11    0.113856
# 17  feature_17    0.090586
# 15  feature_15    0.077834
# 7    feature_7    0.064553
# 2    feature_2    0.057216
# 16  feature_16    0.053144
# 18  feature_18    0.052963
# 3    feature_3    0.044951
# 1    feature_1    0.044646
# 9    feature_9    0.043703
# 4    feature_4    0.038405
# 8    feature_8    0.035964
# 12  feature_12    0.032798
# 0    feature_0    0.032605
# 6    feature_6    0.017804
# 5    feature_5    0.017762
# 10  feature_10    0.017353
# 13  feature_13    0.016792
# 19  feature_19    0.015797
