from flask import Flask
app = Flask(__name__)

@app.route('/time')
def returnTime():
    from datetime import datetime
    now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return now + "\n Shiwei He \n NetID: sh7787\n"


@app.route('/')
def hello_world():
    return returnTime()


app.run(host='0.0.0.0',
        port=8080,
        debug=True)

