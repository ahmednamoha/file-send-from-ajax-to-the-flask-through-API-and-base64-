# # import base64

# # string_b = " my name is ahmed".encode('utf-8')
# # print(string_b)
# string_byt = base64.b64encode(string_b)
# print(string_byt)
# print(string_byt.decode('utf-8'))

# # print('==================')

# # converted = base64.decodebytes(string_byt)
# # print(converted)
# # print(converted.decode())


# listOfAudioFormat = ['mp3', 'wav', 'ogg', 'mpeg']


# def exten_file_valid(file_type):
#     file_type = file_type.lower()
#     if file_type in listOfAudioFormat:
#         return True
#     else:
#         return False


# isVlaid = exten_file_valid('4')
# if isVlaid:
#     print('good')
# else:
#     print('not')

from pydub import AudioSegment
from os import path
import os
import glob
from pathlib import Path

# src = os.path('ss.mp3')
# dst = 'aa.wav'
# sound = AudioSegment.from_mp3(src)

# sound.export(dst, format="wav")
# print(os.)
# filea = glob.glob('./ss.mp3')
my_file = Path("D://Development/python/test\Projects\Flask/testrest/ss.mp3")
print(my_file)
# print(filea)
# for filea in filea:

sound = AudioSegment.from_mp3(my_file)
sound.export('caac.wav', format="wav")
