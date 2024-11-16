from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

# Configure the folder to save uploaded images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# List to store memories
memories = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        memory = request.form["memory"]
        image_file = request.files.get("image_file")

        # Save the file if uploaded
        image_path = None
        if image_file and image_file.filename != "":
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
            image_file.save(image_path)
            image_path = f"{url_for('static', filename='uploads/' + image_file.filename)}"

        # Store memory with image and timestamp
        memories.append({
            "text": memory,
            "image": image_path,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        return redirect(url_for("memory"))

    return render_template("index.html")

@app.route("/memory", methods=["GET"])
def memory():
    return render_template("memories.html", memories=memories)

if __name__ == "__main__":
    app.run(debug=True)
