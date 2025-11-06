import  json
import studente
from studente import Studente
from pagella import Pagella
from voto import Voto

st = Studente("1","Emanuele",33, "1D")
pg = Pagella(1)
vt = Voto("Italiano",6)

#with open("data.json", "r") as file:
#    data = json.load(file)  # Load JSON data from file
#    print(data)

data = {"id": pg.idStudente, "name": st.name, "age": st.age, "Classroom":st.classroom, f"{vt.materia}":vt.valutazione}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)




