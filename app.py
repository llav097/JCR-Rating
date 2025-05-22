from flask import Flask, request, render_template, jsonify # type: ignore
import json

app = Flask(__name__)

# Load pricay html
@app.route("/privacy")
def privacy_policy():
    return render_template("privacy.html")

# Load JSON once on startup
with open("jcr_data.json", "r") as f:
    jcr_data = json.load(f)

@app.route("/api/jcr-rating", methods=["GET"])
def get_jcr_rating():
    journal_query = request.args.get("journal")
    issn_query = request.args.get("issn")

    for entry in jcr_data:
        if (journal_query and journal_query.lower() == entry["journal"].lower()) or \
           (issn_query and issn_query == entry["issn"]):
            return jsonify(entry)

    return jsonify({"error": "Journal not found"}), 404

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
