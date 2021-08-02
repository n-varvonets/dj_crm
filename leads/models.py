from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser # for customization user

# Create your models here.

# User = get_user_model()

# customize authed user from django.contrib
class User(AbstractUser):
    pass


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


# Models Manager(http://i.imgur.com/r4w5Ixj.png) and Querysets(http://i.imgur.com/suBI35s.png) to database for model(http://i.imgur.com/3LAeJrI.png)
# 1)Car.objects.create(make="BMV", model="X5", year=2017)
# Car.objects.all()
# Car.objects.filter(make="Audi")
# Car.objects.filter(year__gt=2016)
# 2)In my case after creation superuser we can get all (python manage.py migrate) or also can one by specifying his name(http://i.imgur.com/5M9b6ny.png)
# User.objects.all() / >>> admin_user = User.objects.get(username="Nick")
# 3) Also need to create agent which will be matched with User (http://i.imgur.com/aa1a7vL.png)
# 4)We can also create Lead which based on Agent(which based on User) -  http://i.imgur.com/i3eJo0F.png
# nick_agent = Agent.objects.get(user__email="nickolay.varvonets@gmail.com") - this how we can get agent email from existing user
# Lead.objects.create(first_name="Anatoliy", last_name="Varvonets", age=25, agent=nick_agent) - and after - we can passed agent to create the Lead
