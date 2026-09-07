from pathlib import Path
from playsound3 import playsound

audio = Path(__file__).parent / "021.mp3"

playsound(str(audio))
