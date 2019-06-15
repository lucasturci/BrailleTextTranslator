import imageio
import numpy as np
import matplotlib.pyplot as plt

# normalizes image pixels between 0 and 255
def normalize(img):
	imin = np.min(img)
	imax = np.max(img)

	return (((img - imin)/(imax - imin)) * 255).astype(np.float)

# Prints image with minimum value equal to 0 and maximum to 255
def printImage(img):
	plt.figure(figsize=(16,8)) 
	plt.imshow(mat, cmap="gray", vmin=0, vmax=255)
  
# Prints image with matplotlib defaults  
def printImage2(img):
	plt.figure(figsize=(16,8)) 
	plt.imshow(mat, cmap="gray")

# Median difference filter, highlights the shadow pixels
def filter(I, n):
	m = n//2
	J = np.empty(I.shape, dtype=np.float)
	N, M = I.shape
	I = np.pad(I, ((m, m), (m, m)), 'symmetric')

	for i in range(N):
		for j in range(M):
			sub = I[i+m:(i+m+n), j+m:(j+m+n)]
			med = np.median(np.ravel(sub)) # gets median
			J[i, j] = abs(I[i+m, j+m] - med) # applies the difference
	return J

# applies mean filter to image I
def MeanFilter(I, n):
	m = n//2
	J = np.empty(I.shape, dtype=np.float) # the answer
	N, M = I.shape
	I = np.pad(I, ((m, m), (m, m)), 'symmetric')
	for	i in range(N):
		for j in range(M):
			# copies the matrix to sub
			sub = I[i+m:(i+m+n), j+m:(j+m+n)]
			J[i, j] = np.mean(np.ravel(sub)) # get mean of the linearized list
	return J

filename = str(input()).rstrip() # filename of the input image
image = imageio.imread(filename)
matrix = np.array(image, copy=True, dtype=np.float)

N, M, _ = matrix.shape

# Transform RGB to gray scale
for i in range(N):
	for j in range(M):
		matrix[i, j, 0] = matrix[i, j, 0] * 0.2989 + matrix[i, j, 1] * 0.5870 + matrix[i, j, 2] * 0.1140
    
matrix = matrix[:, :, 0:1].squeeze()

# Plot original image
mat = matrix.astype(np.uint8)
printImage(mat)

matrix = normalize(matrix)
dots_matrix = filter(matrix, 21) # Applies filter to normalized matrix
dots_matrix = normalize(dots_matrix)

# Smooth image using mean filter, to reduce noise
dots_matrix = MeanFilter(dots_matrix, 3)

# Thresholding step, 30 is arbitrary value derived from testing with images, but independent of input image gray scale
for i in range(N):
	for j in range(M):
		dots_matrix[i, j] = 0 if dots_matrix[i, j] < 30 else 1

#
#

#	Now we want to ignore some white regions, which must not be seen as braillee circles
#	To do that, we can use image description of our pattern, and use the comparison result to decide to keep or ignore some region 
#	The parameters that must be considered to describe the circles are the colour description, its size in pixels, and its centrality in the image
#	To describe our pattern, we can calculate the mean of the histograms, using centrality as a weight
#	The size of the regions can be used to already discard some regions beforehand (this can be applied optionally) 
#
#
#
#

def pointsInComponent(i, j, pts):
	vis[i, j] = 1
	pts.append((i, j))
	if i + 1 < N and vis[i+1, j] == 0 and dots_matrix[i+1, j] == 1: pointsInComponent(i+1, j, pts)
	if i - 1 >=0 and vis[i-1, j] == 0 and dots_matrix[i-1, j] == 1: pointsInComponent(i-1, j, pts)
	if j + 1 < M and vis[i, j+1] == 0 and dots_matrix[i, j+1] == 1: pointsInComponent(i, j+1, pts)
	if j - 1 >=0 and vis[i, j-1] == 0 and dots_matrix[i, j-1] == 1: pointsInComponent(i, j-1, pts)

vis = np.zeros((N, M))
# Retrieve components (white regions) and its pixels
comp = []
for i in range(N):
	for j in range(M):
		if vis[i, j] == 0 and dots_matrix[i, j] == 1:
			comp.append([])
			pointsInComponent(i, j, comp[-1])


# Calculate histograms of each region using list comprehension
histograms = [
	np.histogram(np.array([matrix[x] for x in pts]), bins=256, range=(0, 255))[0] 
	for pts in comp
]



# Plot segmented image
mat = dots_matrix.astype(np.uint8)
printImage2(mat)

plt.show()