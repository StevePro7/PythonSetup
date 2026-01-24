import pandas as pd
# Create sample raw data
data = {
    "tenure_months": [3, 24, 1, 15, 8],
    "monthly_charge": [9.99, 19.99, 19.99, 14.99, 9.99],
    "last_login_date": ["2025-09-15", "2025-09-10", "2025-08-20", "2025-09-18", "2025-07-01"],
    "subscription_plan": ["Basic", "Premium", "Premium", "Basic", "Basic"]
}

df = pd.DataFrame(data)