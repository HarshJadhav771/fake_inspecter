from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

# Subjects list
subjects = [
    "Elon Musk",
    "Cristiano Ronaldo",
    "MS Dhoni",
    "Alia Bhatt",
    "Ranbir Kapoor",
    "Taylor Swift",
    "Bill Gates",
    "Rohit Sharma",
    "Amitabh Bachchan",
    "CarryMinati"
]

# Actions list
actions = [
    "launched a new project at",
    "gave a surprise speech at",
    "was spotted filming at",
    "announced a collaboration at",
    "hosted a live event at",
    "trained secretly at",
    "invested in a startup at",
    "performed live at",
    "celebrated a victory at",
    "met fans at"
]

# Places list
places = [
    "Delhi Airport",
    "a secret location in Dubai",
    "a tech conference in Bengaluru",
    "Marine Drive",
    "a cricket stadium in London",
    "an underground studio in Mumbai",
    "a startup hub in Pune",
    "a luxury hotel in Paris",
    "a film set in Hyderabad",
    "a private island resort"
]


@app.route("/")
def index():
    subject=random.choice(subjects)
    action=random.choice(actions)
    place=random.choice(places)

    headline=f"BREAKING NEWS: {subject} {action} {place}"
    return render_template("index.html", headline=headline)



if __name__ == "__main__":
    app.run(debug=True)