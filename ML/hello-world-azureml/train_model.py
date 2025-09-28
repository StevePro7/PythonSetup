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

print("TM")