
gifts_brought = {
    "Isabelle": "cat (Isabelle)",
    "Ivy": "shoe (Ivy)",
    "Leah": "wine (Leah)",
    "Kristine": "cookies (Kristine)",
    "Kiko": "brownies (Kiko)",
    "Ahmad": "other shoe (Ahmad)"
}

from random import choice, randint

def exchange_gifts(gift_dict):
    gifts_exchanged = {}

    gifts_list = []

    for person in gift_dict:
        gifts_list.append([person, gift_dict[person]])

    # i = 0
    # while i < len(gifts_list)-1:

    #     gifts_exchanged[_list[1]] = gifts_list[i][1]

    for _list in gifts_list:
        i = gifts_list.index(_list)
        if i != len(gifts_list) - 1:
            gifts_exchanged[_list[0]] = gifts_list[i+1][1]
        else:
            gifts_exchanged[_list[0]] = gifts_list[0][1]

    # print gifts_list
    print gifts_exchanged


def random_exchange_gifts(gift_dict):
    """Exchanging gifts randomly."""
    gifts_exchanged = {}

    gifts_list = []

    for person in gift_dict:
        gifts_list.append([person, gift_dict[person]])

exchange_gifts(gifts_brought)
