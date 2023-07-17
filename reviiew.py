def create_youtube_video(title,description):
	new_youtube_video ={ "title": " shopping haul","description": "idk","likes": 0, "dislikes": 0,"comments" :{}}
	return new_youtube_video

def like (new_youtube_video):
	if "likes" in new_youtube_video:
		new_youtube_video["likes"]+1
	return new_youtube_video 

def dislike(new_youtube_video):
	
	if "dislikes" in new_youtube_video:
		new_youtube_video["dislikes"]+1

def add_comment(new_youtube_video,username,comment_text):
	new_youtube_video["comments"][username]=comment_text
	return new_youtube_video

lalala=new_youtube_video("disgusting","a person eating mushrooms")
new_youtube_video["likes"]+495
