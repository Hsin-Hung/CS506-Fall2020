
def sqrt(x):
    return x**(1/2)

def euclidean_dist(x, y):
    return sqrt(sum([(i[0] - i[1])**2 for i in zip(x,y)]))

def manhattan_dist(x, y):
    return sum([abs(i[0] - i[1]) for i in zip(x,y)])

def jaccard_dist(x, y):

    union = len(list(set.union(set(x), set(y))))
    inter = len(list(set.intersection(set(x), set(y))))
    
    if union == 0:
        return 1
    return (union - inter)/(union)

def cosine_sim(x, y):
    numer = sum([i[0]*i[1]  for i in zip(x,y)])
    deno = sqrt(sum([i**2 for i in x])) * sqrt(sum([j**2 for j in y]))

    if deno == 0:
        return 1

    return numer/deno

# Feel free to add more