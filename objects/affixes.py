"""
Example Affix

affix.name = 'backpack'
affix.type = 'physical'
affix.value = 1
affix.requirements = {'leather: {'target': 3,
                                 'completed': False}
                      }
affix.completed = False
}
"""


class Affix:
    """
    The base class for an item or enchantment.
    name (str): the name
    affix_type (str): type of affix
    value (int): the gold value for completion
    requirements (list): a list of dictionaries that contain the material type, the target number,
                         and the completed status
    completed (bool): completion status of the affix, complete when all requirements are complete
    """
    name = ""
    affix_type = ""
    affix_class = ""
    value = 0
    requirements = {}
    completed = False

    def __init__(self, name, value, requirements):
        self.name = name
        self.value = value
        self.requirements = requirements
        for req in self.requirements.values():
            req.update({'completed': False})


def affix_collection(affix_type, item_list):
    collection = {}
    for item in item_list:
        name = item[0]
        value = item[1]
        reqs = item[2]
        requirements = {}
        for req in reqs:
            requirements.update({req[0]: {'target': req[1]}})
        collection.update({name: affix_type(name, value, requirements)})
    return collection

