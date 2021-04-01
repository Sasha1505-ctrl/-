# importing libraries
import os
import string
import time
import urllib.request
from io import BytesIO
import requests
import vk_api
from ufw.util import open_files, close_files
from vk_api import VkUpload
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api.utils import get_random_id
import nltk
import wikipedia
import warnings
import random
import pymorphy2
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from textblob import TextBlob
from googletrans import Translator

warnings.filterwarnings("ignore")

# if english, then download wordnet and punct
# nltk.download('')

# this is where the program starts
while True:
    f = open('filename1.txt', 'r', errors='ignore')  # data from the first text document with russian language
    raw = f.read()
    f.close()
    raw = raw.lower()  # convert to lowercasw
    sent_tokens = nltk.sent_tokenize(raw, language='russian')  # converts to list of sentences
    cisco = open("filename2.txt", "r", errors="ignore") # data from the second text document with russian language
    rcisco = cisco.read()
    rcisco = rcisco.lower()
    cisco_tokens = nltk.sent_tokenize(rcisco, language='russian')

    def lemmatize_with_postag(sentence):  # lemmatization russian language
        sent = TextBlob(sentence)
        tag_dict = {"J": 'a',
                    "N": 'n',
                    "V": 'v',
                    "R": 'r'}
        words_and_tags = [(w, tag_dict.get(pos[0], 'n')) for w, pos in sent.tags]
        lemmatized_list = [wd.lemmatize(tag) for wd, tag in words_and_tags]
        return " ".join(lemmatized_list)


    token = 'your token'

    groupId = 000000000 # your group id
    key = 'your key'
    server = 'your server'
    ts = 'your ts'
    # connecting VK API
    vk_session = vk_api.VkApi(token=token)
    upload = VkUpload(vk_session)
    longpoll = VkLongPoll(vk_session, groupId)
    vk = vk_session.get_api()

    # keyboard with multiple commands
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('привет', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('клавиатура', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_location_button()
    keyboard.add_line()
    keyboard.add_button('картинка', color=VkKeyboardColor.SECONDARY)

    # some of the bot's commands and responses
    GREETING_INPUTS = ('Ку', 'Привет', 'Хай', 'Хелло', 'Хеллоу', 'привет', 'ку', 'хеллоу', 'хай', 'хелло')
    KEYBOARD = ("Клавиатура", "клавиатура", "клава", "Клава")
    GREENING_RESPONSES = "Привет"
    GOODBYE = (
        "Пока", "пока", "Доброй ночи", "доброй ночи", "До свидания", "до свидания", "гудбай", "Гудбай",
        "Прощай", "прощай")
    GOODBYE_ANSWER = "Пока"
    ADD = "добавь "
    ASK = "ответь "
    URL = ""
    PICKTURE = ("картинка", "пикча", "изображение")

    # some images (in the same project folder)
    IMAGE = ["image1.jpg", "image2.png", "image3.jpeg", "image4.jpeg", "image5.jpeg", "image6.jpeg", "image7.jpeg",
             "image8.jpeg", "image9.jpeg", "image10.jpeg", "image11.jpeg", "image13.jpeg", "image22.jpeg",
             "image31.jpeg", "image47.jpeg", "image59.jpeg", "image79.jpeg"]

    # using Google translate
    transl = Translator()

    def ruen(someone):
        try:
            someone = someone.replace("руангл ", "\n")
            result = transl.translate(someone, sc="russian", dest="en")
            if event.from_user:
                write_message(result.text)
            if event.from_chat:
                write_messagec(result.text)
        except:
            if event.from_user:
                write_message("ошибка")
            if event.from_chat:
                write_messagec("ошибка")
        finally:
            time.sleep(2)


    def enru(someone):
        try:
            someone = someone.replace("enru ", "\n")
            result = transl.translate(someone, sc="en", dest="russian")
            if event.from_user:
                write_message(result.text)
            if event.from_chat:
                write_messagec(result.text)
        except:
            if event.from_user:
                write_message("error")
            if event.from_chat:
                write_messagec("error")
        finally:
            time.sleep(2)


    def ruja(someone):
        try:
            someone = someone.replace("руяп ", "\n")
            result = transl.translate(someone, sc="russian", dest="japanese")
            if event.from_user:
                write_message(result.text)
            if event.from_chat:
                write_messagec(result.text)
        except:
            if event.from_user:
                write_message("ошибка")
            if event.from_chat:
                write_messagec("ошибка")
        finally:
            time.sleep(2)


    def jaru(someone):
        try:
            someone = someone.replace("япру ", "\n")
            result = transl.translate(someone, sc="japanese", dest="russian")
            if event.from_user:
                write_message(result.text)
            if event.from_chat:
                write_messagec(result.text)
        except:
            if event.from_user:
                write_message("ошибка")
            if event.from_chat:
                write_messagec("ошибка")
        finally:
            time.sleep(2)

    # sending messages in conversation and in private
    def write_message(message):
        vk_session.method("messages.send", {"user_id": event.user_id, "message": message, "random_id": get_random_id()})


    def write_messagec(message):
        vk_session.method("messages.send", {"chat_id": event.chat_id, "message": message, "random_id": get_random_id()})

    # sending messages with keyboard
    def write_messagek(message):
        try:
            vk_session.method("messages.send",
                              {"user_id": event.user_id, "keyboard": keyboard.get_keyboard(), "message": message,
                               "random_id": get_random_id()})
        except:
            if event.from_user:
                write_message("Erroe!")
            if event.from_chat:
                write_messagec("Error!")
        finally:
            time.sleep(2)


    def write_messageck(message):
        try:
            vk_session.method("messages.send",
                              {"chat_id": event.chat_id, "keyboard": keyboard.get_keyboard(), "message": message,
                               "random_id": get_random_id()})
        except:
            if event.from_user:
                write_message("Error!")
            if event.from_chat:
                write_messagec("Error!")
        finally:
            time.sleep(2)


    # writing in English
    with open('english.txt', 'r', encoding='utf8', errors='ignore') as fin:
        raweng = fin.read().lower()

    sent_tokenseng = nltk.sent_tokenize(raweng)  # converts to list of sentences
    word_tokenseng = nltk.word_tokenize(raweng)  # converts to list of words


    def LemTokens(tokens):
        lemmereng = nltk.WordNetLemmatizer()
        return [lemmereng.lemmatize(token) for token in tokens]


    def LemNormalize(text):
        remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
        return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


    # Generating response in English
    def responseeng(user_response):
        try:
            ro_reseng = ''
            sent_tokenseng.append(user_response)
            TfidfVeceng = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
            tfidf = TfidfVeceng.fit_transform(sent_tokenseng)
            vals = cosine_similarity(tfidf[-1], tfidf)
            idx = vals.argsort()[0][-2]
            flat = vals.flatten()
            flat.sort()
            req_tfidf = flat[-2]
            if (req_tfidf == 0):
                ro_reseng = ro_reseng + "I am sorry! I don't understand you"
                if event.from_user:
                    write_message(ro_reseng)
                if event.from_chat:
                    write_messagec(ro_reseng)
            else:
                ro_reseng = ro_reseng + sent_tokenseng[idx]
                if event.from_user:
                    write_message(ro_reseng)
                if event.from_chat:
                    write_messagec(ro_reseng)
        except:
            if event.from_user:
                write_message("Error")
            if event.from_chat:
                write_messagec("Error")


    # Generating response in Russian the first file
    def response(us_res):
        try:
            ro_res = ""
            us_res = us_res.replace("ответь", "\0")
            sent_tokens.append(us_res)
            TFidfVec = TfidfVectorizer(tokenizer=lemmatize_with_postag,
                                       stop_words=stopwords.words('russian'))
            tfidf = TFidfVec.fit_transform(sent_tokens)
            vals = cosine_similarity(tfidf[-1], tfidf)
            idx = vals.argsort()[0][-2]
            flat = vals.flatten()
            flat.sort()
            req_tfidf = flat[-2]
            ro_res = ro_res + sent_tokens[idx]
            if event.from_user:
                write_message(ro_res)
            if event.from_chat:
                write_messagec(ro_res)
        except:
            time.sleep(2)


    # Generating response in Russian the second file
    def responsetwo(us_res):
        try:
            ro_res = ""
            us_res = us_res.replace("ответьдва", "\0")
            cisco_tokens.append(us_res)
            TFidfVec = TfidfVectorizer(tokenizer=lemmatize_with_postag,
                                       stop_words=stopwords.words('russian'))
            tfidf = TFidfVec.fit_transform(cisco_tokens)
            vals = cosine_similarity(tfidf[-1], tfidf)
            idx = vals.argsort()[0][-2]
            flat = vals.flatten()
            flat.sort()
            req_tfidf = flat[-2]
            ro_res = ro_res + cisco_tokens[idx]
            if event.from_user:
                write_message(ro_res)
            if event.from_chat:
                write_messagec(ro_res)
        except:
            time.sleep(2)


    # using wiki in Russian
    def wikipedia_data(input):
        reg_ex = input.replace('расскажи о ', " ")
        try:
            if reg_ex:
                # topic = reg_ex.group(1)
                wikipedia.set_lang("RU")
                wiki = wikipedia.summary(reg_ex, sentences=3, auto_suggest=True)
                if event.from_chat:
                    write_messagec(wiki)
                if event.from_user:
                    write_message(wiki)
        except Exception as e:
            if event.from_chat:
                write_messagec("не найдено информации")
            if event.from_user:
                write_message("не найдено информации")


    # sending messages with photo
    def photo_message(photo):
        try:
            attachments = []
            upload_image = upload.photo_messages(photos=photo)[0]
            attachments.append('photo{}_{}'.format(upload_image["owner_id"], upload_image["id"]))
            vk_session.method("messages.send",
                              {"attachment": ",".join(attachments), "random_id": get_random_id(),
                               "chat_id": event.chat_id})
        except:
            time.sleep(2)


    # adding photo
    def plus_pikcha(url, n):
        try:
            url = url.replace("+", "h") # url without "h" at the beginning
            urllib.request.urlretrieve(url, "/home/user/images/img.jpeg")
            name = "image{numb}.jpeg"
            newname = name.format(numb=n)
            os.renames("img.jpeg", newname)
            IMAGE.append(newname)
            if event.from_user:  # Если написали в лс
                write_message("Я добавил твою картинку")
            if event.from_chat:  # if input in chat
                write_messagec("Я добавил твою картинку")
        except:
            if event.from_user:
                write_message("Фиговая картинка!")
            if event.from_chat:
                write_messagec("Фиговая картинка!")
        finally:
            time.sleep(2)


    # adding russian words in the first file
    def adding(some):
        some = some.replace("добавь", "\n")
        some = some + "."
        f = open('filename1.txt', 'a', errors='ignore')
        f.write(str(some))
        f.close()
        if event.from_chat:
            write_messagec("Добавил")
        if event.from_user:
            write_message("Добавил")


    # adding russian words in the second file
    def addingtwo(some):
        some = some.replace("добавьдва ", "\n")
        some = some + "."
        cisco = open('filename2.txt', 'a', errors='ignore')
        cisco.write(str(some))
        cisco.close()
        if event.from_chat:
            write_messagec("ok")
        if event.from_user:
            write_message("ok")


    # adding english words
    def addingeng(someeng):
        someeng = someeng.replace("добавьангл ", "\n")
        someeng = someeng + "."
        eng = open('english.txt', 'a', errors='ignore')
        eng.write(str(someeng))
        eng.close()
        if event.from_chat:
            write_messagec("Добавил english")
        if event.from_user:
            write_message("Добавил english")

    # mention of participants in the conversation (you can add them individually)
    def vizov(mess):
        try:
            mess = mess.replace("вызов ", " ")
            if "всех" in mess:
                write_messagec("@all")
            if "онлайн" in mess:
                write_messagec("@online")
            else:
                write_messagec("Нет такого челеловека.")
        except:
            time.sleep(2)

    # the process of communicating with the bot itself
    try:
        for event in longpoll.listen():  # Проверяем ЛонгПул
            if (event.type == VkEventType.MESSAGE_NEW and event.text):  # Новое событие (Новое сообщение)
                us_res = event.text.lower()
                if ADD in us_res:  # adding senteses
                    adding(us_res)
                if "добавьдва" in us_res:
                    adcisco(us_res)
                if "добавьангл" in us_res:
                    addingeng(us_res)
                if "вызов " in us_res:
                    vizov(us_res)
                if "ответьдва " in us_res:
                    if event.from_user:
                        try:
                            ciscores(us_res)
                            cisco_tokens.remove(us_res)
                        except ValueError:
                            time.sleep(5)
                    if event.from_chat:
                        try:
                            ciscores(us_res)
                            cisco_tokens.remove(us_res)
                        except ValueError:
                            time.sleep(5)
                if "ответь англ" in us_res:
                    if event.from_user:
                        try:
                            responseeng(us_res)
                            sent_tokenseng.remove(us_res)
                        except ValueError:
                            time.sleep(5)
                    if event.from_chat:
                        try:
                            responseeng(us_res)
                            sent_tokenseng.remove(us_res)
                        except ValueError:
                            time.sleep(5)
                if us_res in PICKTURE:
                    photo_message(random.choice(IMAGE))
                if "+" in us_res:
                    n = random.randint(20, 100)
                    plus_pikcha(us_res, n)
                if "руангл " in us_res:
                    ruen(us_res)
                if "англру " in us_res:
                    enru(us_res)
                if "руяп " in us_res:
                    ruja(us_res)
                if "япру " in us_res:
                    jaru(us_res)
                if "расскажи о" in us_res:  # and (req_tfidf == 0)
                    if event.from_user:
                        write_message("Обратимся к википедии")
                        ro_res = wikipedia_data(us_res)
                        if us_res is not None:
                            write_message(ro_res)
                    if event.from_chat:
                        write_messagec("Обратимся к википедии")
                        ro_res = wikipedia_data(us_res)
                        if us_res is not None:
                            write_messagec(ro_res)
                if us_res in GREETING_INPUTS:  # greeting
                    if event.from_user:  # Если написали в лс
                        write_message(random.choice(GREENING_RESPONSES))
                    if event.from_chat:  # if input in chat
                        write_messagec(random.choice(GREENING_RESPONSES))
                if us_res in KEYBOARD:
                    if event.from_user:
                        write_messagek('Держи')
                if us_res in GOODBYE:
                    if event.from_user:
                        write_message(random.choice(BADBYE_ANSWER))
                    if event.from_chat:
                        write_messagec(random.choice(BADBYE_ANSWER))
                if "ответь " in us_res:
                    if event.from_user:
                        try:
                            write_message(response(us_res))
                            sent_tokens.remove(us_res)
                        except ValueError:
                            time.sleep(5)
                    if event.from_chat:
                        try:
                            write_messagec(response(us_res))
                            sent_tokens.remove(us_res)
                        except ValueError:
                            time.sleep(5)
    except vk_api.exceptions.ApiError:
        time.sleep(2)
