from flask import request
import builtin_dynamics


def index(user=None):
    return {}


def api_test():
    return {"this_is": "SPARTAAAAA"}


pub_sources = {
    "index": index,
    "create_account": builtin_dynamics.create_account
}
priv_sources = {"index": index}

api_sources = {"test": api_test}
