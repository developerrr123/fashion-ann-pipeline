"""Train the parameterized fully connected Fashion-MNIST ANN."""

import csv
import random
from pathlib import Path

import numpy as np
import tensorflow as tf
import yaml


ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = ROOT / "data" / "processed"
MODELS_DIR = ROOT / "models"


def main() -> None:
    with (ROOT / "params.yaml").open(encoding="utf-8") as handle:
        config = yaml.safe_load(handle)["train"]

    seed = config["seed"]
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)

    train = np.load(PROCESSED_DIR / "train.npz")
    validation = np.load(PROCESSED_DIR / "val.npz")
    model = tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(28, 28)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(config["dense_units"], activation="relu"),
            tf.keras.layers.Dropout(config["dropout_rate"]),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=config["learning_rate"]),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    history = model.fit(
        train["images"],
        train["labels"],
        validation_data=(validation["images"], validation["labels"]),
        epochs=config["epochs"],
        batch_size=config["batch_size"],
        verbose=2,
    )

    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    model.save(MODELS_DIR / "model.h5")
    with (MODELS_DIR / "history.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        keys = list(history.history)
        writer.writerow(["epoch", *keys])
        for index, values in enumerate(zip(*(history.history[key] for key in keys)), start=1):
            writer.writerow([index, *values])
    print(f"Saved model and training history to {MODELS_DIR}")


if __name__ == "__main__":
    main()
