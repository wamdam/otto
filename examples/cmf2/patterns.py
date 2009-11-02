class Annotation(object):
    """ Annotation on objects. Annotations are stored in a "_annotations" attribute.

        >>> class MyObj(object):
        ...     pass
        >>> o = MyObj()
        >>> annotations = Annotations(o, 'mynamespace')
        >>> annotations
        {}
    """
    def __new__(self, obj, namespace):
        try:
            annotations = obj._annotations
        except AttributeError:
            # XXX Should we check if the object supports __setitem__?
            obj._annotations = dict()
            annotations = obj._annotations
        try:
            return annotations[namespace]
        except KeyError:
            annotations[namespace] = dict()
            return annotations[namespace]


