from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, username, password):        
        
        if not email:            
            raise ValueError('이메일을 등록해주세요.')
        if not username:
            raise ValueError('유저이름을 등록해주세요')
        if not password:            
            raise ValueError('패스워드를 등록해주세요.')

        user = self.model(
            user_type = User.USER_TYPE_CHOICES[0],
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):        

        user = self.create_user(
            user_type = User.USER_TYPE_CHOICES[0],
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user 


class User(AbstractBaseUser, PermissionsMixin):    
   
    objects = UserManager()

    # Default : id / password / last_login
    USER_TYPE_CHOICES = (
        ('django', 'Django'),
        ('kakao', 'Kakao'),
        ('gmail', 'Gmail')
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default=USER_TYPE_CHOICES[0])

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=10, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'    
    REQUIRED_FIELDS = ['email',]

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin