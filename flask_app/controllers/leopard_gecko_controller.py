from flask import render_template, redirect, request, session

from flask_app import app
from flask_app.models.leopard_gecko_model import LeopardGecko
from flask_app.models.user_model import User



@app.route('/new/leo')
def new_leo():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template("new_leo.html", user=User.get_one(data))


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    user=User.get_one(data)

    return render_template('dashboard.html',user=user, all_leos=LeopardGecko.get_all())



@app.route('/create/leo',methods=['POST'])
def create_leo():
    if not LeopardGecko.validate(request.form):
        return redirect('/new/leo')
    data = {
        "genetics": request.form["genetics"],
        "sex": request.form["sex"],        
        "hatch_date": request.form["hatch_date"],
        "user_id": session["user_id"],
        "gecko_id": request.form["gecko_id"],
        "breeder": request.form["breeder"],
        "weight": request.form["weight"],
        "dam": request.form["dam"],
        "sire": request.form["sire"],
        "location": request.form["location"],
        "image": request.form["image"]
    }
    LeopardGecko.save(data)
    return redirect('/dashboard')


@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    user_data ={
        "id":session["user_id"]
    }
    context ={
        'leo': LeopardGecko.get_one({'id': id})
    }
    edit=LeopardGecko.get_one(user_data)                              #WHY DON'T YOU PREPOPULATEEEEEEEE?!?!#
    print(edit)
    return render_template('edit_leo.html', edit=edit,user=User.get_one(user_data), **context)
    

@app.route('/update/<int:id>', methods=['post'])
def update(id):                                            
    if 'user_id' not in session:
        return redirect('/logout')
    if not LeopardGecko.validate(request.form):
        return redirect(f'/edit/{id}')
    data = {
        "id":id,
        "genetics": request.form["genetics"],
        "sex": request.form["sex"],
        "hatch_date": request.form["hatch_date"],
        "gecko_id": request.form["gecko_id"],
        "breeder": request.form["breeder"],
        "weight": request.form["weight"],
        "dam": request.form["dam"],
        "sire": request.form["sire"],
        "location": request.form["location"],
        "image": request.form["image"]
    }
    LeopardGecko.update(data)
    return redirect('/dashboard')



@app.route('/display/<int:id>')
def display_leo(id):
    context= {
        'user': User.get_one({'id': session['user_id']}),
        'leo': LeopardGecko.get_one({'id': id})
    }
    return render_template('display.html', **context)

@app.route('/delete/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    LeopardGecko.destroy(data)
    return redirect('/dashboard')