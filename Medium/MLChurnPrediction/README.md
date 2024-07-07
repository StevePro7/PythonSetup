End-to-End Machine Learning Project: Churn Prediction
05-Jul-2024

https://medium.com/@ramazanolmeez/end-to-end-machine-learning-project-churn-prediction-e9c4d0322ac9

GitLab
https://github.com/rolmez/Customer-Churn-Project


pip install -r requirements.txt


contourpy==1.2.0
llvmlite==0.42.0
matplotlib=3.7.5
numba==0.59.0
numpy==1.26.4
scipy==1.12.0

pip install --upgrade pip


PKL
https://marketplace.visualstudio.com/items?itemName=Percy.vscode-pydata-viewer

https://stackoverflow.com/questions/63379164/how-do-i-access-data-from-python-files-pkl-pickle
#pip install pickle-mixin
import pickle

with open(path, "rb") as f:
    content = pickle.load(f)


01.
train_model.py

02.
streamlit-app.py
streamlit run /home/stevepro/GitHub/StevePro9/PythonSetup/Medium/MLChurnPrediction/src/streamlit-app.py
http://localhost:8501/

03.
fast-api.py
python fast-api.py

http://127.0.0.1:5000/docs

04.
predict.py

05.
docker build -t churn-prediction-app .
