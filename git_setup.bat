@echo off
REM Git setup commands for ecom_cursor_demo project
REM Replace <your-username> with your actual GitHub username

echo Adding all files to Git...
git add .

echo Committing changes...
git commit -m "Added Cursor E-Commerce demo"

echo Setting branch to main...
git branch -M main

echo Adding remote origin...
echo NOTE: Replace <your-username> with your actual GitHub username
git remote add origin https://github.com/<your-username>/ecom_cursor_demo.git

echo Pushing to GitHub...
git push -u origin main

echo Done! If you see an error, make sure you've:
echo 1. Created the repository on GitHub first
echo 2. Replaced <your-username> with your actual GitHub username
echo 3. Configured your Git credentials

pause

