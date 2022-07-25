def create_youtube_video(title, desc):
	video= {"Title": title, "Desc": desc, "Likes": 0, "Dislikes" : 0, "Username": {}}
	return video

video = create_youtube_video("video1", "vid")
def likes(dict1):
	if "Likes" in dict1.keys():
		video["Likes"] += 1
	return video
likes(video)

def dislikes(dict2):
	if "Dislikes" in dict2.keys():
		video["Dislikes"] += 1
		return video
likes(video)

def add_comment(youtube_video, username, comment_text):
	comments = {"username" : comment_text}

