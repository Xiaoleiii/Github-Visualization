from flask import Flask, render_template, request, jsonify
from controller import searchUser, searchRepoByUser
app = Flask(__name__)


# GET - Home Page
@app.route('/', methods=["GET"])
def home():  # put application's code here
    return render_template("index.html")


# POST - fetch user by Name
@app.route('/api/user', methods=["POST"])
def fetchUserByName():
    users = searchUser(request.json["name"])
    if users:
        return jsonify({"status": 1, "data": users, "type": "success"})
    return jsonify({"status": 0, "msg": "Not User Found", "type": "danger"})


# POST - fetch stats  by username
@app.route('/api/user/stats', methods=["POST"])
def fetchReposByName():
    commits, languages_dict, stars_list, topics_list = searchRepoByUser(request.json["name"])
    if len(commits) > 0:
        return jsonify({"status": 1, "commits": commits, "languages": languages_dict, "stars": stars_list,
                        "topics": topics_list, "type": "success"})
    return jsonify({"status": 0, "msg": "Not User Found", "type": "danger"})


if __name__ == '__main__':
    app.run(debug=True)
