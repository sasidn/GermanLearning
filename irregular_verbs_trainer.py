import csv

# Load verbs from the CSV file
def load_verbs(file_path="Irregular_verbs.csv"):
    verbs = {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip the header row
            for row in reader:
                if not row or len(row) < 8:  # Skip empty or incomplete rows
                    continue
                verb = row[0].strip().lower()
                verbs[verb] = row[1:]  # Store conjugations
    except FileNotFoundError:
        print("Error: Irregular_verbs.csv not found!")
    return verbs

# Function to test the user
def practice_verb(verbs):
    verb_input = input("Enter a verb in its infinitive form: ").strip().lower()

    if verb_input in verbs:
        conjugations = verbs[verb_input]
        prompts = ["Ich", "Du", "Er/Sie/Es", "Wir", "Ihr", "Sie", "Past Participle"]

        print(f"\nPracticing verb '{verb_input}':\n")

        for i, prompt in enumerate(prompts):
            while True:
                answer = input(f"{prompt}: ").strip().lower()
                if answer == "n":
                    print(f"The correct answer for {prompt} is: {conjugations[i]}\n")
                    break
                elif answer == conjugations[i].lower():
                    print("Correct!\n")
                    break
                else:
                    print("Try again!")

    else:
        print(f"No verb found for '{verb_input}'.\n")

# Main execution
if __name__ == "__main__":
    verbs_data = load_verbs()
    if verbs_data:
        practice_verb(verbs_data)

