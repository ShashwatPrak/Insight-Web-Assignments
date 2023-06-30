from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=50, null=True)
    publish_date = models.DateField(null=True)
    CATEGORY = (('Non-Fiction', 'Non-Fiction'),
                ('Romance', 'Romance'),
                ('Thriller', 'Thriller'),
                ('Autobiography', 'Autobiography'),
                ('Review', 'Review'),
                ('Science', 'Science'),
                ('Fiction', 'Fiction')
                )
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)

    def __str__(self):
        return self.title
