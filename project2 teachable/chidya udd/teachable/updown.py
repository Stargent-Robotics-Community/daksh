from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import pyttsx3 as pts
import random

engine=pts.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
def speak(input):
    engine.say(input)
    engine.runAndWait()

def gen_labels():
    labels = {}
    with open("labels.txt", "r") as label:
        text = label.read()
        lines = text.split("\n")
        for line in lines[0:-1]:
            hold = line.split(" ", 1)
            labels[hold[0]] = hold[1]
    return labels



# Load the model
model = load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image
image = Image.open("down.jpg")
#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)
# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
print(prediction)

a=gen_labels()[str(result)]
print(a)


number=random.randint(1,10)

if number%2 == 0:
    up = random.randint(kingfisher, dove, vulture, parrot, owl, eagle,bat, crane, hummingbird, peacock)
    speak(up)
    print(up)
    if str(a) == up:
        print('you won')
    else:
        print('you lose')
else:
   down = random.randint( ostrich, rooster, penguin, swan, crane, duck )
   speak(down)
   print(down)
   if str(a) == down:
       print('you won')
   else:
       print('you lose')




