from django.apps import AppConfig

#for each application, we need to add the app.config to the installed apps in project’s settings.py.
#This will let django know to look for folders within that app e.g. templates
class BlogappConfig(AppConfig):
    name = 'blogapp'
