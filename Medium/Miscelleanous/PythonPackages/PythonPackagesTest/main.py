from mlpredictor import MLPredictor

def test_train_and_predict():
    model = MLPredictor()
    model.train()
    result = model.predict([5.1, 3.5, 1.4, 0.2])
    print(result)

if __name__ == "__main__":
    test_train_and_predict()

