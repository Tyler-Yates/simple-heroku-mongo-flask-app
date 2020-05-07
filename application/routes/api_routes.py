from flask import request, jsonify, redirect
from flask_accept import accept

from application import app, dao
from application.data.dao import ID_FIELD


@app.route("/documents")
@accept('application/json')
def documents_api_page():
    documents = dao.get_documents()
    return jsonify(list(documents))


@app.route("/documents/<document_id>")
@accept('application/json')
def document_api_page(document_id):
    document = dao.get_document(document_id)
    if document:
        return jsonify(document)
    else:
        return _as_json("Document with ID {document_id} not found!"), 404


@app.route("/documents", methods=["POST"])
@accept('application/json')
def add_document_api_json():
    json_data = None
    if request.json:
        json_data = request.json.get("document_text", None)

    if json_data:
        inserted_document = dao.insert_document(json_data)
        return jsonify({ID_FIELD: str(inserted_document.inserted_id)}), 201
    else:
        return _as_json("Document must have text!"), 400


@app.route("/documents", methods=["POST"])
@add_document_api_json.support('application/x-www-form-urlencoded', 'multipart/form-data', 'text/html')
def add_document_api_form():
    form_data = None
    if request.form:
        form_data = request.form.get("document_text", None)

    if form_data:
        inserted_document = dao.insert_document(form_data)
        return redirect(f"/documents/{inserted_document.inserted_id}", code=302)
    else:
        return "Document must have text!", 400


def _as_json(message: str):
    return jsonify({"message": message})
