from datetime import timezone

from flask import render_template, redirect
from flask_accept import accept

from application import app, dao
from application.api_routes import document_api_page, documents_api_page
from application.models import TTL_SECONDS


@app.route("/")
def homepage():
    return "<a href='/documents'>Documents</a>"


@documents_api_page.support("text/html")
def documents_page():
    documents = dao.get_documents()
    return render_template("documents.html", documents=documents, collection_ttl=TTL_SECONDS)


@app.route("/documents/<document_id>")
@document_api_page.support("text/html")
def document_page(document_id):
    document = dao.get_document(document_id)
    return render_template("document.html", document=document)


# HTML forms do not allow use of the DELETE method so use POST and make the endpoint path descriptive
@app.route("/delete_document/<document_id>", methods=["POST"])
@accept("text/html")
def delete_document(document_id):
    dao.delete_document(document_id)
    return redirect("/documents", code=302)


# HTML forms do not allow use of the DELETE method so use POST and make the endpoint path descriptive
@app.route("/delete_documents", methods=["POST"])
@accept("text/html")
def delete_documents():
    dao.delete_documents()
    return redirect("/documents", code=302)


@app.route("/create_document")
def add_document_page():
    return render_template("create_document.html")
