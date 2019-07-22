from flask import Flask,render_template,request
import os

app = Flask(__name__)


@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:

        if request.form.get('minute'):
            # print(type(request.form.get('minute')))
            time  =  str(int(request.form.get('minute')) * 60)
            str1 = 'shutdown -s -t %s' %time
            os.system(str1)
            print(str1)
            status = "%s分钟后关机" %time


        if request.form.get('shutdown'):
            str2 = 'shutdown -a'
            os.system(str2)
            print(str2)
            status = "已取消关机"

        return render_template("index.html",status=status)

if __name__ == '__main__':
    app.run()