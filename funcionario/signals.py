from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Funcionario
from rich import print
from django.contrib.auth.models import User
from django.db import transaction, atomic


@receiver(post_save, sender=Funcionario)
def create_user_funcionario(sender, instance, created, **kwargs):
    if created:
        try:
            with transaction.atomic():
                if User.objects.filter(username=instance.user.email).exists():
                    user = User.objects.create(username=instance.user.email)
                    user.set_password(instance.user.password)
                    user.save()
                else:
                    print(":sos_button: Usuário já existe")
        except Exception as e:
            print(":danger: Erro ao criar usuário: ", e)
