import pandas as pd
import os

def test_dataset_exists():
    """Check if the dataset file exists in the current directory."""
    assert os.path.exists("dataset_2.csv"), "dataset_2.csv not found"

def test_load_data():
    """Verify that the dataset can be loaded into a pandas DataFrame."""
    try:
        df = pd.read_csv("dataset_2.csv")
        assert not df.empty, "DataFrame is empty"
        assert isinstance(df, pd.DataFrame), "Object is not a pandas DataFrame"
    except Exception as e:
        assert False, f"Failed to load data: {e}"

if __name__ == "__main__":
    test_dataset_exists()
    test_load_data()
    print("All tests passed!")
