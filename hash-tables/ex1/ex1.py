def get_indices_of_item_weights(weights, limit):
  history = {}
  for i in range(len(weights)):
    if weights[i] not in history:
      history[weights[i]] = i
    

    if limit - weights[i] in history and history[limit - weights[i]] != i:
      return (i, history[limit - weights[i]])
  
  return ()


if __name__ == '__main__':
  print(get_indices_of_item_weights([4,6,10,15,16], 21))