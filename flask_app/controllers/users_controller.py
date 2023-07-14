from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.users_model import User

# #add this so that you are redirected to home page
@app.route('/')
def root_redirect():
    return redirect('/users')


# /table_name/id(if needed)/actions
@app.route('/users')
def all_users():
    all_users = User.get_all()
    return render_template("users.html", all_users=all_users)


@app.route('/users/new') #route to display new dog form
def new_user():
    return render_template("new_user.html")


@app.route('/users/create', methods=['POST']) #route to process the form
def create_user():
    print(request.form)
    #a call to our dog class to create a user from our request form
    User.create(request.form)
    return redirect('/users')


@app.route('/users/<int:id>/view')
def view_one_user(id):
    data ={
        'id' : id
    }
    one_user = User.get_one(data)
    return render_template("show_user.html", one_user=one_user)


@app.route('/users/<int:id>/edit')
def edit_user_fom(id):
    data ={
        'id' : id
    }
    one_user = User.get_one(data)
    return render_template("edit_user.html", one_user=one_user)


@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'id': id
    }
    # data ={
    #     **request.form, #unpacking
    #     'id': id
    # }
    User.update(data)
    return redirect('/')


@app.route('/users/<int:id>/delete')
def delete_user(id):
    data ={
        'id' : id
    }
    User.delete(data)
    return redirect('/')