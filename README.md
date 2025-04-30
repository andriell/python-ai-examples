# Python AI examples

    python -V
    Python 3.12.10

## Зависимости

    pip install swig
    pip install numpy
    pip install opencv-python
    pip install gTTS
    pip install SpeechRecognition
    pip install networkx
    pip install matplotlib
    pip install tensorflow
    pip3 install pocketsphinx

## Установка распознания речи

https://habr.com/ru/articles/351376/

Файлы можно получить по ссылкам:

cmusphinx-ru-5.2.zip https://disk.yandex.ru/d/Iu7pltt0MaQmbw

zero_ru_cont_8k_v3.zip https://disk.yandex.ru/d/hKj3OurEhE4wng

    pip install swig
    pip install SpeechRecognition
    pip3 install pocketsphinx

Скопировать файлы из архива zero_ru_cont_8k_v3.zip в папку

    C:\ProgramFiles\Python312\Lib\site-packages\pocketsphinx\model\ru

При этом нужны только файлы

    zero_ru.cd_cont_4000 
    zero_ru.cd_ptm_4000
    zero_ru.cd_semi_4000
    ru.dic
    ru.lm

## Установка tensorflow

Для Windows Native требуется распространяемый пакет Microsoft Visual C++ для Visual Studio 2015, 2017 и 2019.

Эта версия будет работать на CPU

    pip install tensorflow

Эта версия будет работать на GPU

    pip install tensorflow[and-cuda]

Проверка установки

    python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

В ответе должно быть tf.Tensor(...)
