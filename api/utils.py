import hashlib


def get_hash(unique_str):
    md5 = hashlib.md5()
    md5.update(unique_str.encode('utf-8'))
    return md5.hexdigest()