from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

UserAccount = get_user_model()
 
class Command(BaseCommand):
 
    def handle(self, *args, **options):
        if not UserAccount.objects.filter(phone=settings.ADMIN_ID).exists():
            UserAccount.objects.create_superuser(settings.ADMIN_ID, settings.ADMIN_PW)
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))
