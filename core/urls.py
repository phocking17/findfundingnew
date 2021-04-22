from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("aboutme", views.aboutme, name='About Me'), 
    path("aboutme/<int:instance>", views.aboutme, name='About Me'),
    path("aboutme/<int:instance>/<str:metatag>/<str:addedtag>", views.addtag, name='AddTag'),
    path("quickfind", views.quickfind, name='QuickFind'), 
    path("results", views.results, name='Results'), 
    path("program/<str:pro_name>", views.program, name="program"),
    path("organization/<str:org_name>", views.organization, name='test org'),
    path("photos/<int:orgid>/<str:photoname>", views.photo, name="photos"),
    path("results/<str:arching_name>", views.results_general, name="results general"),
    path("results/custom/<int:instance>", views.results, name="results"),
    path("results/<str:semi_name>/<str:tag_name>", views.results_tagspecific, name="results tagspecific"),
    path("add", views.add_organization, name="add"),
    path("forpartners", views.add_organization, name="add"),
    path("added", views.organization_completed, name="added"),
    path("all", views.all_opportunities, name="all_opportunities")
]