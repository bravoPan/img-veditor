import os
from moviepy.editor import *
from moviepy.audio.fx import *

fps_rate = 0.4
EFFECT_DURATION = 0.5

images_path = "test"
audio_file_path = "audio/test_audio.mp3"

images = []
for img in os.listdir(images_path):
    if img.endswith("png") or img.endswith("jpeg") or img.endswith("jpg"):
        images.append(img)

for idx, img in enumerate(images):
    cur_fps_rate = fps_rate
    if idx == 0 or idx == len(images)-1:
        cur_fps_rate = 1/(1/fps_rate - EFFECT_DURATION)
    clip = ImageSequenceClip([images_path+"/"+img], fps=cur_fps_rate)
    clip.write_videofile("output/stage/"+str(idx)+".mp4")

video_clips = [i for i in os.listdir("output/stage/")]
video_clips.sort(key=lambda x: int(x.split(".")[0]))
video_clips = list(map(lambda x: "output/stage/"+x, video_clips))
video_clips = [VideoFileClip(i) for i in video_clips]

video_fx_list = [video_clips[0]]

idx = video_clips[0].duration - EFFECT_DURATION
for video in video_clips[1:-1]:
    video_fx_list.append(video.set_start(idx).crossfadein(EFFECT_DURATION))
    idx += video.duration - EFFECT_DURATION

final_video = CompositeVideoClip(video_fx_list)
audioclip = AudioFileClip(audio_file_path).subclip(0, final_video.duration)
audioclip = audioclip.volumex(0.3)

audio_video = final_video.set_audio(audioclip)
audio_video.write_videofile("output/test.mp4", fps=24, codec='libx264', audio_codec='aac')