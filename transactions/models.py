from django.db import models
from django.contrib.auth.models import User
from books.models import Book

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.book.title} - {self.member.user.username}"