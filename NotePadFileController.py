import NotePadFileModel
import speech_recognition as s

class Controller:
    def __init__(self):
        self.file_model = NotePadFileModel.File_Model()

    def save_file(self, msg, url):
        self.file_model.save_file(msg, url)


    def save_as(self, msg1, url):
        self.file_model.save_as(msg1, url)

    def read_file(self, url):
        self.msg, self.base = self.file_model.read_file(url)
        return self.msg, self.base

    def new_file(self):
        self.file_model.new_file()

    def takeQuery(self):
        sr = s.Recognizer()
        sr.pause_threshold = 3
        print("speak")
        with s.Microphone() as m:
            audio = sr.listen(m)
            sr.adjust_for_ambient_noise(m, duration=5)
            text = sr.recognize_google(audio, language='eng-in')
            return text



