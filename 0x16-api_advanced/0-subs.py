#!/usr/bin/python3
""" queries the Reddit API """

import requests


def number_of_subscribers(subreddit):
    """ Args:
	subreddit: subreddit name
    Returns: no of subscriber to subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'xica369'}
    json_data = requests.get(url, headers=headers, allow_redirects=False)

    if json_data.status_code == 200:
        return json_data.json().get('data').get('subscribers')
    return 0
