from flask import Flask, request, abort

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def feed():
    expected_keys = ['date', 'hour', 'minute', 'ticker', 'op', 'hp', 'lp', 'cp', 'volume', 'amount']
    actual_keys = list(request.args.keys())
    if sorted(expected_keys) != sorted(actual_keys):
        abort(400)
    return request.args


if __name__ == '__main__':
    app.run(debug=True)