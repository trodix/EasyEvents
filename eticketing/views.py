from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from django.views.generic.detail import DetailView, View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Event, EventDetail, Item, Order, OrderItem


def event_list(request):
    events = Event.objects.all()

    return render(request, 'eticketing/event_list.html', {
        'events': events
    })


def event_detail(request, id):
    event = Event.objects.get(pk=id)

    return render(request, 'eticketing/event_detail.html', {
        'event': event
    })


def event_detail_variation(request, id):
    event_detail = EventDetail.objects.get(pk=id)

    return render(request, 'eticketing/event_variation.html', {
        'event_detail': event_detail
    })


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect('app:events-list')
        return render(self.request, 'eticketing/order_summary.html', {
            'object': order
        })


@login_required
def add_to_cart(request, id):
    item = get_object_or_404(Item, id=id)
    event_detail = item.event_detail
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )

    # check if the user have an unpaid order
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # check if order_item is in order
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
            return redirect('app:event-detail-variation', id=event_detail.id)
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart")
            return redirect('app:event-detail-variation', id=event_detail.id)

    else:
        order = Order.objects.create(
            user=request.user, ordered_date=timezone.now())
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
        return redirect('app:event-detail-variation', id=event_detail.id)


@login_required
def add_single_to_cart(request, id):
    item = get_object_or_404(Item, id=id)
    event_detail = item.event_detail

    # check if the user have an unpaid order
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # check if order_item is in order
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
            return redirect('app:order-summary')
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('app:order-summary')
    else:
        messages.info(request, "You do not have an active order")
        return redirect('app:order-summary')


@login_required
def remove_from_cart(request, id):
    item = get_object_or_404(Item, id=id)
    event_detail = item.event_detail

    # check if the user have an unpaid order
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # check if order_item is in order
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            OrderItem.objects.get(pk=order_item.id).delete()
            order.items.remove(order_item)
            messages.info(request, "This item was removed to your cart")
            return redirect('app:order-summary')
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('app:event-detail-variation', id=event_detail.id)
    else:
        messages.info(request, "You do not have an active order")
        return redirect('app:event-detail-variation', id=event_detail.id)


@login_required
def remove_single_from_cart(request, id):
    item = get_object_or_404(Item, id=id)
    event_detail = item.event_detail

    # check if the user have an unpaid order
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # check if order_item is in order
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated")
            return redirect('app:order-summary')
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('app:event-detail-variation', id=event_detail.id)
    else:
        messages.info(request, "You do not have an active order")
        return redirect('app:event-detail-variation', id=event_detail.id)
