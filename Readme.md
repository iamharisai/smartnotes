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
1. Create a first app called home `django-admin startapp home` and add 'home' in installed apps of 'settings.py'
2. Create 'home.html' and render 'url:home' to this html by view.home
3. Include 'home.urls' in main url file

#### Adding Users 
1. Before creating users we need to setup database connection so users will be stored
2. To do this we can simply run `python manage.py migrate` to apply built-in migrations for app(s): admin, auth, contenttypes, sessions.
3. Create a admin user now `python manage.py createsuperuser`
4. Created a authorised page which can be viewed by loggedin users

#### ORM
1. Create a new app notes `django-admin startapp notes` and add it in 'setting.py'
2. Create a model 'notes' in 'models.py' of notes folder
3. To make a relation of this model, we need to make migrations `python manage.py makemigrations`
4. Perform actual migration `python manage.py migrate` # The table 'notes' will be created in database
5. Register you model in 'admin.py'
6. Now you can manage 'notes' model from admin page

#### Dynamic web pages
1. Create a logic(view) to display all notes in 'notes_list.html' and add 'notes.url' in main urls
2. Create a logic to disaply single note 

#### Class based views
1. Rewrite the functions into classes
2. Change the pointing in urls file

#### Static files 
1. Create a new folder 'static' in main project folder and have sepearte folders for css,images...
2. Add the STATICFILES_DIRS in 'settings.py'
3. Create a style.css and load static files in html pages
4. Created a 'base.html' and extends it to other html pages
