from flask import Flask, request
from dynamo.dynamo import Dynamo
import plyvel
db = plyvel.DB('/tmp/testdb/', create_if_missing=True)
db.put(b"1", b"2")

print(db.get(b"1"))
app = Flask(__name__)
dynamo = Dynamo()

@app.route('/')
def index():
  return 'Server Works!'


@app.route("/get")
def get():
  key = request.args.get("key")
  return dynamo.get(key)