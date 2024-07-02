from mpd import MPDClient


client = MPDClient()
client.timeout = 25
client.idletimeout = None

def connect(ip='localhost', port=6600):
    client.connect(ip, port)





