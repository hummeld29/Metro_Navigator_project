from graph import Graph
from bst import BST
from hash_table import HashTable
from linked_list import LinkedList
from min_heap import MinHeap
from linked_stack import Stack, is_balanced
from linked_queue import Queue, board_passengers
from hash_set import HashSet


def main():
   print("metro navigator demonstration")

   print()
   print("=" * 66)
   graph = Graph()

   stations = ["Airport", "Downtown", "Beach", "Harbor",
                "Campus", "Library", "Museum", "Stadium"]
   for station in stations:
      graph.add_vertex(station)

   connections = [
        ("Airport", "Downtown"), ("Downtown", "Campus"), ("Campus", "Beach"),
        ("Downtown", "Stadium"), ("Stadium", "Harbor"), ("Harbor", "Beach"),
        ("Campus", "Library"), ("Library", "Museum"), ("Museum", "Downtown"),
    ]
   for connection in connections:
        graph.add_edge(connection[0], connection[1])

   print(str(graph))
   print(graph.vertex_count(), "stations,", graph.edge_count(), "connections")
   print()
   print("=" * 66)

   bst = BST()

   directory = [
        ("Downtown", "Red Line"), ("Beach", "Blue Line"),
        ("Library", "Green Line"), ("Airport", "Red Line"),
        ("Campus", "Blue Line"), ("Harbor", "Blue Line"),
        ("Stadium", "Red Line"), ("Museum", "Green Line"),
    ]
   for item in directory:
      bst.insert(item[0], item[1])

   print("Stations stored:", len(bst))
   print("Alphabetical (inorder):", ", ".join(bst.inorder()))
   print("Levelorder:", ", ".join(bst.level_order()))
   print("Lookup: Campus is on the", bst.get("Campus"))
   print()
   print("=" * 66)
   
   z = HashTable()

   fares = [
        ("Airport", 1), ("Downtown", 2), ("Beach", 3), ("Offices", 2),
        ("Campus", 2), ("City Center", 4), ("Garden", 3),
    ]
   for fare in fares:
      z.put(fare[0], fare[1])

   for station in ["Airport", "Downtown", "Beach", "City Center"]:
      print(station, "-> Zone", z.get(station))
   print("home ->", z.get("home", "not in the network"))
   print("Zones stored:", len(z))

   print()
   print("=" * 66)


   trip = LinkedList()
   for stop in ["Airport", "Downtown", "Campus", "Beach"]:
      trip.append(stop)

   print("foeward :", trip)
   trip.reverse()
   print("reversed:", trip)
   print()
   print("=" * 66)
   print("These numbers are maintenance task priotities low = high priotrity.")
   print()
   tasks = MinHeap()
   maintenance = [
      (3, "repaint beach platform"),
      (1, "repair downtown escalator"),
      (4, "inspect harbor elevator"),
      (2, "replace airport signage"),
      (5, "clean library entrance"),
    ]
   for task in maintenance:
      tasks.push(task[0], task[1])

   print("Removing tasks from the heap, lowest task priority first:")
   while not tasks.is_empty():
      task = tasks.pop()
      print("  Task priority", task[0], "-", task[1])
   print()
   print("=" * 66)
   history = Stack()
   for page in ["Airport", "Downtown", "Campus", "Beach"]:
      history.push(page)

   print("Rider is at:", history.peek())
   left = history.pop()
   print("  Back pressed: left", left, "- now at", history.peek())
   left = history.pop()
   print("  Back pressed: left", left, "- now at", history.peek())
   print("History left (newest first):", ", ".join(history.to_list()))

   print()
   line = Queue()
   for rider in ["Ana", "Ben", "Cara", "Dev"]:
      line.enqueue(rider)

   print("Service line (front first):", ", ".join(line.to_list()))
   served = line.dequeue()
   print("  Served", served, "- next in line is", line.peek())
   print("Still waiting:", ", ".join(line.to_list()))
   print()
   print("=" * 66)


   red = HashSet()
   for stop in ["Airport", "Downtown", "Campus", "Museum"]:
      red.add(stop)

   blue = HashSet()
   for stop in ["Downtown", "Stadium", "Campus", "Harbor"]:
      blue.add(stop)
   print("Red Line stops :", ", ".join(sorted(red.to_list())))
   print("Blue Line stops:", ", ".join(sorted(blue.to_list())))
   both = red.union(blue)
   print("Union (every stop on either line):", ", ".join(sorted(both.to_list())))
   shared = red.intersection(blue)
   print("Intersection (stops on both lines):", ", ".join(sorted(shared.to_list())))

   print("=" * 66)
   for text in ["{[(Airport)] Downtown}", "{[(Airport]) Downtown}", "((Beach)"]:
      print("Text:", text)
      print("  Balanced?", is_balanced(text))

   print()
   result = board_passengers(3, ["Ana", "Ben", "Cara", "Dev", "Eli"])
   print("3 seats, 5 people waiting")
   print("  Boarded:", result[0])
   print("  Still waiting:", result[1])

   result = board_passengers(10, ["Ana", "Ben"])
   print("10 seats, 2 people waiting")
   print("  Boarded:", result[0])
   print("  Still waiting:", result[1])

   result = board_passengers(0, ["Ana"])
   print("0 seats, 1 person waiting")
   print("  Boarded:", result[0])
   print("  Still waiting:", result[1])
   print()

if __name__ == "__main__":
   main()