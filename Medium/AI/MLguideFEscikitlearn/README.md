Feature Engineering for Machine Learning:
A Practical Guide with Scikit-learn

24-Jan-2026


Ex 01
   tenure_months  monthly_charge last_login_date subscription_plan
0              3            9.99      2025-09-15             Basic
1             24           19.99      2025-09-10           Premium
2              1           19.99      2025-08-20           Premium
3             15           14.99      2025-09-18             Basic
4              8            9.99      2025-07-01             Basic


Ex02
  last_login_date  days_since_last_login
0      2025-09-15                      4
1      2025-09-10                      9
2      2025-08-20                     30
3      2025-09-18                      1
4      2025-07-01                     80


Ex 03
   tenure_months  tenure_group
0              3           0.0
1             24           2.0
2              1           0.0
3             15           1.0
4              8           0.0


Ex 04
   tenure_months  monthly_charge  tenure_charge_interaction
0              3            9.99                      29.97
1             24           19.99                     479.76
2              1           19.99                      19.99
3             15           14.99                     224.85
4              8            9.99                      79.92


Ex 05
   subscription_plan_Basic  subscription_plan_Premium
0                      1.0                        0.0
1                      0.0                        1.0
2                      0.0                        1.0
3                      1.0                        0.0
4                      1.0                        0.0


Ex06
[[0.0 1.0 0.0 9.99 Timestamp('2025-09-15 00:00:00') 4]
 [2.0 0.0 1.0 19.99 Timestamp('2025-09-10 00:00:00') 9]
 [0.0 0.0 1.0 19.99 Timestamp('2025-08-20 00:00:00') 30]
 [1.0 1.0 0.0 14.99 Timestamp('2025-09-18 00:00:00') 1]
 [0.0 1.0 0.0 9.99 Timestamp('2025-07-01 00:00:00') 80]]