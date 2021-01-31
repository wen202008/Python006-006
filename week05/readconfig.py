import configparser

def read_config(filename='config.ini',section='redis'):
    config = configparser.ConfigParser()
    config.read(filename)

    if config.has_section(section):
        item = config.items(section)
    else:
        raise Exception('{0} not found in the {1} file.'.format(section,filename))

    return dict(item)


if __name__ == '__main__':
    print(read_config(filename=r'F:\Python006-006\week05\config.ini'))