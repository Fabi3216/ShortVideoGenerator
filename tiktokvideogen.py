import os
import random
import time
from gtts import gTTS
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip

# Liste mit extrem schwarzem Humor Witzen
jokes = [
    "Was ist schlimmer als ein Witz über Kinder mit Krebs? Ein Kind mit Krebs!",
    "Warum freut sich ein Waisenkind über ein Puzzle? Weil auf der Packung steht: 'Familie ab 3 Jahren'",
    "Warum bringen Blinde keine Rückgaben ins Geschäft? Weil sie nicht sehen, dass es falsch ist!",
    "Warum darf man in einem Krematorium nicht lachen? Weil sonst jemand vor Lachen stirbt!",
    "Warum sind Friedhöfe so ruhig? Weil die Kundschaft nie wieder Beschwerden einreicht!"
]

# Erstelle den Video-Ordner falls nicht vorhanden
output_folder = "generated_videos"
os.makedirs(output_folder, exist_ok=True)

def generate_video():
    joke = random.choice(jokes)
    
    # Sprachsynthese mit gTTS
    tts = gTTS(joke, lang='de')
    audio_path = "voice.mp3"
    tts.save(audio_path)
    
    # Hintergrundvideo zufällig auswählen
    background_videos = [f for f in os.listdir("background_videos") if f.endswith(".mp4")]
    bg_video_path = os.path.join("background_videos", random.choice(background_videos))
    
    # Video und Audio laden
    video = VideoFileClip(bg_video_path).subclip(0, 20)
    audio = AudioFileClip(audio_path)
    
    # Text Overlay
    txt_clip = TextClip(joke, fontsize=40, color='white', size=video.size, method='caption')
    txt_clip = txt_clip.set_position('center').set_duration(20)
    
    # Zusammensetzen des finalen Videos
    final_video = CompositeVideoClip([video, txt_clip])
    final_video = final_video.set_audio(audio)
    
    # Speichern
    output_path = os.path.join(output_folder, f"tiktok_joke_{int(time.time())}.mp4")
    final_video.write_videofile(output_path, fps=30, codec='libx264')
    
    print(f"Video gespeichert: {output_path}")
    
    # Aufräumen
    os.remove(audio_path)
    
# Automatische Erstellung von 3 Videos am Tag
for _ in range(3):
    generate_video()
    time.sleep(5)  # Pause für Demo-Zwecke
