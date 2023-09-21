import dlib
import os

path = os.getcwd() + '/img' + '/'
files = [
    path + 'balloon.jpg',
    path + 'barbara.jpg',
    path + 'cameraman.jpg',
    path + 'couple.jpg',
    path + 'girl.jpg',
    path + 'lenna.jpg',
    path + 'mandrill.jpg',
    path + 'parrots.jpg',
    path + 'man.jpg',
    path + 'woman.jpg',
]

# Dlibの顔検出器を初期化
detector = dlib.get_frontal_face_detector()
for f in files:
    img = dlib.load_rgb_image(f)
    # The 1 in the second argument indicates that we should upsample the image
    # 1 time.  This will make everything bigger and allow us to detect more
    # faces.
    dets = detector(img, 1)

    # 顔が検出されたかどうかをチェックして結果を出力
    # if len(dets) > 0:
    #     print('{}: {}'.format(True, f))
    # else:
        # print('{}: {}'.format(False, f))
    if len(dets) > 0:
        print('\033[92m{}: {}\033[0m'.format(True, f))
    else:
        print('\033[91m{}: {}\033[0m'.format(False, f))
