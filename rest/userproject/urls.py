from userproject.views import ProjectView, EducationView, EducationUpdateView
from django.urls import path

urlpatterns = [
    path('project/', ProjectView.as_view()),  
    #path('project-details/', GetProjectView.as_view()),
    #path('experience/', ExperienceView.as_view()),


    path('education/', EducationView.as_view()),
    path('education/<str:pk>', EducationView.as_view()),
    path('education-update/<str:pk>', EducationUpdateView.as_view()),
    ]