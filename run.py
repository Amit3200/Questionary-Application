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
    return render_template("login.html",value="")

@app.route("/overview/")
def overview():
    return render_template("overview.html")

@app.route("/ecological/")
def ecological():
    if "username" in session:
        cur = mysql.connection.cursor()
        cur.execute("Select * from questions where category='ecological' and subcategory='Shift'")
        records=cur.fetchall()
        questions1=[]
        for row in records:
                questions1.append(row[1])
        #print(questions1)
        mysql.connection.commit()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute("Select * from questions where category='ecological' and subcategory='New'")
        records=cur.fetchall()
        questions=[]
        for row in records:
                questions.append(row[1])
        #print(questions)
        mysql.connection.commit()
        cur.close()
        d={"allnews":questions,"new1":questions1}
        return render_template("ecological.html",**d)
    else:
        return render_template("sign-in.html")

@app.route("/economic/")
def economic():
    if "username" in session:
        cur = mysql.connection.cursor()
        cur.execute("Select * from questions where category='economic' and subcategory='Shift'")
        records=cur.fetchall()
        questions1=[]
        for row in records:
                questions1.append(row[1])
        #print(questions1)
        mysql.connection.commit()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute("Select * from questions where category='economic' and subcategory='New'")
        records=cur.fetchall()
        questions=[]
        for row in records:
                questions.append(row[1])
        #print(questions)
        mysql.connection.commit()
        cur.close()
        d={"allnews":questions,"new1":questions1}
        return render_template("economic.html",**d)
    else:
        return render_template("sign-in.html")

@app.route("/political/")
def political():
    if "username" in session:
        cur = mysql.connection.cursor()
        cur.execute("Select * from questions where category='political' and subcategory='Shift'")
        records=cur.fetchall()
        questions1=[]
        for row in records:
                questions1.append(row[1])
        #print(questions1)
        mysql.connection.commit()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute("Select * from questions where category='political' and subcategory='New'")
        records=cur.fetchall()
        questions=[]
        for row in records:
                questions.append(row[1])
        #print(questions)
        mysql.connection.commit()
        cur.close()
        d={"allnews":questions,"new1":questions1}
        return render_template("political.html",**d)
    else:
        return render_template("sign-in.html")
    
@app.route("/social/")
def social():
    if "username" in session:
        cur = mysql.connection.cursor()
        cur.execute("Select * from questions where category='social' and subcategory='Shift'")
        records=cur.fetchall()
        questions1=[]
        for row in records:
                questions1.append(row[1])
        #print(questions1)
        mysql.connection.commit()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute("Select * from questions where category='social' and subcategory='New'")
        records=cur.fetchall()
        questions=[]
        for row in records:
                questions.append(row[1])
        #print(questions)
        mysql.connection.commit()
        cur.close()
        d={"allnews":questions,"new1":questions1}
        return render_template("social.html",**d)
    else:
        return render_template("sign-in.html")

@app.route("/spiritual/")
def spiritual():
    if "username" in session:
        cur = mysql.connection.cursor()
        cur.execute("Select * from questions where category='spiritual' and subcategory='Shift'")
        records=cur.fetchall()
        questions1=[]
        for row in records:
                questions1.append(row[1])
        #print(questions1)
        mysql.connection.commit()
        cur.close()
        cur = mysql.connection.cursor()
        cur.execute("Select * from questions where category='spiritual' and subcategory='New'")
        records=cur.fetchall()
        questions=[]
        for row in records:
                questions.append(row[1])
        #print(questions)
        mysql.connection.commit()
        cur.close()
        d={"allnews":questions,"new1":questions1}
        return render_template("spiritual.html",**d)
    else:
        return render_template("sign-in.html")

@app.route("/join_us/")
def join_us():
    if "username" in session:
        return render_template("join_us.html")
    else:
        return render_template("sign-in.html")

@app.route("/study_group/")
def study_group():
    if "username" in session:
        return render_template("study_group.html")
    else:
        return render_template("sign-in.html")

@app.route("/sign-in/")
def sign_in():
    if "username" not in session:
        return render_template("sign-in.html")
    else:
        return render_template("user_dashboard.html",name=session["username"])

@app.route("/sign-up/")
def sign_up():
    if "username" not in session:
        return render_template("sign-up.html")
    else:
        return render_template("user_dashboard.html",name=session["username"])

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/privacy/")
def privacy():
    return render_template("privacy.html")

@app.route("/support/")
def support():
    return render_template("support.html")
#am
#it
#add
#32
#00
#proof


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
    if "username" not in session:
        if(request.method=="POST"):
            firstname=request.form['first-name']
            secondname=request.form['second-name']
            userid=request.form['emailid']
            pass1=request.form['passcode1']
            cur = mysql.connection.cursor()
            cur.execute("Insert into users(first_name,last_name,email_id,passcode_user) values(%s,%s,%s,%s)",(firstname,secondname,userid,pass1))
            mysql.connection.commit()
            cur.close()        
            return render_template("sign-up.html",value="Account Created Successfully, Kindly proceed with login")
    else:
        return "Logged in"

