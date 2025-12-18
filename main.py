import heapq
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

class GoogleCloudDeliverySystem:
    def __init__(self, service_key_path, database_url):
        # Initializing Firebase connection
        cred = credentials.Certificate(service_key_path)
        firebase_admin.initialize_app(cred, {'databaseURL': database_url})
        self.graph = {}

    def add_road(self, u, v, weight):
        """Adds a road between two locations with a travel time/weight."""
        if u not in self.graph: self.graph[u] = []
        if v not in self.graph: self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def find_shortest_path(self, start, end):
        """Standard Dijkstra's Algorithm using Min-Heap."""
        if start not in self.graph or end not in self.graph:
            return None, None
            
        queue = [(0, start, [])]
        visited = set()

        while queue:
            (cost, current, path) = heapq.heappop(queue)
            if current in visited: continue
            
            visited.add(current)
            path = path + [current]

            if current == end: return cost, path

            for neighbor, weight in self.graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path))
        return float("inf"), []

    def sync_to_cloud(self, start, end, route, time):
        """Logs the detailed route to Firebase Realtime Database."""
        ref = db.reference('deliveries')
        ref.push().set({
            'from': start,
            'to': end,
            'path': " -> ".join(route),
            'total_time': time,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print(f"📡 Cloud Sync Successful: {start} to {end} in {time} mins.")

# --- INITIALIZING DYNAMIC MAP ---
if __name__ == "__main__":
    # CONFIG (Update these with your specific details)
    KEY_FILE = 'serviceAccountKey.json'
    DATABASE_URL = 'https://delivery-pathfinder-2026-default-rtdb.asia-southeast1.firebasedatabase.app/'

    system = GoogleCloudDeliverySystem(KEY_FILE, DATABASE_URL)

    # Adding 12 Points to create a "Complex City Map"
    city_roads = [
        ("Warehouse", "Metro_Station", 5), ("Warehouse", "Airport", 15),
        ("Metro_Station", "Shopping_Mall", 3), ("Metro_Station", "Point_A", 2),
        ("Airport", "Luxury_Hotel", 10), ("Airport", "Tech_Park", 12),
        ("Shopping_Mall", "Residential_Zone_1", 4), ("Shopping_Mall", "Point_B", 6),
        ("Point_A", "Point_B", 1), ("Point_B", "Customer_Home", 4),
        ("Tech_Park", "Customer_Home", 5), ("Luxury_Hotel", "Point_C", 5),
        ("Point_C", "Customer_Home", 2), ("Residential_Zone_1", "Customer_Home", 8)
    ]
    for u, v, w in city_roads: system.add_road(u, v, w)

    # --- USER INTERACTION ---
    print("\n📍 Available Locations: " + ", ".join(system.graph.keys()))
    start = input("Enter Pickup Location: ").strip()
    end = input("Enter Delivery Destination: ").strip()

    cost, path = system.find_shortest_path(start, end)

    if cost and cost != float("inf"):
        print(f"\n✅ Optimal Route: {' -> '.join(path)}")
        print(f"⏱️ Total Estimated Time: {cost} minutes")
        system.sync_to_cloud(start, end, path, cost)
    else:
        print("❌ Error: Path not found or invalid location names.")