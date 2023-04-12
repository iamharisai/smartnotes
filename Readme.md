## Smartnotes
### You can have your notes here.

#### Initialization 
1. Create a directory smartnotes
2. Go to that directory and initalize venv `python -m venv .`
3. Activate the environment `source bin/activate `
4. `pip install django`
5. `Django-admin startproject smartnotes .`
6. Create an empty repository in git and perform below steps in local
```
git init .
#add .gitignore
git add .
git commit -m "initial commit"
git remote add origin https://github.com/hariiisai/smartnotes.git
git branch -M main
git push -u origin main
```

#### Project setup
1. Create a first app called home `django-admin startapp home` and add 'home' in installed apps of `settings.py`
2. Create 'home.html' and render 'url:home' to this html by view.home
3. Include 'home.urls' in main url file