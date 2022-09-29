from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
# from .schema import schema
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('tosearch/<slug:data>',SearchContent),
    path('register', register_Users),
    path('login', login_user),
    path('logout',logout_user),
    path('trending/<slug:data>', SearchTrend),
    path('twitter', searchtwitter)
]
