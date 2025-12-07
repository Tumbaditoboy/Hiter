from flask import Flask, render_template, request, jsonify

from entities.peleas import Peleas, get_all as get_all_peleas
from entities.peleadores import Peleadores, get_all as get_all_peleadores

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/peleas', methods=['GET'])
def peleas():
    peleas_list = get_all_peleas() 
    return render_template('peleas.html', peleas=peleas_list)

@app.route('/peleas', methods=['POST'])
def save_peleas():
    data = request.get_json()
    p = Peleas(peleador1_id = data['peleador1_id'], peleador2_id = data['peleador2_id'], fecha= data['fecha'], ubicacion= data['ubicacion'], estado= data['estado'], ganador= data['ganador'])
    id = p.save()
    success = id is not None 
    return jsonify(success), 201

@app.route('/peleas/<int:id>', methods=['PUT'])
def update_peleas(id):
    data = request.get_json()
    peleador1_id = data.get('peleador1_id')
    peleador2_id = data.get('peleador2_id')
    fecha = data.get('fecha')
    ubicacion = data.get('ubicacion')
    estado = data.get('estado')
    ganador = data.get('ganador')

    p = Peleas(id=id)
    p.update(peleador1_id, peleador2_id, fecha, ubicacion, estado, ganador)
    success = p.update(peleador1_id, peleador2_id, fecha, ubicacion, estado, ganador)
    
    return jsonify(success = success), (200 if success else 404)

@app.route('/peleas/<int:id>' , methods=['DELETE'])
def delete_peleas(id):
    p = Peleas(id=id)
    success = p.delete()
    return jsonify(success = success), (200 if success else 404)

#Aki van ahora los del customer 
@app.route('/peleadores', methods=['GET'])
def peleadores():
    peleadores_list = get_all_peleadores() 
    return render_template('peleadores.html', peleadores=peleadores_list)

@app.route('/peleadores', methods=['POST'])
def save_peleadores():
    data = request.get_json()
    p = Peleadores(nombre= data['nombre'], alias= data['alias'], edad= data['edad'], ubicacion= data['ubicacion'], nivel_pelea= data['nivel_pelea'], foto= data['foto'], descripcion= data['descripcion'])
    id = p.save()
    success = id is not None 
    return jsonify(success), 201

@app.route('/peleadores/<int:id>', methods=['PUT'])
def update_peleadores(id):
    data = request.get_json()
    nombre = data.get('nombre')
    alias = data.get('alias')
    edad = data.get('edad')
    ubicacion = data.get('ubicacion')
    nivel_pelea = data.get('nivel_pelea')
    foto = data.get('foto')
    descripcion = data.get('descripcion')

    p = Peleadores(id=id)
    p.update(nombre, alias, edad, ubicacion, nivel_pelea, foto, descripcion)
    success = p.update(nombre, alias, edad, ubicacion, nivel_pelea, foto, descripcion)
    
    return jsonify(success = success), (200 if success else 404)

@app.route('/peleadores/<int:id>' , methods=['DELETE'])
def delete_peleadores(id):
    p = Peleadores(id=id)
    success = p.delete()
    return jsonify(success = success), (200 if success else 404)

if __name__ == '__main__':
    app.run()