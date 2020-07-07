from django.contrib import admin
from linktosite.models import Category, Link, UnauthorizedUserLink
from django.utils.safestring import mark_safe


class LinkInline(admin.TabularInline):
    model = Link
    extra = 0
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="48"')

    get_image.short_description = 'Image'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)
    inlines = [LinkInline]


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'slug', 'link', 'get_image')
    list_display_links = ('title',)
    list_filter = ('category',)
    search_fields = ('title', 'category__name')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="48"')

    get_image.short_description = 'Image'


@admin.register(UnauthorizedUserLink)
class UnauthorizedUserLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'link', 'get_image')
    list_display_links = ('title',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="48"')

    get_image.short_description = 'Image'


title_admin = 'LinkToSite'

admin.site.site_title = title_admin
admin.site.site_header = title_admin
