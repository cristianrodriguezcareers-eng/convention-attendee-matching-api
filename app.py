from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("convention.db")

@app.route("/")
def home():
    return {"status": "Convention Matching API running"}

@app.route("/matches/<int:user_id>")
def get_matches(user_id):
    db = get_db()
    cursor = db.cursor()

    query = """
    SELECT u.id, u.name
    FROM users u
    JOIN user_conventions uc ON u.id = uc.user_id
    JOIN user_interests ui ON u.id = ui.user_id
    WHERE uc.convention_id = (
        SELECT convention_id FROM user_conventions WHERE user_id = ?
    )
    AND ui.interest_id IN (
        SELECT interest_id FROM user_interests WHERE user_id = ?
    )
    AND u.id != ?
    GROUP BY u.id
    """
    cursor.execute(query, (user_id, user_id, user_id))
    results = cursor.fetchall()

    matches = [{"id": r[0], "name": r[1]} for r in results]
    return jsonify(matches)

if __name__ == "__main__":
    app.run(debug=True)
