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
    pip3 install tensorflow
    pip3 install pocketsphinx
    pip install pillow

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

Нужно установить последний драйвер
https://www.nvidia.com/en-us/drivers/

Эта версия будет работать на CPU

    pip3 install tensorflow

### Установка tensorflow[and-cuda] (для вычислений на GPU не обязательно)

1. Драйверы графического процессора NVIDIA® https://www.nvidia.com/drivers
2. Инструментарий CUDA® 12.3. https://developer.nvidia.com/cuda-toolkit-archive
3. cuDNN SDK 8.9.7. https://developer.nvidia.com/cudnn
4. (Необязательно) TensorRT для улучшения задержки и пропускной способности вывода. https://docs.nvidia.com/deeplearning/tensorrt/archives/index.html#trt_7 

Эта версия будет работать на GPU, ее можно и не ставить

    pip3 install tensorflow[and-cuda]

Проверка установки

    python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

В ответе должно быть tf.Tensor(...)
