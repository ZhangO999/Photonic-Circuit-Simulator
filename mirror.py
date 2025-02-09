from photon import Photon

'''
Name:   Oliver Zhang
SID:    520651281
Unikey: ozha8307

Mirror - A surface that reflect photons, changing the direction in which they
travel. A photon may also become lost depending on the type of mirror and the
photon's initial direction when it reaches the mirror.

You are free to add more attributes and methods, as long as you aren't
modifying the existing scaffold.
'''


class Mirror:
    def __init__(self, symbol: str, x: int, y: int):
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''
        Initialises a Mirror instance given a symbol, x and y value.

        component_type: str - represents the type of component ('mirror')
        symbol:         str - the symbol of this mirror
                              ('/', '\', '>', '<', '^' or 'v')
        x:              int - x position of this mirror
        y:              int - y position of this mirror

        Parameters
        ----------
        symbol: str - the symbol to set this mirror to
        x:      int - the x position to set this mirror to
        y:      int - the y position to set this mirror to
        '''
        self.component_type = "mirror"
        self.symbol = symbol
        self.x = x
        self.y = y

        # dictionary of mapping rules for photon reflections:
        '''
        Motivation: This direction map is to avoid the jungle of if-elif-else... casework
        to make my code more readable, i.e., more easily debuggable later. The key idea is
        that we observe that each mirror type is associated to a finite set of
        directional-mappings. For instance, "/" is associated with two 2-cycles (N,E) and
        (N,W) (Cases for each mirror were first exhaustively identified on paper).
        '''
        self.reflection_rules = {
            '/': {'N': 'E', 'E': 'N', 'S': 'W', 'W': 'S'},
            '\\': {'N': 'W', 'W': 'N', 'S': 'E', 'E': 'S'},
            '>': {'N': 'E', 'S': 'E'},  # only vertical approaches permitted
            '<': {'N': 'W', 'S': 'W'},  # only vertical approaches permitted
            '^': {'E': 'N', 'W': 'N'},  # only horizontal approaches permitted
            'v': {'E': 'S', 'W': 'S'}   # only horizontal approaches permitted
        }

    def reflect_photon(self, photon: Photon) -> None:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''
        Reflects a photon off the surface of this mirror. If the photon has
        already been absorbed, you should return out early.

        Otherwise, the photon will travel in a new direction depending on the
        type of mirror and its current direction. If the reflection causes the
        photon to be absorbed, the direction is not changed but the photon
        should be updated to get absorbed.

        Parameter
        ---------
        photon - the photon to reflect off this mirror
        '''
        if photon.is_absorbed():
            return
        # supposing photon is NOT absorbed:
        # extract the specific reflection mapping based on the mirror symbol
        # and apply it if it exists:
        mappings = self.reflection_rules.get(self.symbol, {})

        i = 0
        keys = list(mappings.keys())  # make subscriptable
        direction_found = False
        # loop over all approach directions, see if one matches our photon's
        # one. If so, apply this mapping to the photon's direction
        while i < len(keys):
            if photon.direction == keys[i]:
                photon.direction = mappings[photon.direction]
                direction_found = True
                break
            i += 1

        '''
         For our specific mirror and approach direction of photon, no mapping on approach direction is defined. Only the "pointy" mirrors, i.e., '<','^'
         mirrors have domains that are not fully specified. We can define the mappings on the "unpermitted" approach directions to allow for absorption
         instead of change direction of photon. Thus, only "pointy" mirrors can absorb photons.
         For example, mirror.symbol == "<" but photon.direction == "W". No corresponding "W" domain element existsc for this direction mapping.
        '''
        if not direction_found:
            photon.got_absorbed()  # photon.direction unchanged

    def get_component_type(self) -> str:
        '''Returns component type.'''
        return self.component_type

    def get_symbol(self) -> str:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''Returns symbol.'''
        return self.symbol

    def get_x(self) -> int:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''Returns x.'''
        return self.x

    def get_y(self) -> int:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''Returns y.'''
        return self.y

