import mido

class FindMidiPort:
    def findPort(self) -> str:
        print("Input Ports:")
        ports = mido.get_input_names()
        if not ports:
            print("Error: No MIDI input ports found.")
            return ""
        for port in ports:
            print(port)

        portNumber = input("Enter your DJ-Controller Port Number:")
        try:
            portNumber = int(portNumber)
            if portNumber < 0 or portNumber >= len(ports):
                raise ValueError("Port number not found in list.")
        except:
            print(f"{portNumber} is not a valid Number")

        return mido.get_input_names()[portNumber]