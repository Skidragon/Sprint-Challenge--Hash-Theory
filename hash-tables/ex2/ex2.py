def reconstruct_trip(tickets):
  
  places = {}

  for i in range(len(tickets)):
    source = tickets[i][0]
    destination = tickets[i][1]
    places[source] = destination
  
  source = None
  trip = []

  for i in range(len(tickets)):
    if source in places:
      if places[source] is not None:
        trip.append(places[source])
      source = places[source]

    else:
      return []
  
  return trip

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass
