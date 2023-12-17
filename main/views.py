from django.contrib.auth import logout
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
from rest_framework import generics
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404

def _exten(request, Qpost=True, Qzams=False) -> dict:
    auth = IsAuthenticated.has_permission(APIView, request=request, view=APIView)
    posts = {}
    zams = {}
    if Qpost:
        posts = Status.objects.select_related('main_status').values('Name', 'Img1', 'url')
    if Qzams:
        zams = Buy.objects.all()

    url = request.path
    data = {
        'url': url,
        'user': request.user.is_staff,
        'auth': auth,
        'posts': posts,
        'zams': zams,
        'by': request.META.get('HTTP_REFERER', '')
    }
    if auth:
        data['username'] = request.user.username
        print(f"Server using by {request.user.username}")
    if not auth:
        print(f"Server using by {request.META.get('HTTP_X_FORWARDED_FOR', '') or request.META.get('REMOTE_ADDR')}, {request.user}, {request.META.get('HTTP_REFERER', '')}, {request.META.get('HTTP_USER_AGENT', '')}")
    return data

def adddict(dict1, dict2) -> dict:
    for k, v in dict2.items():
        dict1[k] = v

    return dict1

def _check_m(request, Form):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = form.errors
            return error

def opost(data, tbd, posturl) -> dict:
    return adddict(data, {'post': get_object_or_404(tbd, url=posturl)})

def oform(data, form) -> dict:
    return adddict(data, {'form': form})

def index(request):
    return render(request, 'main/index.html', adddict(_exten(request), {'title': 'Головна'}))

def addprod(request):
    POST = _check_m(request, StatusForm)
    error = ''

    if POST != None:
        error = POST
        return POST

    data = {
        'username': request.user.username,
        'error': error
    }

    return render(request, 'main/add.html', adddict(oform(adddict(data, _exten(request)), StatusForm), {'title': 'Додати товар'}))

def menu(request):
    return render(request, 'main/menu.html')

def hatynka(request, post_url):
    return render(request, 'main/hatynka.html', opost(_exten(request), Status, post_url))

def buy(request, post_url):
    auth = IsAuthenticated.has_permission(APIView, request=request, view=APIView)
    POST = _check_m(request, BuyForm)
    error = ''

    if POST != None:
        error = POST
        return POST

    data = {
        'errors': error,
        'post': post_url
    }
    if auth:
        data['email'] = request.user.email
    return render(request, 'main/contact.html', adddict(oform(opost(adddict(data, _exten(request)), Status.objects.all().values('Name'), post_url), BuyForm), {'title': 'Заказ'}))

def update(request, post_url):
    if request.user.is_staff:
        model = Status
        post = get_object_or_404(model, url=post_url)
        error = ''

        if request.method == 'POST':
            form = StatusForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                error = form.errors

        data = {
            'error': error,
            'post': post
        }

        return render(request, 'main/update_hatyn.html', adddict(oform(adddict(data, _exten(request)), StatusForm), {'title': 'Змінити'}))

def delete(request, post_url):
    if request.user.is_staff:
        post = Status.objects.get(url=post_url)

        if request.method == 'POST':
            post.delete()
            return redirect('home')

        return render(request, 'main/delete_hatyn.html', adddict(_exten(request), {'title': 'Видалити', 'post': post}))

def zamovlenia(request):
    if request.user.is_staff:
        if request.method == 'POST':
            post = Buy.objects.get(idi=request.POST.get('idi'))
            post.delete()
            return redirect('zam')
        return render(request, 'main/zam.html', adddict(_exten(request, Qzams=True), {'title': 'Замовлення'}))
# class MainAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
class MainAPIView(APIView):
    def get(self, request):
        lust = User.objects.all().values()
        return Response({'users': list(lust)})

    def post(self, request):
        return Response({'title': 'Aniguri'})

class MainAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)

def logout_user(request):
    logout(request)
    return redirect('home')