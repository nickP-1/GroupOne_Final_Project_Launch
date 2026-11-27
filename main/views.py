from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import PokemonCard
from .forms import PokemonCardForm


def home(request):
    return render(request, "main/home.html", {
        "name": "User"
    })


def inventory_list(request):
    cards = PokemonCard.objects.all()

    return render(request, "main/inventory.html", {
        "cards": cards
    })


def add_card(request):
    if request.method == "POST":
        form = PokemonCardForm(request.POST)

        if form.is_valid():
            new_card = form.save(commit=False)

            existing_card = PokemonCard.objects.filter(
                name=new_card.name,
                set_name=new_card.set_name,
                card_number=new_card.card_number,
                condition=new_card.condition,
            ).first()

            if existing_card:
                existing_card.quantity += new_card.quantity
                existing_card.save(update_fields=["quantity"])

                messages.success(
                    request,
                    f"Updated {existing_card.name} quantity."
                )
            else:
                new_card.save()

                messages.success(
                    request,
                    f"Added {new_card.name} to inventory."
                )

            return redirect("inventory")

    else:
        form = PokemonCardForm()

    return render(request, "main/card_form.html", {
        "form": form,
        "page_title": "Add Card"
    })


def edit_card(request, card_id):
    card = get_object_or_404(PokemonCard, pk=card_id)

    if request.method == "POST":
        form = PokemonCardForm(request.POST, instance=card)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                f"Updated {card.name} successfully."
            )

            return redirect("inventory")

    else:
        form = PokemonCardForm(instance=card)

    return render(request, "main/card_form.html", {
        "form": form,
        "page_title": "Edit Card"
    })


def delete_card(request, card_id):
    card = get_object_or_404(PokemonCard, pk=card_id)

    if request.method == "POST":
        card_name = card.name
        card.delete()

        messages.success(
            request,
            f"Deleted {card_name} from inventory."
        )

        return redirect("inventory")

    return render(request, "main/card_confirm_delete.html", {
        "card": card
    })
