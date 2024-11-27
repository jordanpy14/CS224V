import praw
from tqdm import tqdm
reddit = praw.Reddit(
    client_id='6YPbIjiwsl0PVtSi2B3qWw',
    client_secret='D2RTWe2n1RLmFM6vw8uWB44n2gCJQQ',
    user_agent='ezLEGAL by /u/Gullible-Beautiful44',
    username='Gullible-Beautiful44',
    password='Jordanapy14'
)
subreddit = reddit.subreddit('es') 

# Scrape submissions
text = ''
try:
    for i, submission in enumerate(tqdm(subreddit.top(limit=100000, time_filter='all'),desc="scraping reddit spanish" )):  # Adjust the limit as needed
        # print(submission.title)  # Prints the title of the submissions
        # print(submission.selftext, '\n\n\n************')  # Prints the body of the submission
        text += submission.title + ' ' + submission.selftext + '\n\n\n************'
        if i % 1000 == 0 and i != 0:  # Save every thousand submissions
            with open(f'reddit_es_{i}.txt', 'a') as f:
                f.write(text)
            text = ''
finally:
    if text:  # Save any remaining text if the loop ends before hitting another thousand
        with open(f'reddit_es_{i}.txt', 'a') as f:
            f.write(text)
