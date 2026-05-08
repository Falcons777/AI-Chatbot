import random
import time
import sys
import re
from chat_math_database import solve_math_expression
import socket

def start_server():
    host = "0.0.0.0"
    port = 5050

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print("🚀 ChatBoss Local Server ON")
    print("📡 Duke pritur lidhje ne port 5050...")

    while True:
        client, addr = server.accept()
        print(f"🔌 Nje lidhje ne Ip-ne...: {addr}")
        client.send("🤖 ChatBoss: Mire se erdhe ne server!\n".encode())
        client.close()

def start_client(ip):
    port = 5050
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print(s.recv(1024).decode())
        s.close()
    except Exception as e:
        print("❌ Nuk u lidha me serverin:", e)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "server":
            start_server()
        else:
            start_client(sys.argv[1])
    else:
        print("Përdor: python chatboss.py server | ip_address")

#Animacioni i tre pikave ...
def typing_animation(text="ChatBoss po shkruan 💬"):
    for i in range(3):
        for dots in [".  ", ".. ", "..."]:
            sys.stdout.write(f"\r{text}{dots}")
            sys.stdout.flush()
            time.sleep(0.2)
    print("\r", end="")

# Titulli kur te bisedoni me ChatBoss-in pjesa e pare informuese
print("Shkruani per te filluar nje bisede")
while True:
    msg = input("👤Ti: ")   # Merr tekstin nga përdoruesi
    msg = msg.lower()       # Konverton çdo shkronjë në të vogël për t’u krahasuar saktë

    # Pjesa automatike e matematikës — brenda loop
    math_result = solve_math_expression(msg)
    if math_result is not None:
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print(f"🤖ChatBoss: Rezultati eshte {math_result}")
        continue
