def words(statement):
  results = {}
  X = statement.split()
  for word in X:
    if word not in results:
        if word.isnumber():
            results[int(word)] = 1
        else:
            results[word] = 1

    else:
        if word.isnumber():
            results[int(word)] += 1
        else:
            results[word] += 1
  return results

words('word')
words('one of each')
words('one fish two fish red fish blue fish')
words('car : carpet as java : javascript!!!&@$%^8')
