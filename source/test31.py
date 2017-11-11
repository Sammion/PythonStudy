import xml.sax
class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""
    #元素开始事件处理
    def startElement (self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("*****Movie*****")
            title = attributes['title']
            print("Title", title)

    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == 'type':
            self.type = content
        elif self.CurrentData == 'format':
            self.format = content
        elif self.CurrentData == 'year':
            self.year = content
        elif self.CurrentData == 'rating':
            self.rating = content
        elif self.CurrentData == 'stars':
            self.stars = content
        elif self.CurrentData == 'description':
            self.description = content

    #元素结束事件打印出来
    def endElement(self, tag):
        if self.CurrentData == 'type':
            print("Type: ", self.CurrentData)
        elif self.CurrentData == 'format':
            print("Format: ", self.CurrentData)
        elif self.CurrentData == 'year':
            print("year: ", self.CurrentData)
        elif self.CurrentData == 'rating':
            print("Rating: ", self.CurrentData)
        elif self.CurrentData == 'stars':
            print("Stars: ", self.CurrentData)
        elif self.CurrentData == 'description':
            print("Description: ", self.CurrentData)
        self.CurrentData = ""

if (__name__ == "__main__"):

    # 创建一个XMLReader
    parser = xml.sax.make_parser()
    # turn off namespaces
    # parser.setFeature(xml.sax.ContentHandler., 0)
    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)
    parser.parse("../data/configuration")