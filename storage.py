import json
import os

def save_note(note):
    if os.path.exists("notes.json"):

        with open("notes.json", "w") as file:
            try:
                notes = json.load(file)
            except json.JSONDecodeError:
                notes = []

    else:
        notes = []

    notes.append({"note": note})

    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)


def load_note():

    with open("notes.json", "r") as file:
        return json.load(file)
