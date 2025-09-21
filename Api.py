from flask import Flask, request, jsonify, make_response, render_template
import main
app = Flask(__name__)

@app.route("/check", methods=["POST"])
def check_password():
    """API endpoint to check strength and get strong password."""
    data = request.get_json()
    if not data or "password" not in data:
        return jsonify({"error": "Password is required"}), 400

    user_pw = data["password"]
    strength = main.Strengthchecker(user_pw)

    strong_pw = main.Generate_password(user_pw)
    result ={
        "strength": strength,
        "secure_password": strong_pw
    }
    response = make_response(jsonify(result))
    response.headers["Cache-Control"]= "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["pragma"] = "no-cache"
    return response

@app.route("/")
def serve_frontend():
    return render_template("main.html")
if __name__ == "__main__":
    app.run(debug=True)
