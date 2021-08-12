from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser  # for customization user
from django.db.models.signals import post_save  # post_save activated once something was created
# Create your models here.

# User = get_user_model()

# customize authed user from django.contrib
class User(AbstractUser):
    """so for checking if the User is organizer - show him the whole list if not then it should the agent
    who can see only leads belong to his organization(UserProfile)"""
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    organization = models.ForeignKey(UserProfile, default=1, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)

    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    # every lead will be assigned on category
    category = models.ForeignKey("Category", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=30)  # New, Contacted, Remind, Success, Lost

    # every category needs to be linked to organization
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



def post_user_created_signal(sender, instance, created, **kwargs):
    """we gonna listen once the user will something create in db"""
    """so we want to call this func when we received the POST-save event"""
    # print(instance)  # >>> Nick
    # print(sender)  # >>> <class 'leads.models.User'>
    # print(created)  # >>> False - tells us about creating new record or his updated. False - because I've updated his.
    if created:
        UserProfile.objects.create(user=instance)


"""so we taken a signal from sender model(once a new record will be created this method execute the indicated func)"""
post_save.connect(post_user_created_signal, sender=User)




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
