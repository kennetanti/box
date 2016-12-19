from flask import request
import builtin_dynamics

def index(user=None):
  return {}
pub_sources = {		"index": index,
			"create_account": builtin_dynamics.create_account}
priv_sources = {	"index": index}

api_sources = {		"test": builtin_dynamics.api_test}
