  ## def update_price(self, inventory_id, new_price):
    #    if not self.validate_price(new_price):
    #        print("Invalid price. Please enter a valid decimal number.")
    #        return

    #    card = self.get_card(inventory_id)
    #    if card:
    #        card.price = new_price
    #        print(f"Updated {card.name}'s price to ${new_price:.2f}.")
    #    else:
    #        print("Card not found.") 

    #def update_quantity(self, inventory_id, new_quantity):
    #    if not self.validate_quantity(new_quantity):
    #        print("Invalid quantity. Please enter a nonnegative whole number.")
    #        return
    #    card = self.get_card(inventory_id)
    #    if card:
    #        card.quantity = new_quantity
    #        print(f"Updated {card.name}'s quantity to {new_quantity}.")
    #    else:
    #        print("Card not found.")

    #def update_description(self, inventory_id, new_description):
    #    card = self.get_card(inventory_id)
    #    if card:
    #        card.description = new_description
    #        print(f"Updated {card.name}'s description.")
    #    else:
    #        print("Card not found.")

    #def update_condition(self, inventory_id, new_condition):
    #    card = self.get_card(inventory_id)
    #    if card:
    #        card.condition = new_condition
    #        print(f"Updated {card.name}'s condition to {new_condition}.")
    #    else:
    #        print("Card not found.")