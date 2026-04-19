from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Existing paths for index and course details...
    path(route='', view=views.CourseListView.as_view(), name='index'),
    path(route='<int:pk>/', view=views.CourseDetailView.as_view(), name='course_details'),

    # Task 6: Required paths for the exam submission and results
    path(route='<int:course_id>/submit/', view=views.submit, name='submit'),
    path(route='course/<int:course_id>/submission/<int:submission_id>/resut/', 
         view=views.show_exam_result, 
         name='show_exam_result'),
]
