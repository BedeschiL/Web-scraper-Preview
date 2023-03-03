import json
from json import JSONEncoder

class PreviewEncoder(JSONEncoder):
    def default(self, o):
         return o.__dict__
    
class PreviewDecoder(json.JSONDecoder):
    def decode(self, json_str):
        preview_dict = super().decode(json_str)
        return Preview(preview_dict['title'], preview_dict['desc'], preview_dict['img'])

def deserialize_preview(json_str):
    return json.loads(json_str, cls=PreviewDecoder)

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
print(p)
prevJSONData = json.dumps(p, indent=4, cls=PreviewEncoder)
print(prevJSONData)

prevJSONdecode=deserialize_preview(prevJSONData)
print(type(prevJSONdecode))
print(prevJSONdecode)
