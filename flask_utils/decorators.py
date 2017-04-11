# -*- coding: utf-8 -*-

import functools

from flask import request, make_response, jsonify

from flask_utils.tools import Signer


def sign_required(signer=Signer, status=200, default=''):
    """
    装饰器,用来装饰class-based view的method方法(get, post, etc.)
    :param signer: 签名类,必须有validate方法
    :param status: 整型,http状态码
    :param default: 签名失败的返回值
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            nonlocal default

            if request.method == 'GET':
                params = request.args
            elif request.method == 'POST':
                params = request.json
            else:
                return func(*args, **kwargs)

            if signer.validate(params):
                resp = func(*args, **kwargs)
            else:
                if isinstance(default, dict):
                    default = jsonify(default)
                resp = make_response(default, status)

            return resp
        return wrapper
    return decorator
