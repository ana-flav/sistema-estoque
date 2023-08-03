from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Funcionario
from rich import print
from django.contrib.auth.models import User
from django.db import transaction
from extras.util import make_random_password

@receiver(post_save, sender=Funcionario)
def create_user_funcionario(sender, instance, created, **kwargs):
    if created or not instance.user:
        try:
            with transaction.atomic():
                if not User.objects.filter(username=instance.email).exists():
                    user = User.objects.create_user(
                        instance.email,
                        instance.email,
                        make_random_password(8),
                    )
                    instance.user = user
                    instance.save()
                else:
                    instance.user = User.objects.get(username=instance.user.email)

        except Exception as e:
            print(":danger: Erro ao criar usuário: ", e)
