"""Normalize raw Fashion-MNIST data and create a validation split."""

from pathlib import Path

import numpy as np
import yaml
from sklearn.model_selection import train_test_split


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"


def main() -> None:
    with (ROOT / "params.yaml").open(encoding="utf-8") as handle:
        config = yaml.safe_load(handle)["preprocess"]

    train = np.load(RAW_DIR / "train.npz")
    test = np.load(RAW_DIR / "test.npz")
    x_train = (train["images"].astype("float32") / 255.0) ** 0.8
    x_test = (test["images"].astype("float32") / 255.0) ** 0.8
    y_train = train["labels"]
    y_test = test["labels"]
    x_train, x_val, y_train, y_val = train_test_split(
        x_train,
        y_train,
        test_size=config["test_size"],
        random_state=config["seed"],
        stratify=y_train,
    )

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(PROCESSED_DIR / "train.npz", images=x_train, labels=y_train)
    np.savez_compressed(PROCESSED_DIR / "val.npz", images=x_val, labels=y_val)
    np.savez_compressed(PROCESSED_DIR / "test.npz", images=x_test, labels=y_test)
    print(f"Saved processed train/validation/test arrays to {PROCESSED_DIR}")


if __name__ == "__main__":
    main()
