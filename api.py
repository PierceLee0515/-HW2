import requests
import json
from datetime import datetime

# 串接 Lorem Picsum API 獲取隨機圖片資訊
url = "https://picsum.photos/v2/list?page=1&limit=1"
response = requests.get(url)
data = response.json()

# 增加擷取時間標籤
data[0]['download_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 儲存為 JSON 格式 (作業規範要求)
with open('picsum_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("資料抓取成功並已儲存為 picsum_data.json")
