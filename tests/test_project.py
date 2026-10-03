from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_expected_pipeline_files_exist():
    expected = [
        "README.md",
        ".gitignore",
        "params.yaml",
        "dvc.yaml",
        "src/prepare.py",
        "src/preprocess.py",
        "src/train.py",
        "src/evaluate.py",
    ]
    assert all((ROOT / path).exists() for path in expected)


def test_pipeline_has_four_stages_and_metric():
    with (ROOT / "dvc.yaml").open(encoding="utf-8") as handle:
        pipeline = yaml.safe_load(handle)
    assert set(pipeline["stages"]) == {"prepare", "preprocess", "train", "evaluate"}
    assert pipeline["stages"]["evaluate"]["metrics"] == ["metrics.json"]


def test_parameters_are_declared():
    with (ROOT / "params.yaml").open(encoding="utf-8") as handle:
        params = yaml.safe_load(handle)
    assert params["train"]["dense_units"] > 0
    assert 0 < params["preprocess"]["test_size"] < 1
