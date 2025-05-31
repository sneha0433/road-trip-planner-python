def get_user_input():
    source = input("Enter the starting city: ")
    destination = input("Enter the destination city: ")
    return source, destination

def plan_road_trip(source, destination):
    print(f"Planning your road trip from {source} to {destination}...")
    print("Estimated distance: 300 km")
    print("Estimated travel time: 5 hours")

def main():
    print("Welcome to the Road Trip Planner!")
    source, destination = get_user_input()
    plan_road_trip(source, destination)

if __name__ == "__main__":
    main()
  
