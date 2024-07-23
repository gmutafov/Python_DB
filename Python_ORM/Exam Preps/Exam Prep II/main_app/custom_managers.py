from django.db import models


class ProfileModelManager(models.Manager):

    def get_regular_customers(self):
        return self.annotate(orders_count=models.Count('profiles')).filter(orders_count__gt=2).order_by('-orders_count')
