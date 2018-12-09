"""" configuracoes gerais da aplicacao """
from os import path


path = path.dirname(__file__)
path_data = path + r'\data'

purge_full = str.maketrans(dict.fromkeys("/*-+.,!@#$%¨&)'(_}{`^?:><;~][´=-¹²³£¢¬§ªº°"))