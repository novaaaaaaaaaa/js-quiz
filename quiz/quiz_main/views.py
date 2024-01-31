from django.shortcuts import render
from django.http import HttpResponse

questions = ['1+1','2+2','3+3','4+4','5+5','6+6','7+7','8+8','9+9','10+10']
answers = [2, 4 , 6, 8, 10, 12, 14, 16, 18, 20]
user_score = 0
question_index_global = 0

# Create your views here.
def landing(request):
    if request.method == 'POST':
        global question_index_global, user_score

        def check_answer(question_index):
            user_answer = request.POST['answer_box']

            if int(user_answer) == answers[question_index]:
                return {'message':'correct', 'result':True}
            else:
                return {'message':'incorrect', 'result':False}
            
        answer_check = check_answer(question_index_global)

        if answer_check['result']:
            user_score += 1
            question_index_global += 1
        else:
            question_index_global += 1

        if not question_index_global > len(questions):

            context = {
                'next_question' : questions[question_index_global],
                'message' : answer_check['message'],
                'ques_num' : question_index_global+1
            }

            return render(request, 'quiz_main/index.html', context=context)

        else:

            context = {
                'score'
            }
    
    else:
        return render(request, 'quiz_main/index.html', {'next_question' : questions[question_index_global], 'message' : 'started','ques_num' : question_index_global+1})
    
def leaderboard(request):
    return HttpResponse('exists')