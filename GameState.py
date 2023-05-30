'''
    weapon class to store weapon data in the inventory 
'''
class Weapon(object):

    def __init__(self, dictionary_data) -> None:
        self.as_dict = dictionary_data
        for key in dictionary_data:
            setattr(self, key, dictionary_data[key])
    
    def __eq__(self, other) -> bool:
        return self.weapon_name == other.weapon_name and self.weapon_class == other.weapon_class
    
    def __hash__(self) -> int:
        return hash(self.weapon_name)
    
    def __str__(self) -> str:
        return str(self.as_dict)

'''
    StatePerFrame data to store information in each row/dictionary
    Modified to store the weapon data 
'''
class StatePerFrame(object):

    def __init__(self, dictionary_data) -> None:
        self.as_dict = dictionary_data
        for key in dictionary_data:
            if (key != 'inventory'):
                setattr(self, key, dictionary_data[key])
            if (key == 'inventory'):
                weapons = dict()
                if dictionary_data[key] is not None:
                    for weapon in dictionary_data[key]:
                        curr_weapon = Weapon(weapon)
                        curr_class = curr_weapon.weapon_class
                        if curr_class in weapons:
                            weapons[curr_class].append(curr_weapon)
                        else:
                            weapons[curr_class] = [curr_weapon]

                setattr(self, key, weapons)
                

    def __str__(self) -> str:
        return str(self.as_dict)




