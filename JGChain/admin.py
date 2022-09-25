from django.contrib import admin
from .models import Block, JGChain
# Register your models here.
class BlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'current_hash', 'previous_hash', 'timestamp', 'data', 'nonce')

admin.site.register(Block, BlockAdmin)
admin.site.register(JGChain)