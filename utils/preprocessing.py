import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_data(file_path):
    """
    Load CSV dataset
    """
    return pd.read_csv(file_path)


def clean_data(df):
    """
    Handle missing values and remove duplicates
    """
    df = df.drop_duplicates()

    # Fill missing numerical values
    numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in numerical_cols:
        df[col] = df[col].fillna(df[col].median())

    # Fill missing categorical values
    categorical_cols = df.select_dtypes(include=["object"]).columns

    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df


def encode_categorical(df):
    """
    Encode categorical columns
    """
    label_encoders = {}

    categorical_cols = df.select_dtypes(include=["object"]).columns

    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

        label_encoders[col] = le

    return df, label_encoders


def preprocess_data(file_path):
    """
    Complete preprocessing pipeline
    """
    df = load_data(file_path)

    df = clean_data(df)

    df, encoders = encode_categorical(df)

    return df, encoders


if __name__ == "__main__":
    df, encoders = preprocess_data("data/Indian_Startups.csv")

    print("Preprocessing Completed Successfully!")
    print(df.head())
