from storage import save_note, load_note

def main():
    print("=" * 40)
    print("     Christian's AI Assistant")
    print("=" * 40)

    print("1. Ask AI")
    print("2. Save Note")
    print("3. View Notes")
    print("4. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        print("\n🚀 AI feature coming soon!")

    elif choice == "2":
        note = input("Enter your note: ")
        save_note(note)
        print("Note saved!")



    elif choice == "3":
        notes = load_note()

        print("\nSaved Notes:\n")

        for note in notes:
            print("-", note["note"])

    elif choice == "4":
        print("\n👋 Goodbye!")

    else:
        print("\n❌ Invalid option.")





main()