from wegemoc.celery import app
from celery import shared_task
from .models import Embed
from django.core.files.base import ContentFile
import requests
import PIL

@shared_task
def download_and_save_photo(embed_id: int):
   download_photo_command(Embed.objects.get(id=embed_id))
 