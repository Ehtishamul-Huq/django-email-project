from userproject.views import ProjectView, GetProjectView, ExperienceView, EducationView
from django.urls import path

urlpatterns = [
    path('project/', ProjectView.as_view()),  
    path('project-details/', GetProjectView.as_view()),
    path('experience/', ExperienceView.as_view()),
    path('education/', EducationView.as_view()),
    ]