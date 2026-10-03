# DVC Google Drive setup

Use this guide after the first Git commit and from the project root.

```powershell
python -m pip install "dvc[gdrive]"
dvc init
dvc remote add -d gdrive gdrive://YOUR_GOOGLE_DRIVE_FOLDER_ID
git add .dvc/config
git commit -m "Configure Google Drive DVC remote"
```

For current Google restrictions, create a Google Cloud OAuth Desktop application:

1. Enable the Google Drive API.
2. Configure the OAuth consent screen as External.
3. Add your Google account under Test users.
4. Create an OAuth client ID of type Desktop app.
5. Set the credentials without quotes:

```powershell
dvc remote modify gdrive gdrive_client_id YOUR_CLIENT_ID
dvc remote modify gdrive gdrive_client_secret YOUR_CLIENT_SECRET
```

If authentication is stale, remove the local token and retry. PowerShell:

```powershell
Remove-Item .dvc\tmp\gdrive-user-credentials.json -Force -ErrorAction SilentlyContinue
dvc push
```

If you see `GEN_EMAIL`, repair the dependency pair in the active virtual environment:

```powershell
pip install "pyOpenSSL==24.2.1" cryptography --upgrade
```

Never commit `.dvc/tmp`, client secrets, or OAuth tokens. Run `dvc push` only after the remote and test-user account are configured.
