import json

class WriteObject:

    def WriteOnJson(self, data):
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, cls=CustomEncoder, ensure_ascii=False)

    def ReadOnJson(self):
        with open("data.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def QueryOnJson(self, key_name, default_value):
        with open("data.json", "r") as file:
            data = json.load(file)
            result = data.get(key_name, default_value)
            return result

class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, 'to_dict'):
            return o.to_dict()
        return super().default(o)
