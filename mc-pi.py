import random

def approx_pi(n, seed = 0):
        random.seed(seed)
        inside = 0
        total = 0
        
        for i in range(n):
                point = [random.random(), random.random()]
                dist = dist_to_origin(point)

                if dist <= 1:
                        inside += 1
                total += 1

        return  4 * inside / total



#returns the distance from point (list of two floats) to (0,0)
def dist_to_origin(p):
        return (p[0] ** 2 + p[1] ** 2) ** 0.5


print(approx_pi(int(input("N: ")), float(input("Seed: "))))
