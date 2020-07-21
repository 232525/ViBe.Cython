# -*- coding: utf-8 -*-
"""
Created on 2020/7/20

@author: curya
"""
import cv2
import numpy as np
import time
from lib_vibe.py_vibe import ViBe

cap = cv2.VideoCapture('./***.avi')
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
video_out = cv2.VideoWriter('./***_detectioin.avi', fourcc, fps, (frame_width, frame_height), False)

vibe = ViBe()

frame_cnt = 0
segmentation_time = 0
update_time = 0
t1 = time.time()
while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if frame_cnt == 0:
        vibe.AllocInit(gray_frame)
        
    t2 = time.time()
    segmentation_map = vibe.Segmentation(gray_frame)
    segmentation_map = np.array(segmentation_map, np.uint8)
    
    video_out.write(segmentation_map)
    
    t3 = time.time()
    vibe.Update(gray_frame, segmentation_map)
    
    t4 = time.time()
    segmentation_time += (t3-t2)
    update_time += (t4-t3)
    print('Frame %d, segmentation: %.4f, updating: %.4f' % (frame_cnt, t3-t2, t4-t3))

    frame_cnt += 1
t5 = time.time()
cap.release()
video_out.release()
print('All time cost %.3f' % (t5-t1))
print('segmentation time cost: %.3f, update time cost: %.3f' % (segmentation_time, update_time))