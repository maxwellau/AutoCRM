import requests
from datetime import datetime, timedelta
import ocrspace

class telegramBot:
    def __init__(self, botToken, chatID):
        assert botToken == str(botToken), 'Name has to be a string'
        assert (chatID) == str(chatID), 'Color has to be a string'
        self.botToken = botToken
        self.chatID = chatID

    def sendText(self, msg):
        try:
            base_url = f'https://api.telegram.org/bot{self.botToken}/sendMessage?chat_id={self.chatID}&text={msg}'
            requests.post(base_url)  # Sending automated message
            return "Text Sent"
        except:
            return "Failed to send Text"


    def sendImage(self, directory):
        try:
            imgpath = {'photo': open(directory, 'rb')}
            requests.post(
                f'https://api.telegram.org/bot{self.botToken}/sendPhoto?chat_id={self.chatID}',
                files=imgpath)  # Sending Automated Image
            return "Image Sent"
        except:
            return "Failed to send Image"

    def waitNewMessage(self, specifity, waittime):
        assert waittime == float(waittime), 'waittime has to be a float'
        assert '-' not in self.chatID, 'ChatID is that of a Channel, unable to poll for responses'
        assert type(specifity) == bool, 'Specificity has to be a Boolean Value'
        site = f'https://api.telegram.org/bot{self.botToken}/getUpdates'
        data = requests.get(site).json()  # reads data from the url getUpdates
        try:
            lastMsg = len(data['result']) - 1
            updateIdSave = data['result'][lastMsg]['update_id']
        except:
            updateIdSave = ''
        time = datetime.now()
        waitTime = time + timedelta(seconds=waittime)

        while True:
            try:
                data = requests.get(site).json()  # reads data from the url getUpdates
                lastMsg = len(data['result']) - 1
                updateId = data['result'][lastMsg]['update_id']
                chatid = str(data['result'][lastMsg]['message']['chat']['id'])  # reads chat ID
                if specifity == True:
                    condition = self.chatID == chatid
                else:
                    condition = True
                if updateId != updateIdSave and condition:  # compares update ID
                    newmessage = True
                    if "text" in data['result'][lastMsg]['message']:
                        msgtype = "text"
                    elif "photo" in data['result'][lastMsg]['message']:
                        msgtype = "photo"
                    else:
                        msgtype = "others"
                    break
                if waitTime < datetime.now():
                    newmessage = False
                    msgtype = "others"
                    break
            except:
                pass
        requests.get(
            f'https://api.telegram.org/bot{self.botToken}/getUpdates?offset=' + str(updateId))
        return newmessage, msgtype

    def ocr_space_file(self, filename, overlay=False, api_key='helloworld', language='eng', OCRengine=2):
        """ OCR.space API request with local file.
            Python3.5 - not tested on 2.7
        :param filename: Your file path & name.
        :param overlay: Is OCR.space overlay required in your response.
                        Defaults to False.
        :param api_key: OCR.space API key.
                        Defaults to 'helloworld'.
        :param language: Language code to be used in OCR.
                        List of available language codes can be found on https://ocr.space/OCRAPI
                        Defaults to 'en'.
        :param OCREngine: Engine to be used in OCR.
                        List of available Engines can be found on https://ocr.space/OCRAPI
                        Defaults to '2(Western Lang)'.
        :return: Result in JSON format.
        """

        payload = {'isOverlayRequired': overlay,
                   'apikey': api_key,
                   'language': language,
                   'OCRengine': OCRengine
                   }
        with open(filename, 'rb') as f:
            try:
                r = requests.post('https://api.ocr.space/parse/image',
                                  files={filename: f},
                                  data=payload,
                                  )
                return r.json()['ParsedResults'][0]['ParsedText'].split("\n")
            except:
                payload['OCRengine'] = 1
                r = requests.post('https://api.ocr.space/parse/image',
                                  files={filename: f},
                                  data=payload,
                                  )
                return r.json()['ParsedResults'][0]['ParsedText'].split("\r\n")

    def makePrediction(self):
        getUpdates = f"https://api.telegram.org/bot{self.botToken}/getUpdates"
        update = requests.get(getUpdates).json()
        length = len(update['result']) - 1
        file = update['result'][length]['message']['photo']
        FILEPATH = file[len(file) - 1]['file_id']

        getFilePath = f"https://api.telegram.org/bot{self.botToken}/getFile?file_id={FILEPATH}"
        PATH = requests.get(getFilePath).json()['result']['file_path']

        download = f"https://api.telegram.org/file/bot{self.botToken}/{PATH}"
        resp = requests.get(download)
        with open('lol.jpeg', "wb") as f:
            f.write(resp.content)
        # Or if you have a custom API host, API key or desired language, pass those:
        resp = self.ocr_space_file(filename='lol.jpeg', api_key = "495d31400588957")
        return resp

    def getLastMsg(self):
        site = f'https://api.telegram.org/bot{self.botToken}/getUpdates'
        data = requests.get(site).json()  # reads data from the url getUpdates
        lastMsg = len(data['result']) - 1
        return data['result'][lastMsg]['message']['text']

    def pollResponse(self, specifity, waittime):
        assert waittime == float(waittime), 'waittime has to be a float'
        assert '-' not in self.chatID, 'ChatID is that of a Channel, unable to poll for responses'
        assert type(specifity) == bool, 'Specificity has to be a Boolean Value'
        site = f'https://api.telegram.org/bot{self.botToken}/getUpdates'
        data = requests.get(site).json()  # reads data from the url getUpdates
        try:
            lastMsg = len(data['result']) - 1
            updateIdSave = data['result'][lastMsg]['update_id']
        except:
            updateIdSave = ''
        time = datetime.now()
        waitTime = time + timedelta(seconds=waittime)

        while True:
            try:
                data = requests.get(site).json()  # reads data from the url getUpdates
                lastMsg = len(data['result']) - 1
                updateId = data['result'][lastMsg]['update_id']
                chatid = str(data['result'][lastMsg]['message']['chat']['id'])  # reads chat ID
                if specifity == True:
                    condition = self.chatID == chatid
                else:
                    condition = True
                if updateId != updateIdSave and condition:  # compares update ID
                    try:
                        text = data['result'][lastMsg]['message']['text']  # reads what they have sent\
                        break
                    except:
                        pass
                if waitTime < datetime.now():
                    text = 'null'
                    break
            except:
                pass
        requests.get(
            f'https://api.telegram.org/bot{self.botToken}/getUpdates?offset=' + str(updateId))
        return text