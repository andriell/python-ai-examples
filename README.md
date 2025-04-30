# Python AI examples

    python -V
    Python 3.13.3

## Зависимости

    pip install swig
    pip install numpy
    pip install opencv-python
    pip install gTTS
    pip install SpeechRecognition
    pip install networkx
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

    C:\ProgramFiles\Python313\Lib\site-packages\pocketsphinx\model\ru

При этом нужны только файлы

    zero_ru.cd_cont_4000 
    zero_ru.cd_ptm_4000
    zero_ru.cd_semi_4000
    ru.dic
    ru.lm
