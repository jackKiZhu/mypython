from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "my flask web"

@app.route("/user")
def user_info():
    return "username:123, userpassword:321"


if __name__ == "__main__":
    app.run()
    

