from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/callback', methods=['POST'])
def callback():
    raw = request.stream.read()
    row = json.loads(raw)

    print(row)

    return '{"code":200, "msg":"ok"}'

if __name__ == '__main__':
    app.run(port=9999, debug=True)