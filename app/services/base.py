from flask import jsonify
from functools import wraps
from http import HTTPStatus


def base_service(base_controller_function):
    @wraps(base_controller_function)
    def wrapper(*args, **kwargs):
        items, error = base_controller_function(*args, **kwargs)
        response = items if not error else {"error": error}
        status_code = HTTPStatus.OK if not error else HTTPStatus.BAD_REQUEST
        return jsonify(response), status_code

    return wrapper
