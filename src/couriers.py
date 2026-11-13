"""Kuryerlarni boshqarish moduli (boshlang'ich struktura)."""


def add_courier(courier_id, full_name, phone):
    """Yangi kuryer qo'shadi."""
    return {
        "id": courier_id,
        "full_name": full_name,
        "phone": phone,
        "active": True,
    }
