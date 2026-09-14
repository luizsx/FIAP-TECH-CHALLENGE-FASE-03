
from typing import Iterable
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DEFAULT_FEATURES = [
    "sigla_uf",
    "serie",
    "rede",
    "presenca",
    "preenchimento_caderno",
]

def load_dataset(path: str, sep: str = ";") -> pd.DataFrame:
    return pd.read_csv(path, sep=sep, low_memory=False)

def to_numeric_br(series: pd.Series) -> pd.Series:
    if pd.api.types.is_numeric_dtype(series):
        return pd.to_numeric(series, errors="coerce")
    cleaned = (
        series.astype("string")
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
    )
    return pd.to_numeric(cleaned, errors="coerce")

def prepare_types(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    for col in result.columns:
        if result[col].dtype == "object":
            converted = to_numeric_br(result[col])
            if converted.notna().mean() >= 0.95:
                result[col] = converted
    return result

def split_temporal(
    df: pd.DataFrame,
    year_col: str = "ano",
    train_year: int = 2023,
    test_year: int = 2024,
):
    train = df[df[year_col] == train_year].copy()
    test = df[df[year_col] == test_year].copy()
    if train.empty or test.empty:
        raise ValueError("A separação temporal não encontrou treino ou teste.")
    return train, test

def build_preprocessor(X_train: pd.DataFrame) -> ColumnTransformer:
    numeric_cols = X_train.select_dtypes(include=["number", "bool"]).columns.tolist()
    categorical_cols = [c for c in X_train.columns if c not in numeric_cols]

    numeric_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])

    return ColumnTransformer([
        ("numeric", numeric_pipe, numeric_cols),
        ("categorical", categorical_pipe, categorical_cols),
    ])
