import mido
import vgamepad as vg
from findMidiPort import FindMidiPort
from controllerMapper import ControlMap
from helpers.controlChangeHelper import controlChangeHelper
from helpers.noteHelper import noteHelper

#find MIDI port for DJ Controller
findMidi = FindMidiPort()
port = findMidi.findPort()
try:
    input_port = mido.open_input(port)
except Exception as e:
    print(f"Error opening MIDI port: {e}")
    exit(1)

#Initilize classes (Singleton)
gamepad = vg.VX360Gamepad()
controlchangeHelper = controlChangeHelper(gamepad)
noteHelper = noteHelper(gamepad)
mapper =  ControlMap(controlchangeHelper, noteHelper)

print('Gamepad Has Started')

for msg in input_port:
    mapper.mapMidiToGamepad(msg)
    gamepad.update()

    if(msg.type == 'note_on' and msg.note == 101 and msg.velocity == 127):
        break

    