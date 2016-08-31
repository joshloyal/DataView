import functools


registry = {}


def register_class(target_class):
    registry[target_class.__name__] = target_class


class DataViewMeta(type):
    def __new__(meta, name, bases, class_dict):
        cls = type.__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls
