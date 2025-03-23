from my_functions import get_totals, calc_total


def get_total(*orders):
    for orden in orders:
        total_orden = get_totals(orden)
    total_suma = calc_total(total_orden)
    return total_suma


orders = [
    {
        "customer_name": "Nicolas",
        "total": 100,
        "delivered": True,
    },
    {
        "customer_name": "Zulema",
        "total": 120,
        "delivered": False,
    },
    {
        "customer_name": "Santiago",
        "total": 20,
        "delivered": False,
    }
]

total = get_total(orders)
print(total)
