import numpy as np
import matplotlib.pyplot as plt

rA = [0, 0, -100]
rB = [0, 0, 100]
R = 350

rP = [50, 0, 0]

rA = np.array(rA)
rB = np.array(rB)
rP = np.array(rP)

print("End-points of the cylinder:")
print("A =", rA)
print("B =", rB)
print("Radius =", R)
print("P =", rP)


def norm(A):
    sum = 0
    for i in range(len(A)):
        sum += A[i] * A[i]
    return np.sqrt(sum)


def is_inside(rP):
    e = rA - rB
    m = np.cross(rA, rB)

    d = norm((np.cross(e, rP - rA)))/norm(e)

    rQ = rP + ((np.cross(e, m + np.cross(e, rP))) / (norm(e)**2))
    # print("Q =", rQ)

    rArA = np.dot(rA, rA)
    rArB = np.dot(rA, rB)
    rBrB = np.dot(rB, rB)
    rQrA = np.dot(rQ, rA)
    rQrB = np.dot(rQ, rB)

    wA = -(rArB - rBrB - rQrA - rBrB * rQrA + rQrB + rArB * rQrB) / \
        (rArA - 2.0 * rArB - rArB**2 + rBrB + rArA * rBrB)

    wB = -(rArA - rArB - rQrA - rArB * rQrA + rQrB + rArA * rQrB) / \
        (-rArA + 2.0 * rArB + rArB**2 - rBrB - rArA * rBrB)

    inside = True

    if (d > R):
        inside = False
    if (wA < 0):
        inside = False
    if (wA > 1):
        inside = False
    if (wB < 0):
        inside = False
    if (wB > 1):
        inside = False

    return inside


def distance_from_axis(rP):
    e = rA - rB
    d = norm((np.cross(e, rP - rA)))/norm(e)
    return d


def distance_from_surface(rP):
    return R - distance_from_axis(rP)


if (is_inside(rP) == True):
    print("P", rP,  "is inside")
else:
    print("P =", rP,  "is outside")

print("Distance of P from the axis =", distance_from_axis(rP))
print("Distance of P from the surface =", distance_from_surface(rP))
