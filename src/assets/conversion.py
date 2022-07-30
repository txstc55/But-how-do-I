import math
from pickle import TRUE
import numpy as np
from random import random
DIFFERENCE_THREASHOLD = 0.0000001
amplifier = 200


class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        pointString = "x: {0}, y: {1}, z: {2}".format(self.x, self.y, self.z)
        return pointString

    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __truediv__(self, number):
        return point(self.x/number, self.y/number, self.z/number)

    def length(self):
        # length from origin
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def cross(self, other):
        return point(self.y*other.z - self.z*other.y,
                     self.z*other.x - self.x*other.z,
                     self.x*other.y - self.y*other.x)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z


class edge:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.length = (p2 - p1).length()

    def __str__(self):
        vectorString = "p1: {0}\np2: {1}\nlength: {2}".format(
            str(self.p1), str(self.p2), self.length)
        return vectorString

    def length(self):
        return self.length


class triangle:
    def __init__(self, p1, p2, p3, explicit):
        v1 = edge(p1, p2)
        v2 = edge(p2, p3)
        v3 = edge(p1, p3)
        longest_edge = max(v1.length, v2.length, v3.length)
        shortest_edge = min(v1.length, v2.length, v3.length)
        if not explicit:

            # longest edge always have v1 and v2
            # shortest edge always have v2 and v3
            if v1.length == longest_edge and v2.length == shortest_edge:
                self.p1 = p1
                self.p2 = p2
                self.p3 = p3
            elif v1.length == shortest_edge and v2.length == longest_edge:
                self.p1 = p3
                self.p2 = p2
                self.p3 = p1
            elif v1.length == longest_edge and v3.length == shortest_edge:
                self.p1 = p2
                self.p2 = p1
                self.p3 = p3
            elif v1.length == shortest_edge and v3.length == longest_edge:
                self.p1 = p3
                self.p2 = p1
                self.p3 = p2
            elif v2.length == longest_edge and v3.length == shortest_edge:
                self.p1 = p2
                self.p2 = p3
                self.p3 = p1
            else:
                self.p1 = p1
                self.p2 = p3
                self.p3 = p2
            if self.p3.x <= DIFFERENCE_THREASHOLD and math.pow(self.p1.x + self.p2.x, 2) <= DIFFERENCE_THREASHOLD and self.p1.y == self.p2.y and self.p1.x > 0:
                self.p1.x = -self.p1.x
                self.p2.x = -self.p2.x
        else:
            self.p1 = p1
            self.p2 = p2
            self.p3 = p3
        # print(explicit)
        # print((self.p1 - self.p2).length())
        # print((self.p2 - self.p3).length())
        # print((self.p1 - self.p3).length())
        # assert((self.p1 - self.p2).length() == longest_edge)
        # assert((self.p2 - self.p3).length() == shortest_edge)
        
        self.rotation_matrix = np.matrix(
            [[1.0, 0.0, 0], [0, 1.0, 0], [0, 0, 1.0]])

    def p1_rotated(self):
        p1_array = np.array([self.p1.x, self.p1.y, self.p1.z])
        p1_rotated = self.rotation_matrix.dot(p1_array)
        return point(p1_rotated[0, 0], p1_rotated[0, 1], p1_rotated[0, 2])

    def p2_rotated(self):
        p2_array = np.array([self.p2.x, self.p2.y, self.p2.z])
        p2_rotated = self.rotation_matrix.dot(p2_array)
        return point(p2_rotated[0, 0], p2_rotated[0, 1], p2_rotated[0, 2])

    def p3_rotated(self):
        p3_array = np.array([self.p3.x, self.p3.y, self.p3.z])
        p3_rotated = self.rotation_matrix.dot(p3_array)
        return point(p3_rotated[0, 0], p3_rotated[0, 1], p3_rotated[0, 2])

    def rotate_x(self, theta):
        # theta has to be in radiance
        rot = np.matrix([[1, 0, 0], [0, math.cos(
            theta), -math.sin(theta)], [0, math.sin(theta), math.cos(theta)]])
        self.rotation_matrix = np.matmul(rot, self.rotation_matrix)
        return self

    def rotate_y(self, theta):
        # theta has to be in radiance
        rot = np.matrix([[math.cos(theta), 0, math.sin(theta)], [
                        0, 1, 0], [-math.sin(theta), 0, math.cos(theta)]])
        self.rotation_matrix = np.matmul(rot, self.rotation_matrix)
        return self

    def rotate_z(self, theta):
        # theta has to be in radiance
        rot = np.matrix([[math.cos(theta), -math.sin(theta), 0],
                         [math.sin(theta), math.cos(theta), 0], [0, 0, 1]])
        self.rotation_matrix = np.matmul(rot, self.rotation_matrix)
        return self

    def __str__(self):
        triangleString = "p1: {0}\np2: {1}\np3: {2}".format(
            self.p1, self.p2, self.p3)
        return triangleString

    def center(self):
        return (self.p1 + self.p2 + self.p3) / 3

    def triangleCenteredAtOrigin(self):
        center = self.center()
        return triangle(self.p1 - center, self.p2 - center, self.p3 - center, True)

    def triangleCenteredAtOriginFlat(self):
        # we know the edge lengths of this triangle
        # we need to put the longest edge on x axis
        # then calculate the other point's location
        # then, center it at origin
        p1 = point(0, 0, 0)
        # this will be our l1
        longest_edge_length = (self.p2 - self.p1).length()
        p2 = point(longest_edge_length, 0, 0)
        # this will be l2
        shortest_edge_length = (self.p2 - self.p3).length()
        # this will be l3
        middle_edge_length = (self.p3 - self.p1).length()
        assert(longest_edge_length >=
               middle_edge_length and middle_edge_length >= shortest_edge_length)
        # print(longest_edge_length, shortest_edge_length, middle_edge_length)
        # x1 = (l1^2 + l2^2 - l3^2) / (2 * l1)
        x1 = (pow(longest_edge_length, 2) + pow(middle_edge_length, 2) -
              pow(shortest_edge_length, 2))/(2 * longest_edge_length)
        x3 = math.sqrt(pow(middle_edge_length, 2) - pow(x1, 2))
        p3 = point(x1, x3, 0)
        # print((p1 - p2).length())
        # print((p1 - p3).length())
        # print((p2 - p3).length())
        triangle_point_origin = triangle(p1, p2, p3, True)
        triangleAtCenter = triangle_point_origin.triangleCenteredAtOrigin()
        assert(triangleAtCenter.p1.x < 0 and triangleAtCenter.p1.y < 0)
        assert(triangleAtCenter.p3.y > 0)
        assert(triangleAtCenter.p2.x > 0 and triangleAtCenter.p2.y < 0)
        return triangleAtCenter
        # return self

    def check_triangle_equal(this, other):
        rotated_p1 = this.p1_rotated()
        rotated_p2 = this.p2_rotated()
        rotated_p3 = this.p3_rotated()
        # print((rotated_p1 - rotated_p2).length())
        # print((rotated_p2 - rotated_p3).length())
        # print((rotated_p1 - rotated_p3).length())
        # print((other.p1 - other.p2).length())
        # print((other.p2 - other.p3).length())
        # print((other.p1 - other.p3).length())
        # print()
        # there will be a finite difference, but it shouldn't be greater than a value we set
        assert(math.pow((rotated_p2 - rotated_p1).length() -
                        (other.p2 - other.p1).length(), 2) <= DIFFERENCE_THREASHOLD)
        assert(math.pow((rotated_p3 - rotated_p1).length() -
                        (other.p3 - other.p1).length(), 2) <= DIFFERENCE_THREASHOLD)
        assert(math.pow((rotated_p3 - rotated_p2).length() -
                        (other.p3 - other.p2).length(), 2) <= DIFFERENCE_THREASHOLD)
    
    # Checks if a matrix is a valid rotation matrix.
    def isRotationMatrix(R) :
        Rt = np.transpose(R)
        shouldBeIdentity = np.dot(Rt, R)
        I = np.identity(3, dtype = R.dtype)
        n = np.linalg.norm(I - shouldBeIdentity)
        return n < 1e-6

    # ok so this function can only compute the rotation
    # from a flat triangle to rotated triangle
    def computeTransformation(self, rotated):
        assert(self.p1.z == 0 and self.p2.z == 0 and self.p3.z == 0)
        triangle.check_triangle_equal(self, rotated)

        # first we want to rotate self around z so that p1's y is equal to 0
        theta = math.atan(-self.p1.y/self.p1.x)
        self.rotate_z(theta)
        rotated_p1 = self.p1_rotated()
        if rotated_p1.x > 0:
            self.rotate_z(math.pi)
            rotated_p1 = self.p1_rotated()
        rotated_p2 = self.p2_rotated()
        rotated_p3 = self.p3_rotated()
        # check all assertion
        assert(rotated_p1.x < 0)
        assert(rotated_p2.x > 0 and rotated_p2.y < 0)
        assert(rotated_p3.y > 0)
        assert(abs(rotated_p1.y) <= DIFFERENCE_THREASHOLD)
        triangle.check_triangle_equal(rotated, rotated)

        # next we want to rotate the other one, first, again we rotate around z axis so that p1's y == 0
        theta = math.atan(-rotated.p1.y/rotated.p1.x)
        rotated.rotate_z(theta)
        rotated_p1 = rotated.p1_rotated()
        if rotated_p1.x > 0:
            rotated.rotate_z(math.pi)
            rotated_p1 = rotated.p1_rotated()
        rotated_p2 = rotated.p2_rotated()
        rotated_p3 = rotated.p3_rotated()
        assert(rotated_p1.x < 0)
        assert(abs(rotated_p1.y) <= DIFFERENCE_THREASHOLD)
        triangle.check_triangle_equal(rotated, rotated)

        # now we want to rotate around y so that p1 is at z=0
        theta = math.atan(rotated_p1.z / rotated_p1.x)
        rotated.rotate_y(theta)
        rotated_p1 = rotated.p1_rotated()
        if rotated_p1.x > 0:
            rotated.rotate_y(math.pi)
            rotated_p1 = rotated.p1_rotated()
        rotated_p2 = self.p2_rotated()
        rotated_p3 = self.p3_rotated()
        assert(rotated_p1.x < 0 and abs(rotated_p1.z) <= DIFFERENCE_THREASHOLD)
        assert(rotated_p2.x > 0 and rotated_p2.y < 0)
        assert(rotated_p3.y > 0)
        triangle.check_triangle_equal(rotated, rotated)

        # last, we rotate around x so that let's say, p3 is at z = 0
        rotated_p3 = rotated.p3_rotated()
        theta = math.atan(-rotated_p3.z / rotated_p3.y)
        rotated.rotate_x(theta)
        rotated_p3 = rotated.p3_rotated()
        if (rotated_p3.y < 0):
            rotated.rotate_x(math.pi)
            rotated_p3 = rotated.p3_rotated()
        rotated_p2 = rotated.p2_rotated()
        rotated_p1 = rotated.p1_rotated()
        assert(abs(rotated_p2.z) <=
               DIFFERENCE_THREASHOLD and rotated_p2.x >= 0 and rotated_p2.y <= 0)
        assert(abs(rotated_p3.z) <= DIFFERENCE_THREASHOLD and rotated_p3.y >= 0)
        assert(abs(rotated_p1.y) <= DIFFERENCE_THREASHOLD and abs(rotated_p1.z) <=
               DIFFERENCE_THREASHOLD and rotated_p1.x <= 0)
        triangle.check_triangle_equal(rotated, rotated)

        ## now we get the final rotation matrix
        self.rotation_matrix = rotated.rotation_matrix.transpose() * self.rotation_matrix
        r1 = self.p1_rotated()
        r2 = self.p2_rotated()
        r3 = self.p3_rotated()
        ## assert the rotated triangle actually matches the rotatted triangle
        assert((r1 - rotated.p1).length() <= DIFFERENCE_THREASHOLD)
        assert((r2 - rotated.p2).length() <= DIFFERENCE_THREASHOLD)
        assert((r3 - rotated.p3).length() <= DIFFERENCE_THREASHOLD)
        # print(self.rotation_matrix)

        ## we now compute yaw, pitch and roll
        ## https://learnopencv.com/rotation-matrix-to-euler-angles/
        assert(triangle.isRotationMatrix(self.rotation_matrix))
        sy = math.sqrt(self.rotation_matrix[0,0] * self.rotation_matrix[0,0] +  self.rotation_matrix[1,0] * self.rotation_matrix[1,0])
        singular = sy < 1e-6
        if  not singular :
            yaw = math.atan2(self.rotation_matrix[2,1] , self.rotation_matrix[2,2])
            pitch = math.atan2(-self.rotation_matrix[2,0], sy)
            roll = math.atan2(self.rotation_matrix[1,0], self.rotation_matrix[0,0])
        else :
            yaw = math.atan2(-self.rotation_matrix[1,2], self.rotation_matrix[1,1])
            pitch = math.atan2(-self.rotation_matrix[2,0], sy)
            roll = 0


        self.rotation_matrix = np.matrix(
            [[1.0, 0.0, 0], [0, 1.0, 0], [0, 0, 1.0]])

        self.rotate_x(yaw)
        self.rotate_y(pitch)
        self.rotate_z(roll)

        # print(self.rotation_matrix)
        r1 = self.p1_rotated()
        r2 = self.p2_rotated()
        r3 = self.p3_rotated()
        assert((r1 - rotated.p1).length() <= DIFFERENCE_THREASHOLD)
        assert((r2 - rotated.p2).length() <= DIFFERENCE_THREASHOLD)
        assert((r3 - rotated.p3).length() <= DIFFERENCE_THREASHOLD)
        return (yaw, pitch, roll)


