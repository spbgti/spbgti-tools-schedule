import json

filled = False


def fill_database(filler):
    def real_decorator(test):
        def wrapper(*args, **kwargs):
            global filled
            if not filled:
                filler()
                filled = True
            test(*args, **kwargs)

        return wrapper

    return real_decorator


def is_object_equal_to_json(obj, json_str):
    return obj == json.loads(json_str)
