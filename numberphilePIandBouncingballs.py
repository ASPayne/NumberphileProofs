# based off of a video by Numberphile
# https://youtu.be/abv4Fz7oNr0
# PURPOSE
# determine the number times it takes for the 
# Acceleration of a large ball to become negetive

#----------------------------------------------------------
# PHYSICS NOTES

# notes from
# https://www.physicsclassroom.com/calcpad/momentum
#  Momentum (p) possessed by the moving object is the 
#  product of mass (m) and velocity (v). In equation form:
#                      p = m • v

#  The momentum change experienced by object 1 is equal in
#  magnitude and opposite in direction to the momentum 
#  change experienced by object 2. This statement could be
#  written in equation form as
#              m1 • Delta v1 = - m2 • Delta v2

#  The sum of the momentum of object 1 and the momentum of
#  object 2 before the collision is equal to the sum of the
#  momentum of object 1 and the momentum of object 2 after
#  the collision. The following mathematical equation is
#  often used to express the above principle.
#         m1 • v1 + m2 • v2 = m1 • v1' + m2 • v2'

# Other notes
#  taking the third equation listed above as well as the 
#  equation of conservation of kenetic energy (not listed)
#  we can derive the last equations used for determining
#  the velocities after the collision
#     v1f =   (((m1 - m2) / (m1 + m2)) * v1i) 
#           + (((2 * m2) / (m1 + m2)) * v2i)
#  and 
#     v2f =   (((m2 - m1) / (m1 + m2)) * v2i) 
#           + (((2 * m1) / (m1 + m2)) * v1i) 

#----------------------------------------------------------
# for purposes of not dividing or multiplying by one, 
# zero or by a small number that can cause a strange 
# values (suech as 2), the value of m (the small object)
# will be a prime.
m = 7

# As explained in the video, N is a multiple. 
# This number can be changed throughout testing
N = 2

# As explained in video, M is the mass of large object
# and is defined by
# M = 16 x 100^N m
M = 16 * pow(100, N) * m

# For similar purposes as the mass of the small object,
# the starting velocity for the large object will 
# be a positive prime number to start.
Mveloc = 11

# The starting velocity for the small object is zero
# because the large object has not yet collided with it.
mveloc = 0

#-------------------------------------------------------

# Display staring values
print("+----------------+")
print("| INITIAL VALUES |")
print("+----------------+")
print("N =                    ", N)
print("mass of small object = ", m)
print("mass of large object = ", M)
print("vol of small object =  ", mveloc)
print("vol of large object =  ", Mveloc)
print("\n")

#------------------------------------------------------
print("+--------------------------+")
print("| SIMULATION OF COLLISIONS |")
print("+--------------------------+")
print("\n")

NumOfCollision = 0
# ----COLLISION LOOP-----
while Mveloc > 0:

#  ----Large object collides with small object----
#   create temporary initial variables for both objects 
#   velocities
	tempMveloc = Mveloc
	tempmveloc = mveloc

	print("\n *objects collide* ")
    
	NumOfCollision += 1
#   Determine the final velocity of small object after 
#   collision (equation 4)
	mveloc = (((m - M) / (M + m)) * tempmveloc) + (((2 * M) / (M + m)) * tempMveloc)


#   Determine the final velocity of large object after 
#   collision (equation 4)
	Mveloc = (((M - m) / (M + m)) * tempMveloc) + (((2 * m) / (M + m)) * tempmveloc)

#   display new velocities
	print("vol of small after collision = ", mveloc)
	print("vol of large after collision = ", Mveloc)

#  ----small object bounces against back wall----
	mveloc = -1 * mveloc

	print("\n")
	print("vol of small after hitting wall = ", mveloc)
	

print("\n")
print("Number of times objects collided = ", NumOfCollision)