from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    attendance=None
    status=None
    skip=None
    need=None
    color="green"

    if request.method=="POST":

        total=int(request.form["total"])
        attended=int(request.form["attended"])
        missed=int(request.form["missed"])

        # YOUR FORMULA
        attendance=(attended*100)/(total-missed)

        if attendance>=75:
            status="Eligible"
            skip=math.floor((attended/0.75)-total)
            color="green"
        else:
            status="Not Eligible"
            need=math.ceil((0.75*total-attended)/0.25)
            color="red"

    return render_template(
        "index.html",
        attendance=attendance,
        status=status,
        skip=skip,
        need=need,
        color=color
    )

if __name__=="__main__":
    app.run(debug=True)