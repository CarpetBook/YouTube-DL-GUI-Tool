import pyperclip
import PySimpleGUI as sg
import os
import subprocess

searchforconfig = os.listdir();
audioformat = None
videoformat = None

os.chdir("C:/Users/Owner/Downloads")

youtubelink = pyperclip.paste()

sg.theme("SystemDefaultForReal")

layout = [ [ sg.Text("Video link to download:"), sg.InputText(youtubelink, key = "-LINK-") ],
           #[ sg.Text("New file name (optional):"), sg.InputText(key = "-NEWNAME-") ],
           #[ sg.Text("Video format:"), sg.Radio("MP4", key = "MP4", group_id = "video", default = True), sg.Radio("MOV", key = "MOV", group_id = "video", default = False), sg.Radio("MKV", key = "MKV", group_id = "video", default = False) ],
           [ sg.Checkbox("Audio only", enable_events = True, default = False, key = "-AUDIO-"), sg.Radio("MP3", key = "MP3", group_id = "audio", disabled = True, default = True), sg.Radio("WAV", key = "WAV", group_id = "audio", disabled = True, default = False), sg.Radio("M4A", key = "M4A", group_id = "audio", disabled = True, default = False) ],
           [ sg.Button("Download"), sg.Button("Cancel") ] ]

window = sg.Window('YouTube-DL', layout)

def downloadLink(values):
    link = values["-LINK-"]
    audioonly = values["-AUDIO-"]
    audioformat = None
    videoformat = None
    
    if values["MP3"]:
        audioformat = 'mp3'
    elif values["WAV"]:
        audioformat = 'wav'
    elif values["M4A"]:
        audioformat = 'm4a'

##    if values["MP4"]:
##        videoformat = 'mp4'
##    elif values["MOV"]:
##        videoformat = 'mov'
##    elif values["MKV"]:
##        videoformat = 'mkv'

    cmd = None
    if audioonly:
        cmd = ['youtube-dl', link, '-x', '--audio-format', audioformat]
    else:
        cmd = ['youtube-dl', link]
               #, '--exec', '\"ffmpeg \"']
    print(cmd)
    
    process = subprocess.run(cmd)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == "Cancel":
        window.close()
        break
    if event == '-AUDIO-':
        # check audio only checkbox, disable video options if true
        if window['-AUDIO-'].get():
##            window['MP4'].update(disabled = True)
##            window['MOV'].update(disabled = True)
##            window['MKV'].update(disabled = True)
            window['MP3'].update(disabled = False)
            window['WAV'].update(disabled = False)
            window['M4A'].update(disabled = False)
        elif not window['-AUDIO-'].get():
##            window['MP4'].update(disabled = False)
##            window['MOV'].update(disabled = False)
##            window['MKV'].update(disabled = False)
            window['MP3'].update(disabled = True)
            window['WAV'].update(disabled = True)
            window['M4A'].update(disabled = True)
    elif event == 'Download':
        window.close()
        downloadLink(values)
        break
