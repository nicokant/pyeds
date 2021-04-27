#  Created by Martin Strohalm, Thermo Fisher Scientific


class Lockable(object):
    """
    The pyeds.Lockable class provides a simple mechanism to prevent any
    accidental attribute changes of a derived classes instances. It is used by
    most of the pyeds classes to lock them after initialization to avoid damage
    of the internal data consistency.
    """
    
    
    def __init__(self):
        """Initializes a new instance of Lockable."""
        
        self._locked = False
    
    
    def __setattr__(self, name, value):
        """Sets instance attribute if allowed."""
        
        if name == '_locked' or not getattr(self, '_locked', False):
            super(Lockable, self).__setattr__(name, value)
        
        else:
            message = "%s instance is read-only! Use Unlock() first, but be cautious!" % self.__class__.__name__
            raise AttributeError(message)
    
    
    def Lock(self):
        """Prevents further attributes changes."""
        
        self._locked = True
    
    
    def Unlock(self):
        """Enables further attributes changes."""
        
        self._locked = False
