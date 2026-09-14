import matplotlib.pyplot as plt
import seaborn as sns

def plot_confusion_matrix(cm, title="Matriz de confusão"):
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt=",", cmap="Blues", cbar=False, ax=ax)
    ax.set_title(title)
    ax.set_xlabel("Predito")
    ax.set_ylabel("Real")
    fig.tight_layout()
    return fig, ax

def plot_model_metrics(results_df):
    metric_cols = ["accuracy", "precision", "recall", "f1", "roc_auc"]
    ax = results_df.set_index("modelo")[metric_cols].plot(
        kind="bar", figsize=(10, 5), ylim=(0, 1)
    )
    ax.set_ylabel("Métrica")
    ax.set_title("Comparação dos modelos")
    ax.grid(axis="y", alpha=0.3)
    fig = ax.get_figure()
    fig.tight_layout()
    return fig, ax
