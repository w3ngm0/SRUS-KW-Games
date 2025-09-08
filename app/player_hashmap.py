from player_list import PlayerList


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

    


