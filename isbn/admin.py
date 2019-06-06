from django.contrib import admin

from .models import SearchWord, Book

class SearchWordAdmin(admin.ModelAdmin):
    list_display=('pk','word', 'flag')
 
class BookAdmin(admin.ModelAdmin):
    list_display=('pk','word', 'isbn', 'salesDate', 'title', 'itemPrice', 'imageUrl', 'reviewAverage','reviewCount')

admin.site.register(SearchWord, SearchWordAdmin)
admin.site.register(Book, BookAdmin)
