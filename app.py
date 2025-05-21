from flask import Flask, request, jsonify # type: ignore
import json

app = Flask(__name__)

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
    app.run()