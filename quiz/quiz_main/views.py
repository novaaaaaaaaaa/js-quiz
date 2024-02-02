from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

questions = ['1+1','2+2','3+3','4+4','5+5','6+6','7+7','8+8','9+9','10+10']
answers = [2, 4 , 6, 8, 10, 12, 14, 16, 18, 20]
user_score = 0
question_index_global = 0
username = ''

# Create your views here.
def landing(request):
    global username, user_score, question_index_global

    # Initialize global variables
    user_score = 0
    question_index_global = 0
    username = ''

    # Handle POST request
    if request.method == 'POST':
        # Get the username from the request data
        username = request.POST['username']

        # Redirect to the 'quiz' URL
        return redirect('quiz_main:quiz')

    # Handle GET request
    else:
        # Render the 'quiz_main/landing.html' template
        return render(request, 'quiz_main/landing.html')



def quiz(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Set the global variables question_index_global user_score
        global question_index_global, user_score

        # Define a nested function to check the user's answer
        def check_answer(question_index):
            # Get the user's answer from the request data
            user_answer = request.POST['answer_box']
            # Check if the user's answer is correct
            if int(user_answer) == answers[question_index]:
                return {'message':'correct', 'result':True}
            else:
                return {'message':'incorrect', 'result':False}

        # Check the user's answer
        answer_check = check_answer(question_index_global)

        # If the answer is correct, increment the user's score and the question index
        if answer_check['result']:
            user_score += 1
            question_index_global += 1
        # If the answer is incorrect, increment the question index
        else:
            question_index_global += 1

        print('Question index:',question_index_global)

        # If the question index is less than 10, render the 'quiz.html' template with the next question and the result of the user's answer
        if not question_index_global == 10:

            context = {
                'next_question' : questions[question_index_global],
                'message' : answer_check['message'],
                'ques_num' : question_index_global+1
            }

            return render(request, 'quiz_main/quiz.html', context=context)

        # If the question index is equal to 10, redirect to the 'score' URL
        else:

            return redirect('quiz_main:score')

    # If the request method is GET, render the 'quiz.html' template with the first question and a message indicating that the quiz has started
    else:
        return render(request, 'quiz_main/quiz.html', {'next_question' : questions[question_index_global], 'message' : 'started','ques_num' : question_index_global+1})
    


def score(request):    # Create a new Leaderboard_scores object with the user's username and score
    new_leaderboard_record = Leaderboard_scores(username=username, user_score=user_score)
    # Save the new Leaderboard_scores object to the database
    new_leaderboard_record.save()

    # Render the 'score.html' template with the user's score
    return render(request, 'quiz_main/score.html', {'score':user_score})
    


def leaderboard(request):
    # Retrieve the top 10 user scores from the database
    user_scores = Leaderboard_scores.objects.all().order_by('-user_score')[:10].values()

    # Render the leaderboard.html template and pass in the user scores as a context variable
    return render(request, 'quiz_main/leaderboard.html', {'table_vals':user_scores})