
import time
from pypresence.presence import Presence
app_id = 'Application ID'
time_elapsed = True

RPC = Presence(app_id)
RPC.connect()


start = None
if time_elapsed == True:
    start = time.time()


RPC.update(
    details='...', # Premiere ligne
    state='...', # Deuxieme ligne
    large_image='GRANDE IMAGE',
    large_text='Texte sur la grande image',
    small_image='PETITE IMAGE',
    small_text='Texte sur la petite image',
    buttons=[
        {
            "label": 'Texte sur le bouton 1',
            "url": 'URL'
        },
        {
            "label": 'Texte sur le bouton 2',
            "url": 'URL'
        }
    ],
    start=start
)