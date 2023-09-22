from flask import Flask, render_template
from imprimir_ticket import imprimir_ticket

app = Flask(__name__)

# Configuración para servir archivos estáticos desde la carpeta 'static'
app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/imprimir_ticket', methods=['POST'])
def imprimir():
    imprimir_ticket()  # Llama a la función para imprimir el ticket
    return 'Ticket impreso con éxito'

if __name__ == '__main__':
    app.run()