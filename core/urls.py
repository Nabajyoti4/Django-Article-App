
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from blog.api import router as blog_router

api = NinjaAPI(
    title='Blog API',
    version='1.0',
    description='Blog API'
)
api.add_router('/blog/', blog_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]