# Fillimi i Databazes se pyetjeve nga User-i
    # Pjesa e pare e DB per #PERSHENDETJET DHE PYETJEVE SI SI KE QENE
    if msg in ("si je",
               "hey si je",
               "si je o lali",
               "he mo si je",
               "si je o plak",
               "si shkon",
               "si je o zemra",
    "si je ti"):
        responses = [                 #Kthimi i pergjigjjes pra "response" nga ChatBoss-i qe del si output nga terminali
            "Mire po ti si je?",
            "Mire jam po ti si ke qene?",
            "Po mire kam qene ti si ke qene?",
            "Shume mire jam, ti si je?",
            "Une jam mire faleminderit, ti si ke qene"
        ]
        print("ChatBoss po shkruan💬...", end="\r")  #Dhenja e informacionit qe ChatBoss-i po shkruan ose pergjijet User-it nga pyetja e tij
        time.sleep(1.2)             #Koha per te cilen do te marre dhenja e informacionit pra eshte nje animacion i cili nuk perfshin analizimin e pyetjes
        typing_animation()          #Deklarimi i animacionit per tre pikat ... dhe dhenja e ketij e animacionit ketij sektori
        print("🤖ChatBoss:", random.choice(responses)) #Jep pergjigjje te ndryshme te rastesishme User-it

    elif msg in ("ckemi",
                 "hey",
                ):
        responses = [
            "ckemi",
            "ckemi, me cfare mund te te ndihmoj",
            "pershendetje, si je?",
            "pershendetje, me cfare mund te te ndihmoj sot",
            "hey si je?"
        ]
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

    elif msg in ("hello",
                 "hello there",
                 "hi"
                 ):
        responses = [
            "Hello do you want to proceed in english will ChatBoss if yes or ok. Thank You"
        ]
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

    elif msg in ("yes",
                 "ok"
                 ):
        responses = [
            "Im am Ai chatbot i can offer you it information. Do you want to continue in english"
        ]
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses)
        )

    elif msg in ("no"):
        responses = [
            "Ok vazhdojme ne gjuhen shqipe atehere"
        ]
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses)
        )

    elif msg in ("ca bere", 
                 "ca bone",
                 "ca bone o lali",
                 "ca bone m zmr",
                 "ca bone m zemra"):
        responses = [
            "Hic per zotin, po rrija ketu e po prisja te flisje ti 😄",
            "Jo ndonjë gjë, po çlodhesha pak 😌",
            "Po beja ca kodime se s’mund te rri dot pa to 💻",
            "Hic mo, po merresha me ca gjera te mia 😁",
            "Po shihja ca filma, ti ca bere? 🎬",
            "Asgje vecse po mendoja per te fol me ty 😉",
            "Po rrija e po mendoja ca ide te reja per ChatBoss 🤖",
            "Po haja nje biskote me kafe ☕",
            "Po beja pak pushim, se me lodhi jeta virtuale 😂",
            "Po merresha me ca probleme teknike, por i zgjidha 😎"
        ]
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

    elif msg in ("si ke qene",
                 "a ke qene mire",
                 "a ke qen mire",
                 "a ke qen mire me shendet"):
        responses = [
        "Mire kam qene, shyqyr 😊 po ti si je?",
        "Shume mire jam, plot energji ⚡ ti si kalon?",
        "Po mbaj veten, faleminderit qe pyet, po ti?❤️",
        "Kam qene mire, s’ankohna 😁 ti vet?",
        "Po mire jam, ca dite me mire ca me lodhje, po ti? 😅",
        "Mire me shendet, vetem pak i zene me projektet, po ti? 💻",
        "Kam qene super, faleminderit qe pyete, po ti? 🙌",
        "Mire, po mezi prisja te flisnim prap, po ti? 😉",
        "Po mundohem te jem gjithmone pozitiv, po ti? 😎",
        "Shume mire jam, jeta virtuale shkon per mrekulli, po ti? 🤖"
        ]
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

    elif msg in ("mire kam qene",
                 "mire",
                 "mire faleminderit",
                 "mir faleminderit",
                 "po mire m",
                 "pz mir kam qen",
                 "per zotin mire kam qene",
                 "po mire kam qene",
                 "per zotin mir kam qen",
                 "mire jam"):
        responses = [
        "Shume mire! 😊 Me pelqen qe po kalon mire.",
        "Super! 😎 Po shpresoj qe dita jote po shkon edhe me mire.",
        "Shyqyr! 😁 Ca ke plan për sot?",
        "Mire pra! 🙌 Le të vazhdojmë bisedën.",
        "E mrekullueshme! 🎉 Mos harro te qeshesh shpesh 😄",
        "Po mire jam, gjithmonë kenaqesi te bisedoj me ty 🤖",
        "Shume mire! 😇",
        "Fantastike! 😃 Le të shohim se çfarë mund të flasim tani.",
        "Super, më pelqen të dëgjoj që po kalon mire! 😌"
        ]
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

   #Pjesa 2 e DB pjesa per pyetjet si KAM NJE PYETJE, CFARE JE TI, DHE PRANIMI PER TE BISEDUAR
    elif msg in ("kam nje pyetje per te te bere",
                 "kam nje pyetje per te bere",
                 "kam nje pyetje per ty",
                 "kam nje pyetje",
                 "du me te bo i pyetje",
                 "do tboj i pyetje",
                 "kam me te te bo nje pyetje",
                 "dua te te bej nje pyetje",
                 "e te te pyes per dicka",
                 "du me te te bo nje pyetje",
                 "dua te te bej nje pyetje",
                 "dua te bej nje pyetje"):
        responses = [
        "Sigurisht! Me pyet çdo gjë që do 😄",
        "Po, jam i gatshëm të të dëgjoj 🤖",
        "Çfarë pyetje ke? 😎",
        "Le të shohim si mund të ndihmoj 😌",
        "Përpara, pyete! 🙌",
        "Mezi pres të dëgjoj pyetjen tënde 😉",
        "Jam këtu për ty, pyete çdo gjë! 💬",
        "Sigurohu që pyetja të jetë e qartë 😁",
        "Po, më thuaj çfarë të shqetëson 📌",
        "Jam i gatshëm të të ndihmoj sa më mirë ❤️"
        ]
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2) 
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

    elif msg in ("ore ca je ti", "ca je ti", "kush je ti", "cfare je ti"):
        responses = [
            "Po une jam nje ChatBot, pra une komunikoj me ty me ane te fjaleve qe ti thua😉",
            "Une jam nje ChatBot i krijuar nga nje Nxenes me emrin Erind dhe jam ketu per te biseduar me ty💬",
            "Jam nje ChatBot qe mund te bisedoj me ty😄",
            "Po me pak fjale une jam nje ChatBot me emrin ChatBoss-i"
        ]
        print("ChatBoss po shkruan💬...",end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

    elif msg in ("ca ben ti",
                 "cfare ben ti",
                 "ca bon ti",
                 "ca ofron",
                 "cfare mund te besh ti",
                 "ca mund te besh ti",
                 "ca ofron ti"):
         responses = [
           "Une ofroj bisede me ty",
           "Te komunikoj me ty dhe te te jap informacion mbi teknologjine e fundit",
           "Une mund te te jap informacion mbi teknologjine sepse per mbaj nje database shume te madhe mbi teknologjine",
           "Mund te te jap shume informacion mbi teknologjine",
           "Une mund te te jap informacion mbi teknologjine"
         ]
         print("ChatBoss po shkruan💬...", end="\r")
         time.sleep(1.2)
         typing_animation()
         print("🤖ChatBoss:", random.choice(responses))

    #Pjesa 3 DB Informacion mbi teknologjine

    elif msg in ("me jep informacion mbi inxhinierine softwerike",
                 "a mundesh me me dhene informacion mbi inxhinierine softwerike",
                 "software engineer",
                 "cfare eshte nje software engineer",
                 "cfare eshte nje software inxhinier",
                 "cfare eshte nje inxhinier softweri",
                 "ca eshte inxhinieri i softwareit",
                 "ca eshte inxhinieri i softwerit",
                 "ca eshte inxhinieri i softwarit"):
        responses = (
            "🧠 Inxhinieria softuerike është fusha që merret me krijimin, zhvillimin "
            "dhe mirëmbajtjen e programeve kompjuterike.\n"
            "Ajo kombinon njohuri nga informatika, matematika dhe inxhinieria"
            "për të ndërtuar sisteme të qëndrueshme dhe të sigurta.",

            "👨‍💻 Një inxhinier softueri është personi që projekton, teston dhe përmirëson "
            "aplikacione kompjuterike.\nAi mund të punojë në zhvillim web, aplikacione mobile, "
            "AI, siguri kibernetike dhe shumë fusha të tjera.",

            "💡 Qëllimi kryesor i një inxhinieri softueri është të zgjidhë probleme reale "
            "duke përdorur kod.\nAi planifikon strukturën e një aplikacioni, shkruan kodin, "
            "teston funksionet dhe kujdeset që gjithçka të funksionojë siç duhet.",

            "📘 Inxhinieria softuerike përfshin disa faza si: analiza e kërkesave, dizajnimi, "
            "zhvillimi, testimi dhe mirëmbajtja.\nKëto ndihmojnë që çdo projekt të jetë i qartë, "
            "i organizuar dhe i qëndrueshëm në afatgjatë.",

            "🚀 Si profesion, Software Engineering është ndër më të kërkuarit sot.\n"
            "Një inxhinier softueri mund të punojë në kompani teknologjike, banka, spitale, "
            "apo madje edhe të krijojë aplikacionet e veta!"
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
            "çfarë është inteligjenca artificiale",
            "çfarë eshte ai",
            "ce eshte ai",
            "shpjego inteligjencen artificiale",
            "si funksionon ai",
            "ce eshte machine learning"):
        
        responses = (
        "Inteligjenca artificiale (AI) është fusha që krijon sisteme që mund të kryejnë detyra që kërkojnë inteligjencë njerëzore—p.sh. njohje teksti, imazhi, vendimmarrje.",
        "Machine Learning është nënfushë e AI që mëson nga të dhënat për të bërë parashikime ose klasifikime."
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))
    # search types: "encyclopedic explanation", "Wikipedia", "Chat Gpt", "Internet Information"

    elif msg in (
    "çfarë është cyber security",    # Siguria Kibernetike Information DB
    "cfare eshte cyber security",
    "ca eshte cyber security",
    "ce eshte cyber security",
    "ca osht cyber security",
    "cka eshte cyber security",
    "qa eshte cyber security",
    "cfar osht cyber security",
    "cyber security cfar eshte",
    "mund te ma shpjegosh cyber security",
    "cybersecurity cfar eshte",
    "cyber security do me thene",
    "me shpjego pak cyber security",
    "shpjego cyber security",
    "cyber security qka eshte",
    "qka osht cyber security",
    "qa osht cyber security",
    "cybersecurity çfarë është",
    "çfarë do të thotë cyber security",
    "cfare domethene cyber security",
    "cyber security si kuptohet",
    "cyber security do me thon ca",
    "ca dmth cyber security",
    "cfar dmth cyber security",
    "ce dmth cyber security",
    "ca kuptim ka cyber security",
    "cyber security shpjegoje pak",
    "cyber security me fjale te thjeshta",
    "cyber security ca nenkupton",
    "cyber security ca do te thote"
        ):
        responses = (
        "Cyber Security është fusha që merret me mbrojtjen e sistemeve kompjuterike dhe rrjeteve nga sulmet dixhitale. 🛡️",
        "Në pak fjalë, Cyber Security është mbrojtja e informacionit dhe e sistemeve nga hakerat dhe rreziqet online. 🔐",
        "Cyber Security është si një rojtar dixhital që mbron të dhënat e tua personale nga vjedhja. 💂‍♂️💻",
        "Mendoje si një sistem alarmi dhe bravash të forta, por për shtëpinë tënde dixhitale. 🏠🔒",
        "Është mburoja që bllokon viruset, malware-t dhe sulmet phishing para se ato të bëjnë dëm. 🛡️🦠",
        "Cyber Security është arti i parandalimit të aksesit të paautorizuar në pajisjet dhe llogaritë e tua online. 🚫🔓",
        "Shkurtimisht: Është mbrojtja e jetës sate dixhitale nga kriminelët kibernetikë. 🦸‍♂️💻",
        "Është praktika që garanton që mesazhet, fotot dhe informacionet e tua bankare të mbeten plotësisht private. 🕵️‍♂️💳",
        "Në thelb, Cyber Security siguron që teknologjia që përdorim çdo ditë të jetë e sigurt dhe e besueshme. 📱✅"
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

    
    elif msg in (
        "çfarë është inteligjenca artificiale", "cfare eshte inteligjenca artificiale",
        "çfarë është ai", "cfare eshte ai", "ca eshte ai", "qfar eshte ai",
        "shpjego inteligjencen artificiale", "me trego per ai", "ai teknologjia"
    ):
        responses = (
            "Inteligjenca Artificiale (AI) është aftësia e makinerive për të simuluar inteligjencën njerëzore, si mësimi dhe zgjidhja e problemeve. 🤖",
            "Në terma të thjeshtë, AI i lejon kompjuterët të mendojnë dhe të veprojnë si njerëzit për detyra specifike. 🧠",
            "AI është teknologjia që fuqizon mjetet si ChatGPT, makinat pa shofer dhe asistentët si Siri apo Alexa. 🚀",
            "Është fusha e informatikës që krijon sisteme të afta për të marrë vendime autonome bazuar në të dhëna. 📈"
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))


    elif msg in (
        "çfarë është quantum computing", "cfare eshte quantum computing",
        "çfarë është kompjutimi kuantik", "cfare eshte kompjutimi kuantik",
        "ca eshte quantum computing", "shpjego teknologjine kuantike"
    ):
        responses = (
            "Quantum Computing është një teknologji e re që përdor fizikën kuantike për të zgjidhur probleme që kompjuterët tanë aktualë nuk mund t'i zgjidhin. ⚛️",
            "Kompjuterët kuantikë janë jashtëzakonisht të shpejtë dhe mund të përpunojnë miliona të dhëna në sekondë duke përdorur 'qubits'. ⚡",
            "Mendoje si një super-kompjuter që mund të bëjë llogaritje që një kompjuteri normal do t'i duheshin mijëra vjet. 🌀"
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))


    elif msg in (
        "çfarë është blockchain", "cfare eshte blockchain", "ca eshte blockchain",
        "shpjego blockchain", "qka eshte blockchain", "si funksionon blockchain"
    ):
        responses = (
            "Blockchain është një lloj blloku shënimesh dixhital ku informacioni ruhet në mënyrë të tillë që nuk mund të ndryshohet apo hakohet. ⛓️",
            "Është teknologjia pas Bitcoin-it, por përdoret edhe për siguri, kontrata inteligjente dhe votime dixhitale. 🔒",
            "Mendoje si një zinxhir të dhënash të shpërndara në shumë kompjuterë, ku transparenca është rregulli kryesor. 🌐"
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))


    elif msg in (
        "çfarë është cloud computing", "cfare eshte cloud computing",
        "ca eshte cloud", "qfar eshte cloud", "shpjego cloud-in",
        "ruajtja ne cloud", "aws", "azure", "google cloud"
    ):
        responses = (
            "Cloud Computing është ofrimi i shërbimeve kompjuterike (si serverët, ruajtja e të dhënave, bazat e të dhënave) përmes internetit. ☁️",
            "Në vend që t'i kesh të dhënat në hard diskun tënd, i mban ato në serverë të fuqishëm që mund t'i aksesosh nga kudo. 🌍",
            "Shërbimet më të njohura të Cloud-it janë Amazon Web Services (AWS), Microsoft Azure dhe Google Cloud. 🚀",
            "Mendoje si të marrësh energji elektrike: nuk ke nevojë për gjeneratorin tënd, thjesht paguan për atë që përdor nga rrjeti. ⚡"
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

    
    elif msg in (
        "çfarë është data science", "cfare eshte data science",
        "ca eshte data science", "shkenca e te dhenave",
        "shpjego big data", "cfare eshte big data", "analiza e te dhenave"
    ):
        responses = (
            "Data Science është fusha që kombinon statistikën dhe programimin për të nxjerrë informacione të vlefshme nga sasitë e mëdha të të dhënave. 📊",
            "Data Scientists janë njerëzit që 'parashikojnë' të ardhmen duke analizuar modelet e sjelljes në të kaluarën. 🔍",
            "Big Data i referohet sasive aq të mëdha të të dhënave saqë softuerët tradicionalë nuk mund t'i përpunojnë dot më. 🐘",
            "Është teknologjia që i lejon kompanive si Spotify ose Youtube të të sugjerojnë fiks këngën ose videon që të pëlqen. 🎧"
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))


    elif msg in (
        "çfarë është iot", "cfare eshte iot", "internet of things",
        "interneti i gjerave", "ca eshte iot", "pajisjet smart",
        "shtepia inteligjente", "qka eshte iot"
    ):
        responses = (
            "Internet of Things (IoT) është rrjeti i pajisjeve fizike (si dritat, frigoriferët, makinat) që lidhen me internetin për të shkëmbyer të dhëna. 🏠📡",
            "IoT lejon që pajisjet e shtëpisë sate të 'flasin' me njëra-tjetrën dhe ti t'i kontrollosh ato përmes telefonit. 📱",
            "Mendo një orë që mat rrahjet e zemrës dhe ia dërgon raportin direkt mjekut tënd – kjo është fuqia e IoT! ⌚❤️",
            "Së shpejti, çdo pajisje elektronike do të jetë pjesë e IoT, duke e bërë botën më të ndërlidhur. 🌐"
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))


    elif msg in (
        "çfarë është devops", "cfare eshte devops", "ca eshte devops",
        "shpjego devops", "qfar eshte devops", "puna ne devops"
    ):
        responses = (
            "DevOps është një bashkëpunim midis programuesve (Dev) dhe ekipit të operacioneve TI (Ops) për të krijuar softuer më shpejt dhe me më pak gabime. 🛠️",
            "Qëllimi i DevOps është automatizimi i procesit të ndërtimit, testimit dhe dërgimit të softuerit te përdoruesi fundor. 🔄",
            "Është një kulturë pune ku inxhinierët kujdesen për të gjithë ciklin e jetës së një aplikacioni. ♾️",
            "Nëse një aplikacion si Facebook përditësohet pa u bllokuar fare, kjo është meritë e proceseve të mira DevOps. ✅"
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))


    elif msg in (
        "çfarë është edge computing", "cfare eshte edge computing",
        "ca eshte edge computing", "shpjego edge", "pse eshte i rendesishem edge"
    ):
        responses = (
            "Edge Computing është teknologjia që i përpunon të dhënat pranë vendit ku ato krijohen (p.sh. brenda telefonit ose kamerës), në vend që t'i dërgojë në një server të largët. ⚡",
            "Kjo e bën teknologjinë shumë më të shpejtë sepse eliminon vonesat (latency) që shkakton dërgimi i të dhënave në Cloud. 🕒",
            "Edge Computing është thelbësor për makinat që ecin vetë, sepse ato duhet të marrin vendime në milisekonda pa pritur përgjigje nga interneti. 🚗💨"
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))


    elif msg in (
        "çfarë është digital forensics", "cfare eshte forenzika dixhitale",
        "hetimi i krimeve kibernetike", "ca eshte forenzika", "si zbulohen hakerat"
    ):
        responses = (
            "Digital Forensics është shkenca që merret me mbledhjen dhe analizimin e provave nga pajisjet elektronike për të zbuluar krime. 🕵️‍♂️💻",
            "Forenzikët dixhitale mund të gjejnë skedarë të fshirë, të gjurmojnë vendndodhjen e një sulmi dhe të zbulojnë kush fshihet pas një hakerimi. 🔍",
            "Është si puna e CSI-së, por në vend të shenjave të gishtave në mur, ata kërkojnë 'gjurmë' në kod dhe në memorie. 💾🛡️"
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))


    elif msg in (
        "çfarë është generative ai", "cfare eshte generative ai",
        "ca eshte genai", "shpjego ai gjenerative", "si funksionon chatgpt",
        "inteligjenca artificiale gjenerative"
    ):
        responses = (
            "Generative AI është një lloj inteligjence artificiale që mund të krijojë përmbajtje të re, si tekst, imazhe, muzikë apo edhe kod programimi. ✨",
            "Ndryshe nga AI tradicional që vetëm analizon të dhënat, GenAI krijon diçka plotësisht origjinale bazuar në ato që ka mësuar. 🎨",
            "Mendoje si një asistent super-kreativ që mund të shkruajë një ese ose të vizatojë një pikturë në pak sekonda. ✍️"
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))
        
    elif msg in (
    "çfarë është machine learning",   # Machine Learning Information DB 
    "ce eshte machine learning",
    "cfare eshte machine learning",
    "çfarë do të thotë machine learning",
    "me shpjego machine learning",
    "cfare kuptojme me machine learning",
    "mund te ma shpjegosh machine learning",
    "si funksionon machine learning",
    "me trego per machine learning",
    "me thuaj ca eshte machine learning",
    "me jep nje shpjegim per machine learning",
    "machine learning cfare eshte",
    "ca kuptim ka machine learning",
    "ca eshte machine learning",
    "machine learning ne fjale te thjeshta"
        ):
        responses = (
            "Machine Learning (Mësimi i Makinerive) është një degë e inteligjencës artificiale që i lejon kompjuterët\ntë mësojnë nga përvoja, pa qenë të programuar drejtpërdrejt. Ai përdor të dhëna për të ndërtuar modele që parashikojnë ose vendosin në mënyrë automatike.",
    "Me Machine Learning, një kompjuter mëson nga të dhënat – për shembull, mund të mësojë të njohë fytyra,\nstë dallojë email-et spam, apo të parashikojë motin, duke analizuar shembujt e mëparshëm.",
    "Machine Learning është procesi ku një kompjuter mëson të marrë vendime ose të bëjë parashikime në bazë të të dhënave, ashtu si një njeri mëson nga përvoja."
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është ethical hacking",   # Ethical Hacking Information DB
    "cfare eshte ethical hacking",
    "qfar eshte ethical hacking",
    "qka eshte ethical hacking",
    "ca eshte ethical hacking",
    "ce eshte ethical hacking",
    "shpjego ethical hacking",
    "me shpjego ethical hacking",
    "çfar kuptohet me ethical hacking",
    "cfar kuptohet me ethical hacking",
    "çfare eshte etikal heking",
    "cfare eshte etikal heking",
    "ca eshte etikal heking",
    "helo",
    "ce eshte etikal heking",
    "çfare eshte hacking etik",
    "cfare eshte hacking etik",
    "ca eshte hacking etik",
    "qfar eshte hacking etik",
    "shpjego hacking etik",
    "me shpjego hacking etik"
        ):
       responses = (
        "Ethical Hacking është procesi i testimit të sigurisë së sistemeve kompjuterike për të zbuluar dobësi — por me leje dhe në mënyrë ligjore.",
        "Hakerët etikë përdorin të njëjtat teknika si hakerët e zakonshëm, por qëllimi i tyre është të ndihmojnë në përmirësimin e sigurisë.",
        "Ethical Hacking do të thotë të zbulosh dhe të rregullosh dobësitë në sisteme përpara se dikush tjetër t’i shfrytëzojë ato keq.",
        "Një haker etik është si një “roje dixhitale” që kontrollon sistemet për t’u siguruar që janë të mbrojtura.",
       "Ethical Hacking është pjesë e Cyber Security dhe është thelbësore për mbrojtjen e të dhënave dhe rrjeteve nga sulmet."
        )
       print("ChatBoss po shkruan💬...", end="\r")
       time.sleep(1.2)
       typing_animation()
       print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është deep learning",  # Deep Learning Information DB
    "cfare eshte deep learning",
    "qfar eshte deep learning",
    "qka eshte deep learning",
    "ca eshte deep learning",
    "ce eshte deep learning",
    "shpjego deep learning",
    "me shpjego deep learning",
    "çfar kuptohet me deep learning",
    "cfar kuptohet me deep learning",
    "cka kuptohet me deep learning",
    "qka kuptohet me deep learning",
    "ca kuptohet me deep learning",
    "çfare eshte te mesuarit e thelle",
    "cfare eshte te mesuarit e thelle",
    "qfar eshte te mesuarit e thelle",
    "ca eshte te mesuarit e thelle",
    "shpjego te mesuarit e thelle",
    "me shpjego te mesuarit e thelle"
        ):
       responses = (
        "Deep Learning është një nënfushë e Machine Learning që përdor rrjete të thella neuronesh për të mësuar nga sasi të mëdha të dhënash.",
        "Është teknologjia pas inteligjencës artificiale që i lejon kompjuterët të mësojnë modele shumë komplekse – si zëri, imazhi apo teksti.",
        "Deep Learning imiton mënyrën si funksionon truri i njeriut, duke përdorur shtresa neuronesh për të njohur modele dhe për të bërë parashikime.",
        "Në thelb, është mënyra më e avancuar që kompjuterët përdorin për të 'mësuar vetë' nga përvoja dhe të dhënat.",
        "Përmes Deep Learning, sistemet moderne si ChatGPT, njohja e fytyrës dhe veturat autonome mund të kuptojnë botën dixhitale më thellë."
       )
       print("ChatBoss po shkruan💬...", end="\r")
       time.sleep(1.2)
       typing_animation()
       print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është neural network",    # Neural Network Information DB 
    "cfare eshte neural network",
    "qfar eshte neural network",
    "qka eshte neural network",
    "ca eshte neural network",
    "ce eshte neural network",
    "shpjego neural network",
    "me shpjego neural network",
    "çfar kuptohet me neural network",
    "cfar kuptohet me neural network",
    "qka kuptohet me neural network",
    "cka kuptohet me neural network",
    "ca kuptohet me neural network",
    "çfare eshte rrjeti neuronesh",
    "cfare eshte rrjeti neuronesh",
    "qfar eshte rrjeti neuronesh",
    "ca eshte rrjeti neuronesh",
    "shpjego rrjeti neuronesh",
    "me shpjego rrjeti neuronesh"
        ):
       responses = (
        "Neural Network është një sistem i inspiroar nga truri i njeriut, që përdor një rrjet të shtresave neuronesh për të mësuar modele nga të dhënat.",
        "Është baza e shumicës së algoritmeve të Deep Learning, duke i lejuar kompjuterëve të njohin modele komplekse si imazhe, zëra ose tekste.",
        "Rrjetet neuronesh përpunojnë informacion në shtresa të ndryshme, duke nxjerrë karakteristika të ndryshme dhe duke mësuar lidhje midis tyre.",
        "Në thelb, një neural network imiton mënyrën se si neuronet në tru lidhen dhe komunikojnë për të marrë vendime dhe parashikime.",
        "Këto rrjete përdoren për sistemet e njohjes së fytyrës, për përpunimin e gjuhës natyrore dhe shumë aplikacione të tjera të AI."
       )
       print("ChatBoss po shkruan💬...", end="\r")
       time.sleep(1.2)
       typing_animation()
       print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është nlp",       # Natural Language Processing Information DB
    "cfare eshte nlp",
    "qfar eshte nlp",
    "ca eshte nlp",
    "ce eshte nlp",
    "shpjego nlp",
    "me shpjego nlp",
    "çfar kuptohet me nlp",
    "cfar kuptohet me nlp",
    "qka kuptohet me nlp",
    "cka kuptohet me nlp",
    "ca kuptohet me nlp",
    "çfarë është natural language processing",
    "cfare eshte natural language processing",
    "qfar eshte natural language processing",
    "ca eshte natural language processing",
    "shpjego natural language processing",
    "me shpjego natural language processing"
        ):
      responses = (
        "Natural Language Processing (NLP) është fusha e AI që mëson kompjuterët të kuptojnë dhe përpunojnë gjuhën njerëzore.",
        "NLP përdoret për të analizuar tekst, njohur zërin, përkthime automatike dhe biseda me chatbot-e.",
        "Kjo fushë kombinon linguistikën dhe mësimin makinerik për të kuptuar kuptimin e fjalisë dhe kontekstin e të dhënave gjuhësore.",
        "Për shembull, sistemi që përktheh tekst automatikisht ose chatboti që flasin me ty përdor NLP për të kuptuar çfarë thuhet.",
        "Algoritmet NLP mund të nxjerrin fjalë kyçe, analiza sentimentin e një teksti dhe të krijojnë përgjigje të kuptueshme."
      )
      print("ChatBoss po shkruan💬...", end="\r")
      time.sleep(1.2)
      typing_animation()
      print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është ai",
    "ca eshte ai",
    "cfare eshte ai",
    "ce eshte inteligjenca artificiale",
    "ca eshte artificial intelligence",
    "me shpjego ai",
    "ai ne fjale te thjeshta",
    "çfare ben ai",
    "si funksionon ai",
    "me jep nje shpjegim per ai",
    "me trego per inteligjencen artificiale",
    "ai shpjegim i thjeshte"
        ):
      responses = (
        "Inteligjenca Artificiale (AI) është aftësia e kompjuterëve për të kryer detyra që zakonisht kërkojnë inteligjencë njerëzore: njohje të imazheve, të folurit, vendimmarrje dhe parashikime.",
        "AI është teknologjia që i lejon makinat të mësojnë nga të dhënat, të mendojnë dhe të marrin vendime automatikisht.",
        "Inteligjenca Artificiale është mënyra se si kompjuterët simulojnë mënyrën si mendon njeriu, duke përdorur algoritme dhe të dhëna.",
        "AI kombinon algoritme të avancuara për të kryer detyra inteligjente si rekomandime, njohje fytyrash, analiza dhe shumë më tepër."
      )
      print("ChatBoss po shkruan💬...", end="\r")
      time.sleep(1.2)
      typing_animation()
      print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është frontend development",
    "cfare eshte frontend",
    "ce eshte frontend",
    "front end cfare eshte",
    "front-end cfare eshte",
    "front end development cfare eshte",
    "çka është frontend",
    "cka eshte frontend",
    "frontend do me thene cfare",
    "me shpjego frontend",
    "cfare kuptojme me frontend development",
    "frontend development çfarë është",
    "frontend ne programim çfarë është",
    "frontend programim cfare eshte",
    "me trego çfarë është frontend",
    "hajde ma shpjego frontend",
    "frontend ne fjale te thjeshta cfare eshte",
    "si funksionon frontend",
    "front end domethenia",
    "domethenia e frontend development"
        ):
      responses = (
        "Frontend Development është pjesa e faqes ose aplikacionit që përdoruesi e sheh dhe ndërvepron.\n"
        "Kjo përfshin dizajnin, elementët vizualë dhe logjikën që ndodh në browser.",

        "Frontend është pjesa vizuale e një website—faqet, butonat, ngjyrat dhe çdo gjë që prek përdoruesi.\n"
        "Shpesh përdor HTML, CSS dhe JavaScript.",

        "Frontend Development merret me ndërtimin e ndërfaqeve të përdoruesit.\n"
        "Programuesit frontend punojnë që një faqe të jetë e bukur, e shpejtë dhe funksionale.",

        "Pjesa frontend është ‘fytyra’ e një aplikacioni.\n"
        "Ajo është ajo që përdoruesi sheh dhe përdor direkt në ekran.",

        "Frontend është teknologjia që i jep formë pamjes së jashtme të aplikacioneve.\n"
        "Qëllimi është thjeshtë: përdoruesi të ketë një eksperiencë të këndshme dhe intuitive."
      )
      print("ChatBoss po shkruan💬...", end="\r")
      time.sleep(1.2)
      typing_animation()
      print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është frontend development",
    "cfare eshte frontend",
    "ce eshte frontend",
    "front end cfare eshte",
    "front-end cfare eshte",
    "front end development cfare eshte",
    "çka është frontend",
    "cka eshte frontend",
    "frontend do me thene cfare",
    "me shpjego frontend",
    "cfare kuptojme me frontend development",
    "frontend development çfarë është",
    "frontend ne programim çfarë është",
    "frontend programim cfare eshte",
    "me trego çfarë është frontend",
    "hajde ma shpjego frontend",
    "frontend ne fjale te thjeshta cfare eshte",
    "si funksionon frontend",
    "front end domethenia",
    "domethenia e frontend development"
        ):
      responses = (
        "Frontend Development është pjesa e faqes ose aplikacionit që përdoruesi e sheh dhe ndërvepron.\n"
        "Kjo përfshin dizajnin, elementët vizualë dhe logjikën që ndodh në browser.",

        "Frontend është pjesa vizuale e një website—faqet, butonat, ngjyrat dhe çdo gjë që prek përdoruesi.\n"
        "Shpesh përdor HTML, CSS dhe JavaScript.",

        "Frontend Development merret me ndërtimin e ndërfaqeve të përdoruesit.\n"
        "Programuesit frontend punojnë që një faqe të jetë e bukur, e shpejtë dhe funksionale.",

        "Pjesa frontend është ‘fytyra’ e një aplikacioni.\n"
        "Ajo është ajo që përdoruesi sheh dhe përdor direkt në ekran.",

        "Frontend është teknologjia që i jep formë pamjes së jashtme të aplikacioneve.\n"
        "Qëllimi është thjeshtë: përdoruesi të ketë një eksperiencë të këndshme dhe intuitive."
      )
      print("ChatBoss po shkruan💬...", end="\r")
      time.sleep(1.2)
      typing_animation()
      print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është backend development",
    "cfare eshte backend development",
    "ca eshte backend development",
    "backend cfare do te thote",
    "me shpjego backend-in",
    "backend ne programim",
    "backend explanation"
        ):
        responses = (
        "Backend Development është pjesa e prapme e një aplikacioni, ku menaxhohen të dhënat, logjika e sistemit dhe komunikimi me serverët.",
        "Backend është infrastruktura që qëndron pas një aplikacioni: serveri, databaza dhe logjika që bën gjithçka të funksionojë.",
        "Me pak fjalë, Backend është ‘truri’ i aplikacionit që përpunon informacionin që përdoruesi nuk e sheh."
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))
    
    elif msg in (
    "çfarë është cloud computing",
    "cfare eshte cloud computing",
    "ca eshte cloud computing",
    "cloud computing cfare do te thote",
    "what is cloud computing",
    "cloud computing explanation",
    "cloud computing ne menyre te thjeshte",
    "cloud shpjegim",
    "cloud computing meaning"
       ):
       responses = (
        "Cloud Computing është ofrimi i shërbimeve kompjuterike (servera, databaza, storage, rrjete) përmes internetit, pa pasur nevojë të kesh pajisje fizike.",
        "Cloud Computing do të thotë të përdorësh servera në distancë për ruajtje, përpunim të të dhënave dhe aplikacione – pra gjithçka ndodh ONLINE.",
        "Me pak fjalë: Cloud lejon që kompjuteri yt të mos bëjë punë të rëndë, por ta bëjnë serverat e kompanive si Amazon, Google dhe Microsoft."
       )
       print("ChatBoss po shkruan💬...", end="\r")
       time.sleep(1.2)
       typing_animation()
       print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është robotics engineering",
    "cfare eshte robotics engineering",
    "ce eshte robotics engineering",
    "me shpjego robotics engineering",
    "ca kuptimi ka robotics engineering",
    "robotics engineering shpjegim",
    "robotics engineering ne fjale te thjeshta",
    "me thuaj ca eshte robotics engineering",
    "çfare do te thote robotics engineering",
    "robotika cfare eshte",
    "ca eshte robotika",
    "me trego per robotics engineering",
    "robotics engineering informacion",
    "informatat per robotics engineering",
    "si funksionon robotics engineering",
    "robotics engineer cfare ben",
    "pune robotics engineering",
    "robotics engineering penefit",
    "robotics engineering what is",
    "explain robotics engineering"
       ):
       responses = (
        "Robotics Engineering është fusha që merret me krijimin, ndërtimin dhe programimin e robotëve. "
        "Ajo kombinon mekanikën, elektronikën dhe programimin për të krijuar makina që kryejnë detyra në mënyrë të pavarur.",

        "Në Robotics Engineering, dizajnoni robotë që mund të ecin, të kapin objekte, të montojnë pajisje, "
        "të navigojnë hapësirë dhe të bashkëveprojnë me njerëzit. Është një ndër fushat më të avancuara të teknologjisë.",

        "Robotics Engineering bashkon mekanikën, inxhinierinë elektrike dhe programimin. "
        "Robotët përdoren në mjekësi, industri, hapësirë, ushtri, bujqësi dhe shtëpi smart.",

        "Një robotics engineer krijon sisteme inteligjente që mund të lëvizin, perceptojnë mjedisin dhe të vendosin vetë. "
        "Është një profesion shumë i kërkuar dhe i paguar mirë.",

        "Thjesht: Robotics Engineering = krijimi i robotëve dhe sistemeve autonome që bëjnë detyra që njerëzit s’i bëjnë dot "
        "ose nuk duan t’i bëjnë. Një fushë super futuristike."
       )
       print("ChatBoss po shkruan💬...", end="\r")
       time.sleep(1.2)
       typing_animation()
       print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është system administration",
    "cfare eshte sysadmin",
    "ce eshte system administration",
    "me shpjego system administration",
    "çfarë bën sysadmin",
    "puna e sysadmin",
    "system administrator cfare ben",
    "system administration shpjegim",
    "me trego për sysadmin",
    "system administration ne fjale te thjeshta",
    "sysadmin informacion",
    "si funksionon system administration",
    "sysadmin job",
    "detyrat e sysadmin",
    "system administration perks",
    "çfarë kuptimi ka system administration",
    "explain sysadmin",
    "what is system administration"
       ):
       responses = (
        "System Administration është fusha që merret me menaxhimin, konfigurimin dhe mirëmbajtjen e sistemeve kompjuterike dhe rrjeteve.",

        "Një sysadmin siguron që serverat dhe rrjetet të funksionojnë pa probleme, të azhurnohen dhe të jenë të sigurt.",

        "Sysadmins monitorojnë performancën e sistemeve, rregullojnë gabimet dhe menaxhojnë përdoruesit dhe aksesin në rrjet.",

        "Thjesht: System Administration = të mbash gjithçka kompjuterike të funksionojë, nga serverat e rrjetet tek aplikacionet dhe databazat.",

        "Puna e sysadmin është kritike për çdo kompani që përdor teknologji. Ata janë 'gardianët' e sistemeve kompjuterike."
       )
       print("ChatBoss po shkruan💬...", end="\r")
       time.sleep(1.2)
       typing_animation()
       print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është embedded systems",
    "cfare eshte embedded systems",
    "ce eshte IoT",
    "çfarë është Internet of Things",
    "me shpjego IoT",
    "embedded systems shpjegim",
    "si funksionon IoT",
    "çfarë bën një embedded engineer",
    "me trego për IoT",
    "puna në embedded systems",
    "IoT në fjale të thjeshta",
    "embedded systems cfare jane",
    "puna me embedded devices",
    "çfarë kuptimi ka IoT",
    "si funksionojnë embedded systems",
    "Internet of Things job",
    "embedded systems info"
       ):
       responses = (
        "Embedded Systems janë kompjuterë të vegjël të integruar në pajisje për të kryer funksione specifike.",

        "IoT (Internet of Things) i lidh këto pajisje me internetin, duke i bërë ato të 'të zgjuara' dhe të komunikojnë mes tyre.",

        "Shembuj: frigoriferët smart që të paralajmërojnë kur mungon ushqimi, sensorët në makina që monitorojnë performancën, apo dritat që ndizën automatikisht.",

        "Embedded Systems + IoT = pajisje inteligjente që marrin dhe dërgojnë të dhëna për të bërë jetën më të lehtë dhe kompanitë më efikase.",

        "Një inxhinier Embedded/IoT krijon softuerin dhe harduerin që lejon këto pajisje të funksionojnë dhe lidhen me internetin."
       )
       print("ChatBoss po shkruan💬...", end="\r")
       time.sleep(1.2)
       typing_animation()
       print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është software testing",
    "cfare eshte QA automation",
    "ce eshte testimi i softuerit",
    "çfarë bën një QA engineer",
    "software testing shpjegim",
    "si funksionon QA automation",
    "puna në software testing",
    "me trego për QA",
    "testimi automatik i softuerit",
    "QA automation info",
    "software testing në fjale të thjeshta",
    "testimi manual vs automatik",
    "puna e QA engineer",
    "çfarë kuptimi ka testimi i softuerit",
    "si bëhet QA automation",
    "për çfarë përdoret software testing"
       ):
       responses = (
        "Software Testing është procesi i kontrollimit të softuerit për të siguruar që funksionon saktë dhe pa gabime.",

        "QA Automation përdor skripta dhe mjete për të testuar automatikisht softuerin, duke kursyer kohë dhe rritur saktësinë.",

        "Shembuj: testimi i faqeve web, aplikacioneve mobile, lojërave, apo sistemeve komplekse për të siguruar që çdo gjë funksionon si duhet.",

        "Një QA engineer siguron që produkti final të jetë i besueshëm, i sigurt dhe i kënaqshëm për përdoruesit.",

        "Testimi manual bëhet nga njerëzit, ndërsa testimi automatik përdor softuer që ekzekuton testet vetë, shpesh gjatë zhvillimit të aplikacioneve."
       )
       print("ChatBoss po shkruan💬...", end="\r")
       time.sleep(1.2)
       typing_animation()
       print("🤖ChatBoss:", random.choice(responses))
    
    elif msg in (
    "çfarë është cloud computing",
    "cfare eshte cloud architecture",
    "cloud architecture shpjegim",
    "cloud computing ne fjale te thjeshta",
    "si funksionon cloud",
    "çfarë bën një cloud architect",
    "cloud info",
    "cka eshte cloud",
    "cloud developer cfare ben",
    "si punohet me cloud",
    "cloud vs server",
    "si funksionon aws",
    "azure shpjegim",
    "google cloud info",
    "cloud architecture si fillestar"
       ):
       responses = (
        "Cloud Architecture është mënyra se si ndërtohen dhe menaxhohen aplikacionet në internet duke përdorur servera në distancë, jo kompjuterat lokal.",
        
        "Cloud përdor shërbime si Compute, Storage, Database dhe Networking për të ndërtuar aplikacione të shpejta, të sigurta dhe të shkallëzueshme.",
        
        "Një Cloud Architect dizajnon sistemet në AWS, Azure ose Google Cloud, duke u siguruar që janë të sigurta, të shpejta dhe me kosto të ulët.",
        
        "Në cloud përdoren teknologji si virtual machines, containers (Docker), serverless functions dhe databaza cloud-native.",
        
        "Përfitimet kryesore të cloud: më pak kosto, më shumë siguri, rritje automatike e kapacitetit dhe akses nga çdo pajisje."
       )
       print("ChatBoss po shkruan💬...", end="\r")
       time.sleep(1.2)
       typing_animation()
       print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është data engineering",
    "cfare eshte data engineering",
    "data engineer shpjegim",
    "puna e data engineer",
    "si funksionon data engineering",
    "data pipelines çfarë janë",
    "etl çfare eshte",
    "si ndertohen data pipelines",
    "çfarë bën një data engineer",
    "data engineering ne fjale te thjeshta",
    "big data shpjegim",
    "cka ben nje data engineer"
       ):
       responses = (
        "Data Engineering merret me mbledhjen, pastrimin, transformimin dhe ruajtjen e të dhënave në sisteme të mëdha.",
        "Një Data Engineer krijon data pipelines që marrin të dhëna nga shumë burime dhe i dërgojnë në databaza apo sisteme analitike.",
        "Data Engineers punojnë me ETL, databaza, cloud services dhe big data tools si Hadoop apo Spark.",
        "Qëllimi i Data Engineering është të sigurojë që të dhënat të jenë të sakta, të shpejta dhe të gatshme për analiza."   
       )
       print("ChatBoss po shkruan💬...", end="\r")
       time.sleep(1.2)
       typing_animation()
       print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është ar",
    "cfare eshte ar"
    "çfarë është vr",
    "cfare eshte vr",
    "cfare eshte ar vr",
    "cfarë eshte ar vr",
    "ar vr development shpjegim",
    "si funksionon vr",
    "realitet i shtuar çka eshte",
    "realitet virtual shpjegim",
    "punë në ar vr",
    "cka ben nje ar developer",
    "cka ben nje vr developer",
    "ar vr ne fjale te thjeshta"
      ):
      responses = (
        "AR (Augmented Reality) shton objekte virtuale mbi botën reale, ndërsa VR (Virtual Reality) krijon një botë plotësisht të re.",
        "AR/VR Development përdor Unity, Unreal Engine, 3D modeling dhe sensorë për të krijuar eksperienca realiste.",
        "VR kërkon pajisje si Meta Quest, ndërsa AR përdoret edhe në telefona me kamera.",
        "Një AR/VR developer ndërton lojëra, simulime, aplikacione edukative, trajnime ose eksperienca interaktive."
      )
      print("ChatBoss po shkruan💬...", end="\r")
      time.sleep(1.2)
      typing_animation()
      print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është blockchain",
    "cfare eshte blockchain development",
    "blockchain shpjegim",
    "si funksionon blockchain",
    "çfarë është kriptografia blockchain",
    "çfarë bën një blockchain developer",
    "smart contracts cfare jane",
    "solidity shpjegim",
    "web3 shpjegim",
    "blockchain ne fjale te thjeshta"
       ):
       responses = (
        "Blockchain është një teknologji ku të dhënat ruhen në blloqe të lidhura që nuk mund të ndryshohen lehtë.",
        "Një Blockchain Developer krijon Smart Contracts dhe aplikacione Web3 që funksionojnë pa server qendror.",
        "Blockchain përdor kriptografi për siguri të lartë dhe është baza e Bitcoin, Ethereum dhe shumë sistemeve të tjera.",
        "Smart contracts janë programe që ekzekutohen automatikisht në blockchain pa ndërhyrje njerëzore."
       )
       print("ChatBoss po shkruan💬...", end="\r")
       time.sleep(1.2)
       typing_animation()
       print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është game development",
    "cfare eshte game development",
    "cfare eshte game dev",
    "puna e game developer",
    "si krijohen lojërat",
    "si funksionon game engine",
    "unity shpjegim",
    "unreal engine shpjegim",
    "cka ben nje game developer",
    "game development ne fjale te thjeshta",
    "si behet nje loje",
    "lojerat si krijohen"
       ):
       responses = (
        "Game Development është procesi i krijimit të lojërave duke përdorur game engines si Unity ose Unreal Engine.",
        "Game Developers krijojnë mekanika loje, grafikë, animacione, logjikë dhe sisteme fizike.",
        "Një lojë kalon në faza: ideja, dizajni, programimi, grafika, testimi dhe publikimi.",
        "Lojërat 2D dhe 3D kërkojnë kod, art, zëra, fizikë dhe optimizim të performancës."
       )
       print("ChatBoss po shkruan💬...", end="\r")
       time.sleep(1.2)
       typing_animation()
       print("🤖ChatBoss:", random.choice(responses))

    elif msg in (
    "çfarë është mobile app development",
    "cfare eshte mobile app development",
    "mobile app development shpjegim",
    "mobile development shpjegim",
    "cfare eshte mobile development",
    "puna e mobile developer",
    "çfarë bën një mobile developer",
    "cka ben nje mobile developer",
    "sa veshtire eshte mobile development",
    "me shpjego mobile app development",
    "backend per mobile app cfare eshte"
       ):
       responses = (
        "Mobile App Development është procesi i krijimit të aplikacioneve për Android dhe iOS.",
        "Programuesit mobile përdorin teknologji si Flutter, React Native, Kotlin dhe Swift për të zhvilluar aplikacione.",
        "Mobile development është krijimi i aplikacioneve për telefona.",
        "Do të thotë të programosh aplikacione që punojnë në Android ose iPhone.",
        "Është procesi i ndërtimit të aplikacioneve që përdorim çdo ditë në celular.",
        "Mobile development është zhvillimi i programeve për pajisje mobile.",
        "Është teknologjia që lejon ndërtimin e aplikacioneve mobile.",
        "Quhet zhvillimi i aplikacioneve për celularë dhe tabletë.",
        "Është puna e programimit të aplikacioneve mobile.",
        "Do të thotë të krijosh app-e që instalohen në telefon.",
        "Në mobile development, duhet të mendosh për performancë, për përdoruesit celularë, madhësinë e aplikacionit dhe përdorimin e burimeve."
       )
       print("ChatBoss po shkruan💬...", end="\r")
       time.sleep(1.2)
       typing_animation()
       print("🤖ChatBoss:", random.choice(responses))

