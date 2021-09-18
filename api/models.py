from django.db import models
from django.core.mail import send_mail
from contactService import settings
# Create your models here.


class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        send_mail(self.name, self.message,
                  settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)

        super().save(*args, **kwargs)
