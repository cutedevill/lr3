import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models

def recognize(img):
    (training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()

    training_images, testing_images = training_images / 255, testing_images / 255

    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

    training_images = training_images[:6000]
    training_labels = training_labels[:6000]
    testing_images = testing_images[:4000]
    testing_labels = testing_labels[:4000]

    model = models.load_model('image_classifier.model')

    image = cv.imread(img)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    prediction = model.predict(np.array([image]) / 255)
    index = np.argmax(prediction)

    return class_names[index]
