# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from home.models import PaintingRequest, TemporaryPaintingRequest

# @receiver(post_save, sender=User)
# def transfer_temporary_requests(sender, instance, created, **kwargs):
#     if created:
#         temporary_requests = TemporaryPaintingRequest.objects.filter(email=instance.email)
#         for request in temporary_requests:
#             PaintingRequest.objects.create(
#                 user=instance,
#                 email=request.email,
#                 description=request.description,
#                 size=request.size,
#                 add_signature=request.add_signature,
#                 examples=request.examples,
#                 examples2=request.examples2
#             )
#             request.delete()
