from flask import Flask, Response, request
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(request.args)
    key = request.args.get('key')
    return Response("<h1>Flask</h1><p>You visited: /%s</p><p>key=%s</p>" % (path,key), mimetype="text/html")

    
if __name__ == "__main__":
    app.run(debug = True)
