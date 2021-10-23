from flask import Flask,render_template,request,send_from_directory
app=Flask(__name__,template_folder='template')
@app.route("/",defaults={'filename':'file1.txt'})
@app.route("/<filename>")
def OpenFile(filename):
    start=request.args.get('start',default=0,type=int)
    end=request.args.get('end',default=":",type=int)
    try:
      if(filename=="file4.txt"):
        if end !=":":
          with open(filename,'r',encoding="utf-16le",errors="ignore") as f:
            contents=f.readlines()
            contents=contents[start:end+1]
            str1=" "
            ltext=str1.join(contents)
            return render_template('index.html',contents=ltext)
        else:
          with open(filename,'r',encoding="utf-16le",errors="ignore") as f:
            contents=f.readlines()
            contents=contents[start:]
            str1=" "
            ltext=str1.join(contents)
            return render_template('index.html',contents=ltext)
      else:
        if end !=":":
          with open(filename) as f:
            contents=f.readlines()
            contents=contents[start:end+1]
            str1=" "
            ltext=str1.join(contents)
            return render_template('index.html',contents=ltext)
        else:
          with open(filename) as f:
            contents=f.readlines()
            contents=contents[start:]
            str1=" "
            ltext=str1.join(contents)
            return render_template('index.html',contents=ltext)
    except FileNotFoundError:
      return render_template('index.html',contents="File Not Found Please Enter correct File Name")


@app.errorhandler(404)
def PageNotfound(e):
  return render_template('index.html',contents=e)
@app.errorhandler(500)
def PageNotfound(e):
  return render_template('index.html',contents=e)
      
    
      
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='images/icon.ico')
        
if(__name__=="__main__"):
    app.run(debug=True)

