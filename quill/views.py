from django.shortcuts import render

from q.models import Post


def home(request):
    if request.method == "POST":
        p = Post()
        p.content = request.POST.get('f-body')
        p.save()

    return render(request, "home.html")


def v(request, pk):
    p = Post.objects.get(pk=pk)
    print(p.content)
    return render(request, "view.html", {'post': p})
