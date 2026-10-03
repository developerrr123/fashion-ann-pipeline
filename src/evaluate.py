"""Evaluate the trained ANN and write metrics plus a confusion matrix."""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = ROOT / "data" / "processed"
MODEL_PATH = ROOT / "models" / "model.h5"
REPORTS_DIR = ROOT / "reports"


def main() -> None:
    test = np.load(PROCESSED_DIR / "test.npz")
    model = tf.keras.models.load_model(MODEL_PATH)
    loss, accuracy = model.evaluate(test["images"], test["labels"], verbose=0)
    predictions = np.argmax(model.predict(test["images"], verbose=0), axis=1)

    metrics = {"test_loss": float(loss), "test_accuracy": float(accuracy)}
    with (ROOT / "metrics.json").open("w", encoding="utf-8") as handle:
        json.dump(metrics, handle, indent=2)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    display = ConfusionMatrixDisplay(
        confusion_matrix(test["labels"], predictions),
        display_labels=["T-shirt", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"],
    )
    display.plot(xticks_rotation="vertical", values_format="d")
    plt.tight_layout()
    plt.savefig(REPORTS_DIR / "confusion_matrix.png", dpi=160)
    plt.close()
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
