"""
Created on 2020/7/20

@author: curya
"""
# refer to: 
# https://cython.readthedocs.io/en/latest/src/userguide/memoryviews.html#pass-data-from-a-c-function-via-pointer
# https://moonlet.gitbooks.io/cython-document-zh_cn/content/ch3-using_c_libraries.html
# https://github.com/cython/cython/blob/master/Demos/libraries/setup.py
# https://stackoverflow.com/questions/14657375/cython-fatal-error-numpy-arrayobject-h-no-such-file-or-directory
import numpy as np
cimport numpy as np
cimport c_vibe

ctypedef unsigned char            uint8_t
ctypedef unsigned short int         uint16_t
ctypedef unsigned int             uint32_t
ctypedef int                   int32_t
    
cdef class ViBe:
    cdef c_vibe.vibeModel_Sequential_t* model
    def __cinit__(self):
        self.model = c_vibe.libvibeModel_Sequential_New()
        if self.model is NULL:
            raise MemoryError()
    
    def __dealloc__(self):
        if self.model is not NULL:
            c_vibe.libvibeModel_Sequential_Free(self.model)

    def AllocInit(self, uint8_t[:, :] image):
        cdef uint32_t width = <uint32_t>image.shape[1]
        cdef uint32_t height = <uint32_t>image.shape[0]

        # &image_data[0, 0] --> the pointer of image
        cdef uint8_t *image_data_ptr = &image[0, 0]

        # call C function
        cdef int32_t back
        back = c_vibe.libvibeModel_Sequential_AllocInit_8u_C1R(self.model, image_data_ptr, width, height)

    def Segmentation(self, uint8_t[:, :] image):        
        cdef int width = image.shape[1]
        cdef int height = image.shape[0]
        
        # cdef np.ndarray[uint8_t, ndim=2] segmentation = np.zeros([width, height], dtype=np.uint8)
        cdef uint8_t[:, :] segmentation_map = np.empty((height, width), dtype=np.uint8)
        
        
        cdef uint8_t *image_data_ptr = &image[0, 0]
        cdef uint8_t *segmentation_map_ptr = &segmentation_map[0, 0]
        
        # call C function
        cdef int32_t back
        back = c_vibe.libvibeModel_Sequential_Segmentation_8u_C1R(self.model, image_data_ptr, segmentation_map_ptr)
        # Error: need convert segmentation_map to numpy.array
        # return segmentation_map
        return np.asarray(segmentation_map)

    def Update(self, uint8_t[:, :] image, uint8_t[:, :] segmentation):
        cdef uint8_t *image_data_ptr = &image[0, 0]
        cdef uint8_t *updating_mask_ptr = &segmentation[0, 0]
        
        # call C function
        cdef int32_t back
        back = c_vibe.libvibeModel_Sequential_Update_8u_C1R(self.model, image_data_ptr, updating_mask_ptr)
