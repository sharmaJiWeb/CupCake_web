---
description: How to set up Firebase and get the serviceAccountKey.json file
---

# Setting up Firebase for CupcakeWin

To fix the "serviceAccountKey.json not found" error and enable database/login features, follow these steps:

## 1. Create a Firebase Project
1. Go to the [Firebase Console](https://console.firebase.google.com/).
2. Click **"Add project"** (or "Create a project").
3. Name your project (e.g., `CupcakeWin`).
4. Disable Google Analytics (optional, makes setup faster) and click **"Create project"**.
5. Once ready, click **"Continue"**.

## 2. Get the Private Key (serviceAccountKey.json)
1. In your project dashboard, click the **Gear icon ⚙️** (next to "Project Overview") and select **"Project settings"**.
2. Go to the **"Service accounts"** tab.
3. Ensure "Python" is selected under "Admin SDK configuration snippet".
4. Click the **"Generate new private key"** button.
5. Click **"Generate key"** in the popup.
6. A file will download. **Rename this file** to: `serviceAccountKey.json`
7. **Move this file** into your project folder: `c:\Users\Disha Sharma\OneDrive\Desktop\cupcakes\`

## 3. Enable Authentication
1. On the left sidebar, click **"Build"** -> **"Authentication"**.
2. Click **"Get started"**.
3. Under "Sign-in method", click **"Email/Password"**.
4. Toggle **"Enable"** (the first switch) and click **"Save"**.

## 4. Enable Firestore Database
1. On the left sidebar, click **"Build"** -> **"Firestore Database"**.
2. Click **"Create database"**.
3. Choose a location (default is usually fine) and click **"Next"**.
4. Select **"Start in test mode"** (easier for development) or "Start in production mode".
   - *Note: Test mode allows anyone to read/write for 30 days. For production, you'll need to set up rules later.*
5. Click **"Create"**.
6. Once created, click the **"Rules"** tab and ensuring it allows writing for now if you chose Production mode, or stick with Test mode until you deploy.

## 5. Restart Your App
1. Go to your terminal where `python app.py` is running.
2. Press `Ctrl+C` to stop it.
3. Run `python app.py` again.
4. You should see "Firebase initialized successfully." instead of the warning!
