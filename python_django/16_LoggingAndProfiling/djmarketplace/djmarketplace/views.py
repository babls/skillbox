from app_users.models import *
from django.db import transaction
from django.db.models import Count
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from djmarketplace.forms import AddMoneyForm
import logging


logger = logging.getLogger(__name__)


def index_view(request):
    listProducts = ListProductShop.objects.select_related('shop', 'product').all()

    return render(request, 'djmarketplace/shops.html', {
        'listProducts': listProducts,
    })


def money_view(request):
    if request.method == 'POST':
        money_form = AddMoneyForm(request.POST)
        print(money_form)
        if money_form.is_valid():
            money = money_form.cleaned_data['add_money']
            profile = Profile.objects.get(user=request.user)
            profile.balance += money
            profile.save(update_fields=['balance'])  # оптимизация метода save
            logger.info('Пополнение баланса ' + str(profile.balance) + ' Пользователь - ' + request.user)
            return HttpResponseRedirect(reverse('lk'))
    else:
        money_form = AddMoneyForm()
    return render(request, 'djmarketplace/money.html', {'form': money_form})


def addHistory_shopping(id_user, id_product):
    ListProduct = ListProductShop.objects.get(id=id_product)
    ListProduct.amount -= 1
    product = ListProduct.product
    shop = ListProduct.shop
    user = User.objects.get(username=id_user)
    add = History_shopping(product=product, count=1, shop=shop, user=user, status='A')
    add.save()


class addBasket_view(View):
    def get(self, request, id_product):
        ListProduct = ListProductShop.objects.get(id=id_product)
        id_shop = ListProduct.shop.id
        with transaction.atomic():
            if ListProduct.amount > 0:
                ListProduct.amount -= 1
            else:
                return HttpResponseRedirect(reverse('shops'))
            ListProduct.save(update_fields=['amount'])
            addHistory_shopping(request.user, id_product)
            logger.info('Оформление заказа ID_PRODUCT - ' + str(id_product))
        return HttpResponseRedirect(reverse('shops'))


class deleteBasket_view(View):
    def get(self, request, id_history_shopping):
        ListHistoryShopping = History_shopping.objects.get(id=id_history_shopping)
        addAmountListProductShop = ListProductShop.objects.get(shop=ListHistoryShopping.shop,
                                                               product=ListHistoryShopping.product)

        with transaction.atomic():
            if ListHistoryShopping.status == 'A':
                ListHistoryShopping.status = 'C'
            else:
                return HttpResponseRedirect(reverse('shops'))
            ListHistoryShopping.save(update_fields=['status'])
            addAmountListProductShop.amount += 1
            addAmountListProductShop.save(update_fields=['amount'])

        return HttpResponseRedirect(reverse('history_shopping'))


class buyBasket_view(View):
    def get(self, request, id_history_shopping):
        ListHistoryShopping = History_shopping.objects.get(id=id_history_shopping)
        buyProduct = Product.objects.get(name=ListHistoryShopping.product)
        user = Profile.objects.get(user=request.user)
        if user.balance - buyProduct.price >= 0:
            with transaction.atomic():
                ListHistoryShopping.status = 'P'
                user.balance -= buyProduct.price
                user.balanceShopping += buyProduct.price

                if user.balanceShopping >= 200:
                    user.status = 'В'
                    logger.info('переход пользователя по статусной системе ' + user.status)
                elif user.balanceShopping >= 100:
                    user.status = 'С'
                    logger.info('переход пользователя по статусной системе ' + user.status)
                else:
                    user.status = 'Н'
                user.save()
                logger.info('списание баллов с баланса ' + str(user.balance) +' - '+str(buyProduct.price))
                ListHistoryShopping.save(update_fields=['status'])

            return HttpResponseRedirect(reverse('history_shopping'))
        else:
            return HttpResponse("У Вас недостаточно средств на счёте, пополните баланс! ")


def report_view(request):
    СReport = Product.objects.filter(history_shopping__status='C')
    СReport = СReport.annotate(count_buy=Count('history_shopping', distinct=True)).order_by('-count_buy')

    PReport = Product.objects.filter(history_shopping__status='P')
    PReport = PReport.annotate(count_buy=Count('history_shopping', distinct=True)).order_by('-count_buy')
    # print(str(Report.query))

    UserReport = Profile.objects.all().order_by('balanceShopping').order_by('-balanceShopping')

    return render(request, 'djmarketplace/report.html', {
        'СReport': СReport, 'PReport': PReport, 'UserReport': UserReport
    })
