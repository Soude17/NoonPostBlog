from django.shortcuts import render,get_object_or_404
from .models import Article


def article_detail(request,slug):
    article = get_object_or_404(Article,slug=slug)
    viewed_articles = request.session.get('viewed_articles', [])
    if article.id not in viewed_articles:
        article.views += 1
        article.save(update_fields=['views'])
        viewed_articles.append(article.id)
        request.session['viewed_articles'] = viewed_articles
    context ={
        'article':article
    }
    return render(request,'blog/article_detail.html',context)
    