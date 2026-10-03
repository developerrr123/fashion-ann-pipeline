# Fashion ANN Pipeline

End-to-end Fashion-MNIST classification with Git, DVC, Google Drive, and TensorFlow.

## Setup

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Initialize Git and DVC:

```powershell
git init
git add .
git commit -m "Initial project structure"
git branch -M main
git checkout -b dev
dvc init
dvc remote add -d gdrive gdrive://YOUR_GOOGLE_DRIVE_FOLDER_ID
```

Configure Google Drive OAuth using the instructions in `docs/dvc-google-drive.md`. Never commit client secrets or token files.

## Run the pipeline

```powershell
dvc repro
dvc metrics show
```

The pipeline downloads Fashion-MNIST, preprocesses it, trains a fully connected ANN, and writes `metrics.json` plus `reports/confusion_matrix.png`.

## Expected structure

- `src/prepare.py`: download and store raw arrays
- `src/preprocess.py`: normalize and create train/validation/test arrays
- `src/train.py`: train and save the ANN
- `src/evaluate.py`: evaluate, write metrics, and create a confusion matrix
- `params.yaml`: single source of truth for configurable values
- `dvc.yaml` and `dvc.lock`: reproducible pipeline definition and lockfile
- `report/assignment3_report.md`: evidence checklist and report template

## External evidence still required

The code and local pipeline can be prepared here. You must perform Google OAuth, use your own Google Drive folder, push to your own GitHub repository, and capture screenshots of your own command output and conflict-resolution workflow. Do not place credentials in this repository.
