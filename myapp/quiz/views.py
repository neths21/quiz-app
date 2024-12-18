from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import QuizQuestions
import random

def question(request):
    # Initialize session variables if not already set
    if 'score' not in request.session:
        reset_quiz_session(request)

    # Fetch a question from the database
    question = get_random_question(request)
    feedback = None  # To store feedback for the user's response

    if request.method == "POST":
        # Retrieve the selected option
        selected_option = request.POST.get('selected_option')
        print(f"Debug - Selected Option: {selected_option}")
        print(f"Debug - Correct Answer: {question.OptionAns}")

        # Check if the selected option matches the correct answer
        if int(selected_option) == question.OptionAns:
            request.session['score'] += 1
            request.session['correct_answers'] += 1
            feedback = "Correct!"
            print("Correct answer! Score updated.")
        else:
            request.session['incorrect_answers'] += 1
            feedback = f"Incorrect! The correct answer was: {question.OptionAns}"
            print("Incorrect answer.")

        # Increment the question counter
        request.session['question_number'] += 1

        # If 10 questions have been answered, redirect to the results page
        if request.session['question_number'] > 10:
            return redirect('results')

    # Pass the question and session data to the template
    context = {
        'question': question,
        'question_number': request.session['question_number'],
        'score': request.session['score'],
        'correct_answers': request.session['correct_answers'],
        'incorrect_answers': request.session['incorrect_answers'],
        'feedback': feedback,  # Add feedback to the context
    }

    return render(request, 'quiz.html', context)


def results(request):
    # Pass session data to the results page
    context = {
        'score': request.session.get('score', 0),
        'correct_answers': request.session.get('correct_answers', 0),
        'incorrect_answers': request.session.get('incorrect_answers', 0),
    }

    # Clear session data to reset the quiz
    reset_quiz_session(request)

    return render(request, 'results.html', context)

def get_random_question(exclude=[]):
    questions = list(QuizQuestions.objects.all())
    return random.choice(questions)

def reset_quiz_session(request):
    request.session['score'] = 0
    request.session['question_number'] = 1
    request.session['correct_answers'] = 0
    request.session['incorrect_answers'] = 0
