from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Rider
from .models import Checkpoint

def index(request):
    registered_riders = Rider.objects.order_by('bib_id')
    template = loader.get_template('hhpi/index.html')
    context = RequestContext(request, {
	'registered_riders': registered_riders,
    })
    return HttpResponse(template.render(context))

def checkpoint(request):
    cp_timestamp = Checkpoint.objects.order_by('id')
    template = loader.get_template('hhpi/checkpoint.html')
    context = RequestContext(request, {
	'cp_timestamp': cp_timestamp,
    })
    return HttpResponse(template.render(context))