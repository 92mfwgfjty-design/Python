
from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 17", "+79991234567"),
    Smartphone("Samsung", "Galaxy S25", "+79997654321"),
    Smartphone("Xiaomi", "15 Pro", "+79995554433"),
    Smartphone("Google", "Pixel 10", "+79998887766"),
    Smartphone("OnePlus", "13", "+79993332211")
]


for phone in catalog:
    print(
        f"{phone.brand} - {phone.model}. "
        f"{phone.phone_number}"
    )
