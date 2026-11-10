"""Buyurtmalarni boshqarish moduli (boshlang'ich struktura)."""

ORDER_STATUSES = ["Yangi", "Biriktirilgan", "Yo'lda", "Yetkazilgan", "Muammo yuz bergan"]


def create_order(order_id, customer, address):
    """Yangi buyurtma yaratadi."""
    return {
        "id": order_id,
        "customer": customer,
        "address": address,
        "status": "Yangi",
    }
