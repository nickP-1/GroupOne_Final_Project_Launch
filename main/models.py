from django.db import models


class PokemonCard(models.Model):
    name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=50)
    set_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=30)
    condition = models.CharField(max_length=50)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "name",
                    "set_name",
                    "card_number",
                    "condition"
                ],
                name="unique_inventory_card_variant"
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.set_name})"
