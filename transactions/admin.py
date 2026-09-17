from django.contrib import admin
from .models import Member, Transaction

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership_id', 'phone', 'join_date')
    search_fields = ('user__username', 'membership_id')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'issue_date', 'due_date', 'return_date', 'fine_amount')
    list_filter = ('return_date',)
    search_fields = ('book__title', 'member__user__username')