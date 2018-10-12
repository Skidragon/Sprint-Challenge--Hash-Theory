def get_indices_of_item_weights(weights, limit):
  history = {}
  for i in range(len(weights)):
    if weights[i] not in history:
      history[weights[i]] = i
    
    if limit - weights[i] in history:
      return (i, history[limit - weights[i]])
  
  return None


if __name__ == '__main__':
  print(get_indices_of_item_weights([4,6,10,15,16], 21))