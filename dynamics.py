from flask import request
import builtin_dynamics

def index():
  return {}
pub_sources = {	"index": index}
priv_sources = {	"index": index,
			"create_account": builtin_dynamics.create_account}
