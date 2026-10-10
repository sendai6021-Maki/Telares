from flask import Flask, request, render_template

app = Flask(__name__)

# Lista temporal para guardar los registros
registros = []

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        telar = request.form.get('telar')
        turno = request.form.get('turno')
        produccion = request.form.get('produccion')
        
        registros.append({"telar": telar, "turno": turno, "produccion": produccion})
        return f"<h3>Guardado con éxito: Telar {telar} | Turno {turno} | Producción: {produccion}</h3><br><a href='/registro?telar={telar}'>Volver</a>"

    # Captura el telar enviado desde el QR (?telar=Fx001)
    telar_qr = request.args.get('telar', '')
    return render_template('registro.html', telar=telar_qr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
