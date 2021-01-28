from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

# Create your models here.


def upload_path(instance, fileName):
    """
    docstring
    """
    ext = fileName.split(".")[-1]
    return "/".join(["image", str(instance.userPro.id)+str(instance.nickName)+str(".")+str(ext)])


class UserManager(BaseUserManager):
    """
    UserModelのobjects
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        user作成
        """
        if not email:
            raise ValueError("Email is must")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """
        superuser作成
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    UserModelのオーバーライド
    """
    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return str(self.email)


class Profiel(models.Model):
    """
    プロフィールモデル
    """
    nickName = models.CharField(max_length=20)
    userPro = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="userPro",
        on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(blank=True, null=True, upload_to=upload_path)


class FriendRequest(models.Model):
    """
    友達申請
    """
    askFrom = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="askFrom",
        on_delete=models.CASCADE)
    askTo = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="askTo",
        on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    class Meta:
        unique_together = (("askFrom", "askTo"),)

    def __str__(self):
        return str(self.askFrom) + "->" + str(self.askTo)


class Message(models.Model):
    """
    docstring
    """
    message = models.CharField(max_length=140)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="sender",
        on_delete=models.CASCADE)
    reciver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="reciver",
        on_delete=models.CASCADE)

    def __str__(self):
        return self.message + " " + str(self.sender) + "->" + str(self.reciver)
