from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('calc.html')


@app.route('/calculadora', methods=['POST'])
def calcular():
    valor1 = int(request.form['v1'])
    valor2 = int(request.form['v2'])
    operacao = request.form['operacao'].upper()
    if operacao == 'SOMA':
        resultado = valor1 + valor2
        return render_template('resultado.html', resultado=resultado)
    elif operacao == 'SUBTRACAO':
        resultado = valor1 - valor2
        return render_template('resultado.html', resultado=resultado)
    elif operacao == 'MULTIPLICACAO':
        resultado = valor1 * valor2
        return render_template('resultado.html', resultado=resultado)
    elif operacao == 'DIVISAO':
        if valor2 == 0:
            return '<h1>Não existe divisão por zero</h1>'
        resultado = valor1 / valor2
        return render_template('resultado.html', resultado=resultado)
    else:
        return '<h1> Operação inválida </h1>'


app.run(debug=True)
