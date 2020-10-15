import pathlib
import flask
import git

import message_handler
import vk_io

app = flask.Flask(__name__)


@app.route("/rest", methods=["POST"])
def processing():
    data = flask.json.loads(flask.request.data)
    if "type" in data.keys() and data["type"] == "confirmation":
        return vk_io.confirmation_token
    else:
        message_handler.handle(data)
        return "ok"


@app.route("/webhook", methods=["POST"])
def webhook():
    repo = git.Repo(pathlib.Path().absolute())
    origin = repo.remotes.origin
    repo.create_head("master", origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    origin.pull()
    return "", 200
