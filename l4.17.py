import speech_recognition as sr

# Создание объекта Recognizer
recognizer = sr.Recognizer()

# Загрузка аудиофайла
audio_file = "output.wav"

with sr.AudioFile(audio_file) as source:

    # Запись аудио из файла
    audio_data = recognizer.record(source)

    # Преобразование аудио в текст с использованием Google Web Speech API
    text = recognizer.recognize_sphinx(audio_data, language="ru-RU")

# Вывод результата
print("Текст из аудио:", text)
