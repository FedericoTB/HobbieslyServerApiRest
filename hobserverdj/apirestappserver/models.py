from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import PermissionsMixin, User
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils import timezone


# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_active, is_staff, is_superuser, **extrafields):
        if not username:
            raise ValueError("the given username is not valid")
        if not email:
            raise ValueError("the given email is not valid")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_active=True, is_staff=is_staff, is_superuser=is_superuser, date_joined=timezone.now(), **extrafields)
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_user(self, username, email, password, **extrafields):
        return self._create_user(username, email, password, is_active=True, is_staff=False, is_superuser=False, **extrafields)
    
    def create_superuser(self, username, email, password, **extrafields):
        user = self._create_user(username, email, password, is_active=True, is_staff=True, is_superuser=True, **extrafields)
        user.save(using=self.db)

        return user
    

class Categories(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=75)
    description = models.TextField(max_length=150)

    def __str__(self):
        return self.name

GENDER_CHOICES = (('M','Male'),('F','Female'),)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateField(default=timezone.now())
    birth_date = models.DateField(default=timezone.now())
    adress = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    image_url = models.URLField()
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS= ['email',]

    class Meta:
        ordering=('username',)
    
    def __str__(self):
        return self.username


class UsersGroups(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image_url = models.URLField
    created_at = models.DateField(default=timezone.now())
    owner = models.ForeignKey(User, related_name="g_user", on_delete=models.SET_NULL, blank=True, null=True)
    members = models.ManyToManyField(User, related_name="g_members", through='Membership')

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name


class Classification(models.Model):
    objects = models.Manager
    category = models.ForeignKey(Categories, related_name="clas_category", on_delete=models.SET_NULL, blank=True, null=True)
    group = models.ForeignKey(UsersGroups, related_name="clas_group", on_delete=models.SET_NULL, blank=True, null=True)

def __str__(self):
        return "Group: "+self.group+" with Category: "+self.category


class Membership(models.Model):
    objects = models.Manager
    user = models.ForeignKey(User, related_name="memb_user", on_delete=models.SET_NULL, blank=True, null=True)
    group = models.ForeignKey(UsersGroups, related_name="memb_group", on_delete=models.SET_NULL, blank=True, null=True)
    date_joined = models.DateField(default=timezone.now())
    invite_reason = models.CharField(max_length=128)

def __str__(self):
        return "User: "+self.user +" of Group: "+self.group


class Rooms(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image_url = models.URLField
    created_at = models.DateField(default=timezone.now())
    updated_at = models.DateField(default=timezone.now())
    group = models.ForeignKey(UsersGroups, related_name="r_group", on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name= "r_user", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Messages(models.Model):
    content = models.TextField()
    created_at = models.DateField(default=timezone.now())
    updated_at = models.DateField(default=timezone.now())
    room = models.ForeignKey(Rooms, related_name="m_room", on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name="m_user", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.content