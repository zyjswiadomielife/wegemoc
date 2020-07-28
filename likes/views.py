import json
     
from django.http import HttpResponse
from django.views import View
from django.contrib.contenttypes.models import ContentType
     
from .models import Like
     
     
class VotesView(View):
    model = None    # Data Model - Articles or Comments
     
    def delete(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        # GenericForeignKey does not support get_or_create
        try:
            like = Like.objects.get(content_type=ContentType.objects.get_for_model(obj), object_id=obj.id, user=request.user)
            like.delete()
        except Like.DoesNotExist:
            pass
     
        return HttpResponse(
            json.dumps({
                "like_count": obj.votes.count(),
            }),
            content_type="application/json"
        )