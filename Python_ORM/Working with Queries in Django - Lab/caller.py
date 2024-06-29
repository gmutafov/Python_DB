import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Author, Book, Review

# Create and check models

def find_books_by_genre_and_language(genre, language):
    books = Book.objects.filter(genre=genre, language=language)
    return books


def find_authors_nationalities():
    authors = Author.objects.exclude(nationality=None)
    result = [f"{a.first_name} {a.last_name} is {a.nationality}" for a in authors]
    return '\n'.join(result)


def order_books_by_year():
    books = Book.objects.order_by('publication_year', 'title')
    result = [f"{b.publication_year} year: {b.title} by {b.author}" for b in books]

    return '\n'.join(result)


def delete_review_by_id(reviewer_id):
    review = Review.objects.get(pk=reviewer_id)
    review.delete()

    return f"{str(review)} was deleted"


def filter_authors_by_nationalities(nationality):
    authors = Author.objects.filter(nationality=nationality).order_by('first_name', 'last_name')
    result = []

    for a in authors:
        result.append(a.biography) if a.biography is not None else result.append(f"{a.first_name} {a.last_name}")

    return '\n'.join(result)


def filter_authors_by_birth_year(first_year, second_year):
    authors = Author.objects.filter(birth_date__year__range=(first_year, second_year)).order_by('-birth_date')
    result = [f"{a.birth_date}: {a.first_name} {a.last_name}" for a in authors]

    return '\n'.join(result)


def change_reviewer_name(reviewer_name, new_name):
    Review.objects.filter(reviewer_name=reviewer_name).update(reviewer_name=new_name)
    return Review.objects.all()

