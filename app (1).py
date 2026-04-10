from flask import Flask, render_template, request, session
import random

from hangman_words import words_with_hints
from hangman_art import stages

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/", methods=["GET", "POST"])
def game():

    # INIT
    if "word" not in session or "hint" not in session:
        word, hint = random.choice(words_with_hints)
        session["word"] = word
        session["hint"] = hint
        session["display"] = ["_"] * len(word)
        session["lives"] = 6
        session["game_over"] = False
        session["guessed"] = []

    # RESTART
    if request.method == "GET" and session.get("game_over", False):
        session.clear()
        return game()

    # INPUT
    if request.method == "POST" and not session.get("game_over", False):
        guess = request.form["guess"].lower()

        # ignore repeat guesses
        if guess not in session["guessed"]:
            session["guessed"].append(guess)

            if guess in session["word"]:
                display = session["display"]

                for i in range(len(session["word"])):
                    if session["word"][i] == guess:
                        display[i] = guess

                session["display"] = display
                session.modified = True

            else:
                if session["lives"] > 0:
                    session["lives"] -= 1

        # lose
        if session["lives"] == 0:
            session["game_over"] = True

        # win
        if "_" not in session["display"]:
            session["game_over"] = True

    return render_template(
        "index.html",
        display=" ".join(session["display"]),
        lives=session["lives"],
        stage=stages[session["lives"]],
        hint=session.get("hint", ""),
        game_over=session.get("game_over", False),
        word=session.get("word", ""),
        guessed=session.get("guessed", [])
    )


app.run(debug=True)