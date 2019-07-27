# NLP 2019 @ Arts Chula : teaching materials
|week - date| lab | Programing Assignment |
|:-:|:-:|:-:|
|week1 - 15/8|[week1_lab](https://github.com/nozomiyamada/NLP2019/tree/master/week1/week1_lab)|[PA1](https://github.com/nozomiyamada/NLP2019/tree/master/week1/PA1)|
|week2 - 22/8|[colab](https://colab.research.google.com/drive/1f4UQh-U7U3kWh7tDVB1hd9HOV2zrEZP_)|PA2|
|week3 - 29/8|||
|week4 - 5/9|||

## Q&A 
## ทำไมต้องเรียนการเขียนโปรแกรม? มีประโยชน์อย่างไร

-> https://www.youtube.com/watch?v=Dc7Q9p6YepE <br>
-> https://www.youtube.com/watch?v=sbaLxwUdrI4

## ไม่เก่งคณิต เรียนไหวไหม?
ต้องการบางส่วน แต่ไม่มาก ที่สำคัญก็คือการคิดแบบ logically และทักษะ problem solving

## ทำไมใช้ Python
- ไวยากรณ์ค่อนข้างง่าย -> [comparing programming languages](https://github.com/nozomiyamada/NLP2019/issues/2)<br>
  ลองได้ที่นี่ [CodeChef](https://www.codechef.com/ide)
- มี interactive interpreter ซึ่งทำให้เช็คผลง่ายขึ้น
- มี package(library) สำหรับ machine learning จำนวนมาก
- (ข้อเสีย: ช้า)

## interactive interpreter คืออะไร

interface ที่สามารถรันโปรแกรมทีละบรรทัดได้ (เขียนโค้ดไว้แล้ว รันทีเดียวก็ได้)

jupyter notebook (ไฟล์จะเป็น .ipynb)
![jupyter](https://user-images.githubusercontent.com/44984892/61967609-04e33b00-b000-11e9-85ae-9f1d7b048a6b.png)

คนที่ใช้ mac ไม่ต้องดาวนโหลดก็มีอยู่แล้ว <br>เปิด terminal > พิมพ์ `ipython`
![ipython](https://user-images.githubusercontent.com/44984892/61967950-e9c4fb00-b000-11e9-9f78-ce3deff8d6f3.png)

online editor: google colabolatory (ดีกว่า jupyter เยอะ)

https://colab.research.google.com/notebooks/welcome.ipynb
![colab](https://user-images.githubusercontent.com/44984892/61969994-07489380-b006-11e9-9ae6-6b424ca398da.png)

## ใช้ software อะไรดี
ควรใช้ IDE (integrated development environment) ซึ่งทำได้ทุกอย่าง เช่น เขียน รัน debug อัพโหลด ฯลฯ

Anaconda มี application หลายอย่างรวม IDE -> [วิธีติดตั้ง Anaconda](https://docs.google.com/document/d/15UdZINoQhB8zAWBCMKoAofSxQUmDMXoaz-iibF2IkZ4/edit?usp=sharing)

แรกๆ แนะนำใช้สองอันนี้ที่มีอยู่ใน Anaconda

- jupyter notebook (หรือ google colaboratory) เป็น interactive interpreter
- spyder เป็น IDE เพราะดูง่าย -> [วิธีใช้ (youtube)](https://www.youtube.com/watch?v=a1P_9fGrfnU)

หลังๆ เริ่มใช้ IDE ที่มีฟังก์ชันเยอะ เช่น

- PyCharm
- Visual Studio Code (by Microsoft)
- Atom (by GitHub & Facebook)

## package คืออะไร install อย่างไร
package (library) เป็นชุดฟังก์ชั่น package ที่ใช้บ่อยมีอยู่ใน Anaconda แล้ว

ตัวอย่าง package
- numpy: ฟังก์ชั่นเกี่ยวกับคณิตศาสตร์
- pandas: ฟังก์ชั่นเกี่ยวกับการจัดการข้อมูลแบบ spread sheet
- pythainlp: ฟังก์ชั่นเกี่ยวกับการประมวลผลภาษาไทย
- scikit-learn: ฟังก์ชั่นเกี่ยวกับ Machine Learning
- keras: ฟังก์ชั่นเกี่ยวกับ Deep Learning (ส่วงหนึ่งของ Machine Learning)

ถ้าต้องการอย่างอื่นก็จะสามารถดาวนโหลดได้ เปิด anaconda prompt (windows) / terminal (mac) แล้ว พิมพ์ว่า

`pip install XXXXX`

![pip](https://user-images.githubusercontent.com/44984892/61989202-ec057480-b055-11e9-8192-516a34bed675.png)

เขียน `import XXXXX` ในโค้ดก็จะใช้ได้
