from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/login_registration/",methods=["POST"])
def login_registration():
    #show all the questions here
    #book mark schema
    return render_template("login.html",value="")

@app.route("/register_registration/",methods=["POST","GET"])
def register_registration():
    return render_template("register.html",value="")


@app.route("/login/",methods=["POST","GET"])
def login():
    if(request.method=="POST"):
            username=request.form['emailid']
            passcode=request.form['passcode']
            if(username=="tusharamit@yahoo.com" and passcode=="12345"): #to be changed
                return render_template("user_dashboard.html",name="Amit")
            else:
                return "error" # to be addded

@app.route("/register/",methods=["POST","GET"])
def register():
    if(request.method=="POST"):
        username=request.form['name']
        userid=request.form['emailid']
        pass1=request.form['passcode1']
        pass2=request.form['passcode2']
        if pass1==pass2:
            print(username,userid,pass1,pass2)#delete after verification
            return render_template("login.html",value="Account Created Successfully, Kindly proceed with login")
        else:
            return render_template("register.html",value="Account Creation Failed")

@app.route("/ecological_discuss/",methods=["POST"])
def ecological_discuss():
    #show all the questions here
    #book mark schema
    #session check 
    d={"name":"Amit","subject":"Ecological","ques":""}
    return render_template("question_activity_layout.html",**d)

@app.route("/questions_discuss/",methods=["POST","GET"])
def questions_discuss():
    return render_template("adding_questions.html")

@app.route("/add_questions/",methods=["POST","GET"])
def add_questions():
    if(request.method=="POST"):
        questions_fetched=request.form['questions']
        #add session checking
        print(questions_fetched) #add in the database with the timestamp and other things
        d={"name":"Amit","subject":"Ecological","ques":questions_fetched}
        return render_template("question_activity_layout.html",**d)
        
        

app.run()
