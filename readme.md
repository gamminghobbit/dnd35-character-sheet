# D&D 3.5e Character Sheet Builder

A web application that creates a simplified Dungeons & Dragons 3.5 Edition character sheet. The user enters character information through a Django form, and the application validates the input, calculates several character statistics, and generates a formatted character sheet.

The application calculates:

- Ability score modifiers
- Armor Class
- Touch Armor Class
- Flat-footed Armor Class
- Fortitude, Reflex, and Will saving throws
- Melee and ranged attack bonuses

## Software Demo

[Software Demo Video](https://youtu.be/DARuzoxDsws)

## Instructions for Build and Use

Steps to build and run the software:

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Create a Python virtual environment:

   ```powershell
   python -m venv .venv
   ```

4. Activate the virtual environment:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

5. Install the required packages:

   ```powershell
   python -m pip install -r requirements.txt
   ```

6. Apply the Django migrations:

   ```powershell
   python manage.py migrate
   ```

7. Start the development server:

   ```powershell
   python manage.py runserver
   ```

8. Open the following address in a web browser:

   ```text
   http://127.0.0.1:8000/
   ```

Instructions for using the software:

1. Enter the character's identity information, including name, player name, race, class, level, and alignment.
2. Enter the character's six ability scores.
3. Enter hit points, armor bonuses, base attack bonus, and base saving throws.
4. Select **Generate Character Sheet**.
5. Review the generated character sheet and the calculated statistics.
6. Use **Create Another Character** to return to the form and create a new character.

The application checks the submitted data before generating the sheet. For example, the level must be between 1 and 20, ability scores must remain within the allowed range, and current hit points cannot be greater than maximum hit points.

## Development Environment

To recreate the development environment, the following software and libraries are needed:

- Python 3.14
- Django 6.0.7
- Visual Studio Code
- HTML5
- CSS3
- Git and GitHub
- A modern web browser

The Python package versions used by the project are also listed in `requirements.txt`.

## Useful Websites to Learn More

I found these websites useful while developing this software:

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Forms Documentation](https://docs.djangoproject.com/en/stable/topics/forms/)
- [Django Templates Documentation](https://docs.djangoproject.com/en/stable/topics/templates/)
- [Python Documentation](https://docs.python.org/3/)
- [MDN CSS Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS)

## Project Features

- Django-generated HTML pages
- User input through a character creation form
- Server-side input validation
- Dynamic character calculations
- Locally stored CSS styling
- Responsive page layout
- Error messages displayed beside invalid fields

## Future Work

The following items could be improved or added in the future:

- [ ] Save characters in a database
- [ ] Edit and delete saved characters
- [ ] Add equipment, weapons, armor, and inventory
- [ ] Add skills, feats, and racial modifiers
- [ ] Add spell lists and spell slots
- [ ] Support multiclass characters
- [ ] Add character portraits
- [ ] Export character sheets as PDF files
- [ ] Add automated tests for forms and calculations