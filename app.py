import csv
from flask import Flask, render_template, request

# Load verb data from CSV
def load_verbs(filename="Irregular_verbs.csv"):
    verbs = {}
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) >= 8:
                    verbs[row[0].strip().lower()] = row[1:]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return verbs

# Initialize the Flask app
app = Flask(__name__)

# Load verb data
verbs_data = load_verbs()

# Web page route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        verb = request.form["verb"].strip().lower()
        if verb in verbs_data:
            conjugations = verbs_data[verb]
            pronouns = ["Ich", "Du", "Er/Sie/Es", "Wir", "Ihr", "Sie", "Past Participle"]
            answers = []
            for i, pronoun in enumerate(pronouns):
                answer = request.form.get(f"answer{i}")
                if answer == conjugations[i]:
                    answers.append(f"{pronoun}: Correct!")
                elif answer.lower() == "n":
                    answers.append(f"{pronoun}: The correct answer is {conjugations[i]}")
                else:
                    answers.append(f"{pronoun}: Incorrect!")
            return render_template("index.html", verb=verb, answers=answers)
        else:
            return render_template("index.html", error=f"Sorry, the verb '{verb}' is not in the list.")
    return render_template("index.html", verb=None, answers=None, error=None)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

