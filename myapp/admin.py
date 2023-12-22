from django.contrib import admin
from .models import Product,Category, ProductImage

"""TabularInlineは、関連するデータを表形式で表示するためのクラスです。これにより、Productオブジェクトを編集する際に、そのProductに関連するProductImageオブジェクトを直接編集画面で見ることができます。"""
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    """この属性は、デフォルトで表示される空のインラインフォームセットの数を指定します。この場合、extra = 1とすることで、Productを編集する際に最初から1つの空のProductImageフォームが表示されることを意味します。これにより、新しいProductImageを追加する際に便利です。"""


"""ProductAdminクラス内で設定され、Productオブジェクトの管理ページにProductImageInlineを追加します。つまり、Productオブジェクトを編集する際に、関連するProductImageオブジェクトも一緒に表示され、編集や追加が可能になります。"""
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ['name', 'price', 'short_description'] 



admin.site.register(Product, ProductAdmin)
admin.site.register(Category)