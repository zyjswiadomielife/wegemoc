from wegemoc.celery import app
from .models import Embed
from django.core.files.base import ContentFile
import requests
import PIL


@app.task
def handle_image_download(instance_pk):
    try:
        instance = Embed.objects.get(pk=instance_pk)
        if instance.thumbnail_url and not instance.image:
            req = requests.get(instance.thumbnail_url)
            image_bytes = io.BytesIO(req.content)
            img = PIL.Image.open(image_bytes)
            if img.mode != "RGB":
                img = img.convert("RGB")
            img.save(image_bytes, format="JPEG")
            instance.image.save(instance.slug + '.jpeg', ContentFile(image_bytes.getvalue()), save=False)
            instance.save()
    except ObjectDoesNotExist:
        # Abort
        logger.warning("Saved object was deleted before this task get a chance to be executed [id = %d]" % instance_pk)