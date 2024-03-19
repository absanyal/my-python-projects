import numpy as np

rA = np.array([-5, 0, 0])
rB = np.array([5, 0, 0])
R = 5

print("End-points of the cylinder:")
print("A =", rA)
print("B =", rB)
print("Radius =", R)

rP = np.array([10.0, 0.0, -0.1])
print("P =", rP)


def norm(A):
    sum = 0
    for i in range(len(A)):
        sum += A[i] * A[i]
    return np.sqrt(sum)


e = rA - rB
m = np.cross(rA, rB)

d = norm((np.cross(e, rP - rA)))/norm(e)

rQ = rP + ((np.cross(e, m + np.cross(e, rP))) / (norm(e)**2))
print("Q =", rQ)

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

print("d =", d)
print("wA=", wA)
print("wB =", wB)
print("wA + wB =", wA + wB)
# print("wA^2 + wB^2 =", wA**2 + wB**2)

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

if (inside == False):
    print("Point", rP, "is outside the cylinder")
else:
    print("Point", rP, "is inside the cylinder")
