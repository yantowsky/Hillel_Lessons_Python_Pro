from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver, Signal

from courses_app.models import Course
from members_app.models import Member

# ------------------------------------
# 1. Кастомний сигнал
# ------------------------------------
course_member_synced = Signal()


# ------------------------------------
# ---------------- Course signals -----
# ------------------------------------

@receiver(pre_save, sender=Course)
def course_pre_save(sender, instance, **kwargs):
    print(f"[pre_save][Course] Готується до збереження: {instance.title}")


@receiver(post_save, sender=Course)
def course_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"[post_save][Course] Створено новий курс: {instance.title}")
    else:
        print(f"[post_save][Course] Курс оновлено: {instance.title}")


@receiver(pre_delete, sender=Course)
def course_pre_delete(sender, instance, **kwargs):
    print(f"[pre_delete][Course] Курс буде видалено: {instance.title}")


@receiver(post_delete, sender=Course)
def course_post_delete(sender, instance, **kwargs):
    print(f"[post_delete][Course] Курс видалено: {instance.title}")


# ------------------------------------
# ---------------- Member signals -----
# ------------------------------------

@receiver(pre_save, sender=Member)
def member_pre_save(sender, instance, **kwargs):
    print(f"[pre_save][Member] Готується до збереження: {instance.name}")


@receiver(post_save, sender=Member)
def member_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"[post_save][Member] Створено нового учасника: {instance.name}")
    else:
        print(f"[post_save][Member] Учасника оновлено: {instance.name}")


@receiver(pre_delete, sender=Member)
def member_pre_delete(sender, instance, **kwargs):
    print(f"[pre_delete][Member] Учасник буде видалений: {instance.name}")


@receiver(post_delete, sender=Member)
def member_post_delete(sender, instance, **kwargs):
    print(f"[post_delete][Member] Учасника видалено: {instance.name}")


# ------------------------------------
# 2-в-1 Хендлер (слухає два сигнали)
# ------------------------------------
@receiver([post_save, course_member_synced], sender=Member)
def multi_handler(sender, instance, **kwargs):
    print(f"[MULTI] Спрацював (post_save або custom) для Member: {instance.name}")
