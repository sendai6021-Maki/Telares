from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Control de Telar</title>
    <style>
        body { font-family: sans-serif; padding: 20px; max-width: 420px; margin: auto; background-color: #f8f9fa; }
        .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        label { display: block; margin-top: 15px; font-weight: bold; color: #333; }
        input, select, button { width: 100%; padding: 12px; margin-top: 5px; box-sizing: border-box; font-size: 16px; border-radius: 6px; border: 1px solid #ccc; }
        input[readonly] { background-color: #e9ecef; font-weight: bold; color: #495057; }
        button { background-color: #0d6efd; color: white; border: none; margin-top: 25px; font-weight: bold; cursor: pointer; }
        .success { background-color: #d1e7dd; color: #0f5132; padding: 12px; border-radius: 6px; margin-bottom: 15px; text-align: center; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Registro de Producción</h2>
        {% if guardado %}
            <div class="success">
                <strong>¡Guardado exitoso!</strong><br>
                Telar: {{ telar }} | Turno: {{ turno }} | Cantidad: {{ produccion }}
            </div>
        {% endif %}
        <form method="POST">
            <label>Telar:</label>
            <input type="text" name="telar" value="{{ telar }}" readonly required>

            <label>Turno:</label>
            <select name="turno" required>
                <option value="">Selecciona turno</option>
                <option value="1">Turno 1</option>
                <option value="2">Turno 2</option>
                <option value="3">Turno 3</option>
            </select>

            <label>Producción (Metros / Kilos):</label>
            <input type="number" step="any" name="produccion" placeholder="0.00" required>

            <button type="submit">Guardar Registro</button>
        </form>
    </div>
</body>
</html>
"""

# Lista temporal en memoria
registros = []

@app.route('/')
def home():
    return "<h3>Servidor activo. Escanea un QR de telar o entra a: <a href='/registro?telar=Fx001'>/registro?telar=Fx001</a></h3>"

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        telar = request.form.get('telar', '')
        turno = request.form.get('turno', '')
        produccion = request.form.get('produccion', '')
        registros.append({"telar": telar, "turno": turno, "produccion": produccion})
        return render_template_string(HTML_PAGE, telar=telar, turno=turno, produccion=produccion, guardado=True)

    telar_qr = request.args.get('telar', '')
    return render_template_string(HTML_PAGE, telar=telar_qr, guardado=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