@app.route("/ecological_discuss/",methods=["POST"])
def ecological_discuss():
    if "username" in session:
        #print(session["username"])
        cur = mysql.connection.cursor()
        cur.execute("Select * from questions")
        records=cur.fetchall()
        questions=[]
        for row in records:
            questions.append(row[1])
        #print(questions)
        mysql.connection.commit()
        cur.close()
        d={"name":"Amit","subject":"Ecological","ques":"","allnews":questions}
        return render_template("question_activity_layout.html",**d)
    else:
        return render_template("sign-in.html",value="")

@app.route("/questions_discuss/",methods=["POST","GET"])
def questions_discuss():
    if "username" in session: #tobe changed
        if request.method=="POST":
            f=request.form['category']
            #print(f)
            return render_template("adding_questions.html",category=f)
    else:
        return render_template("sign-in.html",value="")

@app.route("/add_questions/",methods=["POST","GET"])
def add_questions(): #for_ecological
    if "username" in session:    
        if(request.method=="POST"):
            s="Unknown"
            if "username" in session:
                s=session["username"]
            questions_fetched=request.form['questions']
            type_sec=request.form['subtype']
            category=request.form['category']
            #print(questions_fetched,type_sec)
            cur = mysql.connection.cursor()
            #print('Insert into questions(question) values("'+questions_fetched+'")')
            cur.execute('Insert into questions(question,category,userid,subcategory) values(%s,%s,%s,%s);',(questions_fetched,category,s,type_sec))
            mysql.connection.commit()
            cur.close()
            cur1 = mysql.connection.cursor()
            #print("Select * from questions where category='"+category+"'order by qid desc")
            cur1.execute("Select * from questions where category='"+category+"' and subcategory='New' order by qid desc")
            records=cur1.fetchall()
            questions=[]
            for row in records:
                questions.append(row[1])
            #print(questions)
            cur1.close()
            cur1 = mysql.connection.cursor()
            cur1.execute("Select * from questions where category='"+category+"' and subcategory='Shift' order by qid desc")
            records=cur1.fetchall()
            questions1=[]
            for row in records:
                questions1.append(row[1])
            cur1.close()
            d={"allnews":questions,"new1":questions1}
            return render_template(category+".html",**d)
    else:
        return render_template("sign-in.html")
    
@app.route("/discussion_board/",methods=["POST"])
def discussion_board():
    if "username" in session:
        return render_template("discussion_forum.html",added_sol="")
    else:
        return render_template("sign-in.html",value="")

@app.route("/add_suggestion/",methods=["POST"])
def add_suggestion():
    if "username" in session:
        if(request.method=="POST"):
            user_suggestion=request.form['suggestion']
        return render_template("discussion_forum.html",added_sol=user_suggestion)
    else:
        return render_template("sign-in.html",value="")

#amit3200
    
@app.route("/bookmarking_work/",methods=["POST","GET"])
def bookmarking_work():
    #add the variable session
    #print("reached")
    if "username" in session:
        if request.method=="POST":
            if "bookmark" in request.form:
                s="Unknown"
                if "username" in session:
                    s=session["username"]
                bookmarked_question=request.form['data-select']
                cur1 = mysql.connection.cursor()
                cur1.execute('select * from questions where question="'+bookmarked_question+'"')
                records=cur1.fetchall()
                qid=records[0][0]
                userid=records[0][4]
                category=records[0][3]
                #print(records)
                cur1.close()
                #print(bookmarked_question,qid,userid,category)
                cur = mysql.connection.cursor()
                cur.execute('Insert into bookmarked(question,userid,qid,category) values(%s,%s,%s,%s)',(bookmarked_question,s,qid,category))
                mysql.connection.commit()
                cur.close()
                return render_template("fav_inter.html",value=bookmarked_question)
            if "flag" in request.form:
                #print("flagged")
                s="Unknown"
                if "username" in session:
                    s=session["username"]
                if request.method=="POST":
                    flag_question=request.form['data-select']
                    cur1 = mysql.connection.cursor()
                    cur1.execute('select * from questions where question="'+flag_question+'"')
                    records=cur1.fetchall()
                    qid=records[0][0]
                    userid=records[0][4]
                    category=records[0][3]
                    #print(records)
                    cur1.close()
                    #print(flag_question,qid,userid,category)
                    cur = mysql.connection.cursor()
                    cur.execute('Insert into flagged(question,userid,qid,category) values(%s,%s,%s,%s)',(flag_question,s,qid,category))
                    mysql.connection.commit()
                    cur.close()
                    return render_template("flag_inter.html",value=flag_question)
                return "Error"
    else:
        return render_template("sign-in.html",value="")
    
app.run()
