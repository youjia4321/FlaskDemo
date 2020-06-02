import hashlib


class Dev(object):
    ENV = 'development'  # 开发环境配置 默认环境(production)
    SECRET_KEY = 'daj@jwfn231%lodsdai#@'  # 密钥配置


class Product(object):
    ENV = 'production'
    SECRET_KEY = 'daj@jwfn231%lods%$s#@'


def encryption(pwd):
    return hashlib.md5(pwd.encode('utf-8')).hexdigest()
