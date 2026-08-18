import cv2
import pyttsx3
import speech_recognition as sr
import time

# Initialize speech engine and recognizer
engine = pyttsx3.init()
recognizer = sr.Recognizer()

# Destination checklist dictionary
DESTINATIONS = {
    "gym": "your water bottle, towel, and headphones",
    "work": "your laptop, charger, and ID badge",
    "beach": "sunscreen, a towel, and sunglasses",
    "grocery": "reusable bags and wallet",
    "school": "your backpack, binder, and lunch"
}

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_destination():
    speak("Where are you going?")
    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            # Listen with a 4-second timeout so frame processing isn't stalled long
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=4)
            return recognizer.recognize_google(audio).lower()
        except Exception:
            return None

last_trigger_time = 0
cooldown = 20  # Delay between interactions in seconds

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Insert your OpenCV person detection trigger here
    person_detected = True 

    current_time = time.time()
    if person_detected and (current_time - last_trigger_time > cooldown):
        destination = get_destination()
        
        if destination:
            # Find matching items based on destination keywords
            matched_items = next((items for location, items in DESTINATIONS.items() if location in destination), None)
            
            if matched_items:
                speak(f"Heading to {destination}? Don't forget {matched_items}!")
            else:
                speak(f"Have fun at {destination}! Make sure you have your keys and phone.")
        
        last_trigger_time = time.time()

    cv2.imshow('Smart Doorway Reminder', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()