import requests
import telegram
from bs4  import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler


bot = telegram.Bot(token = '816580560:AAENpbomNq7kMD-XZ7ujC1z-Oid9AW2Qjog')
url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190923"

def job_function():
    html = requests.get(url)

    soup = BeautifulSoup(html.text,'html.parser')
    forDX = soup.select_one('span.forDX')

    if(forDX):
        forDX = forDX.find_parent('div',class_='col-times')
        title = forDX.select_one('div.info-movie > a > strong').text.strip()
        bot.send_message(chat_id = 568425088, text = title + "4DX 예매가 열렸습니다.")
        sched.pause()
   

sched = BlockingScheduler()
sched.add_job(job_function,'interval',seconds=30)
sched.start()