f = open("sphere.obj", 'r')
points = []
faces = []
center = point(0, 0, 0)
for line in f:
    line = line.strip()
    if (line.split(" ")[0] == 'v'):
        line = line.split(" ")
        points.append(point(float(
            line[1]) * amplifier, float(line[2]) * amplifier, float(line[3]) * amplifier))
        # print(points[-1])
        # center += points[-1]
        # print(points[-1])
    elif (line.split(" ")[0] == 'f'):
        line = line.split(" ")
        p1_index = int(line[1].split('/')[0]) - 1
        p1 = points[p1_index]
        p2_index = int(line[2].split('/')[0]) - 1
        p2 = points[p2_index]
        p3_index = int(line[3].split('/')[0]) - 1
        p3 = points[p3_index]
        faces.append(triangle(p1, p2, p3, False))
        center += p1 + p2 + p3
        # print(faces[-1])
# print(center)
flat_triangles = []
rotated_triangles = []
for face in faces:
    # print(len(flat_triangles))
    flat_triangles.append(face.triangleCenteredAtOriginFlat())
    rotated_triangles.append(face.triangleCenteredAtOrigin())
    # check if those two triangles are equal, as in they are just rotation and translation difference
    triangle.check_triangle_equal(flat_triangles[-1], rotated_triangles[-1])
    triangle.check_triangle_equal(face, flat_triangles[-1])


