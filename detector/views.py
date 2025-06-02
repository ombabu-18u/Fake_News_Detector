from django.shortcuts import render, redirect
from .forms import NewsSubmissionForm
from .models import NewsArticle
from .utils import analyze_credibility

# Home page view
def home(request):
    articles = NewsArticle.objects.all().order_by('-submitted_at')[:5]
    return render(request, 'detector/home.html', {'articles': articles})

# Submit news view
def submit_news(request):
    if request.method == 'POST':
        form = NewsSubmissionForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article = analyze_credibility(article)
            article.save()
            return redirect('results')
    else:
        form = NewsSubmissionForm()
    return render(request, 'detector/submit.html', {'form': form})

# Results page view
def results(request):
    articles = NewsArticle.objects.all().order_by('-submitted_at')
    analyzed_articles = [a for a in articles if a.credibility_score > 0]
    avg_score = sum(a.credibility_score for a in analyzed_articles) / len(analyzed_articles) if analyzed_articles else 0
    
    return render(request, 'detector/results.html', {
        'articles': articles,
        'credibility_stats': {
            'avg_score': round(avg_score, 2),
            'reliable_sources': len([a for a in articles if a.source_reliability == 'Reliable'])
        }
    })