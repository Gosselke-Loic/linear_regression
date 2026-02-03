import sys
import json

from pandas import DataFrame

from load_csv import load
from normalize import normalize


def main() -> None:
    """
    Linear regression program that return weights to estimate price cars
    """
    PATH = "./resources/data.csv"

    df: DataFrame = load(PATH)
    if df is None:
        sys.exit("Error to parse csv, closing program.")

    mileage = df["km"].values

    m = len(mileage)
    mileage_norm = normalize(mileage)
    price_norm = normalize(df["price"].values)

    theta00 = 0.0
    theta01 = 0.0
    iterations = 5000
    learning_rate = 0.01

    for _ in range(iterations):
        sum0 = 0.0
        sum1 = 0.0

        for i in range((m)):
            prediction = theta00 + (theta01 * mileage_norm[i])
            error = prediction - price_norm[i]
            sum0 += error
            sum1 += error * mileage_norm[i]

        theta00 -= learning_rate * (1/m) * sum0
        theta01 -= learning_rate * (1/m) * sum1

    with open("model_weights.json", mode="w", encoding="utf-8") as write_file:
        json.dump({"theta0": theta00, "theta1": theta01}, write_file)


if __name__ == "__main__":
    main()
