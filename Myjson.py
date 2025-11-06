import  json

class WriteObject:

    def WriteOnJson(self, data):
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    def ReadOnJson(self):
        with open("data.json", "r") as file:
            data = json.load(file)
