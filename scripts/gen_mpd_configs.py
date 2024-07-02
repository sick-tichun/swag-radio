
def gen(name, port_og, number=0, ip='localhost',  ):
    #generate the mpd cfg file with appropriate ports
    cfg_file = """
audio_output {
    type        "shout"
    encoding    "ogg"
    name        "{name}"
    host        "{ip}"
    port        "{port}"
    mount       "/example.ogg"
    user        "source"
    password    "<source-password>"

# Set either quality or bit rate
#   quality     "5.0"
    bitrate     "64"
    format      "44100:16:1"
# Optional Parameters
#   description "here is my long description"
#   genre       "jazz"
}

# Need this so that mpd still works if icecast is not running
audio_output {
    type "null"
    name "fake out"
}
    """.format(name=name, port=str(port_og + number), ip=ip)
    #generate the systemd service file
    service_file = """
[Unit]
Description=mpd{i}
After=network.target

[Service]
Type=notify
ExecStart=/usr/bin/mpd --no-daemon mpd{i}.conf

[Install]
wantedBy=multi-user.target
    """.format(i=number)

    open('mpd'+str(number)+'.conf', 'w+').write(cfg_file)
    open('mpd'+str(number)+'.service', 'w+').write(service_file)


