from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("careerdash.db")

    conn.execute("""
    CREATE TABLE IF NOT EXISTS applications(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    position TEXT NOT NULL,
    status TEXT NOT NULL,
    date_applied TEXT NOT NULL
    )
    """)

    conn.close()

init_db()

@app.route("/")
def home():
    search = request.args.get("search", "")
    status_filter = request.args.get("status", "")

    conn = sqlite3.connect("careerdash.db")
    conn.row_factory = sqlite3.Row

    query = "SELECT * FROM applications WHERE 1=1"
    parameters = []

    if search:
        query += " AND (company LIKE ? OR position LIKE ?)"
        search_term = f"%{search}%"
        parameters.extend([search_term, search_term])

    if status_filter:
        query += " AND status = ?"
        parameters.append(status_filter)

    query += " ORDER BY id DESC"

    applications = conn.execute(
        query,
        parameters
    ).fetchall()

    total_applications = conn.execute(
        "SELECT COUNT(*) FROM applications"
    ).fetchone()[0]

    total_interviews = conn.execute(
        "SELECT COUNT(*) FROM applications WHERE status = 'Interview'"
    ).fetchone()[0]

    total_offers = conn.execute(
        "SELECT COUNT(*) FROM applications WHERE status = 'Offer'"
    ).fetchone()[0]

    total_rejected = conn.execute(
        "SELECT COUNT(*) FROM applications WHERE status = 'Rejected'"
    ).fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        applications=applications,
        total_applications=total_applications,
        total_interviews=total_interviews,
        total_offers=total_offers,
        total_rejected=total_rejected,
        search=search,
        status_filter=status_filter
    )

@app.route("/add", methods=["GET", "POST"])
def add_application():
    
    if request.method == "POST":
        company = request.form["company"]
        position = request.form["position"]
        status = request.form["status"]
        date_applied = request.form["date_applied"]

        conn = sqlite3.connect("careerdash.db")

        conn.execute(
            "INSERT INTO applications (company, position, status, date_applied) VALUES (?, ?, ?, ?)",
            (company, position, status, date_applied)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_application(id):

    if request.method == "POST":
        company = request.form["company"]
        position = request.form["position"]
        status = request.form["status"]
        date_applied = request.form["date_applied"]

        conn = sqlite3.connect("careerdash.db")

        conn.execute(
            """
            UPDATE applications
            SET company = ?, position = ?, status = ?, date_applied = ?
            WHERE id = ?
            """,
            (company, position, status, date_applied, id)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    conn = sqlite3.connect("careerdash.db")
    conn.row_factory = sqlite3.Row

    application = conn.execute(
        "SELECT * FROM applications WHERE id = ?",
        (id,)
    ).fetchone()

    conn.close()

    return render_template("edit.html", application=application)

@app.route("/delete/<int:id>", methods=["POST"])
def delete_application(id):
    conn = sqlite3.connect("careerdash.db")

    conn.execute(
        "DELETE FROM applications WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)