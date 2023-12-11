# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from home.models import PaintingRequest, UserProfile

# @receiver(post_save, sender=PaintingRequest)
# def update_on_save(sender, instance, created, **kwargs):
#     """
#     Update order total on lineitem update/create
#     """
#     instance.order.update_total()

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         user, created = User.objects.get_or_create(email=instance.email)
        
#         # Создаем профиль пользователя, если он новый
#         if created:
#             UserProfile.objects.create(user=user, other_field=instance.other_field)