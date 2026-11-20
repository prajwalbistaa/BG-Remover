from flask import Flask, render_template, request, send_file
from rembg import remove
from pathlib import Path

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    image = request.files["image"]

    input_data = image.read()

    output_data = remove(
        input_data,
        providers=["CPUExecutionProvider"],
    )

    output_path = "output.png"

    with open(output_path, "wb") as f:
        f.write(output_data)

    return send_file(output_path, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)