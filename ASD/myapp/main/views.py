from django.shortcuts import render
from .models import User

def index(request):

    users = User.objects.order_by('id')

    for user in users:
        print(f'{user.name}:{user.age}:{user.cash}')

    data = {'names' : [i.name for i in users]}
    return render(request,'main/index.html',data)
# Create your views here.
