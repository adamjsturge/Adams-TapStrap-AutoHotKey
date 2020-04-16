from tapsdk import TapSDK, TapInputMode
from tapsdk.models import AirGestures
import pyautogui



tapNum = 1


tap_instance = []
tap_identifiers = []

keyDict = "0abcdefghijklmnopqrstuvwxyz123456789"


def on_connect(identifier, name, fw):
    print(identifier + " Tap: " + str(name), " FW Version: ", fw)
    if identifier not in tap_identifiers:
        tap_identifiers.append(identifier)
    print("Connected taps:")
    for identifier in tap_identifiers:
        print(identifier)


def on_disconnect(identifier):
    print("Tap has disconnected")
    if identifier in tap_identifiers:
        tap_identifiers.remove(identifier)
    for identifier in tap_identifiers:
        print(identifier)



def on_tap_event(identifier, tapcode):
    global tapNum
    if tapNum == 1 and int(tapcode) == 31:
        #pyautogui.keyDown('f21')
        pyautogui.keyUp('f21')
        tapNum = 0
        
    elif tapNum == 0 and int(tapcode) == 31:
        pyautogui.keyUp('f21')
        tapNum = 1

    elif(tapNum == 1):
        pyautogui.keyDown('f21')
        pyautogui.keyDown(keyDict[tapcode])
        pyautogui.keyUp(keyDict[tapcode])
        pyautogui.keyUp('f21')
            
    # pyautogui.keyDown('f21')
    # pyautogui.keyDown(keyDict[tapcode])
    # pyautogui.keyUp(keyDict[tapcode])
    # pyautogui.keyUp('f21')
    print(identifier, str(tapcode))
    

    # if int(tapcode) == 17:
    #     sequence = [500, 200, 500, 500, 500, 200]
    #     tap_instance.send_vibration_sequence(sequence, identifier)






def on_raw_sensor_data(identifier, raw_sensor_data):
    # print(raw_sensor_data)
    if raw_sensor_data.GetPoint(1).z > 2000 and raw_sensor_data.GetPoint(2).z > 2000 and raw_sensor_data.GetPoint(3).z > 2000 and raw_sensor_data.GetPoint(4).z > 2000:
        tap_instance.set_input_mode(TapInputMode("controller"), identifier)


def main():
    global tap_instance
    tap_instance = TapSDK()
    tap_instance.run()
    tap_instance.register_connection_events(on_connect)
    tap_instance.register_disconnection_events(on_disconnect)
    tap_instance.register_tap_events(on_tap_event)
    tap_instance.register_raw_data_events(on_raw_sensor_data)
    

    tap_instance.set_input_mode(TapInputMode("controller"))

    while True:
        pass


if __name__ == "__main__":
    main()