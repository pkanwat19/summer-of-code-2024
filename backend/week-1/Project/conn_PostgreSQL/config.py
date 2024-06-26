from configparser import ConfigParser
import os

def config(filename="database.ini", section="postgresql"):
    # Get the absolute path of the config file
    config_path = os.path.join(os.path.dirname(__file__), filename)
    
    parser = ConfigParser()
    parser.read(config_path)
    
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} is not found in the {1} file.'.format(section, filename))

    return(db)