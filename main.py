# Just an example of usage

from selections import arunce_20220605
tracks = arunce_20220605.split('\n')
track_ids = sorted([n[n.index('=')+1:] for n in tracks])
print('DUPLICATES:', [n for n in set(track_ids) if track_ids.count(n) > 1])

# Make sure you drop duplicates
# then use these lines to put your songs into `songs_mp3` and `songs_mp4` folders:

# for url in tracks: download(url)