from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save, sender=User)
def postsave_state(sender, instance, created, **kwargs):
    if created:
        count = User.objects.all().count()
        print('New User is created')
        print('Number of users after saving is {}'.format(count))
    if created == False:
        count = User.objects.all().count()
        print('User is updated')
        print('Number of users after saving is {}'.format(count))


@receiver(pre_save, sender=User)
def presave_state(sender, instance, **kwargs):
    count = User.objects.all().count()
    print('New User is about to be created or updated')
    print('Number of users before saving is {}'.format(count))
