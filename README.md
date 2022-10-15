# Loop News Scrapper- (Selenium and BeautifulSoup)
The target website for this bot is dynamic. Unlike static websites, dynamic sites use Js to render content. This bot adopts selenium and firefox web driver to load content, and the response is parsed by bs4. The data was used to study how news affect stock prices for 8 companies for a specified period.  

_**start_requests**_ function is called by _**main**_  at the start with keyword and p parameters. **keyword parameter** is a specific company's trading symbol. **p parameter** is the search result page numbers. The response is converted to bs4 object and all data from main block is extracted, consequently article links are extracted and stored in a list. _**start_requests**_ calls _**parse_pages**_ function and supplies the list of links to it.

_**parse_pages**_ function visits each article link from the list and scrolls to the bottom of the page to ensure all content is rendered. Date, headline and content of each page is appended to df , each in its respective column. Once data from all links is extracted and stored to data frame, the resulting data frame is written in append mode to a csv file whose name is the keyword supplied to the _**start_requests**_.

### Disclaimer
**Client granted permission to publish this work**
