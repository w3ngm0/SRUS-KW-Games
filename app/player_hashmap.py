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
            key = key.uid
            print("Is an instance ")
            return hash(key) % self.size
        elif not isinstance(key, str):
            raise TypeError("key must be a str or Player")
        return self.hash_function(key)

    def __setitem__(self, key: str, name: str) -> None:
        """
        Insert of update a player in the hash map.

        Steps:
        1. Find the slot index using key
        2. Check if the player already exists in the slot.
            - If yes, update the player's name.
            - If no, create a new Player and add to the slot.
        """
        # use key to calculate index into the hash map
        index_value = self.get_index(key)
        print(f"Setting the key={key!r}, name={name!r}, index={index_value}")

        node = self.hashmap[index_value].find(key)
        if node is not None:
            print("New updated key-value pairs:")
            node.player._name = name
            return

        print(" --> inserted new key-value pair")

        # if it does not exist insert new
        # get the player's appropriate PlayerList:
        player_list = self.hashmap[self.get_index(key)]
        player_list.insert_at_head(Player(uid=key, name=name))
        self.count += 1  # If it isn't, create a player and add the player to the player list





