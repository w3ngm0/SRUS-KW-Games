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
        uid = key.uid if isinstance(key, Player) else key
        return Player.my_chosen_hash_function(uid) % self.size

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

    def __getitem__(self, key: str) -> Player:
        """
        Retrieve a player by key
        :param key : str
            The unique identifier for the player
        :returns Player
            The player object associated with key
        :raises KeyError
            If the key does not exist in the hash map
        """
        index_value = self.get_index(key)
        print(f"This is your {key}, key={key!r}, index={index_value}")
        node = self.hashmap[index_value].find(key)
        if node is None:
            raise KeyError(key)
        print(f" --> found name={node.player.name!r}")
        return node.player

    def __delitem__(self, key: str) -> None:
        """
        Delete a player by key.
        :param key: str
            The unique identifier for the player
        :raises KeyError
            If the key does not exist in the hash map

        """
        index_value = self.get_index(key)
        print(f"Deleting key={key!r}, index={index_value}")
        removed_item = self.hashmap[index_value].delete_by_key(key)
        print(" --> removed" if removed_item else "  -> not found")
        if not removed_item:
            raise KeyError(key)
        self.count -= 1

    def __len__(self) -> int:
        """Returns the number of players in the hash map."""
        return self.count

    def display_hash_table(self):
        """Visual representation of the hash map. """
        printed_any = False
        for i in range(self.size):
            p_list = self.hashmap[i]
            if p_list.is_empty:
                continue

            parts = []

            node = p_list.head
            while node is not None:
                #
                parts.append(f"{node.player.name} ({node.key})")
                node = node.next

            print(f"[{i}] -->" + "<->".join(parts))
            printed_any = True

        if not printed_any:
            print("HashMap is empty")


if __name__ == "__main__":
    hash_m = PlayerHashMap(size=10)

    hash_m["001"] = "Alice"
    hash_m["002"] = "Bonny"
    hash_m["003"] = "Cat"

    hash_m.display_hash_table()

    hash_m["002"] = "Bonnie"
    hash_m.display_hash_table()








