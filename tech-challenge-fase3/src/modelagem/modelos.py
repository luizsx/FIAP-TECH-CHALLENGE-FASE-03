

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

def build_models(preprocessor, random_state: int = 42):
    return {
        "Regressão Logística": Pipeline([
            ("preprocessor", preprocessor),
            ("model", LogisticRegression(max_iter=1000, random_state=random_state)),
        ]),
        "Random Forest": Pipeline([
            ("preprocessor", preprocessor),
            ("model", RandomForestClassifier(
                n_estimators=200,
                random_state=random_state,
                n_jobs=-1,
                class_weight="balanced",
            )),
        ]),
    }

def fit_models(models, X_train, y_train):
    for model in models.values():
        model.fit(X_train, y_train)
    return models
