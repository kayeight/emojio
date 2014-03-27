def ensure_int(val):
    try:
        val = int(val)
    except ValueError:
        pass
        # TODO raise a custom exception?
    else:
        return val