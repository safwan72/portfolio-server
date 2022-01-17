from rest_framework import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register("projectcategory", views.ProjectCategoryView, basename="projectcategory"),
urlpatterns = [
    path("allprojects/", views.AllProjects, name="allprojects"),
    path("newsletter/", views.NewsLetterView.as_view(),name="newsletter"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("projects/", views.ProjectView.as_view(),name="projects"),
] + router.urls
