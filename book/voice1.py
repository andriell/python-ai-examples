import os
from pocketsphinx import LiveSpeech, get_model_path

# https://habr.com/ru/articles/351376/
# Файлы можно получить по ссылкам:
# cmusphinx-ru-5.2.zip
# https://disk.yandex.ru/d/Iu7pltt0MaQmbw
# zero_ru_cont_8k_v3.zip
# https://disk.yandex.ru/d/hKj3OurEhE4wng

model_path = get_model_path()

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'ru/zero_ru.cd_cont_4000'),
    lm=os.path.join(model_path, 'ru/ru.lm'),
    dic=os.path.join(model_path, 'ru/ru.dic')
)

print("Say something!")

for phrase in speech:
    print(phrase)
    if str(phrase).strip().lower() == 'стоп':
        print("Goodbye!")
        exit()
