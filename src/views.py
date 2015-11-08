from django.shortcuts import render
from src.models import Home
from src.models import About
from src.models import Services
from src.models import Interior
from src.models import Building
from src.models import Icon
from src.models import Recent
from src.models import Post
# from src.models import Client
# Create your views here.
def load(request):
	return render(request, 'load.html')
def index(request):
	news = Recent.objects.all()
	return render(request, 'index.html', {'news' : news})

def dha(request):
	return render(request, 'blog.html')



# def index(request):
# 	cc1 = Client.c1
# 	cc2 = Client.c2
# 	cc3 = Client.c3
# 	cc4 = Client.c4
# 	cc5 = Client.c5
# 	cc6 = Client.c6
# 	cc7 = Client.c7
# 	cc8 = Client.c8
# 	cc9 = Client.c9
# 	cc10 = Client.c10
# 	cc11 = Client.c11
# 	cc12 = Client.c12
# 	cc13 = Client.c13
# 	cc14 = Client.c14
# 	cc15 = Client.c15
# 	cc16 = Client.c16
# 	cc17 = Client.c17
# 	cc18 = Client.c18
# 	cc19 = Client.c19
# 	cc20 = Client.c20
# 	cc21 = Client.c21
# 	cc22 = Client.c22
# 	cc23 = Client.c23
# 	cc24 = Client.c24
# 	return render(request, 'index.html', {'news' : cc1})