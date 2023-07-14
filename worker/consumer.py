import json
import threading

from channels.generic.websocket import WebsocketConsumer
from worker.my_worker import get_data,set_task
from uploader.models import UploadedFile


class MyConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        # self.send(text_data="preparing the recipie")

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json["message"]
        data = None
        try:
            data = get_data(text_data)
        except KeyError as e:
            obj = UploadedFile.objects.get(id=text_data)
            with obj.file.open(mode='r') as file:
                content = ' '.join(file.readlines())
                set_task(text_data, content.replace('\n', ' '),obj.word_size)
        if data is None:
            msg = "not yet"
        else:
            msg = f"number of word in the file is {data}"
        self.send(msg)
