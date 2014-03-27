def ensure_int(val):
    try:
        val = int(val)
    except ValueError:
        pass
        # TODO raise a custom exception?
    except TypeError:
        # TODO handle None value
        pass
    else:
        return val