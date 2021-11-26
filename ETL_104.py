import requests
import os
from bs4 import BeautifulSoup
import json
import time

if not os.path.exists('./104_JOB_React'):
    os.mkdir('./104_JOB_React')


userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
headers = {
    "User-Agent": userAgent
}

landingUrl= "https://www.104.com.tw/jobs/search/?ro=0&keyword=React"

datastr="""ro: 0
kwop: 11
keyword: React
expansionType: job
order: 14
asc: 0
page: 1
mode: s
langFlag: 0"""

data ={r.split(': ')[0]: r.split(': ')[1] for r in datastr.split('\n')}
# print(data)

ss = requests.session()

for i in range(0,5):

    res = requests.get(landingUrl, headers=headers,data=data)
    soup = BeautifulSoup(res.text, "html.parser")
    article_title_html = soup.select('article[class="b-block--top-bord job-list-item b-clearfix js-job-item"]')

    # print(article_title_html)

    for each_article in article_title_html:
        Job_Post_time = each_article.select('span[class="b-tit__date"]')[0].text.replace(' ','')
        Job_title = each_article['data-job-name']
        Job_company = each_article['data-cust-name']
        content_Key = each_article.a['href'].replace('//','').split('b/')[1][0:5]
        article_url = str('https://'+each_article.a['href'].replace('//',''))

        print(article_url)
        headers1 = {
            "User-Agent": userAgent,
            "Referer": article_url
                    }
        Job_content_url = 'https://www.104.com.tw/job/ajax/content/'+content_Key
        # print(Job_content_url)

        res_Job_content_url = ss.get(Job_content_url, headers=headers1)

        soup_res_Job_content_url = BeautifulSoup(res_Job_content_url.text, "html.parser").text
        # print(soup_res_Job_content_url)
        jobDescription_json = json.loads(soup_res_Job_content_url)['data']['jobDetail']['jobDescription']
        # print(content_json)
        Job_Article = str(Job_Post_time)+str(Job_title)+'\n'+str(Job_company)+'\n'+str(article_url)+'\n'+str(jobDescription_json)
        # print(Job_Article)

        try:
            with open('./104_JOB_React/{}.txt'.format(Job_title).replace("|",""), 'w', encoding="utf-8") as f:
                f.write(Job_Article)
        except FileNotFoundError as e:
            print('==========')
            print(article_url)
            print(e.args)
            print('==========')
        # # article_text = each_article.text.replace('\n','')
        print(Job_Post_time)
        print(Job_title)
        print(Job_company)
        print(article_url, end='\n\n')
        # print(jobDescription_json)
        print('=======')

    data['page'] = str(int(data['page']) + 1)
    time.sleep(5)
        #
