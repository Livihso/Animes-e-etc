from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('cadastro.html')

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == "Lívia" and senha == "quack":
    print("Login realizado com sucesso")
else:
  print("Acesso Negado")

app.run(debug=True)