def importModule(module_name):
    print ("Importing : " + module_name )
    try:
        globals()[module_name] = __import__(module_name)
        reload( globals()[module_name] )
    except ImportError:
        print ("Error importing :" + module_name)

__all__ = ["NWUtilities"]

importModule("NWUtilities")



