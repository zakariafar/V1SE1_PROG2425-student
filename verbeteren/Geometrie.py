#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
import collections

"""
Programming
Verbeteropdracht PROG: Geometrie
(c) 2024 Hogeschool Utrecht,
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.
"""


def bereken_oppervlakte(lengte, breedte):
    """
    Bereken de oppervlakte van een rechthoek met de
    gegeven lengte en breedte.

    Args:
        lengte (float): De lengte van de rechthoek.
        breedte (float): De breedte van de rechthoek.
    Returns:
        float: De berekende oppervlakte.
    """
    return


def bereken_omtrek(lengte, breedte):
    """
    Bereken de omtrek van een rechthoek met de
    gegeven lengte en breedte.

    Args:
        lengte (float): De lengte van de rechthoek.
        breedte (float): De breedte van de rechthoek.
    Returns:
        float: De berekende omtrek.
    """
    return


def is_rechthoek(lengte, breedte):
    """
    Bepaal of de gegeven breedte en lengte passend
    zijn voor een rechthoek. Controleer daarvoor of
    de lengte en breedte beiden groter dan 0 zijn!

    Args:
        lengte (float): De lengte van de rechthoek.
        breedte (float): De breedte van de rechthoek.
    Returns:
        bool: True als beiden waarden > 0, anders False
    """
    return


def analyseer_rechthoeken(rechthoeken):
    """
    Deze functie ontvangt een lijst met tuples. Elke tuple bevat de
    lengte en breedte van een rechthoek. Voorbeeld:

        [(5, 3), (4, 2), (-1, 5)]

    Bepaal van gegeven rechthoeken of het daadwerkelijk een rechthoek
    is. Van elke rechthoek moet de omtrek en oppervlakte uitgerekend
    worden. Gebruik voor deze acties de functies die hierboven staan.

    Lever als resultaat van deze functie een lijst met tuples waar per
    rechthoek de oppervlakte en omtrek in staan (of None als de het geen
    correcte rechthoek is):

        [(15, 16), (8, 12), (None, None)]

    Args:
        rechthoeken (list): Een lijst met tuples (lengte/breedte per rechthoek)
    Returns:
        list: Een lijst met tuples (oppervlakte/omtrek per rechthoek)
    """
    return


def development_code():
    # Plaats hieronder code om je functies tussentijds te testen. Bijv:
    print("development printout:", analyseer_rechthoeken([(5, 3), (4, 2), (-1, 5)]))


def module_runner():
    development_code()      # Comment deze regel om je 'development_code' uit te schakelen
    __run_tests()           # Comment deze regel om de HU-tests uit te schakelen


"""
==========================[ HU TESTRAAMWERK ]================================
Hieronder staan de tests voor je code -- daaraan mag je niets wijzigen!
"""


def __my_assert_args(function, args, expected_output, check_type=False):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output).__name__} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    if str(expected_output) == str(output):
        msg = f"Fout: {function.__name__}{argstr} geeft {output} ({type(output).__name__}) " \
              f"in plaats van {expected_output} (type {type(expected_output).__name__})"
    else:
        msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"

    if type(expected_output) is float and isinstance(output, (int, float, complex)):
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_bereken_oppervlakte():
    case = collections.namedtuple('case', 'length, width expected_output')

    testcases = [case(5, 3, 15), case(1, 4, 4), case(4, 2, 8)]

    for test in testcases:
        __my_assert_args(bereken_oppervlakte, (test.length, test.width), test.expected_output)


def test_bereken_omtrek():
    case = collections.namedtuple('case', 'length, width expected_output')

    testcases = [case(5, 3, 16), case(1, 1, 4), case(2, 5, 14)]

    for test in testcases:
        __my_assert_args(bereken_omtrek, (test.length, test.width), test.expected_output)


def test_is_rechthoek():
    case = collections.namedtuple('case', 'length, width expected_output')

    testcases = [case(5, 3, True), case(0, 1, False), case(1, 0, False),
                 case(1, 1, True), case(0, -1, False), case(-1, 1, False),
                 case(-1, 0, False), case(-1, -1, False), case(-5, 3, False)]

    for test in testcases:
        __my_assert_args(is_rechthoek, (test.length, test.width), test.expected_output)


def test_analyseer_rechthoeken():
    case = collections.namedtuple('case', 'rectangles expected_output')

    testcases = [case([(5, 3), (4, 2), (-1, 5)], [(15, 16), (8, 12), (None, None)]),
                 case([(5, 3), (4, 2), (-1, -1)], [(15, 16), (8, 12), (None, None)]),
                 case([(5, 3), (4, 2), (0, 0)], [(15, 16), (8, 12), (None, None)]),
                 case([(5, 3), (-1, 2), (-1, 5)], [(15, 16), (None, None), (None, None)]),
                 case([(5, 3), (4, 2), (-1, -1)], [(15, 16), (8, 12), (None, None)])]

    for test in testcases:
        __my_assert_args(analyseer_rechthoeken, (test.rectangles,), test.expected_output)


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_bereken_oppervlakte, test_bereken_omtrek, test_is_rechthoek, test_analyseer_rechthoeken ]

    try:
        for test_function in test_functions:
            func_name = test_function.__name__[5:]

            print(f"\n======= Test output '{test_function.__name__}()' =======")
            test_function()
            print(f"Je functie {func_name} werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as e:
        print(e.args[0])
    except Exception as e:
        print(f"Fout: er ging er iets mis! Python-error: \"{e}\"")
        print(traceback.format_exc())


if __name__ == '__main__':
    module_runner()
