from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/python_github"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=True)
    user_password = db.Column(db.String(32))

    def __repr__(self):
        return "用户id:%s 用户名:%s" % (self.id, self.user_name)


@app.route("/", methods=["post", "get"])
def index():
    index_meg = ""
    if request.method == "POST":
        user_name = request.form.get("user_name", "")
        user_pwd = request.form.get("user_pwd", "")
        if not all([user_name, user_pwd]):
            index_meg = "请正确输入信息"
        else:
            user_name_is_exits = User.query.filter(User.user_name == user_name).first()
            if user_name_is_exits:
                index_meg = "用户名已存在"
            else:
                user_obj = User(user_name=user_name, user_password=user_pwd)
                db.session.add(user_obj)
                db.session.commit()
                index_meg = "注册成功"

    return render_template("index.html", index_meg=index_meg)


# @app.route("/login/<user_info>")
# def user_login(user_info):
#     return user_info



if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    app.run(debug=True)
    

