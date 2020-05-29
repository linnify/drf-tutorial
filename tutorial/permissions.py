from rest_framework import permissions

from order.models import Order


class IsOwnerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return Order.objects.filter(
            id=view.kwargs.get("order_pk"),
            user=request.user
        ).exists()

    def has_object_permission(self, request, view, obj):

        return obj.user == request.user