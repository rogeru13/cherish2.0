from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store memories in a list (in memory for simplicity)
memories = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        memory = request.form.get("memory")
        if memory:  # Add memory to the list if it's not empty
            memories.append(memory)
        return redirect(url_for("index"))
    return render_template("index.html")

@app.route("/memories")
def memory_page():
    return render_template("memories.html", memories=memories)

if __name__ == "__main__":
    app.run(debug=True)
