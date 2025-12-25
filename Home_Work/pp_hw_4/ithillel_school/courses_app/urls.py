from django.urls import path
from .views import course_list, create_course, CourseListAPI

urlpatterns = [
    path('', course_list, name="course_list"),
    path('create/', create_course, name="create_course"),
    path('courses/', CourseListAPI.as_view(), name='course-list-api'),
]