angles = []
translates = []
deviation = 0
for i in range(len(flat_triangles)):
    flat = flat_triangles[i]
    rotated = rotated_triangles[i]
    yaw, pitch, roll = flat.computeTransformation(rotated)
    angles.append([yaw, pitch, roll])
    face = faces[i]
    # print((face.p1 - (flat.p1_rotated() + face.center())).length())
    # print((face.p3 - (flat.p3_rotated() + face.center())).length())
    if (face.p1 - (flat.p1_rotated() + face.center())).length() > 1 or (face.p2 - (flat.p2_rotated() + face.center())).length() > 1 or (face.p3 - (flat.p3_rotated() + face.center())).length() > 1:
        deviation += 1
    
    ## here we project the original triangle's center to (0, 0, 0) vector
    ## onto the three normal of the rotated triangle
    normal = flat.rotation_matrix.dot(np.array([0, 0, 1]))
    lookup = flat.rotation_matrix.dot(np.array([0, 1, 0]))
    xdir = flat.rotation_matrix.dot(np.array([1, 0, 0]))
    lhs = np.matrix([[normal[0, 0], normal[0, 1], normal[0, 2]], [
                    lookup[0, 0], lookup[0, 1], lookup[0, 2]], [xdir[0, 0], xdir[0, 1], xdir[0, 2]]]).T
    fc = face.center()
    rhs = np.array([fc.x, fc.y, fc.z])
    translate = np.linalg.inv(lhs).dot(rhs)
    translates.append([translate[0, 2], translate[0, 1], translate[0, 0]])
    # print(flat.p1_rotated() + face.center())
