# DVC Workflow

## 1. Remote Configuration

DVC remote name: `myremote`

Backend: Local directory `~/dvc-remote-storage`

The DVC remote is used to store the actual dataset objects, while Git stores the lightweight DVC metadata files.

## 2. Dataset Versioning Workflow

For each dataset version:

1. Create or modify `data/iris.csv`.
2. Run:
   `dvc add data/iris.csv`
3. Stage the DVC metadata:
   `git add data/iris.csv.dvc`
4. Commit the DVC metadata using Git.
5. Run:
   `dvc push`
6. Push the Git commit to GitHub:
   `git push origin main`

Git tracks the `.dvc` pointer file, while DVC tracks and stores the actual dataset.

## 3. Dataset Versions

### Version 1

Git commit: `251ee71`

Dataset: `data/iris.csv`

Data rows: 150

CSV lines including header: 151

### Version 2

Git commit: `0d75a68`

Dataset: `data/iris.csv`

Data rows: 170

CSV lines including header: 171

Version 2 contains 20 additional rows compared with Version 1.

## 4. Comparing Dataset Versions

The command:

`dvc diff 251ee71 0d75a68`

was used to compare Version 1 and Version 2.

The result showed:

`data\iris.csv` as Modified.

## 5. Restoring Dataset Versions

### Restore Version 1

```bash
git checkout 251ee71 -- data/iris.csv.dvc
dvc checkout data/iris.csv.dvc