from flask import Flask, render_template, redirect
app = Flask(__name__)

#@app.route("/js/<path:path>")
#def js(path):
#    print "redirecting to :"+path
#    return redirect("/static/js/"+path)


@app.route("/<path:path>")
def js(path):
    print "redirecting to :"+path
    return redirect("/static/"+path)


@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == '__main__':
        app.run()




