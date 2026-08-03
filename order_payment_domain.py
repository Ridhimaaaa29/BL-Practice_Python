from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Iterable

# Abstract base class for discount behavior

class DiscountPolicy(ABC):

    @abstractmethod
    def apply_discount(self, order_total: float) -> float:
        pass

class NoDiscount(DiscountPolicy):

    def apply_discount(self, order_total: float) -> float:
        return order_total

class PercentageDiscount(DiscountPolicy):

    def __init__(self, percentage: float):

        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")

        self.percentage = percentage

    def apply_discount(self, order_total: float) -> float:
        return order_total * (1 - self.percentage / 100)

# Item class implementing encapsulation

@dataclass
class Item:
    """dataclass decorator automatically generates init, repr, 
    and other methods it is used here to simplify the creation 
    of classes that primarily store data."""

    name: str
    quantity: int
    price: float
    _price: float = field(init=False, repr=False)

    def __post_init__(self) -> None:

        initial_price = self.price
        self.price = initial_price

        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:

        if value < 0:
            raise ValueError("Price cannot be negative.")

        self._price = value

    @property
    def total(self) -> float:
        return self.quantity * self.price

    def __str__(self) -> str:
        return (
            f"{self.name} | "
            f"Quantity: {self.quantity} | "
            f"Price: ₹{self.price:.2f} | "
            f"Total: ₹{self.total:.2f}"
        )

# Order class

class Order:

    _existing_order_ids: set[str] = set()

    def __init__(
        self,
        order_id: str,
        items: Iterable[Item] | None = None,
        discount_policy: DiscountPolicy | None = None
    ):

        if not order_id.strip():
            raise ValueError("Order ID cannot be empty.")

        self.order_id = order_id
        self._items: list[Item] = list(items) if items else []
        self.discount_policy = discount_policy or NoDiscount()

        Order._existing_order_ids.add(order_id)

    def add_item(self, item: Item) -> None:
        self._items.append(item)

    @property
    def subtotal(self) -> float:
        return sum(item.total for item in self._items)

    @property
    def total(self) -> float:
        return self.discount_policy.apply_discount(self.subtotal)

    @property
    def discount_amount(self) -> float:
        return self.subtotal - self.total

    @classmethod
    def order_exists(cls, order_id: str) -> bool:
        return order_id in cls._existing_order_ids

    # Dunder methods

    def __len__(self) -> int:
        return len(self._items)

    def __contains__(self, item_name: str) -> bool:
        return any(
            item.name.lower() == item_name.lower()
            for item in self._items
        )

    def __getitem__(self, index: int) -> Item:
        return self._items[index]

    def __iter__(self) -> Iterable[Item]:
        return iter(self._items)

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Order)
            and self.order_id == other.order_id
        )

    def __repr__(self) -> str:
        return f"Order(order_id='{self.order_id}')"

    def __str__(self) -> str:

        items = "\n".join(str(item) for item in self._items)

        if isinstance(self.discount_policy, PercentageDiscount):
            discount = f"{self.discount_policy.percentage}%"
        else:
            discount = "No Discount"

        return (
            f"Order ID: {self.order_id}\n"
            f"Items:\n{items}\n"
            f"Number of Items: {len(self)}\n"
            f"Subtotal: ₹{self.subtotal:.2f}\n"
            f"Discount: {discount}\n"
            f"Discount Amount: ₹{self.discount_amount:.2f}\n"
            f"Total After Discount: ₹{self.total:.2f}"
        )

if __name__ == "__main__":

    try:

        # Create Items

        laptop = Item("Laptop", quantity=1, price=50000)
        mouse = Item("Mouse", quantity=2, price=700)
        keyboard = Item("Keyboard", quantity=1, price=2500)

        # Create Order with 20% Discount

        order = Order(
            "ORD-101",
            discount_policy=PercentageDiscount(20)
        )

        # Add Items

        order.add_item(laptop)
        order.add_item(mouse)
        order.add_item(keyboard)

        # Print Complete Order

        print(order)

        # __len__()

        print("\nNumber of Items:")
        print(len(order))

        # __contains__()

        print("\nChecking Item Availability:")
        print("Laptop" in order)
        print("Monitor" in order)

        # __getitem__()

        print("\nFirst Item:")
        print(order[0])

        # __iter__()

        print("\nIterating through Order:")

        for item in order:
            print(item)

        # __eq__()

        another_order = Order(
            "ORD-101",
            discount_policy=NoDiscount()
        )

        print("\nSame Order?")
        print(order == another_order)

        # Class Method

        print("\nChecking Existing Orders:")
        print(Order.order_exists("ORD-101"))
        print(Order.order_exists("ORD-999"))

    except ValueError as error:
        print("Error:", error)