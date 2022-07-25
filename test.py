def create_youtube_video(title, description):
	ytdict1={"Title":title, "Description":description, "Likes":0,"Dislikes":0,"comments" :{"username":""}}
	return ytdict1

def like(ytdict1):
	if "Likes" in ytdict1:
		Likes+= 1
		return ytdict1

def dislike(ytdict1):
	if "Dislikes" in ytdict1:
		Dislikes+= 1
		return ytdict1

def add_comment(youtubevideo, username, comment_text):
	youtubevideo["comments"][username]= comment_text
	return youtubevideo

video = create_youtube_video("WE CONTACTED AMONGUS GODS AT 3 AM!!(SCARY)","Craziest thing ever happened!! Watch and find out what happened")
