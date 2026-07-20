from django import forms


class CharacterForm(forms.Form):
    """Collect the information needed to generate a simplified D&D 3.5e sheet."""

    ALIGNMENTS = [
        ("Lawful Good", "Lawful Good"),
        ("Neutral Good", "Neutral Good"),
        ("Chaotic Good", "Chaotic Good"),
        ("Lawful Neutral", "Lawful Neutral"),
        ("True Neutral", "True Neutral"),
        ("Chaotic Neutral", "Chaotic Neutral"),
        ("Lawful Evil", "Lawful Evil"),
        ("Neutral Evil", "Neutral Evil"),
        ("Chaotic Evil", "Chaotic Evil"),
    ]

    # Character identity
    character_name = forms.CharField(
        label="Character Name",
        max_length=100,
    )
    player_name = forms.CharField(
        label="Player Name",
        max_length=100,
    )
    race = forms.CharField(
        label="Race",
        max_length=50,
    )
    character_class = forms.CharField(
        label="Class",
        max_length=50,
    )
    level = forms.IntegerField(
        label="Level",
        min_value=1,
        max_value=20,
        initial=1,
    )
    alignment = forms.ChoiceField(
        label="Alignment",
        choices=ALIGNMENTS,
    )

    # Ability scores
    strength = forms.IntegerField(
        label="Strength",
        min_value=1,
        max_value=40,
        initial=10,
    )
    dexterity = forms.IntegerField(
        label="Dexterity",
        min_value=1,
        max_value=40,
        initial=10,
    )
    constitution = forms.IntegerField(
        label="Constitution",
        min_value=1,
        max_value=40,
        initial=10,
    )
    intelligence = forms.IntegerField(
        label="Intelligence",
        min_value=1,
        max_value=40,
        initial=10,
    )
    wisdom = forms.IntegerField(
        label="Wisdom",
        min_value=1,
        max_value=40,
        initial=10,
    )
    charisma = forms.IntegerField(
        label="Charisma",
        min_value=1,
        max_value=40,
        initial=10,
    )

    # Combat information
    maximum_hp = forms.IntegerField(
        label="Maximum Hit Points",
        min_value=1,
        initial=10,
    )
    current_hp = forms.IntegerField(
        label="Current Hit Points",
        min_value=-10,
        initial=10,
    )
    armor_bonus = forms.IntegerField(
        label="Armor Bonus",
        min_value=0,
        initial=0,
    )
    shield_bonus = forms.IntegerField(
        label="Shield Bonus",
        min_value=0,
        initial=0,
    )
    base_attack_bonus = forms.IntegerField(
        label="Base Attack Bonus",
        min_value=0,
        initial=0,
    )
    base_fortitude = forms.IntegerField(
        label="Base Fortitude Save",
        min_value=0,
        initial=0,
    )
    base_reflex = forms.IntegerField(
        label="Base Reflex Save",
        min_value=0,
        initial=0,
    )
    base_will = forms.IntegerField(
        label="Base Will Save",
        min_value=0,
        initial=0,
    )

    def clean(self):
        """Perform validation that depends on more than one field."""

        cleaned_data = super().clean()

        current_hp = cleaned_data.get("current_hp")
        maximum_hp = cleaned_data.get("maximum_hp")

        if (
            current_hp is not None
            and maximum_hp is not None
            and current_hp > maximum_hp
        ):
            self.add_error(
                "current_hp",
                "Current hit points cannot be greater than maximum hit points.",
            )

        return cleaned_data