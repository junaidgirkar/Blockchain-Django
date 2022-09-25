from .views import home_view, mine_block, get_chain, block_detail_view, attack_a_block
from django.urls import path

app_name = "JGChain"
urlpatterns = [
    path('', get_chain, name="full_chain"),
    path('mine_block/', mine_block, name="mine_block"),
    path('detail/<int:id>/', block_detail_view, name="block_detail_view"),
    path('attack/', attack_a_block, name="attack_block"),
]
