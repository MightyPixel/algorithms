class Point2D():
    x = 0
    y = 0


def solution(points):
    # Assuming Bob does not move from (0, 0)
    # for each point create a normalized vector
    # save each normalized vector in a set
    # return len(set)
    rays = set()
    for point in points:
        l = (point.x^2 + point.y^2)^0.5
        rays.add((point.x/l, point.y/l))

    return len(rays)
