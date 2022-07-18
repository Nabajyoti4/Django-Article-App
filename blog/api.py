from typing import List

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ninja import Router

from blog.models import Article
from blog.schemas import ArticleOut, ArticleIn

router = Router()


@router.post('/articles/create')
def create_article(request, payload: ArticleIn):
    """
    Create a new article given the payload
    :param request: The request object
    :param payload: The payload schema object
    :return:
    """
    data = payload.dict()
    try:
        author = User.objects.get(id=data['author'])
        del data['author']
        article = Article.objects.create(author=author, **data)
        return {
            'detail': 'Article has been successfully created.',
            'id': article.id,
        }
    except User.DoesNotExist:
        return {'detail': 'The specific user cannot be found.'}


@router.get('/articles/{article_id}', response=ArticleOut)
def get_article(request, article_id: int):
    """
    Return article based on the article_id
    :param request:
    :param article_id:
    :return:
    """
    article = get_object_or_404(Article, id=article_id)
    return article


@router.get('/articles', response=List[ArticleOut])
def get_articles(request):
    """
    Return all articles
    :param request:
    :return: List[ArticleOut]
    """
    articles = Article.objects.all()
    return articles