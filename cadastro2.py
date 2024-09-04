from flask import render_template, redirect, request, url_for
from app.init import app, db
from app.models import User
import re

@app.route('/')
def principal():
    return render_template('index.html')


@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
 if request.method == 'POST':
  def emailc(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None
 
  nome = request.form['nome']
  email = request.form['email']
  emailco = request.form['emailc']
  senha = request.form['senha']
  senhac= request.form['senhac']

  confir= len(senha) and len(senhac)
  confir2= len(nome)

  if confir <=10 and confir >=4 and senha==senhac and confir2<20 and confir2>0 and email==emailco and emailc(email) and nome and email and senha:
    user = User(nome, email, senha)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('principal'))
 
 return render_template('cadastro.html')

app.run(debug=True)
