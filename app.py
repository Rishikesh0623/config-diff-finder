from flask import Flask, render_template, request

from diff_finder.set_diff import set_compare
from diff_finder.sequence_diff import sequence_compare

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("upload.html")


@app.route("/compare", methods=["POST"])
def compare():

    file1 = request.files.get("file1")
    file2 = request.files.get("file2")
    engine = request.form.get("engine")

    if not file1 or not file2:
        return "Both files must be uploaded", 400

    if engine == "set":
        results = set_compare(file1, file2)
        return render_template(
            "result.html",
            mode="set",
            added=results["added"],
            removed=results["removed"]
        )

    elif engine == "sequence":
        results = sequence_compare(file1, file2)
        return render_template(
            "result.html",
            mode="sequence",
            sequence_results=results
        )

    else:
        return "Invalid diff mode selected", 400


if __name__ == "__main__":
    app.run(debug=True)
