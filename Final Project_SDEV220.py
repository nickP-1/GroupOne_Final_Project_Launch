# This will be our final project

from dataclasses import dataclass, replace
from decimal import Decimal, InvalidOperation

@dataclass
class PokemonCard:
    name: str
    rarity: str
    set_name: str
    card_number: str #has to be str to account for letters in the card number
    condition: str
    price: Decimal #handles money better than float
    quantity: int #allow zero inventory to restock updates rather than new inventory id
    description: str = ""
    inventory_id: int | None = None #this makes sure the number is assigned at entry, not creation

class InventoryManager:
    def __init__(self):
        self.inventory = {}
        self.next_inventory_id = 1001

    def find_duplicate(self, new_card):
        for card in self.inventory.values():
            if (card.name == new_card.name and
                card.set_name == new_card.set_name and
                card.card_number == new_card.card_number and
                card.condition == new_card.condition):
                return card
        return None
    def add_card(self, new_card):
        if not self.validate_card_fields(new_card):
            print("Invalid card information.  Required fields cannot be empty.")
            return
        if not self.validate_quantity(new_card.quantity):
            print("Invalid quantity. Please enter a nonnegative whole number.")
            return
        if not self.validate_price(new_card.price):
            print("Invalid price. Please enter a valid decimal number.")
            return
        duplicate_card = self.find_duplicate(new_card)
        if duplicate_card:
            duplicate_card.quantity += new_card.quantity
            print(f"Updated quantity of {duplicate_card.name} to {duplicate_card.quantity}.")
        else:
            new_card.inventory_id = self.next_inventory_id
            self.inventory[self.next_inventory_id] = new_card
            self.next_inventory_id += 1
            print(f"Added {new_card.name} to inventory with ID {new_card.inventory_id}.")

    def get_card(self, inventory_id):
        return self.inventory.get(inventory_id)

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
            return
        for card in self.inventory.values():
            print(f"ID: {card.inventory_id}, Name: {card.name}, Rarity: {card.rarity}, "
                  f"Set: {card.set_name}, Card Number: {card.card_number}, "
                  f"Condition: {card.condition}, Price: ${card.price:.2f}, "
                  f"Quantity: {card.quantity}, Description: {card.description}")
    
    def update_card(self, inventory_id, **kwargs):
        card = self.get_card(inventory_id)
        if not card:
            print("Card not found.")
            return
        
        if not kwargs:
            print("No fields to update.")
            return

        

        protected_fields = {"inventory_id"}
        for key in kwargs:
            if key in protected_fields or not hasattr(card, key):
                print(f"Invalid field: {key}")
                return

        if "quantity" in kwargs:
            if not self.validate_quantity(kwargs["quantity"]):
                print("Invalid quantity. Please enter a nonnegative whole number.")
                return
        if "price" in kwargs:
            if not self.validate_price(kwargs["price"]):
                print("Invalid price. Please enter a valid decimal number.")
                return

        updated_card = replace(card, **kwargs)
        if not self.validate_card_fields(updated_card):
            print("Invalid card information.  Required fields cannot be empty.")
            return
        if self.has_duplicate(updated_card, inventory_id):
            print("Update rejected.  This would create a duplicate inventory record.")
            return
        for key, value in kwargs.items():
            setattr(card, key, value)
        print(f"Updated {card.name} successfully.")

    def delete_card(self, inventory_id):
        if inventory_id in self.inventory:
            removed_card = self.inventory.pop(inventory_id)
            print(f"Deleted {removed_card.name} from inventory.")
        else:
            print("Card not found.")

    def validate_quantity(self, quantity):
        if type(quantity) is not int or quantity < 0:
            return False
        return True

    def validate_price(self, price):
        if price is None:
            return False
        if not isinstance(price, Decimal):
            return False
        return True

    def has_duplicate(self, updated_card, inventory_id):
        for card in self.inventory.values():
            if card.inventory_id == inventory_id:
                continue
            if (card.name == updated_card.name and
                card.set_name == updated_card.set_name and
                card.card_number == updated_card.card_number and
                card.condition == updated_card.condition):
                return True
            
        return False

    def validate_card_fields(self, updated_card):
        required_fields = ("name", "rarity", "set_name", "card_number", "condition")
        for field in required_fields:
            value = getattr(updated_card, field)
            if not isinstance(value, str) or value.strip() == "":
                return False
        return True


inventory = InventoryManager()

menu = ["1. Add a Pokemon card", "2. Display inventory", "3. Search for a card",
        "4. Update a card", "5. Delete a card", "6. Exit"]
def main_menu():
    while True:
        for option in menu:
            print(option)
        choice = input("Select an option (1-6): ")
        if choice == "1":
            add_card_menu
        elif choice == "2":
            inventory.display_inventory()
        elif choice == "3":
            print("Search for a card selected")
        elif choice == "4":
            print("Update a card selected")
        elif choice == "5":
            print("Delete a card selected")
        elif choice == "6":
            print("The program is now exiting")
            break
        else:
            print("Please select an option (1-6)")

def add_card_menu():
    name = input("Enter card name: ")
    rarity = input("Enter card rarity: ")
    set_name = input("Enter set name: ")
    card_number = input("Enter card number: ")
    condition = input("Enter card condition: ")
    while True:
        try:
            price = Decimal(input("Enter card price: "))
            break
        except InvalidOperation:
            print("Invalid price.  Please enter a valid decimal number.")
    while True:
        try:
            quantity = int(input("Enter card quantity: "))
            break
        except ValueError:
            print("Invalid quantity.  Please enter a whole number")    
    description = input("Enter card description: ")

new_card = PokemonCard(
    name=name,
    rarity=rarity,
    set_name=set_name,
    card_number=card_number,
    condition=condition,
    price=price,
    quantity=quantity,
    description=description
)

inventory.add_card(new_card) 