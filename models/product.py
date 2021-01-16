class Product:
    def __init__(self, name=None, price=None, url=None, catagory=None, _dict=None, _csv=None):
        if _dict:
            self.name = _dict.get('name')
            self.price = _dict.get('price')
            self.url = _dict.get('url')
            if _dict.get('catagory'):
                self.catagory = Catagory(_dict=_dict.get('catagory'))
        elif _csv:
            self.name = _csv[0]
            self.price = _csv[1]
            self.url = _csv[2]
        else:
            self.name = name
            self.price = price
            self.url = url
            self.catagory = catagory

    def to_dict(self):
        _dict = {
            'name': self.name,
            'price': self.price,
            'url': self.url,
        }
        for item, value in self.catagory.to_dict().items():
            _dict['catagory_'+item] = value
        return _dict

    def to_csv_header(self):
        return ['name', 'price', 'url']

    def to_csv_row(self):
        return [str(self.name), str(self.price), str(self.url)]

    def get_values(self, fields=None):
        if fields is None:
            fields = []

        values = [self.to_dict()[f] for f in fields]

        return values

    def __str__(self):
        return " ".join(self.to_csv_row())
