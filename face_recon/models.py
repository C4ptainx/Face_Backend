from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, name, especialidad, email, tc, password=None, password2=None):
      """
      Creates and saves a User with the given email, name, tc and password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          name=name,
          especialidad=especialidad,
          tc=tc,
      )

      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, name, tc, especialidad, password=None):
      """
      Creates and saves a superuser with the given email, name, tc and password.
      """
      user = self.create_user(
          email=email,
          name=name,
          especialidad=especialidad,
          tc=tc,
          password=password,
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

#  Custom User Model
class Asistencia(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    carrera = models.CharField(max_length=200)
    grupo = models.CharField(max_length=200)
    puntaje = models.CharField(max_length=10)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Asistencia de {self.user.name} - {self.fecha_registro}'

class User(AbstractBaseUser):
  name = models.CharField(max_length=200)
  especialidad = models.CharField(max_length=200)
# asistencia = models.CharField(max_length=1500, default="[ ]")
  email = models.EmailField(
      verbose_name='Email',
      max_length=255,
      unique=True,
  )
  tc = models.BooleanField()
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name', 'tc']

  def __str__(self):
      return self.email

  def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
      # Simplest possible answer: Yes, always
      return self.is_admin

  def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
      # Simplest possible answer: Yes, always
      return True

  @property
  def is_staff(self):
      "Is the user a member of staff?"
      # Simplest possible answer: All admins are staff
      return self.is_admin
