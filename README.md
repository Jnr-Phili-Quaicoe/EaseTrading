# easeTrading Python Flask Website

This is the Render-ready Python Flask version of the easeTrading website.

## Run on Windows

1. Extract the ZIP folder.
2. Open the `easeTrading-Python` folder in VS Code.
3. Open **Terminal > New Terminal**.
4. Install the requirements:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Start the website:

   ```powershell
   python app.py
   ```

6. Open `http://127.0.0.1:5000` in your browser.

## Upload to GitHub

Upload every file and folder inside `easeTrading-Python` to the root of one GitHub repository. Do not upload only the ZIP.

## Deploy on Render

Create a new **Web Service**, connect the GitHub repository, and use:

- Language: `Python 3`
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Health check path: `/health`

No environment variables or database are required for this version.
