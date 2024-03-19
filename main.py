from flask import Flask, render_template
from flask_socketio import SocketIO, send

# criando app
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)
    
# primeira pagina ou primeira rota
@app.route("/") # decorator
def homepage():
    return render_template("homepage.html")

# roda app
socketio.run(app, host='localhost')