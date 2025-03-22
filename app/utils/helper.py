from flask import session, redirect, current_app

def protectedPage():
  if 'logged_in' not in session or session['logged_in'] == False:
    return redirect("/login")

def is_logged():  
  return session['logged_in'] == True


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']
