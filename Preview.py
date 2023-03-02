import json
from json import JSONEncoder

class PreviewEncoder(JSONEncoder):
    def default(self, o):
         return o.__dict__

class Preview:
    def __init__(self,_title,_img,_desc):
        self.title=_title
        self.img=_img
        self.desc=_desc

    def __str__(self):
        return f"{self.title} , {self.desc} , {self.img}"
            
    title=""
    img=""
    desc=""



p = Preview("LOUIS","https://media.giphy.com/media/8FNlmNPDTo2wE/giphy.gif","Blabla") 
prevJSONData = json.dumps(p, indent=4, cls=PreviewEncoder)
print(prevJSONData)
