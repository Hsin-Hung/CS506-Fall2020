import math

def euclidean_dist(x, y):
    return math.sqrt(sum([(i[0] - i[1])**2 for i in zip(x,y)]))

def manhattan_dist(x, y):
    return sum([abs(i[0] - i[1]) for i in zip(x,y)])

def jaccard_dist(x, y):

    union = len(list(set.union(set(x), set(y))))
    inter = len(list(set.intersection(set(x), set(y))))

    print(inter)

    if union == 0 or inter == 0:
        return 1
    return (union - inter)/(union)

def cosine_sim(x, y):
    numer = sum([i[0]*i[1]  for i in zip(x,y)])
    deno = (sum(list(map(math.sqrt,x))) + sum(list(map(math.sqrt,y))))
    if deno == 0 or x == y:
        return 1
    return numer/deno

# Feel free to add more
print(jaccard_dist([0,0], [1,0]))