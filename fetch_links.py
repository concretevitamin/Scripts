"""
Extracts urls in a given page that end with certain extentions.

Usage: fetch_links.py page_link extentions_list
"""

# Jul 18, 2012

from bs4 import BeautifulSoup
import sys, urllib2

def main():
    # get target page to parse, and target file extensions
    page = urllib2.urlopen(sys.argv[1]).read()
    extensions = sys.argv[2:]

    # get the contained urls that end with target extensions
    urls = [link.get('href') for link in BeautifulSoup(page).find_all('a')]
    target_urls = [url for url in urls for ext in extensions if url.endswith(ext)]

    # print results
    for url in target_urls:
	print url

if __name__ == "__main__":
    main()
