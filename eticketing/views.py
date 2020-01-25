from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Event, EventDetail, Item, Order, OrderItem
from django.utils import timezone
from django.contrib import messages


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
            order.items.remove(order_item)
            messages.info(request, "This item was removed to your cart")
            return redirect('app:event-detail-variation', id=event_detail.id)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('app:event-detail-variation', id=event_detail.id)
    else:
        messages.info(request, "You do not have an active order")
        return redirect('app:event-detail-variation', id=event_detail.id)
