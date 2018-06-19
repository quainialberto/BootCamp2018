import numpy as np

def projectEulerFoo():
    grid = np.load("grid.npy")
    horizontalMax = np.max(
            grid[:,:-3] * grid[:,1:-2] * grid[:,2:-1] * grid[:,3:]
            )
    verticalMax = np.max(
            grid[:-3,:] * grid[1:-2,:] * grid[2:-1,:] * grid[3:,:]
            )
    rightDiagonalMax = np.max(
            grid[:-3,:-3] * grid[1:-2,1:-2] * grid[2:-1,2:-1] * grid[3:,3:]
            )
    leftDiagonalMax = np.max(
            grid[3:,:-3] * grid[2:-1,1:-2] * grid[1:-2,2:-1] * grid[:-3,3:]
            )
    vector = [horizontalMax, verticalMax, rightDiagonalMax, leftDiagonalMax]
    return vector

vector = projectEulerFoo()
print( "Horizontal max is " + str(vector[0]) )
print( "Vertical max is " + str(vector[1]) )
print( "Right diagonal max is " + str(vector[2]) )
print( "Left diagonal max is " + str(vector[3]) )
