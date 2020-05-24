from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def search(request):
    subreddit = request.GET.get('subreddit')
    subreddit = subreddit.replace("r/", "")
    subreddit = subreddit.replace("/", "")
    return render(request, 'search.html', {'subreddit': subreddit})


def research(request):
    return render(request, 'research.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})
