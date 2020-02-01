from django.shortcuts import render, get_object_or_404
import random
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Decorations, Items

#edit if fulltext search
def index(request):
    latest_item_list = Items.objects.order_by('-pub_date')
    template = loader.get_template('dota2_deco/index.html')
    context = {
        'latest_item_list': latest_item_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, item_id):
    item = get_object_or_404(Items, pk=item_id)
    return render(request, 'dota2_deco/detail.html', {'item': item, 'decoration': item.item_type})

#edit if keyword search
@csrf_exempt
def search(request):
    keyword = request.POST.get('keyword')

    print('Items.objects = ', Items.objects)
    # cheapest_item_list = Items.objects.filter(item_type=keyword).order_by('price')
    all_results = Items.objects.all()
    lastest_results = all_results.order_by('pub_date')

    # filter by item_type == keyword
    result = []
    for each in all_results.order_by('price'):
        if each.item_type.decoration_name == keyword:
            result.append(each)


    template = loader.get_template('dota2_deco/search.html')
    context = {
        'user_search_results': result[:20],
        'latest_item_list': lastest_results[:20],
        'keyword': keyword
    }
    return render(request,'dota2_deco/index.html',context)
    # return HttpResponse("hello")

def publish(request):
    type_list = Decorations.objects.all()
    context = {
        'type_list':type_list,
    }
    return render(request,'dota2_deco/publish.html',context)

def item_upload(request):
    this_type = request.POST['type']
    this_price = request.POST['price']
    this_publisher = '#'
    this_item = Items(item_type=this_type,publisher_id=this_publisher,item_price=this_price)
    this_item.save()
    return render(request,'dota2_deco/publish_success.html')
