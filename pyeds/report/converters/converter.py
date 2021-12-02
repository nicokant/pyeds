#  Created by Martin Strohalm, Thermo Fisher Scientific


# init main repository
CONVERTERS = {}


def register(tag):
    """Registers converter by given tag."""
    
    def reg(cls):
        """Registers given class."""
        
        CONVERTERS[tag] = cls
        CONVERTERS[tag.lower()] = cls
        CONVERTERS[tag.upper()] = cls
        
        return cls
    
    return reg


class ValueConverter(object):
    """
    The pyeds.report.ValueConverter class provides a base for all property value
    converters. These converters are automatically attached to specific
    pyeds.PropertyColumn via 'ValueTypeGuid' or 'DataPurpose' when report file
    schema is initialized. They are available later via 'ValueTypeConverter'
    attribute. These converters are used automatically by EDS to convert a
    property value into its final representation.
    
    You can create your custom converters by creating derived class from the
    'pyeds.report.ValueConverter' and registering it by 'pyeds.report.register'
    decorator using appropriate 'ValueTypeGuid' or 'DataPurpose'.
    """
    
    
    def Convert(self, value):
        """
        Converts raw property value into its final type.
        
        Args:
            value: ?
                Raw property value to convert.
        
        Returns:
            ?
                Converted property value.
        """
        
        raise NotImplementedError()