#!/usr/bin/python3
""" queries the Reddit API """
import requests


def top_ten(subreddit):
    """ Returns: top ten post titles
	params:
	subreddit: subreddit to query """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    args = {'limit': 10}
    headers = {'User-Agent': 'xica398'}
    json_data = requests.get(url, headers=headers, allow_redirects=False, 
params=args)
    if json_data.status_code == 200:
        subreddit_titles = json_data.json().get('data').get('children')
        for title in subreddit_titles:
            print(title.get('data').get('title'))
    else:
        print(None)
