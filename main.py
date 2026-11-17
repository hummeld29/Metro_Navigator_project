from graph import Graph
from bst import BST
from hash_table import HashTable
from linked_list import LinkedList
from min_heap import MinHeap
from linked_queue import Stack, Queue, board_passengers
from hash_set import HashSet

WIDTH = 66

STATIONS = ["Airport", "Downtown", "Beach", "offices", "Campus", "City Center", "Garden"]
Connections = [
   ("Airport", "Downtown"),
   ("Airport", "Beach"),
   ("Downtown", "Beach"),
   ("Downtown", "offices"),
   ("Downtown", "Campus"),
   ("Beach", "City Center"),
   ("offices", "City Center"),
   ("Campus", "Garden"),
   ("City Center", "Garden"),
   ("Garden", "Airport")

]
fares = {
   ("Airport", 1),
   ("Downtown", 2),
   ("Beach", 3),
   ("offices", 2),
   ("Campus", 2),
   ("City Center", 4),
   ("Garden", 3)
}


def section(number, title):
   print()
   print("=" * WIDTH)
   print(f"Section {number}: {title}")
def show_graph():
   section(1, "Metro city map (graph)")
   graph = Graph()
   for station in STATIONS:
      graph.add_station(station)

   for connection in Connections:
      graph.add_connection(connection[0], connection[1])
def show_bst():
   section(2, "Metro city map (binary search tree)")
   bst = BST()
   for station in STATIONS:
      bst.insert(station)
def show_hash_table():
   section(3, "Metro city map (hash table)")
   hash_table = HashTable()
   for station in STATIONS:
      hash_table.insert(station)

def main():

