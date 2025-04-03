from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCriarConta

app = Flask(__name__)

lista_usuarios = ['Gabriel', 'Lira', 'Alon','Alessandra', 'Amanda']

app.config['SECRET_KEY'] = '59f6ad173924fe036a481520f95a08b7'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contato")
def contato():
     return render_template('contato.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        print("✅ Login realizado com sucesso!")  # Debug
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}') #Verificar se logou e informar o email ao logar no botão
        return redirect(url_for('home')) #redireciona para pagina homepage

    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        print("✅ Conta criada com sucesso!")  # Debug
        flash(f'Conta criada com sucesso no e-mail: {form_criarconta.email.data}') #conta criada com sucesso botão criar conta
        return redirect(url_for('home')) #redireciona para homepage

    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

if __name__ == '__main__':
    app.run(debug=True) # Esse debug=True faz com que ao editar ja apareça na tela a alteração