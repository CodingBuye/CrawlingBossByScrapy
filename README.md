# CrawlingBossByScrapy
用scrapy爬取Boss直聘职位信息

### 1. 新建项目
- (1) 打开cmd，进入到项目准备所放在的文件夹，执行命令：
    scrapy startproject Boss
- (2) 建立spider文件：
    cd Boss
    scrapy genspider boss_spider www.zhipin.com(爬取的网站的域名)

### 2. 明确目标
- 参看网站：https://www.zhipin.com/job_detail/?ka=header-job
- 确定我们要爬取的信息，在items.py定义数据结构:
    - 职位名称：job_name
    - 月薪：monthly_salary
    - 公司名称：company_name
    - 公司地址：company_addr
    - 公司类型：company_type
    - 公司规模：company_size
    - 是否上市：is_listed
    - 工作经验：experience
    - 学历：education


