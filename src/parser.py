import fileinput

from src import error
from src import config


def parse_file(file):
    int_lst = []
    for line in file:
        line = line.split("#")
        line[0] = line[0].strip()
        if line[0].isdigit() and config.TAQUIN_SIZE == 0 and len(line[0]):
            config.TAQUIN_SIZE = int(line[0])
            if config.TAQUIN_SIZE == 1:
                raise error.ParsingError("Taquin de taille 1 n'est pas valide")
        else:
            tab = [elm for elm in line[0].split(" ") if elm != ""]
            if len(tab) == 0:
                continue
            for x in tab:
                if not x.isdigit():
                    raise error.ParsingError("'{}' is not a number".format(x))
                elif int(x) > int(config.TAQUIN_SIZE)**2 - 1:
                    raise error.ParsingError("'{}' > number max".format(x))
            int_lst += [int(x) for x in tab]
            if len(tab) != int(config.TAQUIN_SIZE):
                raise error.ParsingError("Longueur de ligne (={}) differente de la taille du jeu (={})\nline = '{}'\nfile = '{}'"
                                         .format(len(tab), config.TAQUIN_SIZE, line, file.filename()))
    if len(int_lst) == 0:
        raise error.ParsingError("File is empty")
    if len(set(int_lst)) != len(int_lst):
        raise error.ParsingError("La grille contient des doublons")
    return int_lst


def parser(input_file):
    config.TAQUIN_SIZE = 0
    try:
        with fileinput.input(input_file, openhook=fileinput.hook_encoded("utf-8")) as file:
            int_lst = parse_file(file)
    except UnicodeDecodeError:
        raise error.ParsingError("File contains non utf-8 characters..")
        #except Exception as err:
        #    raise error.ParsingError("Unknown parsing error ({})".format(err))
        #except BaseException as err:
        #    raise error.ParsingError("Program interrupted by system ({})".format(err))
    return int_lst
