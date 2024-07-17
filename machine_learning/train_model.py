import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib


def train_model():
    # Загрузка данных (замени на свои данные)
    data = pd.read_csv('financial_data.csv')

    # Предобработка данных
    X = data[['feature1', 'feature2']]  # замените на свои фичи
    y = data['target']  # замените на свою целевую переменную

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, 'model.pkl')


if __name__ == '__main__':
    train_model()
