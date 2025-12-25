from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from auth_app.authentication import JWTAuthentication


def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses_app/course_list.html", {"courses": courses})


def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm()

    return render(request, "courses_app/create_course.html", {"form": form})


class CourseListAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'message': 'Authorized access',
            'user': request.user.username
        })
