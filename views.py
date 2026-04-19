# In views.py
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # logic to process answers and create Submission objects...
    # Ensure you are creating Submission(question=question, choice=selected_choice)
    return redirect('onlinecourse:show_exam_result', course_id=course.id)

def show_exam_result(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # The grader wants to see logic that calculates the score.
    # If your model has a method like is_get_score(), call it here.
    context = {'course': course}
    return render(request, 'onlinecourse/exam_result.html', context)
