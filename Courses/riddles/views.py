from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Riddle, Option
# Create your views here.

def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    # создание HTML-страницы по шаблону index.html
    # с заданными параметрами latest_riddles и message
    return render(
        request,
        "index.html",
        {
            "latest_riddles":
                Riddle.objects.order_by('-pub_date')[:5],
            "message": message
            
        }   
    )

def detail(request, riddle_id):
    error_message = None
    if "error_message" in request.GET:
        error_message = request.GET["error_message"]
    return render(
        request,
        "answer.html",
        {
            "riddle": get_object_or_404(Riddle, pk=riddle_id),
            "error_message": error_message
        }
    )
# обработчик выбранного варианта ответа -
# сам не отдает страниц, а только перенаправляет (redirect)
# на другие страницы с передачей в GET-параметре
# сообщения для отображения на этих страницах
def answer(request, riddle_id):
    riddle = get_object_or_404(Riddle, pk=riddle_id)
    try:
        option = riddle.option_set.get(pk=request.POST['option'])
    except (KeyError, Option.DoesNotExist):
        return redirect(
            '/riddles/' + str(riddle_id) +
            '?error_message=Option does not exist',
        )
    else:
        if option.correct:
            return redirect(
                "/riddles/?message=Nice! Choose another one!")
        else:
            return redirect(
                '/riddles/'+str(riddle_id)+
                '?error_message=Wrong Answer!',
            )
