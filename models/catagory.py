class Catagory:
    def __init__(self, name=None, url=None, full_name=None, _dict=None, _csv=None):
        if _dict:
            self.name = _dict.get('name')
            self.url = _dict.get('url')
            self.full_name = _dict.get('full_name')
        elif _csv:
            self.name = _csv[0]
            self.full_name = _csv[1]
            self.url = _csv[2]
        else:
            self.name = name
            self.url = url
            self.full_name = full_name

    def to_dict(self):
        return {
            'name': self.name,
            'url': self.url,
            'full_name': self.full_name,
        }

    def to_csv_header(self):
        return ['name', 'full_name', 'url']

    def to_csv_row(self):
        return [str(self.name), str(self.full_name), str(self.url)]

    def __str__(self):
        return " ".join(self.to_csv_row())
