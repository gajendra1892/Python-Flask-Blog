import math
import os.path

from flask import  Flask, render_template,request, session, redirect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import  datetime
import  json
from flask_mail import Mail
from werkzeug.utils import  secure_filename


with open('config.json','r') as file:
    params =json.load(file)["params"]

local_server = params['local_server']

# create the app
app = Flask(__name__)
app.secret_key ="super-secret-key"
app.config["UPLOAD_FOLDER"] =params["upload_location"]
# Not working , block by google
app.config.update(
    MAIL_SERVER ="smtp.gmail.com",
    MAIL_PORT="465",
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params["gmail_user"],
    MAIL_PASSWORD=params["gmail_password"]
)
mail =Mail(app)
if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] =params['prod_uri']

# configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:12345@localhost/flask'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqlconnector://root:12345@localhost/codingthunder'

db = SQLAlchemy(app)


class Contacts(db.Model):
    # sno ,name,email, phone_num,msg,date
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable =False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    phone_num= db.Column(db.Integer, unique=True, nullable=False)
    msg= db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(20), nullable=True)


class Posts(db.Model):
    # sno ,name,email, phone_num,msg,date
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable =False)
    slug = db.Column(db.String(21), nullable=False)
    content= db.Column(db.String(121), nullable=False)
    date = db.Column(db.String(20), nullable=True)
    img_file = db.Column(db.String(20), nullable=True)
    tagline = db.Column(db.String(30), nullable=True)

@app.route("/dashboard", methods=['GET','POST'])
def dashboard():
    if 'user' in session and session['user'] ==params['admin_user']:
        posts = Posts.query.filter_by().all()
        return render_template("dashboard.html",params=params,posts=posts)

    if request.method =='POST':
        user_name =request.form.get('uname')
        user_pass = request.form.get('password')
        if user_name == params['admin_user'] and user_pass == params['admin_pass']:
            session["user"] = user_name
            posts = Posts.query.filter_by().all()
            return render_template("dashboard.html",params=params,posts=posts)

    else:
        return render_template("signin.html", params=params)





@app.route("/")
def home():
    posts =Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['number_of_posts']))

    page =request.args.get('page')
    if not str(page).isnumeric():
        page =1
    page =int(page)
    posts =posts[(page-1) * int(params['number_of_posts']) : (page-1) * int(params['number_of_posts']) + int(params['number_of_posts'])]

    if page == 1:
        prev ="#"
        next ="/?page="+str(page+1)
    elif page == last:
        prev ="/?page="+str(page-1)
        next ="#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)

    # posts= Posts.query.filter_by().all()[0:params['number_of_posts']]
    return render_template("index.html", params=params, posts=posts, prev=prev, next= next)

@app.route("/about")
def about():
    return render_template("about.html",params=params)

@app.route("/contact", methods =['GET','POST'])
def contact():
    print("submitted")
    if request.method == 'POST':
        print("submitted post")
        # Add entry to Databse
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message= request.form.get('message')

        entry =Contacts(name=name, email=email, phone_num=phone, msg=message, date= datetime.now()  )
        db.session.add(entry)
        db.session.commit()

        # mail.send_message('New message from BLOG',
        #                   sender=email,
        #                   recipients=[params["gmail_user"]],
        #                   body= message +"\n"+ phone
        #                   )

    return render_template("contact.html",params=params)

@app.route("/post/<string:post_slug>",methods=["GET"])
def post_route(post_slug):
    post= Posts.query.filter_by(slug=post_slug).first()
    return render_template("post.html",params=params,post=post)


@app.route("/edit/<string:sno>", methods=['GET','POST'])
def edit(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method == 'POST':
            title = request.form.get('title')
            tagline= request.form.get('tagline')
            slug= request.form.get('slug')
            content= request.form.get('content')
            imgFile= request.form.get('imgFile')
            date= datetime.now()

            if sno =="0":
                post = Posts(title=title,slug=slug,tagline=tagline,content=content,img_file=imgFile,date=date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = title
                post.slug =slug
                post.content = content
                post.tagline = tagline
                post.img_file =imgFile
                post.date =date
                db.session.commit()
                return  redirect("/edit/"+sno)

        post = Posts.query.filter_by(sno=sno).first()
        return render_template("edit.html",params=params,post=post)



@app.route("/delete/<string:sno>", methods=['GET','POST'])
def delete(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return  redirect("/dashboard")


@app.route("/uploader", methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        file = request.files["file1"]
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(file.filename)))
        return  "Uploaded Successfully"

@app.route("/logout")
def logout():
    session.pop('user')
    return  redirect('/dashboard')

app.run(debug=True)