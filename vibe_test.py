frame_cnt = 0
read_time = 0
write_time = 0
segmentation_time = 0
update_time = 0
t1 = time.time()
while True:
    t_ = time.time()
    ret, frame = cap.read()
    if not ret:
        break
        
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    t__ = time.time()
    read_time += (t__ - t_)
    
    if frame_cnt == 0:
        vibe.AllocInit(gray_frame)
        
    t2 = time.time()
    segmentation_map = vibe.Segmentation(gray_frame)
    t3 = time.time()
    
    tw_ = time.time()
    video_out.write(segmentation_map)
    tw__ = time.time()
    write_time += (tw__-tw_)
    
    t3_ = time.time()
    vibe.Update(gray_frame, segmentation_map)
    t4 = time.time()
    
    segmentation_time += (t3-t2)
    update_time += (t4-t3_)
    print('Frame %d, read: %.5f, write: %.5f, segmentation: %.5f, updating: %.5f' % (frame_cnt, t__-t_, tw__-tw_, t3-t2, t4-t3_))

    frame_cnt += 1
t5 = time.time()
cap.release()
video_out.release()
print('All time cost %.3f' % (t5-t1))
print('read time cost: %.3f, write time cost: %.3f, segmentation time cost: %.3f, update time cost: %.3f' % (read_time, write_time, segmentation_time, update_time))