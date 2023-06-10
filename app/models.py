from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    status = models.IntegerField(default=2)
    ''' user_status => {1 : Draft, 2 : Active, 3 : In-Active} '''
    profile_image = models.ImageField(upload_to='Temp')
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)



