def get_indices_of_item_weights(weights, limit):
  history = {}
  for i in range(len(weights)):
    if weights[i] not in history:
      history[weights[i]] = i
    
    difference = limit - weights[i]
    
    if difference in history and history[difference] != i:
      return (i, history[difference])
  
  return ()


if __name__ == '__main__':
  print(get_indices_of_item_weights([4,6,10,15,16], 21))