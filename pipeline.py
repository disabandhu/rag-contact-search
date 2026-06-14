import pandas as pd
import numpy as np


def preprocess_data(file_path):
    df = pd.read_csv(file_path)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Drop columns with >90% nulls
    null_percent = df.isnull().mean() * 100
    cols_to_drop = null_percent[null_percent > 90].index
    df = df.drop(columns=cols_to_drop)

    # Remove duplicate columns like .1, .2
    df = df.loc[:, ~df.columns.str.contains(r'\.\d+$')]

    return df


def get_best_email(row):
    if pd.notnull(row.get("Primary Email")):
        return row["Primary Email"]

    best_email = None
    best_score = -1

    for i in range(1, 11):
        email_col = f"Email {i}"
        score_col = f"Email {i} Total AI"
        validation_col = f"Email {i} Validation"

        email = row.get(email_col)
        score = row.get(score_col)
        validation = str(row.get(validation_col)).lower()

        if pd.notnull(email):
            is_valid = "valid" in validation or "verified" in validation

            if score is not None and score > best_score and is_valid:
                best_email = email
                best_score = score

    return best_email


def process_pipeline(file_path):
    df = preprocess_data(file_path)

    # Convert AI scores to numeric
    for i in range(1, 11):
        col = f"Email {i} Total AI"
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Apply email selection logic
    df["best_email"] = df.apply(get_best_email, axis=1)

    return df