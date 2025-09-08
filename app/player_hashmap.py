from player_list import PlayerList
from player import Player


class PlayerHashMap:
    def __init__(self, size=10):
        size: int
        """
        Hash map implementation to store players in slots using separate chain
        
        This class uses `PlayerList` objects as slots where each slot is responsible for 
        handling collisions by maintaining a linked list of entries.
        
        Attributes 
        --------------
        size : int 
        hashmap : list[PlayerList]
        count : int 
        """
        self.size = size
        self.hashmap = [PlayerList() for _ in range(size)]
        self.count = 0

    def hash_function(self, key):
        """
        Hash index for a given key
        """
        return hash(key) % self.size

    def get_index(self, key: str | Player) -> int:
        if isinstance(key, Player):
            return hash(key) % self.SIZE  # TODO: implement __hash__ in player
        else:
            return Player.hash(key) % self.SIZE  # TODO implement a hash class method in Player

    def __setitem__(self, key: str, name: str) -> None:
        """ Psuedo code:
        1. Use the key to calculate an index into the hash map
           (TODO: Implement a hash function in the Player class that returns a player hash and then modulate it by the size of the hashmap)
        2. Get the PlayerList at that index
        3. Check if the player is already on that player list.
             If it is, update the player's name.
             If it isn't, create a player and add the player to the player list.

         """
        # get the player's appropriate PlayerList:
        player_list = self.hashmap[self.get_index(key)]
        # check if the player is in the list
        # If it is, update the player's name
        # If it isn't, create a player and add the player to the player list




