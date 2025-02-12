# My Idea: Gesture Control for Mouse Cursor Using Python

Project Overview:
This project illustrates an innovative approach to control the mouse cursor using hand gestures. The main technologies utilized are a Python library for mouse cursor control and computer vision methodology to identify specific gestures.

## Inspiration
The inspiration derived from an interesting Python library I discovered which offers comprehensive control over the mouse cursor. I was motivated to develop an engaging application to showcase its capabilities.

## Methodology
### Gesture Recognition
For gesture identification, I'm intending to train a YOLO model to analyze images. The model will be trained to identify two specific hand gestures:
- Open Palm: To move the mouse cursor.
- Closed Fist: To simulate the click or hold function of the left mouse button.
> Note: The right button functionality has not been included in the project scope as of now.

### Gesture Translation
Once a specific gesture is identified in the webcam feed, the program computes the center of the detected hand gesture's bounding box. These coordinates get correlated to the mouse cursor's position on the screen. In the case of a closed fist gesture, the program triggers a click or hold action on the left mouse button.

## Conclusion
By integrating Python's powerful libraries and the possibilities of computer vision, this project aims to provide a novel and thrilling way of interacting with your computer. Please stay tuned for more updates.



Основной файл это main
файл robo - самая первая версия моего проекта. Работает очень медленно
файл semka - просто обычная программа которая читает кадры с веб камеры в потоке
остальные файлы использовалаись для обучения модели
файл dt - dataset
файл runs - результаты обучения модели yolo
