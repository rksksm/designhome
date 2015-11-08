from django.contrib import admin
from src.models import Home
from src.models import About
from src.models import Services
from src.models import Interior
from src.models import Building
from src.models import Icon
from src.models import Recent
from src.models import Post
# from src.models import Client

admin.site.register(Post)
admin.site.register(Home)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(Interior)
admin.site.register(Building)
admin.site.register(Icon)
admin.site.register(Recent)
# admin.site.register(Client)