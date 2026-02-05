class Meme:
    def __init__(self, template, caption):
        self.template = template
        self.caption = caption
    
    def post(self):
        return f'{self.template}'
    
m = Meme("шаблон", "подпись")
print(m.post())