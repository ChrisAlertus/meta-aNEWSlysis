from newsplease import NewsPlease

# article format
# ['authors', 'date_download', 'date_modify',
#  'date_publish', 'description', 'filename',
#  'image_url', 'language', 'localpath', 
#  'maintext', 'source_domain', 'text',
#  'title', 'title_page', 'title_rss', 'url']
    
issue = "prostate cancer"
url = "https://www.theglobeandmail.com/canada/british-columbia/article-researchers-plan-national-program-to-bring-innovative-prostate-cancer/"
article = NewsPlease.from_url(url)

for key in article.get_dict().keys():
    print(f"{key}: {article.get_dict()[key]}")