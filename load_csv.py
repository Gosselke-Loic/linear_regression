import pandas as pd


def load(path: str) -> pd.DataFrame:
    """ Load csv file from path file and return pandas DataFrame """

    loaded_csv = None
    try:
        loaded_csv = pd.read_csv(path)
    except Exception as e:
        print(f"An error was occurred: {e}")
        return loaded_csv

    return loaded_csv
