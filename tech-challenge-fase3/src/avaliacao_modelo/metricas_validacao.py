import pandas as pd
from sklearn.metrics import (
    accuracy_score, average_precision_score, confusion_matrix,
    f1_score, precision_score, recall_score, roc_auc_score
)

def evaluate_model(model, X_test, y_test) -> dict:
    pred = model.predict(X_test)
    proba = model.predict_proba(X_test)[:, 1]
    return {
        "accuracy": accuracy_score(y_test, pred),
        "precision": precision_score(y_test, pred, zero_division=0),
        "recall": recall_score(y_test, pred, zero_division=0),
        "f1": f1_score(y_test, pred, zero_division=0),
        "roc_auc": roc_auc_score(y_test, proba),
        "average_precision": average_precision_score(y_test, proba),
        "predictions": pred,
        "probabilities": proba,
        "confusion_matrix": confusion_matrix(y_test, pred),
    }

def evaluate_models(models, X_test, y_test) -> tuple[pd.DataFrame, dict]:
    evaluations = {name: evaluate_model(model, X_test, y_test)
                   for name, model in models.items()}
    rows = []
    for name, result in evaluations.items():
        rows.append({
            "modelo": name,
            **{k: result[k] for k in [
                "accuracy", "precision", "recall", "f1",
                "roc_auc", "average_precision"
            ]}
        })
    return pd.DataFrame(rows).sort_values("f1", ascending=False), evaluations