# PJESE E RENDESISHME ----- KATEGORIA DHE DB E PUNEVE ----- # PJESE E RENDESISHME (JO TE GJITHA PUNET JANE TE PERFSHIRA)
# PJESE E RENDESISHME ----- INFORMACION I RENDESISHEM ----- TE GJITHA INFORMACIONET JANE TE GJETURA DHE TA MARRA NGA BURIMET NE INTERNET ----- INFORMACION I RENDESISHEM

# Data Basa 4 PJESA E PUNEVE DHE PAGESAVE
# ======================================
#   PYETJE: SA PAGUHET SOFTWARE ENGINEER
# ======================================
    elif msg in ("sa paguhet nje software inxhinier",
                 "sa paguhet nje software engineer",
                 "sa paguhet nje inxhinier softweri",
                 "sa mund te marre nje inxhinier softweri",
                 "sa mund te marre nje software inxhiner",
                 "sa mund te marre nje software engineer",
                 "sa mund te paguhet nje engineer softweri",
                 "sa mund te paguhet nje software inxhinier",
                 "sa mund te paguhet nje software engineer",
                 "sa mund te paguhet nje engineer softweri",
                 "sa mund te paguhet nje engineer software",
                 "sa mund te paguhet nje inxhinier softweri"):
        responses =  (
            "💸 Paga e një software inxhinieri varet nga përvoja dhe vendi ku punon.\n"
            "Në Evropë, një fillestar fiton rreth 1,000–2,000€ në muaj, ndërsa një "
            "profesionist me përvojë mund të arrijë 4,000–6,000€+.",

            "🧑‍💻 Në Shqipëri, një inxhinier softueri fillon zakonisht nga 600€ deri 1,200€"
            "në muaj.\nPor me përvojë dhe aftësi të mira (si AI, Cloud, Cybersecurity), "
            "paga mund të kalojë 2,000€.",

            "🌍 Në kompani ndërkombëtare apo në punë remote, një software engineer mund të fitojë "
            "3,000 deri 8,000€+ në muaj.\nKjo varet shumë nga teknologjitë që përdor dhe "
            "sa ekspert është në to.",

            "📈 Në SHBA, paga mesatare e një software engineer është rreth 110,000$ në vit, "
            "por në kompani si Google, Meta apo Amazon mund të shkojë deri në 200,000$+.",

            "💼 Në përgjithësi, sa më shumë eksperiencë dhe projekte reale të kesh, "
            "aq më shumë rritet vlera jote si inxhinier softueri.\n"
            "Një portfolio e fortë = një pagë më e lartë 💪."
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

# PUNA E DYTE 2
# ==============================================
#   PYETJE: SA PAGUHET CYBER SECURITY SPECIALIST
# ==============================================
    elif msg in (
            "sa paguhet nje cyber security",
            "sa merr nje cyber security specialist",
            "paga e nje ethical hacker",
            "rroga cyber security",
            "sa paguhen penetration testerat",
            "paga pentester",
            "sa fiton nje hacker legal",
            "sa paguhet nje soc analyst",
            "paga cyber security engineer",
            "sa fitojne ata qe punojne me cyber security"
        ):
        responses = (
            "🛡️ Një Cyber Security Specialist paguhet 800€–1500€ si fillim, ndërsa ekspertët shkojnë 2500€–6000€+.",
            "💣 Ethical Hacker-at marrin shumë: 2000€–7000€+ në varësi të nivelit dhe certifikatave (OSCP, CEH).",
            "🔐 Në Europë, pagat e cyber security nisin nga 3,000€ dhe arrijnë 8,000€+ në kompani të mëdha.",
            "⚡ Në Shqipëri një fillestar merr 700€–1,200€, ndërsa seniorët kalojnë lehtësisht 2,000€.",
            "🌍 Remote cyber security jobs paguhen 3,000€–10,000€+/muaj."
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

# PJESA E TRETE 3 
# =================================
# PYETJE: SA PAGUHET DATA SCIENTIST
# =================================
    elif msg in (
                "sa paguhet nje data scientist",            
                "sa fiton nje data scientist",
                "paga data scientist",
                "paga e nje data scientist",
                "rroga e nje data scientist",
                "sa merr nje data scientist",
                "sa mund te marr nje data scientist",
                "data scientist paga",
                "data scientist rroga",
                "paga per data scientist ne shqiperi",
                "sa paguhen data scientistet",
                "data scientist salary",
                "how much does a data scientist make",
                "sa fiton nje data scientist fillestar",
                "sa merr nje data scientist me eksperience",
                "paga mujore data scientist",
                "data scientist paga vjetore",
                "data scientist remote salary",
                "sa paguhet data scientist remote",
                "pagat e data scientist ne europe",
                "pagat e data scientist ne usa",
                "paga per nje data scientist ne gjermani",
                "sa e ka pagen nje data scientist ne itali"
        ):
        responses = (
            "💼 Një Data Scientist fillestar fiton zakonisht 1000–2000€ në Evropë, ndërsa profesionistët shkojnë 4000–7000€+.",
            "📊 Në Shqipëri, një Data Scientist paguhet rreth 700–1500€, por në kompani ndërkombëtare shkon 3000–6000€.",
            "🌍 Remote Data Scientists shpesh marrin 3000–8000€ në muaj, në varësi të eksperiencës dhe tech stack.",
            "🏢 Në SHBA, pagat shkojnë nga 120,000$ në 180,000$ në vit për Data Scientists.",
            "📈 Sa më shumë eksperiencë në Python, ML, statistika e modele predictive, aq më e lartë paga."
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

# PJESA E KATERT 4
# =================================
#   PYETJE: SA PAGUHET DATA ANALYST
# =================================
    elif msg in (
        "sa paguhet nje data analyst", 
        "paga data analyst",
        "paga e nje data analyst",
        "sa merr nje data analyst",
        "rroga e nje data analyst",
        "data analyst rroga",
        "data analyst paga mujore",
        "sa fiton nje data analyst",
        "data analyst salary",
        "how much does a data analyst make",
        "sa paguhet nje data analyst fillestar",
        "data analyst paga shqiperi",
        "sa paguhen data analyst ne europe",
        "paga per data analyst remote",
        "data analyst remote salary",
        "data analyst sa merr",
        "paga e data analyst ne gjermani",
        "paga e data analyst ne itali"
        ):
        responses = (
        "📊 Një Data Analyst fillon zakonisht nga 600–1200€ në Shqipëri.",
        "💼 Në Evropë, pagat variojnë nga 1500–3000€ për fillestar dhe deri në 4000€+ për senior.",
        "🌍 Remote Data Analysts marrin 2000–5000€ në muaj.",
        "📈 Me aftësi në SQL, Excel, Tableau dhe Python paga rritet ndjeshëm.",
        "🏢 Në SHBA, paga mesatare është 60,000–90,000$ në vit."
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

# PJESA E KATERT 4
# ===================================
#   PYETJE: SA PAGUHET CLOUD ENGINEER
# ===================================
    elif msg in (
    "sa paguhet cloud engineer",
    "paga cloud engineer",
    "cloud engineer salary",
    "sa fiton nje cloud engineer",
    "paga cloud computing",
    "cloud architect salary",
    "cloud engineer remote",
    "sa lek merr cloud engineer"
       ):
       responses = (
        "Në Europë, një Cloud Engineer fillestar fiton rreth 1,500€–3,000€. Me eksperiencë shkon 4,000–7,000€+.",
        "Në Shqipëri, një Cloud Engineer fiton 800€–1,500€, por me certifikata AWS/Azure paga rritet shumë.",
        "Në SHBA, pagat për Cloud Engineers variojnë nga 100,000$ deri në 200,000$+ në vit, sidomos në kompani të mëdha si Amazon, Google, Microsoft."
       )
       print("ChatBoss po shkruan💬...", end="\r")
       time.sleep(1.2)
       typing_animation()
       print("🤖ChatBoss:", random.choice(responses))

# PJESA E KATERT 4
# ====================================================
#  KUSHTI NESE USER-I JEP SI INPUT FJALEN FALEMINDERIT
# ==================================================== 
    elif msg in ("faleminderit",
                 "shume faleminderit",
                 "rrofsh",
                 "thx",
                 "flm",
                 "falimners",
                 "thank you",
                 "thanx you",
                 "shum flm",
                 "shum faleminderit",
                 "shummm flm",
                 "shummm faleminderit",
                 "shumme faleminderit"):
        responses = (
            "Asgje te lutem une jam ketu per te te ndihmuar, me thuaj sa here te duash",
            "S`ka perse!",
            "Sa here te duash",
            "Kur te duash",
            "Asgje jam ketu per ty",
            "Sa here te kesh nevoje thjeshte me shkruaj",
            "Kur te duash ti vetem me shkruaj"
        )
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))

    elif msg in ("po dal",
                 "ika tani",
                 "po iki tani",
                 "ciao",
                 "bay"
                 "pacim"
                 "mirupafshim"
                 "ika o lali ciao",
                 "ika tash pra ciao se folim",
                 "ika pra ciao"):
        responses = [
            "Ne rregull pra miruafshim, dhe shihemi me vone",
            "Mirupafshim Erind, tja kalosh mire!",
            "Shihemi ne vone pra, Erind",
            "Ok shihemi me vone",
            "Ne rregull Erind mirupafshim",
            "Ok pra ciao Erind",
            "Ciao",
            "Ne rregull pra pacim"
        ]
        print("ChatBoss po shkruan💬...", end="\r")
        time.sleep(1.2)
        typing_animation()
        print("🤖ChatBoss:", random.choice(responses))
        break    #Ben daljen nga ChatBoss-i

# =======================================
#   NUK U GJET ASNJË PYETJE E PARASHIKUAR
# =======================================
    else:
        print("🤖ChatBoss: Nuk e kuptova saktësisht, mund ta thuash ndryshe? 😊")
