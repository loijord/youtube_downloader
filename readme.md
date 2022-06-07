## Requirements

* `Python == 3.8`
* `pytube == 12.1.0`
* `moviepy == 1.0.3`

## Usage

In the June of 2022, a current version of `pytube` needs to be bugfixed:

* Navigate to `venv > lib > python3.8 > site-packages > pytube > cipher.py`
* Replace `regex` in `cipher.py` following these instructions: [https://github.com/pytube/pytube/issues/1326](https://github.com/pytube/pytube/issues/1326)
* Go!

## Recipes

* Find a facebook friend
* Tell him you have a secret way to download his favorite YouTube tracks
* Ask him to share them in messenger
* Copy, paste & edit his track url into a list that looks like this:

  ```
  your_friend = r'''https://youtube.com/watch?v=d5nyyYIcghk
  https://youtube.com/watch?v=z9Jgh3mW5Xo
  https://youtube.com/watch?v=IG1yy9HAVxU
  https://youtube.com/watch?v=t6qmNg0zVI8
  ```
* Convert to `mp3` & `mp4` like so:

  ```
  tracks = your_friend.split('\n')
  for url in tracks: 
      download(url)
  ```
* Check out `songs_mp3` & `songs_mp4` folders
* More recipes: in `main.py`