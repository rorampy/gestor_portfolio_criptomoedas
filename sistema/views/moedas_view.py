from flask import render_template
from sistema import app


@app.route('/moedas')
def moedas_listar():
    return 'Front em desenvolvimento'


@app.route('/moeda/cadastrar')
def moeda_cadastrar():
    return 'Front em desenvolvimento'


@app.route('/moeda/editar/<int:id>')
def moeda_editar(id):
    return 'Front em desenvolvimento'


@app.route('/moeda/excluir/<int:id>')
def moeda_excluir(id):
    return 'Front em desenvolvimento'