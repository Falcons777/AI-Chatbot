import random
from chat_math_database import solve_math_expression

def get_response(msg):
    msg = msg.lower().strip()

    # 1. Math Logic
    math_result = solve_math_expression(msg)
    if math_result is not None:
        return f"Rezultati eshte {math_result}"

    # 2. Pershendetje
    if msg in ("si je", "hey si je", "si je o lali", "he mo si je", "si je o plak", "si shkon", "si je o zemra", "si je ti"):
        return random.choice([
            "Mire po ti si je?", "Mire jam po ti si ke qene?", 
            "Po mire kam qene ti si ke qene?", "Shume mire jam, ti si je?"
        ])

    if msg in ("ckemi", "hey"):
        return random.choice([
            "ckemi", "ckemi, me cfare mund te te ndihmoj", 
            "pershendetje, si je?", "hey si je?"
        ])

    if msg in ("ca bere", "ca bone", "ca bone o lali", "ca bone m zmr"):
        return random.choice([
            "Hic per zotin, po rrija ketu e po prisja te flisje ti 😄",
            "Po beja ca kodime se s’mund te rri dot pa to 💻",
            "Po rrija e po mendoja ca ide te reja per ChatBoss 🤖"
        ])

    # 3. Informacion Teknologjik
    if msg in ("software engineer", "cfare eshte nje software engineer", "ca eshte inxhinieri i softwerit"):
        return ("👨‍💻 Një inxhinier softueri është personi që projekton, teston dhe përmirëson "
                "aplikacione kompjuterike. Ai zgjidh probleme reale duke përdorur kod.")

    if "cyber security" in msg:
        return "Cyber Security është fusha që merret me mbrojtjen e sistemeve kompjuterike dhe rrjeteve nga sulmet dixhitale. 🛡️"

    if "ai" == msg or "inteligjenca artificiale" in msg:
        return "Inteligjenca Artificiale (AI) është aftësia e kompjuterëve për të kryer detyra që zakonisht kërkojnë inteligjencë njerëzore."

    if "blockchain" in msg:
        return "Blockchain është një teknologji ku të dhënat ruhen në blloqe të lidhura që nuk mund të ndryshohen lehtë."

    # 4. Pagat
    if "sa paguhet" in msg or "paga" in msg:
        if "software engineer" in msg or "inxhinier" in msg:
            return "Në Evropë, një software engineer fiton rreth 2,000€–6,000€+ në muaj në varësi të përvojës."
        if "cyber" in msg:
            return "Një Cyber Security Specialist paguhet 800€–1500€ si fillim, ndërsa ekspertët shkojnë 2500€–6000€+."

    # 5. Mirenjohje
    if msg in ("faleminderit", "shume faleminderit", "rrofsh", "flm", "thank you"):
        return random.choice([
            "Asgje te lutem, jam ketu per te te ndihmuar!", 
            "S'ka perse!", "Sa here te kesh nevoje thjeshte me shkruaj."
        ])

    return "🤖 ChatBoss: Nuk e kuptova saktësisht, mund ta thuash ndryshe? 😊"