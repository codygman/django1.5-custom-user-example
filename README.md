django1.5-custom-usermodel
==========================

I created this to 'scratch my own itch' and work out some of the kinks in my knowledge of the new Django user model. What I struggled with initially was creating my custom user model, changing it in the settings, and then trying to run:
    
    python manage.py createsuperuser

This gave me an error, and that led me to start this project to figure out what was wrong. I finally found the [full django 1.5 custom usermodel example)[https://docs.djangoproject.com/en/1.5/topics/auth/customizing/#a-full-example] and figured out that I needed my own usermanager to make sure things worked together correctly. The built in usermanager makes assumptions about the usermodel and the fields it should contain, so extending the BaseUserManager was a msut.

I hope this example helps you quickly be able to play with the new user model and figure out any problems you may have!

- Cody
