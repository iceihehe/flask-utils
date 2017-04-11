# -*- coding: utf-8 -*-

class Signer:
    """
    签名类,必须包含validate方法
    """
    @classmethod
    def validate(cls, params):
        return True
