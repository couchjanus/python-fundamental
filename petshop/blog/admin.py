from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Category

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3

# class CommentInline(admin.ChoiceInline):
#     model = Comment
#     extra = 3


class PostAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {"slug": ("title",)}
    
    list_display = ['title', 'pub_date', 'tag_list']
    list_filter = ('status', 'pub_date')
    search_fields = ['title']

    def get_queryset(self, request):
        return super(PostAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
    
    fieldsets = [
        (None,               {'fields': ['title', 'slug','text', 'picture', 'tags', 'category', 'status']}),
        ('Date information', {'fields': ['updated_date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)