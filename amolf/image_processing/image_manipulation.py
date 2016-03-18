import numpy as np

def downsizeStack( stack, scaleFactor ):

	"""
	This function downsizes an image (3D numpy array) by a scale factor (int).

	input:
		- stack: 3D numpy array with shape (dim0,dim1,dim2), the function only works if dim1=dim2.
		- scaleFactor (int): compression factor
	output:
		- smallstack: 3D numpy arra with shape (dim0,dim1/scaleFactor,dim2/scaleFactor)
	"""

    smallstack = []

    for img in stack:
        Nbig = img.shape[0]
        Nsmall = img.shape[0]/scaleFactor
        smallimg = ( img.reshape([Nsmall, Nbig/Nsmall, Nsmall, Nbig/Nsmall]).mean(3).mean(1) ).astype(np.uint16)
        smallstack.append( smallimg )
    smallstack = np.array(smallstack)

    return smallstack

def crop_image( imgs, c, size ):

	"""
	This function crops all the frames in a 3D image around a center c with a certain size (square). 
	It takes into account for black borders in case the center is too close to the edge of the original image.

	input:
		- imgs: 3D numpy array with shape (dim0,dim1,dim2), the function only works if dim1=dim2.
		- c (int array): the center of the region to be cropped
		- size (int): the size of the cropped image
	output:
		- cropstack: 3D numpy arra with shape (dim0,size,size)
	"""

    # print(imgs.shape, c,size)
    dim = imgs.shape

    if len(imgs.shape) == 3:
        cropstack = np.zeros( ( imgs.shape[0], size, size ) )

        cropstack[ : , 
                    -np.min( [ c[1]-size/2, 0 ] ) : size-np.max( [ c[1]+size/2-dim[1]+1, 0 ] ) , 
                    -np.min( [ c[0]-size/2, 0 ] ) : size-np.max( [ c[0]+size/2-dim[2]+1, 0 ] ) ] = imgs[ :,
                    np.max( [ c[1]-size/2, 0 ] ) : np.min( [ c[1]+size/2, dim[1]-1 ] ) , 
                    np.max( [ c[0]-size/2, 0 ] ) : np.min( [ c[0]+size/2, dim[2]-1 ] ) ]
    if len(imgs.shape) == 2:
        cropstack = np.zeros( ( size, size ) )

        cropstack[
                    -np.min( [ c[1]-size/2, 0 ] ) : size-np.max( [ c[1]+size/2-dim[1]+1, 0 ] ) , 
                    -np.min( [ c[0]-size/2, 0 ] ) : size-np.max( [ c[0]+size/2-dim[2]+1, 0 ] ) ] = imgs[
                    np.max( [ c[1]-size/2, 0 ] ) : np.min( [ c[1]+size/2, dim[1]-1 ] ) , 
                    np.max( [ c[0]-size/2, 0 ] ) : np.min( [ c[0]+size/2, dim[2]-1 ] ) ]

    return cropstack