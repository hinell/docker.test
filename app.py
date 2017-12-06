from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redishostname = "fuckingredis_blahblash"
redis = Redis(host= redishostname , db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<body style='margin: 4em auto 0 auto;max-width: 750px'>"\
           "<h1> docker docker  | HOLY CRAP </h1><br>" \
           "<h2>SOMETHING SHOULD BE WRITTEN HERE!</h2>" \
           "<h3>{name}</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<p> Accessing name {redishostname} </p>" \
           "<b>Visits:</b> {visits}" \
           "<h2>Server is running under {pyver} Python version </h2>" \
           "</body>"
    return html.format(
        redishostname=redishostname,
        name=os.getenv("NAME", "world"),
        hostname=socket.gethostname(),
        visits=visits,
        pyver=os.getenv("PYTHON_VERSION",'Error: invalid env variable!'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
