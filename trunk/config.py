

import sys, os
import ConfigParser



# Configuration dict
cfg = None



def readCfg():

    global cfg

    scriptpath = sys.argv[0]

    # Get full path of Read config.cfg
    path = os.path.join( os.path.dirname( scriptpath ), 'config.cfg')
    
    parser = ConfigParser.ConfigParser()
    try:
        f = open( path )
    except IOError:
        cfg = {}

    else:
        # Read config.cfg
        parser.readfp( f )

        # Get Configuration dict
        cfg = dict( parser.items('Visual Lambda') )

        f.close()



def get( key, default ):
    
    global cfg
    
    if cfg is None:
        readCfg()
    
    return  key in cfg  and  cfg[ key ]  or  default

