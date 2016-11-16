from flask import request

def index():
  return {"slogan": request.args.get("slogan")}
pub_sources = {	"index": index}
priv_sources = {	"index": index}
