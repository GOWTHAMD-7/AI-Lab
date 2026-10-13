"""
EXPERIMENT 1: Data Pre-processing, Annotation, and Creation of Datasets
Course: AI Lab Practical (CSE)
Description:
    Demonstrates data preprocessing (handling missing values, categorical encoding,
    feature scaling), dataset annotation, and dataset creation/export using Python.
"""

import os
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split


def create_raw_dataset():
    """Step 1: Create a raw dataset with mixed types and missing values."""
    print("=" * 70)
    print("STEP 1: CREATION OF RAW DATASET")
    print("=" * 70)

    raw_data = {
        "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108],
        "Study_Hours": [12.0, 18.5, np.nan, 22.0, 8.5, np.nan, 25.0, 15.0],
        "Attendance_Pct": [85.0, 92.0, 78.0, np.nan, 65.0, 88.0, 95.0, np.nan],
        "Department": ["CSE", "ECE", "CSE", "IT", "ECE", "CSE", "IT", "ECE"],
        "Internal_Score": [74.0, 88.0, 62.0, 91.0, 48.0, 79.0, 96.0, 70.0],
        "Result": ["Pass", "Pass", "Pass", "Pass", "Fail", "Pass", "Pass", "Pass"]
    }

    df = pd.DataFrame(raw_data)
    print("Raw Data Preview:")
    print(df.to_string(index=False))
    print(f"\nMissing values per column:\n{df.isnull().sum()}")
    return df


def handle_missing_values(df):
    """Step 2: Handle missing numerical values using Mean Imputation."""
    print("\n" + "=" * 70)
    print("STEP 2: HANDLING MISSING VALUES (IMPUTATION)")
    print("=" * 70)

    df_cleaned = df.copy()
    num_cols = ["Study_Hours", "Attendance_Pct"]

    imputer = SimpleImputer(strategy="mean")
    df_cleaned[num_cols] = imputer.fit_transform(df_cleaned[num_cols])

    # Round imputed values for clean presentation
    df_cleaned[num_cols] = df_cleaned[num_cols].round(2)

    print("Data after Mean Imputation (no missing values):")
    print(df_cleaned.to_string(index=False))
    return df_cleaned


def encode_categorical_features(df):
    """Step 3: Encode categorical features into numerical values."""
    print("\n" + "=" * 70)
    print("STEP 3: CATEGORICAL DATA ENCODING")
    print("=" * 70)

    df_encoded = df.copy()

    # Label Encoding for Department and Result
    le_dept = LabelEncoder()
    le_result = LabelEncoder()

    df_encoded["Dept_Code"] = le_dept.fit_transform(df_encoded["Department"])
    df_encoded["Result_Code"] = le_result.fit_transform(df_encoded["Result"])

    print("Mapping for Department:")
    for code, label in enumerate(le_dept.classes_):
        print(f"  {label} -> {code}")

    print("\nMapping for Result:")
    for code, label in enumerate(le_result.classes_):
        print(f"  {label} -> {code}")

    print("\nData after Label Encoding:")
    print(df_encoded[["Student_ID", "Department", "Dept_Code", "Result", "Result_Code"]].to_string(index=False))
    return df_encoded


def scale_features(df):
    """Step 4: Scale numerical features to range [0, 1] using MinMaxScaler."""
    print("\n" + "=" * 70)
    print("STEP 4: FEATURE SCALING / NORMALIZATION (MIN-MAX SCALER)")
    print("=" * 70)

    df_scaled = df.copy()
    features_to_scale = ["Study_Hours", "Attendance_Pct", "Internal_Score"]

    scaler = MinMaxScaler()
    scaled_values = scaler.fit_transform(df_scaled[features_to_scale])

    scaled_cols = [f"{col}_Scaled" for col in features_to_scale]
    df_scaled[scaled_cols] = np.round(scaled_values, 4)

    print("Scaled Features (Range 0 to 1):")
    print(df_scaled[["Student_ID"] + scaled_cols].to_string(index=False))
    return df_scaled


def annotate_dataset(df):
    """Step 5: Data Annotation / Labeling using AI rule thresholding."""
    print("\n" + "=" * 70)
    print("STEP 5: DATA ANNOTATION / CREATION OF TARGET LABELS")
    print("=" * 70)

    df_annotated = df.copy()

    # Annotation logic:
    # Score >= 85 -> "Distinction"
    # Score >= 60 -> "First_Class"
    # Otherwise   -> "Needs_Improvement"
    def assign_grade_tag(score):
        if score >= 85:
            return "Distinction"
        elif score >= 60:
            return "First_Class"
        else:
            return "Needs_Improvement"

    df_annotated["Performance_Annotation"] = df_annotated["Internal_Score"].apply(assign_grade_tag)

    print("Annotated Dataset with Performance Tags:")
    print(df_annotated[["Student_ID", "Internal_Score", "Performance_Annotation"]].to_string(index=False))
    return df_annotated


def split_and_export_dataset(df):
    """Step 6: Train-Test Split and export final preprocessed dataset."""
    print("\n" + "=" * 70)
    print("STEP 6: TRAIN-TEST SPLITTING & DATASET EXPORT")
    print("=" * 70)

    feature_cols = ["Study_Hours_Scaled", "Attendance_Pct_Scaled", "Dept_Code", "Internal_Score_Scaled"]
    target_col = "Result_Code"

    X = df[feature_cols]
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    print(f"Total instances  : {len(df)}")
    print(f"Training samples : {len(X_train)} (75%)")
    print(f"Testing samples  : {len(X_test)} (25%)")

    # Export clean preprocessed dataset to CSV
    output_filename = os.path.join(os.path.dirname(__file__), "preprocessed_dataset.csv")
    df.to_csv(output_filename, index=False)
    print(f"\nFinal preprocessed dataset saved to: {output_filename}")


def main():
    print("=" * 70)
    print("EXPERIMENT 1: DATA PRE-PROCESSING, ANNOTATION & DATASET CREATION")
    print("=" * 70)

    # Execute all 6 pipeline stages
    df_raw = create_raw_dataset()
    df_imputed = handle_missing_values(df_raw)
    df_encoded = encode_categorical_features(df_imputed)
    df_scaled = scale_features(df_encoded)
    df_annotated = annotate_dataset(df_scaled)
    split_and_export_dataset(df_annotated)

    print("\n" + "=" * 70)
    print("EXPERIMENT 1 COMPLETED SUCCESSFULLY!")
    print("=" * 70)


if __name__ == "__main__":
    main()
