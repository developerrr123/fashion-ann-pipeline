# Assignment 3 Report: Git, DVC & TensorFlow

**Student:** TODO  
**GitHub repository:** TODO  
**Google Drive DVC remote:** TODO  

## 1. Project and target

This project uses Fashion-MNIST and a fully connected ANN. The target is at least 85% test accuracy. The complete pipeline is reproducible with `dvc repro`.

## 2. Git evidence

Capture and paste terminal output or screenshots for:

- `git log --oneline --graph --all`: compact graph of all branches and commit relationships.
- `git log --stat -3`: the latest three commits plus changed-file statistics.
- `git log -p -1`: the latest commit's exact patch.
- `git log main..dev`: commits reachable from `dev` but not `main`.
- `git diff`: unstaged changes.
- `git diff --staged`: staged changes.
- `git diff main..dev`: differences between the two branch tips.
- `git diff main...dev`: differences from the common ancestor to `dev`; this is useful for reviewing what `dev` introduced regardless of changes on `main`.
- `git stash list` before `git stash pop`, showing the `preprocess.py` pause/resume scenario.
- Before and after `git rebase main`.
- `git reset --soft HEAD~1`: changes remain staged; `git reset --hard HEAD~1`: commit and working-tree changes are discarded.
- `git mv` and `git rm` commit history.

## 3. Pipeline implementation

The four scripts are independent command-line programs:

```text
prepare -> preprocess -> train -> evaluate
```

Run the final pipeline and record:

```powershell
dvc repro
dvc metrics show
dvc status
```

Attach the resulting `metrics.json` and confusion matrix screenshot. Confirm test accuracy is at least 0.85.

## 4. DVC and Google Drive evidence

Record the commands and screenshots for `dvc init`, remote configuration, OAuth authorization, `dvc push`, and the Google Drive folder showing the uploaded cache. Confirm `.dvc/tmp` and credentials are excluded by `.gitignore`.

## 5. Parameter reproduction experiment

Change one value in `params.yaml`, for example `train.dense_units`, then run `dvc repro` again. Expected behavior: `train` and `evaluate` rerun because the training parameter changed; `prepare` and `preprocess` are skipped because their dependencies and parameters did not change.

Record v1 and v2 values:

| Version | Dense units | Test loss | Test accuracy |
|---|---:|---:|---:|
| v1 | TODO | TODO | TODO |
| v2 | TODO | TODO | TODO |

## 6. Conflict simulation

Record screenshots showing both conflicts:

1. `preprocess.py` normalization conflict after merging `teammate-sim`.
2. The processed-data DVC pointer conflict.

After resolving, record:

```powershell
dvc checkout
dvc status
dvc repro
git add src/preprocess.py data/processed.dvc dvc.lock
git commit -m "Resolve code and DVC data conflicts"
git push origin main
 dvc push
```

Explain which normalization and processed-data version became authoritative, and why the final `dvc status` is clean.

## 7. Final submission checklist

- [ ] GitHub repository link with unsquashed history and at least six incremental `dev` commits.
- [ ] Google Drive DVC remote shared with the instructor.
- [ ] Final `dvc.lock` committed.
- [ ] `v1` and `v2` tags created and pushed.
- [ ] PDF report exported from this document with screenshots and command output.
- [ ] Final test accuracy meets the 85% target.
