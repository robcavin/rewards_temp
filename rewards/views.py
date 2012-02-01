# Create your views here.

from django.views.generic.list_detail import object_detail
from django.contrib.auth.decorators import login_required

@login_required
def user_object_detail(request, *args, **kwargs):
    kwargs['object_id'] = request.user.id
    return object_detail(request, *args, **kwargs)