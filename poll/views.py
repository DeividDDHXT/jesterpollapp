from django.shortcuts import get_object_or_404, redirect, render
from .models import Question, Choice

# Create your views here.

def home (request):
    questions = Question.objects.all()
    return render(request, 'poll/home.html', {
        "questions": questions
        }
    )

def vote (request, q_id):
    q = get_object_or_404(Question, pk=q_id)
    if request.method == "POST":
        try:
            choice_id = request.POST.get('choice')
            choice = q.choice_set.get(pk=choice_id)
            choice.vote += 1
            choice.save()
            return redirect('poll:result',  q_id)
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'poll/vote.html', {
                "question": q,
                "error_message": "Para votar debes elegir una opción"
    })
    return render(request, 'poll/vote.html', {
            "question": q
})

def result (request, q_id):
    try:
        q = Question.objects.get(pk=q_id)
    except Question.DoesNotExist:
        return redirect('poll:home')
    return render(request, 'poll/result.html', {
        "question": q
        })