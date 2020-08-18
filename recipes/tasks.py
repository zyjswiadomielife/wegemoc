from wegemoc.celery import app
from celery import shared_task
from .models import Embed
from django.core.files.base import ContentFile
import requests
import PIL

def download_photo_command(embed: Embed):
        if embed.thumbnail_url and not embed.image:
            req = requests.get(embed.thumbnail_url)
            image_bytes = io.BytesIO(req.content)
            img = PIL.Image.open(image_bytes)
            if img.mode != "RGB":
                img = img.convert("RGB")
            img.save(image_bytes, format="JPEG")
            embed.image.save(embed.slug + '.jpeg', ContentFile(image_bytes.getvalue()), save=False)
            embed.save()

@shared_task
def download_and_save_photo(embed_id: int):
   download_photo_command(Embed.objects.get(id=embed_id))
 