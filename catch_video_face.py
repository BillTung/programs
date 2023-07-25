import cv2
import os

def extract_frames(video_path, output_path):
    # 確認目標資料夾存在，若不存在則建立
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 使用OpenCV讀取影片
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    # 逐偵讀取影片並儲存畫面
    while True:
        # 讀取影格
        ret, frame = cap.read()

        # 若影格讀取失敗，則結束迴圈
        if not ret:
            break

        # 儲存影格到目標資料夾
        frame_path = os.path.join(output_path, f"Elion_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)

        # 增加影格計數器
        frame_count += 1

    # 釋放資源
    cap.release()

    print(f"影片處理完成！共儲存 {frame_count} 個影格。")

# 測試程式碼
video_path = r"C:\Users\Jenny\Desktop\topic2\Face_cut_Zuan\Zuan.mp4"  # 影片檔案路徑
output_path =r"C:\Users\Jenny\Desktop\topic2\Face_cut_Zuan\Zuan"  # 目標資料夾路徑

extract_frames(video_path, output_path)
