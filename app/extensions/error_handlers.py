from flask import jsonify
from werkzeug.exceptions import HTTPException

def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        response = {
            "error": e.name,
            "message": e.description,
            "status_code": e.code
        }
        return jsonify(response), e.code

    @app.errorhandler(404)
    def not_found_error(e):
        return jsonify({
            "error": "Not Found",
            "message": "The requested resource was not found.",
            "status_code": 404
        }), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({
            "error": "Internal Server Error",
            "message": "An unexpected error occurred.",
            "status_code": 500
        }), 500

    @app.errorhandler(Exception)
    def handle_generic_exception(e):
        return jsonify({
            "error": "Unexpected Error",
            "message": str(e),
            "status_code": 500
        }), 500
