from flask import Flask,render_template,request,session
from flask_mysqldb import MySQL
app=Flask(__name__)
app.secret_key = "ny91em6BIm1QmjbTO5skq2YbzJXntqJ5"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'amit'
app.config['MYSQL_DB'] = 'test_flask'
mysql = MySQL(app)


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
        cur = mysql.connection.cursor()
        cur.execute("select first_name,email_id,passcode_user from users where email_id=%s and passcode_user=%s;",(username,passcode))
        records=cur.fetchall()
        if(len(records)==0):
            return "Error, No Account Exists"
        else:
            if(username==records[0][1] and passcode==records[0][2]):
                session["username"] = username
                return render_template("user_dashboard.html",name=records[0][0])
    else:
        return "error" # to be addded

@app.route("/register/",methods=["POST","GET"])
def register():
    if(request.method=="POST"):
        firstname=request.form['first-name']
        secondname=request.form['second-name']
        userid=request.form['emailid']
        pass1=request.form['passcode1']
        cur = mysql.connection.cursor()
        cur.execute("Insert into users(first_name,last_name,email_id,passcode_user) values(%s,%s,%s,%s)",(firstname,secondname,userid,pass1))
        mysql.connection.commit()
        cur.close()        
        print(firstname,secondname,userid,pass1)#delete after verification
        return render_template("login.html",value="Account Created Successfully, Kindly proceed with login")

@app.route("/ecological_discuss/",methods=["POST"])
def ecological_discuss():
    #show all the questions here
    #book mark schema
    #session check
    if "username" in session:
        cur = mysql.connection.cursor()
        cur.execute("Select * from questions")
        records=cur.fetchall()
        questions=[]
        for row in records:
            questions.append(row[1])
        print(questions)
        mysql.connection.commit()
        cur.close()
        d={"name":"Amit","subject":"Ecological","ques":"","allnews":questions}
        return render_template("question_activity_layout.html",**d)
    else:
        return render_template("login.html",value="")

@app.route("/questions_discuss/",methods=["POST","GET"])
def questions_discuss():
    if "username" in session:
        return render_template("adding_questions.html")
    else:
        return render_template("login.html",value="")

@app.route("/add_questions/",methods=["POST","GET"])
def add_questions():
    if "username" in session:    
        if(request.method=="POST"):
            questions_fetched=request.form['questions']
            #add session checking
            print(questions_fetched) #add in the database with the timestamp and other things
            cur = mysql.connection.cursor()
            #print('Insert into questions(question) values("'+questions_fetched+'")')
            cur.execute('Insert into questions(question) values("'+questions_fetched+'")')
            mysql.connection.commit()
            cur.close()
            cur1 = mysql.connection.cursor()
            cur1.execute("Select * from questions")
            records=cur1.fetchall()
            questions=[]
            for row in records:
                questions.append(row[1])
            print(questions)
            cur1.close()
            d={"name":"Amit","subject":"Ecological","ques":questions_fetched,"allnews":questions}
            return render_template("question_activity_layout.html",**d)
    else:
        return render_template("login.html",value="")
        

@app.route("/discussion_board/",methods=["POST"])
def discussion_board():
    if "username" in session:
        return render_template("discussion_forum.html",added_sol="")
    else:
        return render_template("login.html",value="")

@app.route("/add_suggestion/",methods=["POST"])
def add_suggestion():
    if "username" in session:
        if(request.method=="POST"):
            user_suggestion=request.form['suggestion']
        return render_template("discussion_forum.html",added_sol=user_suggestion)
    else:
        return render_template("login.html",value="")

@app.route("/bookmarking_work/",methods=["POST","GET"])
def bookmarking_work():
    #add the variable session
    print("reached")
    if "username" in session:
        if request.method=="POST":
            if "bookmark" in request.form:
                bookmarked_question=request.form['data-select']
                cur1 = mysql.connection.cursor()
                cur1.execute('select * from questions where question="'+bookmarked_question+'"')
                records=cur1.fetchall()
                qid=records[0][0]
                userid=records[0][4]
                category=records[0][3]
                print(records)
                cur1.close()
                print(bookmarked_question,qid,userid,category)
                cur = mysql.connection.cursor()
                cur.execute('Insert into bookmarked(question,userid,qid,category) values(%s,%s,%s,%s)',(bookmarked_question,userid,qid,category))
                mysql.connection.commit()
                cur.close()
                return bookmarked_question
            if "flag" in request.form:
                print("flagged")
                if request.method=="POST":
                    flag_question=request.form['data-select']
                    cur1 = mysql.connection.cursor()
                    cur1.execute('select * from questions where question="'+flag_question+'"')
                    records=cur1.fetchall()
                    qid=records[0][0]
                    userid=records[0][4]
                    category=records[0][3]
                    print(records)
                    cur1.close()
                    print(flag_question,qid,userid,category)
                    cur = mysql.connection.cursor()
                    cur.execute('Insert into flagged(question,userid,qid,category) values(%s,%s,%s,%s)',(flag_question,userid,qid,category))
                    mysql.connection.commit()
                    cur.close()
                    print("marked")
                    print(flag_question)
                return "flagged"
    else:
        return render_template("login.html",value="")
    
app.run()
