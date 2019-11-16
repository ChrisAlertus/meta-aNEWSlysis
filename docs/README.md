# NLP News: identifying how health issues are discussed in the news cycle around Canada

## Project components

This project is aimed at developing toooling to do a few things:
- Keep a track of major news coverage of specific health issues within Canada
- Compare and contrast the sentiment associated with the particular issues globally across the country and locally within sub-regions
- Identify trending sentiment and interest in particular issues to allow for earlier awareness or concentrate efforts
- Also help to compare the coverage level for particualr issues as compared to their overall mortality impact in the country

### Major scripts
getIssueArticleUrls.py: website -> list of URLs
scrapeArticle.py: url -> ArticleObject
analyzeArticle: ArticleObject -> None
analyzeWebsiteCoverage.py-> list of URLs -> data frame of article sentiment, statistics, metadata, date
- num distinct journalists covering, time between articles, , number year to date for website, number ytd for all
- 
reportFindings.py-> dataframe of article sentiment -> 