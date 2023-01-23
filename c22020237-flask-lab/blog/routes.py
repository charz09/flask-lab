from flask import render_template, url_for, request, redirect, flash
from blog import app, db
from blog.models import User, Post
from blog.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, current_user

@app.route("/")

@app.route("/home")
def home():
  posts=Post.query.all()
  return render_template('home.html',posts=posts)

@app.route("/about")
def about():
  return render_template('about.html', title='About')

@app.route("/portfolio")
def portfolio():
  return render_template('portfolio.html', title='Portfolio')

@app.route("/post/<int:post_id>")
def post(post_id):
  post=Post.query.get_or_404(post_id)
  return render_template('post.html',title=post.title,post=post)

@app.route("/register",methods=['GET','POST'])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email_address=form.email.data, password=form.password1.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(f"Registration successful! You are logged in as {user.username}", category='successfully')
        return redirect(url_for('register'))

    if form.errors != {}: #If there are not error from validations
        for err_msg in form.errors.values():
            flash(f"There are error with creating a user: {err_msg}", category='danger')

    return render_template('register.html',title='Register',form=form)

@app.route("/registered")
def registered():
  return render_template('registered.html', title='Thanks!')

@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      flash('You\'ve successfully logged in,'+' '+ current_user.username +'!')
      return redirect(url_for('home'))
    flash('Invalid username or password.')
  return render_template('login.html',title='Login', form=form)

@app.route("/logout")
def logout():
  logout_user()
  flash('You\'re now logged out. Thanks for your visit!')
  return redirect(url_for('home'))





