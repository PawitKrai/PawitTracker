# PawitTracker ไลบรารี่สำหรับใช้ติดตามรายชื่อคนที่ยังไม่ทำ COVID-19 DAILY REPORT ส่งไปยัง Line Application

PyPi: https://pypi.org/project/PawitTracker/0.1/


### Generate Line Notify TOKEN
https://notify-bot.line.me/th/

### ดาว์นโหลด ChromeDriver ให้ตรงกับ Version ของตนเอง
https://chromedriver.chromium.org/downloads

### วิธีติดตั้ง

เปิด CMD / Terminal

```python
pip install PawitTracker
```

### วิธีใช้งานแพ็คเพจนี้

- เปิด IDLE ขึ้นมาแล้วพิมพ์...

```python
from PawitTracker import SmartTracker

g1 = ['Olivia Wilde' , 'Reese Witherspoon' , 'Bruno Mars']
g2 = [...]
g3 = [...]
g4 = [...]
g5 = ['Gigi Hadid' , ... , 'Pawit Kraisornnukhor']
Group = {'PEI-1':g1,'PEI-2':g2,'CMS':g3,'PIP':g4,'MCAS':g5}

Track = SmartCovid('LINE NOTIFY TOKEN','USER PTTGC','PASSW','TIME_ALARM',Group)
Track.screenweb() #แคปหน้าจอรายงานโควิด
Track.run() #เผื่อ y = ทำเลย n = ตามที่ตั้งเวลา reset = ใส่เวลาใหม่ เช่น '15:29'


```

พัฒนาโดย: Pawit Kraisornnukhor
FB: https://web.facebook.com/jamecdtz.pawit/
