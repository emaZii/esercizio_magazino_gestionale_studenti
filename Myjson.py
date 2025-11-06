import  json
import studente
from studente import Studente
from pagella import Pagella
from voto import Voto

st = Studente("1","Emanuele",33,7)


#with open("data.json", "r") as file:
#    data = json.load(file)  # Load JSON data from file
#    print(data)

data = {"name": st.name, "age": st.age, "voto": st.voto}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)




