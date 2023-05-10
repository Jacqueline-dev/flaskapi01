from flask import Flask

app = Flask(__name__)

# Pegando parâmetro através da URI
@app.route("/<int:numero>", methods=['GET', 'POST'])
def ola(numero):
    return 'Olá mundo. {}'.format(numero)


if __name__ == '__main__':
    app.run(debug=True)
