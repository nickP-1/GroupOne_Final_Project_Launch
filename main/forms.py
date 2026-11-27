from django import forms
from .models import PokemonCard


class PokemonCardForm(forms.ModelForm):

    class Meta:
        model = PokemonCard
        fields = [
            "name",
            "rarity",
            "set_name",
            "card_number",
            "condition",
            "price",
            "quantity",
            "description",
        ]

        widgets = {
            "description": forms.Textarea(attrs={
                "rows": 3
            }),
        }

    def clean(self):
        cleaned_data = super().clean()

        if self.instance.pk:
            duplicate = PokemonCard.objects.filter(
                name=cleaned_data.get("name"),
                set_name=cleaned_data.get("set_name"),
                card_number=cleaned_data.get("card_number"),
                condition=cleaned_data.get("condition"),
            ).exclude(pk=self.instance.pk).exists()

            if duplicate:
                raise forms.ValidationError(
                    "This card already exists in your inventory."
                )

        return cleaned_data
