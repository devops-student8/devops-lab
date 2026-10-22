from flask import Flask
import os
import psycopg2

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        dbname=os.getenv("DB_NAME", "myapp"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "secret")
    )

@app.route("/")
def hello():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS visits (id serial PRIMARY KEY, ts timestamp)")
    cur.execute("INSERT INTO visits (ts) VALUES (NOW())")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM visits")
    count = cur.fetchone()[0]
    return f"<h1>Привет! Ты {count}-й посетитель</h1>"

@app.route("/health")
def health():
    return {"status": "ok"}
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
