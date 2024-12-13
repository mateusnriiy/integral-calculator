from flask import Flask, request, jsonify, render_template
import math
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

app = Flask(__name__)

# Função para cálculo da integral
def riemann(function, lim_i, lim_s, sub, point):
    deltax = (lim_s - lim_i) / sub
    result = 0

    heights = []  # Para armazenar as alturas dos retângulos
    x_positions = []  # Para armazenar as posições dos retângulos

    for i in range(sub):
        if point == 1:  # Baseado no limite inferior
            x_i = lim_i + i * deltax
        elif point == 2:  # Baseado no limite superior
            x_i = lim_i + (i + 1) * deltax
        else:  # Baseado no ponto médio
            x_i = lim_i + i * deltax
            x_i += deltax / 2

        if function == 1:  # Função X²
            f_de_x = x_i ** 2
        else:  # Função sen(X)
            f_de_x = math.sin(x_i)

        result += f_de_x * deltax

        heights.append(f_de_x)  # Adiciona a altura do retângulo
        x_positions.append(x_i - deltax / 2 if point != 2 else x_i)

    return result, x_positions, heights

# Função para plotar o gráfico
def plot_graph(function, a, b, x_positions, heights, deltax):
    x = np.linspace(a, b, 500)
    if function == 1:
        y = x ** 2
    else:
        y = np.sin(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="Função", color="blue")
    plt.bar(x_positions, heights, width=deltax, color="lightblue", edgecolor="blue", alpha=0.7, align='edge', label="Retângulos")
    plt.title("Gráfico da Integral", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("f(x)", fontsize=12)
    plt.axhline(0, color='black', linewidth=0.8, linestyle="--")
    plt.axvline(0, color='black', linewidth=0.8, linestyle="--")
    plt.legend()
    plt.grid(alpha=0.3)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()

    return img_base64

# Rotas do Flask
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        function = int(request.form['function'])
        a = float(request.form['lower'])
        b = float(request.form['upper'])
        n = int(request.form['subintervals'])
        point = int(request.form['point'])

        if a == b or n <= 0:
            return jsonify({'error': 'Verifique os limites e o número de subintervalos.'})

        deltax = (b - a) / n
        integral, x_positions, heights = riemann(function, a, b, n, point)
        graph = plot_graph(function, a, b, x_positions, heights, deltax)

        return jsonify({'integral': integral, 'graph': graph})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
