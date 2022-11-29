from app_store.models import Shop, Action_and_offer
from django.shortcuts import render
from django.core.cache import cache

# from django.views.decorators.cache import cache_page


# @cache_page(30)  Кеширование представлений (страниц)
def main_view(request):
    username = request.user.username
    actions_and_offers = Action_and_offer.objects.all()

    promotions_cache_key = 'actions_and_offers:{}'.format(username)
    cache.get_or_set(promotions_cache_key, actions_and_offers, 30*60)

    # print(actions_and_offers)

    return render(request, 'app_store/main.html', {
        'actions_and_offers': actions_and_offers,
    })


def index_view(request):
    username = request.user.username
    actions_and_offers = Action_and_offer.objects.all()
    shops = Shop.objects.all()

    promotions_cache_key = 'actions_and_offers:{}'.format(username)
    cache.get_or_set(promotions_cache_key, actions_and_offers, 30*60)

    return render(request, 'app_store/index.html', {
        'actions_and_offers': actions_and_offers,
        'shops': shops,
    })


def shops_view(request):
    shops = Shop.objects.all()

    return render(request, 'app_store/shops.html', {
        'shops': shops,
    })
