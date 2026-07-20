from django.shortcuts import render

from .forms import CharacterForm


def ability_modifier(score):
    """Calculate a D&D 3.5e ability modifier."""

    return (score - 10) // 2


def signed_number(number):
    """Format a modifier with a plus or minus sign."""

    return f"{number:+d}"


def character_builder(request):
    """Display the form and generate the completed character sheet."""

    if request.method == "POST":
        form = CharacterForm(request.POST)

        if form.is_valid():
            character = form.cleaned_data

            ability_fields = [
                ("Strength", "strength"),
                ("Dexterity", "dexterity"),
                ("Constitution", "constitution"),
                ("Intelligence", "intelligence"),
                ("Wisdom", "wisdom"),
                ("Charisma", "charisma"),
            ]

            modifiers = {}
            abilities = []

            for ability_name, field_name in ability_fields:
                score = character[field_name]
                modifier = ability_modifier(score)

                modifiers[field_name] = modifier

                abilities.append(
                    {
                        "name": ability_name,
                        "score": score,
                        "modifier": signed_number(modifier),
                    }
                )

            dexterity_modifier = modifiers["dexterity"]

            # Negative Dexterity still affects flat-footed AC.
            flat_footed_dexterity = min(dexterity_modifier, 0)

            context = {
                "character": character,
                "abilities": abilities,
                "armor_class": (
                    10
                    + character["armor_bonus"]
                    + character["shield_bonus"]
                    + dexterity_modifier
                ),
                "touch_ac": 10 + dexterity_modifier,
                "flat_footed_ac": (
                    10
                    + character["armor_bonus"]
                    + character["shield_bonus"]
                    + flat_footed_dexterity
                ),
                "fortitude_save": signed_number(
                    character["base_fortitude"]
                    + modifiers["constitution"]
                ),
                "reflex_save": signed_number(
                    character["base_reflex"]
                    + modifiers["dexterity"]
                ),
                "will_save": signed_number(
                    character["base_will"]
                    + modifiers["wisdom"]
                ),
                "melee_attack": signed_number(
                    character["base_attack_bonus"]
                    + modifiers["strength"]
                ),
                "ranged_attack": signed_number(
                    character["base_attack_bonus"]
                    + modifiers["dexterity"]
                ),
            }

            return render(
                request,
                "characters/character_sheet.html",
                context,
            )

    else:
        form = CharacterForm()

    return render(
        request,
        "characters/character_form.html",
        {"form": form},
    )
