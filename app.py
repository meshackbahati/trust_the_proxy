from flask import Flask, request, abort

app = Flask(__name__)

FLAG = "G24SEC{proxy_trust_is_not_security}"

@app.route("/")
def index():
    return """
    <h1>Internal Dashboard</h1>
    <p>Access to /admin is restricted to localhost only.</p>
    """

@app.route("/admin")
def admin():
    # Vulnerable logic: trusting X-Forwarded-For
    forwarded = request.headers.get("X-Forwarded-For", "")

    if forwarded == "127.0.0.1":
        return f"<h2>Admin Panel</h2><p>Flag: {FLAG}</p>"
    else:
        abort(403)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
