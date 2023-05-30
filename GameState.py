import json
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Weapon) or isinstance(obj, StatePerFrame):
            return obj.as_dict
        return super().default(obj)

class Weapon(object):
    # def __init__(self, weapon_class, weapon_name, ammo_in_mag, ammo_in_reserve) -> None:
    #     self.weapon_class = weapon_class
    #     self.weapon_name = weapon_name
    #     self.ammo_in_mag = ammo_in_mag
    #     self.ammo_in_reserve = ammo_in_reserve
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

class StatePerFrame(object):
    # def __init__(self, round_num, tick, side, team, hp, armor, is_alive, x, y, z, weapon, 
    #              total_utility, equipment_value_freezetime_end, area_name, seconds, clock_time, t_alive, ct_alive, bomb_planted, map_name, utility_used, player) -> None:
    #     self.round_num = round_num
    #     self.tick = tick
    #     self.side = side
    #     self.team = team
    #     self.hp = hp
    #     self.armor = armor
    #     self.is_alive = is_alive
    #     self.x = x
    #     self.y = y
    #     self.z = z
    #     self.weapon = weapon
    #     self.total_utility = total_utility
    #     self.equipment_value_freezetime_end = equipment_value_freezetime_end
    #     self.area_name = area_name
    #     self.seconds = seconds
    #     self.clock_time = clock_time
    #     self.t_alive = t_alive
    #     self.ct_alive = ct_alive
    #     self.bomb_planted = bomb_planted
    #     self.map_name = map_name
    #     self.utility_used = utility_used
    #     self.player = player

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




