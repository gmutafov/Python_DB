import os
from datetime import timedelta, date

import django
from django.db.models import QuerySet, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Create queries within functions
from main_app.models import Author, Book, Song, Artist, Product, Review, Driver, DrivingLicense, Owner, Registration, Car

def show_all_authors_with_their_books():
    authors = Author.objects.all().order_by('id')
    result = []

    for a in authors:
        books = Book.objects.filter(author=a)
        if not books:
            continue

        titles = ', '.join(b.titl for b in books)
        result.append(f'{a.name} has written - {titles}')


def delete_all_authors_without_books() -> None:
    authors_without_books = Author.objects.filter(books__isnull=True)
    authors_without_books.delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.add(song)


def get_songs_by_artist(artist_name: str) -> QuerySet:
    artist = Artist.objects.get(name=artist_name)
    return artist.songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()
    avg_rating = sum(r.rating for r in reviews) / len(reviews)

    return avg_rating


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    get_products_with_no_reviews().delete()


def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.all().order_by('-license_number')

    return '\n'.join(str(l) for l in licenses)


def get_drivers_with_expired_licenses(due_date: date):
    finding_date = due_date - timedelta(days=365)
    drivers_with_expired_licenses = Driver.objects.filter(license__issue_date__gt=finding_date)

    return drivers_with_expired_licenses


def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner

    car.save()

    registration.registration_date = date.today()
    registration.car = car

    registration.save()

    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."
