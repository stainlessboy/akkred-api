def get_attribute(obj, path: str, default=None):
    paths = path.split('.')
    for p in paths:
        obj = getattr(obj, p, default)
    return obj or default
