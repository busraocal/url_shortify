import hashlib

from flask import Blueprint, request, jsonify, redirect
from app.core.db import get_db
from app.services.url_service import UrlService
from app.api.schemas.url_schema import UrlSchema

bp = Blueprint('url', __name__)


@bp.route("/create_short_url", methods=["POST"])
def create_url():
    db = next(get_db())
    url_service = UrlService(db)
    url_schema = UrlSchema()
    data = request.get_json()
    url = url_service.get_url(data["original_url"])
    if url:
        return jsonify(url)
    else:
        short_url = hashlib.md5(data["original_url"].encode()).hexdigest()[:6]
        url = url_service.create_url(data['original_url'], short_url)
        return jsonify(url_schema.dump(url)), 201


@bp.route("/<short_url>", methods=["GET"])
def redirect_to_url(short_url):
    db = next(get_db())
    url_service = UrlService(db)
    url = url_service.get_short_url(short_url)
    if url:
        return redirect(url.original_url)
    return jsonify({'error': 'URL not found'}), 404
