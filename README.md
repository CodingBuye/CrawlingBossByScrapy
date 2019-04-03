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
    
### 3. 爬虫文件的编写
- 在boss_spider文件中确认爬虫名称、允许域名以及入口的url
    - name：爬虫名称，不能与项目名相同
    - allowed_domains：允许的域名
    - start_urls：入口url
- 在解析函数parse中加入：
    print(response.text)
- cd到spiders文件夹下，输入命令：
    - scrapy crawl boss_spider
    - 测试是否能正常返回数据,正常情况下会返回爬虫信息和解析的文件
- 在返回的信息中会发现返回的403信息，主要是由settings.py文件中USER_AGENT不当引起的
    - 打开浏览器的开发者工具，定位到Network那一栏
    - 找到入口url点进去，在headers中找到Request Headers下的user agent,将其复制之后覆盖settings.py文件中的USER_AGENT
    - 再次运行上方的命令(scrapy crawl boss_spider),信息比原来增加了很多，返回了爬取的网址的首页内容
- 设置启动文件(避免频繁执行上方命令)
    - 创建main.py文件，与items.py同级
    - 添加内容(请查看main.py)文件，运行之后可在控制台查看打印的信息
- 重点：解析文件(parse函数)
    - 需要用到xpath，可查看w3school提供的手册
    - 可在chrome浏览器中安装xpath的插件，打开开发者工具之后即可在网页上写xpath规则检验是否正确
    - 具体实现查看boss_spider.py
### 4. 数据存储
- 保存爬取的数据为json文件：
    - cd到Boss文件夹下
    - 输入命令：scrapy crawl boss_spider -o job.json
- 保存爬取的数据为csv文件：
    - cd到Boss文件夹下
    - 输入命令：scrapy crawl boss_spider -o job.csv
- 保存爬取的数据到mongodb
    - 在settings.py文件中配置mongodb的基本信息：
        - mongo_host = "127.0.0.1"
        - mongo_port = 27017
        - mongo_db_name = "boss"
        - mongo_db_connection = "boss_job" 
    - 在pipelines.py中进行数据库相关的编写,详情见文件
    - 记得开启settings.py中的ITEM_PIPELINES，即去掉前面的注释，否则会找不到数据库文件
    


