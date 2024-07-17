import joblib
import pandas as pd


def make_prediction():
    model = joblib.load('machine_learning/model.pkl')

    # Загрузка новых данных для предсказания (замени на свои данные)
    new_data = pd.DataFrame({
        'feature1': [value1],
        'feature2': [value2]
    })

    prediction = model.predict(new_data)
    return prediction[0]
