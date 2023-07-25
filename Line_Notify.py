# Line Notify
import time
import requests

#Line 推播函數,設定輸入參數(小時,幾分,幾秒,"申請的line_token",要輸入的資訊)
def line_notify(hours,minute,sec,line_token,msg):
    # 取得現在時間
    now = time.localtime()
    # 如果現在時間是設定的時間，就執行推播
    if now.tm_hour == hours and now.tm_min == minute and now.tm_sec == sec:
        # 連結 Line 進行推播
        line_url = "https://notify-api.line.me/api/notify"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + line_token,
        }
        msg = f"\n目前學生到班狀況:\n{msg}"
        payload = {'message': msg }
        r = requests.post(line_url, headers = headers, params = payload)
        
        
        
        
    
    
    
"""# 設定每天推播時間
hours = 23
minute = 32
print("設定推播時間 ok")
while True:
# 取得現在時間
now = time.localtime()

# 如果現在時間是設定的時間，就執行推播
if now.tm_hour == hours and now.tm_min == minute:
# 讀取資料

# 連結 Line 進行推播
line_token = "mIipERHuIVa7x4r2FeyVDU19oJMmPkxkxU0hie0PzV1"
line_url = "https://notify-api.line.me/api/notify"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + line_token,
}
msg = f"最新資料: "
payload = {'message': msg }
r = requests.post(line_url, headers = headers, params = payload)
print(r.text)
# 等待下一分鐘
time.sleep(60 - now.tm_sec)"""



"""line_token = "mIipERHuIVa7x4r2FeyVDU19oJMmPkxkxU0hie0PzV1"
line_url = "https://notify-api.line.me/api/notify"

headers = {
    "Authorization": "Bearer " + line_token, 
    "Content-Type" : "application/x-www-form-urlencoded"
}

msg = f"董先生: {time.strftime('%Y/%m/%d')} 您關心的股票殖利率已經更新完畢！"

payload = {'message': msg }
r = requests.post(line_url, headers = headers, params = payload)"""