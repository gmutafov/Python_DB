import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Order, Product
from django.db.models import Count, Q, F, Case, When, Value


# Create queries within functions


def get_profiles(search_string=None):
    result = []
    if search_string is not None:
        profiles = Profile.objects.annotate(orders_count=Count('profiles')).filter(
            Q(full_name__icontains=search_string)
            | Q(email__icontains=search_string)
            | Q(phone_number__icontains=search_string)
        ).order_by('full_name')

        [result.append(
            f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders_count}") for p
         in profiles]

    return '\n'.join(result) if result else ""


def get_loyal_profiles():
    loyal_profiles = Profile.objects.get_regular_customers()
    result = []

    [result.append(f"Profile: {p.full_name}, orders: {p.orders_count}") for p in loyal_profiles]
    return '\n'.join(result) if result else ""


def get_last_sold_products():
    last_order = Order.objects.prefetch_related('products').last()

    if last_order is None or not last_order.products.exists():
        return ''

    products = ', '.join([p.name for p in last_order.products.order_by('name')])

    return f"Last sold products: {products}"


def get_top_products():
    top_products = Product.objects.annotate(
        orders_count=Count('orders')
    ).filter(
        orders_count__gt=0
    ).order_by('-orders_count', 'name')[:5]

    if not top_products:
        return ''

    products = '\n'.join([f"{p.name}, sold {p.orders_count} times" for p in top_products])

    return f"Top products:\n{products}"


def apply_discounts():
    updated_orders_count = Order.objects.annotate(
        products_count=Count('products')
    ).filter(
        products_count__gt=2,
        is_completed=False
    ).update(total_price=F('total_price') * 0.90)

    return f"Discount applied to {updated_orders_count} orders."


def complete_order():
    order = Order.objects.filter(
        is_completed=False
    ).order_by('creation_date').first()

    if not order:
        return ''

    order.products.update(
        in_stock=F('in_stock') - 1,
        is_available=Case(
            When(in_stock=1, then=Value(False)),
            default=F('is_available'),
        )
    )

    order.is_completed = True
    order.save()

    return "Order has been completed!"
