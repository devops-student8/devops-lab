from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Привет от Flask из контейнера!v2</h1>\n"

@app.route("/healthz
")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
