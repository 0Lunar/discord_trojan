def cam_snap():
    import cv2
    cam = cv2.VideoCapture(0)
    img_counter = 0
    while img_counter != int(20):
        ret, frame = cam.read()
        img_counter += 1
    img_name = "photo.png".format(img_counter)
    cv2.imwrite(img_name, frame)
    cam.release()
