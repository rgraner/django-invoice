from django.http import HttpResponse
from django.shortcuts import render
from invoices.models import Invoice


def hello_world(request):
    obj = Invoice.objects.get(id=1)
    # print(obj.get_tags())
    # print(obj.get_positions())
    # print(obj.get_total_amount())
    qs = Invoice.objects.all()
    print(obj.__dict__)
    print('******')
    print(qs.query)
    return render(request, 'home.html', {'obj_': obj})
    # return HttpResponse('hello world')