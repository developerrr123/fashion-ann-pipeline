"""Download Fashion-MNIST and persist the raw arrays."""

from pathlib import Path

import numpy as np
from tensorflow import keras


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    (x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()
    np.savez_compressed(RAW_DIR / "train.npz", images=x_train, labels=y_train)
    np.savez_compressed(RAW_DIR / "test.npz", images=x_test, labels=y_test)
    print(f"Saved {len(x_train)} training and {len(x_test)} test examples to {RAW_DIR}")


if __name__ == "__main__":
    main()
