import cv2

# 列出可用的鏡頭設備
devices = [0, 1, 2, 3]  # 可能的鏡頭設備索引

for device in devices:
    cap = cv2.VideoCapture(device)
    if cap.isOpened():
        print(f"鏡頭設備 {device} 開啟成功")
        cap.release()
    else:
        print(f"無法開啟鏡頭設備 {device}")
