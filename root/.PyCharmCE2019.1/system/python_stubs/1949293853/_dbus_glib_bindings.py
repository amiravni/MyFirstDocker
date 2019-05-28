# encoding: utf-8
# module _dbus_glib_bindings
# from /usr/lib/python3/dist-packages/_dbus_glib_bindings.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# functions

def DBusGMainLoop(set_as_default=False): # real signature unknown; restored from __doc__
    """
    DBusGMainLoop([set_as_default=False]) -> NativeMainLoop
    
    Return a NativeMainLoop object which can be used to
    represent the default GLib main context in dbus-python.
    
    If the keyword argument set_as_default is given and is true, set the new
    main loop as the default for all new Connection or Bus instances.
    
    Non-default main contexts are not currently supported.
    """
    pass

def gthreads_init(): # real signature unknown; restored from __doc__
    """ gthreads_init() """
    pass

def setup_with_g_main(conn): # real signature unknown; restored from __doc__
    """
    setup_with_g_main(conn: dbus.Connection)
    
    Deprecated.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f549390db38>'

__spec__ = None # (!) real value is "ModuleSpec(name='_dbus_glib_bindings', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f549390db38>, origin='/usr/lib/python3/dist-packages/_dbus_glib_bindings.cpython-35m-x86_64-linux-gnu.so')"

