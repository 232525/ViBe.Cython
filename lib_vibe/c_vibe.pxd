# -*- coding: utf-8 -*-
"""
Created on 2020/7/20

@author: curya
"""
cdef extern from "vibe-background-sequential.h":
    ctypedef unsigned char            uint8_t
    ctypedef unsigned short int         uint16_t
    ctypedef unsigned int             uint32_t
    ctypedef int                   int32_t
        
    ctypedef struct vibeModel_Sequential_t:
        pass
    
    vibeModel_Sequential_t *libvibeModel_Sequential_New()
    int32_t libvibeModel_Sequential_Free(vibeModel_Sequential_t *model)
    int32_t libvibeModel_Sequential_AllocInit_8u_C1R(vibeModel_Sequential_t *model, const uint8_t *image_data, 
                                                     const uint32_t width, const uint32_t height)
    int32_t libvibeModel_Sequential_Segmentation_8u_C1R(vibeModel_Sequential_t *model, const uint8_t *image_data, uint8_t *segmentation_map)
    int32_t libvibeModel_Sequential_Update_8u_C1R(vibeModel_Sequential_t *model, const uint8_t *image_data, uint8_t *updating_mask)