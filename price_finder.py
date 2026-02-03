import sys
import json

from pandas import DataFrame

from load_csv import load
from normalize import normalize_one


def get_input() -> str | None:
    """ Get input value from standard input """
    while True:
        try:
            input_value = input("Enter kilometers of your car: ")
            value = int(input_value)

            return value
        except ValueError:
            print("Input value is not a valid integer")
        except EOFError:
            return None


def load_model_weights() -> tuple | None:
    """ Load weights from json file """
    try:
        with open("model_weights.json", mode="r") as f:
            data = json.load(f)
            theta0 = data["theta0"]
            theta1 = data["theta1"]
            return (theta0, theta1)
    except FileNotFoundError:
        print("Error: file 'model_weights.json' not found")
        return None


def main():
    """ Program that return a estimate price for a given mileage car """
    PATH = "./resources/data.csv"

    try:
        df: DataFrame = load(PATH)
        if df is None:
            sys.exit("Error to parse csv, closing program.")

        theta_tuple = load_model_weights()
        if theta_tuple is None:
            sys.exit(0)

        value = get_input()
        if value is None:
            sys.exit(0)

        mileage = df["km"].values
        price = df["price"].values

        val_norm = normalize_one(mileage, value)

        result = theta_tuple[0] + (theta_tuple[1] * val_norm)

        min_price = min(price)
        max_price = max(price)

        final_price = result * (max_price - min_price) + min_price

        print(f"result: {final_price}")
    except Exception as e:
        sys.exit("Error: ", e)


if __name__ == "__main__":
    main()
