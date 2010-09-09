# From Python Cookbook, 2e. Recipe 6.3, "Restricting Attribute Setting".
# Credit: Michele Simionato

def no_new_attributes(wrapped_setattr):
    """ raise an error on attempts to add a new attribute, while
        allowing existing attributes to be set to new values.
    """
    def _ _setattr_ _(self, name, value):
        if hasattr(self, name):    # not a new attribute, allow setting
            wrapped_setattr(self, name, value)
        else:                      # a new attribute, forbid adding it
            raise AttributeError("can't add attribute %r to %s" % (name, 
self))
    return _ _setattr_ _
class NoNewAttrs(object):
    """ subclasses of NoNewAttrs inhibit addition of new attributes, 
while
        allowing existing attributed to be set to new values.
    """
    # block the addition new attributes to instances of this class
    _ _setattr_ _ = no_new_attributes(object._ _setattr_ _)
    class _ _metaclass_ _(type):
        " simple custom metaclass to block adding new attributes to this 
class "
        _ _setattr_ _ = no_new_attributes(type._ _setattr_ _)
