# Git Commands for E-Commerce Cursor Demo

## Prerequisites

1. Make sure you have a GitHub account
2. Create a new repository on GitHub named `ecom_cursor_demo`
3. Replace `<your-username>` with your actual GitHub username in the commands below

## Git Commands

Run these commands in order from the project directory:

```bash
# Add all files to Git
git add .

# Commit changes
git commit -m "Added Cursor E-Commerce demo"

# Set branch to main
git branch -M main

# Add remote origin (replace <your-username> with your GitHub username)
git remote add origin https://github.com/<your-username>/ecom_cursor_demo.git

# Push to GitHub
git push -u origin main
```

## Windows PowerShell Commands

If you're using PowerShell on Windows, you can run:

```powershell
git add .
git commit -m "Added Cursor E-Commerce demo"
git branch -M main
git remote add origin https://github.com/<your-username>/ecom_cursor_demo.git
git push -u origin main
```

## Notes

- Make sure you've created the repository on GitHub first
- If the remote already exists, you can remove it with: `git remote remove origin`
- If you encounter authentication issues, you may need to configure Git credentials or use a personal access token

