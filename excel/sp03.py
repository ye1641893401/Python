import requests
import bs4
import openpyxl

def get_html(url):
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.0; Win32; x86)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36"}
    res = requests.get(url,headers=headers).text
    return res

def get_jobinfo(html):
    jobname = []  #岗位名称
    money = []    #薪资
    company = []   #公司名
    recruitment = []  #岗位需求
    temptation = []  #职位诱惑
    description = [] #岗位描述
    companyinfo = [] #公司信息

    soup = bs4.BeautifulSoup(html,"html.parser")
    targets = soup.find("div",class_ = "cn")
    money.append(targets.strong.text)
    jobname.append(targets.h1.text.strip())
    #print(jobname)

    targets = soup.find("p",class_ = "cname")
    company.append(targets.a.text.strip())

    targets = soup.find("p",class_ = "msg ltype")
    recruitment.append(targets.text.strip())

    targets = soup.find("div",class_="t1")
    temptation.append(targets.text.strip())

    targets = soup.find("div",class_ = "bmsg job_msg inbox")
    description.append(targets.text.strip())

    targets = soup.find("div",class_ = "tmsg inbox")
    companyinfo.append(targets.text.strip())
    #print(companyinfo)

    allinfo = jobname + money + company + recruitment + temptation + description + companyinfo
    return allinfo

def write_info(allinfo):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["岗位名称","薪资","公司名称","岗位需求","岗位诱惑","岗位描述","公司介绍"])
    ws.append(allinfo)
    wb.save("51job.xlsx")

if __name__ == "__main__":
    url = "https://jobs.51job.com/guangzhou-thq/97196004.html?s=01&t=0"
    html = get_html(url)
    allinfo = get_jobinfo(html)
    write_info(allinfo)
