from assistant import ask_ai
from storage import save_note, load_note


messages = []

def main():

    while True:

        print("=" * 40)
        print("     Christian's AI Assistant")
        print("=" * 40)

        print("1. Ask AI")
        print("2. Save Note")
        print("3. View Notes")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":

            prompt = input("\nAsk AI: ")

            messages.append({
                "role": "user",
                "content": prompt
            })

            response = ask_ai(messages)

            if response["action"] == "respond":

                answer = response["message"]

                messages.append({
                    "role": "assistant",
                    "content": answer
                })

                print("\nAI:\n")
                print(answer)

            elif response["action"] == "save_note":

                save_note(response["note"])

                print("\n✅ Note saved!")



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
            print("\n Goodbye!")
            break

        else:
            print("\n❌ Invalid option.")

main()