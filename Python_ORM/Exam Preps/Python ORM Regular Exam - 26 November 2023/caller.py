import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article
from django.db.models import Count, Avg


# Create queries within functions


def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ''

    if search_name is not None and search_email is not None:
        authors = Author.objects.filter(full_name__icontains=search_name, email__icontains=search_email).order_by('-full_name')

    elif search_name is not None:
        authors = Author.objects.filter(full_name__icontains=search_name).order_by('-full_name')

    else:
        authors = Author.objects.filter(email__icontains=search_email).order_by('-full_name')

    result = []
    [result.append(f"Author: {a.full_name}, email: {a.email}, status: {'Banned' if a.is_banned else 'Not Banned'}") for a in authors]

    return '\n'.join(result) if result else ''


def get_top_publisher():
    top_publisher = Author.objects.get_authors_by_article_count().first()
    if top_publisher is None or top_publisher.article_count == 0:
        return ''

    return f"Top Author: {top_publisher.full_name} with {top_publisher.article_count} published articles."


def get_top_reviewer():
    top_reviewer = Author.objects.annotate(review_count=Count('review_author')).order_by('-review_count', 'email').first()

    if not top_reviewer or top_reviewer.review_count == 0:
        return ''

    return f"Top Reviewer: {top_reviewer.full_name} with {top_reviewer.review_count} published reviews."


def get_latest_article():
    latest_article = Article.objects.prefetch_related('authors', 'reviews').order_by('-published_on').first()

    if latest_article is None:
        return ''

    authors_names = ', '.join(a.full_name for a in latest_article.authors.all().order_by('full_name'))
    num_reviews = latest_article.reviews.count()
    avg_rating = sum([r.rating for r in latest_article.reviews.all()]) / num_reviews if num_reviews else 0.0

    return f"The latest article is: {latest_article.title}. Authors: {authors_names}. Reviewed: {num_reviews} times. Average Rating: {avg_rating:.2f}."


def get_top_rated_article():
    top_article = Article.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating', 'title').first()
    num_reviews = top_article.reviews.count() if top_article else 0
    if top_article is None or num_reviews == 0:
        return ''

    avg_rating = top_article.avg_rating or 0.0

    return f"The top-rated article is: {top_article.title}, with an average rating of {avg_rating:.2f}, reviewed {num_reviews} times."


def ban_author(email=None):
    author = Author.objects.prefetch_related('reviews').filter(email__exact=email).first()
    if email is None or author is None:
        return 'No authors banned.'

    num_reviews = author.reviews.count()
    author.is_banned = True
    author.save()
    author.reviews.all().delete()

    return f"Author: {author.full_name} is banned! {num_reviews} reviews deleted."