print("Deviation triangle count:", str(deviation))

f = open('sphere.html', 'w')
f.write('<div class="sphere-wrapper">\n')
for i in range(len(flat_triangles)):
    f.write('<div class="triangle-wrapper" id="tw' + str(i) +
            '"><div class="triangle" id="triangle' + str(i) + '"></div></div>\n')
f.write('</div>\n')

f.write('<style>\n')
f.write(
    ".triangle-wrapper{\n  width: 0px;\n  height: 0px;\n  margin-left: auto;\n  margin-right: auto;\n  transform-style: preserve-3d;\n}\n")
f.write(".sphere-wrapper{\n  width: 0px;\n  height: 0px;\n  margin-left: auto;\n  margin-right: auto;\n  transform-style: preserve-3d;\n  margin-top: 50vh;\n  margin-bottom: 100px;\n  animation-direction: alternate;\n  animation-direction: alternate;\n  animation: spin 10s alternate infinite;\n}\n")
f.write(
    ".triangle{\n  width: 0;\n  height: 0;\n  border-top:0px;\n  position:absolute;\n}\n")
for i in range(len(faces)):
    # compute how far it is away from center
    face_distance = faces[i].center().length()
    # here we calculate the dimension of the triangle
    height = flat_triangles[i].p3.y - flat_triangles[i].p1.y
    border_left = flat_triangles[i].p3.x - flat_triangles[i].p1.x
    border_right = flat_triangles[i].p2.x - flat_triangles[i].p3.x
    assert(border_left >= 0)
    assert(border_right >= 0)
    f.write("#triangle" + str(i) + "{\n")
    f.write("  border-bottom: {0}px solid;\n".format(str(round(height, 5))))
    f.write(
        "  border-left: {0}px solid transparent;\n".format(str(round(border_left, 5))))
    f.write(
        "  border-right: {0}px solid transparent;\n".format(str(round(border_right, 5))))
    f.write("  border-bottom-color: rgba({0}, {1}, {2}, 0.5);\n".format(str(150 + math.floor(
        random() * 100)), str(190 + math.floor(random() * 65)), str(195 + math.floor(random() * 55))))
    f.write("  transform: translateX(-{1}px) translateY(-{0}px);\n".format(
        str(round(flat_triangles[i].p3.y, 2)), str(round(-flat_triangles[i].p1.x))))
    f.write("}\n")
    f.write("#tw" + str(i) + "{\n")
    f.write("  transform: rotateZ({2}rad) rotateY({1}rad) rotateX({0}rad) translateX({3}px) translateY({4}px) translateZ({5}px) rotateZ(3.1415926rad);\n".format(str(round(
        angles[i][0], 10)), str(round(angles[i][1], 10)), str(round(angles[i][2], 10)), str(round(translates[i][0], 10)), str(round(translates[i][1], 10)), str(round(translates[i][2], 10))))
    f.write("}\n")


f.write("@keyframes spin { \n  0%{\n    -webkit-transform: rotateX(0deg) rotateY(0deg);\n    transform:rotateX(0deg) rotateY(0deg); \n  }\n  25%{\n    -webkit-transform: rotateX(180deg) rotateY(0deg);\n    transform:rotateX(180deg) rotateY(0deg); \n  }\n  50%{\n    -webkit-transform: rotateX(180deg) rotateY(180deg);\n    transform:rotateX(180deg) rotateY(180deg); \n  }\n  75%{\n    -webkit-transform: rotateX(270deg) rotateY(300deg);\n    transform:rotateX(270deg) rotateY(300deg); \n  }\n  100% {\n    -webkit-transform: rotateX(360deg) rotateY(180deg);\n    transform:rotateX(360deg) rotateY(180deg); \n  }\n}\n")

f.write("html{\n  background-color:black;\n}\n")

f.write('</style>\n')

# print(len(faces))
# print(flat_triangles[0])
# flat_triangles[0].rotate_x(math.pi/3).rotate_x(math.pi/3)
# print(flat_triangles[0].rotation_matrix)
