class Rhinedottir:
    def __init__(self):
        self.name = "Rhinedottir"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Celestial", "Abyssal", "Hexerei", "Alchemy", "Sinner"
        self.cost = 6
        self.power = 500
        self.hp = 950
        self.passive = "When played, use Transmutation to destroy up to 10 cost characters on the field to play characters up to 10 cost total from the discard pile or hand. Once per turn, give one *Alchemy character immunity to spells"

class Bakunawa:
    def __init__(self):
        self.name = "Bakunawa"
        self.type = "Character"
        self.element = "Cryo"
        self.tag =  "Abyssal", "Alchemy"
        self.cost = 8
        self.power = 500
        self.hp = 500
        self.passive = "When played by Transmutation, Destroy one 6 cost or less characters. While on the field, all 4 or less cost characters have their power reduced to 50"

class Baby_Rifthound:
    def __init__(self):
        self.name = "Baby Rifthound"
        self.type = "Character"
        self.element = "Geo"
        self.tag = "Abyssal", "Alchemy"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played by Transmutation, increase power by 150. When attacking, gets piercing"

class Belyi_Tsar:
    def __init__(self):
        self.name = "Belyi Tsar"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Celestial", "Alchemy", "Fae", "Dragon"
        self.cost = 6
        self.power = 400
        self.hp = 400
        self.passive = "When played by Transmutation, Increase cost by 1 and power by 250. On play, Draw 1 card and freeze an amount of oponent charactes based on the cost of the card drawn for one turn"

class Durin:
    def __init__(self):
        self.name = "Durin"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Abyssal", "Hexerei", "Alchemy", "Dragon", "Feiry Tale"
        self.cost = 6
        self.power = 550
        self.hp = 350
        self.passive = "When played by Transmutation, Delete one 6 or less cost character from the oponent field. At the start of any turn, reduce the first spell cast by 2"

class The_Primordial_Human:
    def __init__(self):
        self.name = "Primordial Human"
        self.type = "Character"
        self.element = "Omni"
        self.tag = "Alchemy"
        self.cost = 10
        self.power = 1000
        self.hp = 1000
        self.passive = "Can only be played by transmutation. On play, disable all spells from the oponent's field. Reduce all *Alchemy cards cost by 6. At the start of the turn, Reduce one oponent character power to 0"

class Primordial_Human_Project:
    def __init__(self):
        self.name = "Primordial Human Project"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Alchemy"
        self.cost = 4
    
        self.passive = "Play one *Alchemy card from the discard pile via Transmutation. Gain one Energy"

class Aksinya:
    def __init__(self):
        self.name = "Aksinya"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Alchemy"
        self.cost = 4
        self.power = 300
        self.hp = 300
        self.passive = "When Played, Draw a Belyi Tsar. When playing a Belyi Tsar, Draw this card from the discard pile, then, use Transmutation"

class The_Shadow_Realm:
    def __init__(self):
        self.name = "The Shadow Realm"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Stellar", "Alchemy"
        self.cost = 2
    
        self.passive = "At the start of every turn, discard one card to draw one"

class Subject_01:
    def __init__(self):
        self.name = "Subject 01"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Alchemy"
        self.cost = 2
        self.power = 200
        self.hp = 300
        self.passive = "When played by Transmutation, draw 1. This card can be played to negate an oponent spell by paying its cost"

class Durin_Remains:
    def __init__(self):
        self.name = "Durin Remains"
        self.type = "Support"
        self.element = "Pyro"
        self.tag = "Abyssal", "Alchemy"
        self.cost = 2
        self.duration = "3 Turns"
        self.passive = "At the start of the turn, destroy one ally character to play one character with its cost reduce by the cost of the destoyed card."

class Alchemy_Bench:
    def __init__(self):
        self.name = "Alchemy Bench"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Alchemy"
        self.cost = 1
        
        self.passive = "Discard 2 cards to: play one spell for free/use Transmutation and draw one "

class Sucrose:
    def __init__(self):
        self.name = "Sucrose"
        self.type = "Character"
        self.element = "Anemo"
        self.tag = "Hexerei", "Alchemy", "Knights of Favonius"
        self.cost = 1
        self.power = 150
        self.hp = 250
        self.passive = "When destroyed, use this card to use Transmutation"

class Timaeus:
    def __init__(self):
        self.name = "Timaeus"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Alchemy"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When destroyed, Draw 1"

class Elemental_Gemstones:
    def __init__(self):
        self.name = "Elemental Gemstones"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Alchemy", "Elemental"
        self.cost = 1
        
        self.passive = "This card can be used for Transmutation. When used, gain one energy of any element"

class Tranmutation_Circle:
    def __init__(self):
        self.name = "Transmutation Circle"
        self.type = "Support"
        self.element = "Geo"
        self.tag = "Alchemy"
        self.cost = 4
        
        self.passive = "use Transmutation to play an character from the discard pile"

class Imortal_Construct:
    def __init__(self):
        self.name = "Imortal Construct"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Alchemy"
        self.cost = 6
        self.power = 500
        self.hp = 300
        self.passive = "When played by Transmutation, use Transmutation to play a card from your hand. When using Transmutation, this card gets an extra attack"

class Chimeric_Armored_Beast:
    def __init__(self):
        self.name = "Chimeric Armored Beast"
        self.type = "Character"
        self.element = "Geo"
        self.tag = "Alchemy"
        self.cost = 2
        self.power = 250
        self.hp = 250
        self.passive = "When played by Transmutation, this card's hp increases by 200. When destroyed, increase one character hp by 200"

class Chimeric_Burrowbeast:
    def __init__(self):
        self.name = "Timaeus"
        self.type = "Character"
        self.element = "Electro"
        self.tag = "Alchemy"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When destroyed by Transmutation, play this card from the discard pile."

class Banndersnatch:
    def __init__(self):
        self.name = "Bundersnatch"
        self.type = "Character"
        self.element = "Electro"
        self.tag = "Alchemy"
        self.cost = 2
        self.power = 300
        self.hp = 200
        self.passive = "When played by Transmutation, this card gets piercing. When destroyed, gain one energy of any element"

class Crystalflies:
    def __init__(self):
        self.name = "Crystalflies"
        self.type = "Character"
        self.element = "Omni"
        self.tag = "Alchemy", "WildLife", "Elemental"
        self.cost = 1
        self.power = 100
        self.hp = 100
        self.passive = "When destroyed, gain one energy"

class Chimeric_Horned_Bear:
    def __init__(self):
        self.name = "Chimeric Horned Bear"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Alchemy"
        self.cost = 4
        self.power = 200
        self.hp = 400
        self.passive = "When played by Transmutation, increase this card power by 300. When destroyed, destroy an 2 cost or less character from the opponent field"

class Venessa:
    def __init__(self):
        self.name = "Venessa"
        self.type = "Character"
        self.element = "Anemo"
        self.tag = "Knights of Favonius", "Four Winds", "Heroes"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Dvalin:
    def __init__(self):
        self.name = "Dvalin"
        self.type = "Character"
        self.element = "Anemo"
        self.tag = "Four Winds", "Hexerei", "Dragon"
        self.cost = 6
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Corrupted_Tears:
    def __init__(self):
        self.name = "Corrupted tears"
        self.type = "Support"
        self.element = "Anemo"
        self.tag = "Abyssal", "Four Winds", "Dragon", "Hexerei"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Pale_furred_Wolf:
    def __init__(self):
        self.name = "Pale-furred Wolf"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Wolvendom", "WildLife"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Razor:
    def __init__(self):
        self.name = "Razor"
        self.type = "Character"
        self.element = "electro"
        self.tag = "Wolvendom", "Hexerei", "WildLife"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Alpha_Wolf:
    def __init__(self):
        self.name = "Alpha Wolf"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Wolvendom", "WildLife"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Wolfs_Gravestone:
    def __init__(self):
        self.name = "Wolf's Gravestone"
        self.type = "Weapon"
        self.element = "Anemo"
        self.tag = "Wolvendom", "Four Winds"
        self.cost = 6
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Jean:
    def __init__(self):
        self.name = "Jean"
        self.type = "Character"
        self.element = "Anemo"
        self.tag = "Knights of Favonius", "Four Winds"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Lisa:
    def __init__(self):
        self.name = "Lisa"
        self.type = "Character"
        self.element = "eLECTRO"
        self.tag = "Knights of Favonius", "Hexerei"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Kaeya:
    def __init__(self):
        self.name = "Kaeya"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Knights of Favonius"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Amber:
    def __init__(self):
        self.name = "Amber"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Knights of Favonius"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Hertha:
    def __init__(self):
        self.name = "Hertha"
        self.type = "Character"
        self.element = "Anemo"
        self.tag = "Knights of Favonius"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Mika:
    def __init__(self):
        self.name = "Mika"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Knights of Favonius", "Expeditioner"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Il_Dottore_Omega_Builda:
    def __init__(self):
        self.name = "Il Dottore Omega Build Segment"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Fatui", "Automaton", "Moonsign"
        self.cost = 8
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Zandik:
    def __init__(self):
        self.name = "Zandik"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Fatui", "Automaton", "Moonsign"

        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Il_Dottore_27:
    def __init__(self):
        self.name = "Il Dottore Segment 27"
        self.type = "Character"
        self.element = "Anemo"
        self.tag = "Fatui", "Automaton", "Moonsign"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Diluc:
    def __init__(self):
        self.name = "Diluc"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Agent", "Knights of Favonius"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Crepus:
    def __init__(self):
        self.name = "Crepus"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Agent"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Forbidden_Knowladge_Capsule:
    def __init__(self):
        self.name = "Forbidden Knowladge Capsule"
        self.type = "Support"
        self.element = "Dendro"
        self.tag = "Akademiya", "Seven Pillars", "Abyssal"
        self.cost = 6
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Apep:
    def __init__(self):
        self.name = "Apep"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Dragon", "Sovereign", "Seven Pillars"
        self.cost = 8
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Guardian_of_the_Oasis:
    def __init__(self):
        self.name = "Guardian of the Oasis"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Dragon", "Seven Pillars"
        self.cost = 6
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Faruzan:
    def __init__(self):
        self.name = "Faruzan"
        self.type = "Character"
        self.element = "Anemo"
        self.tag = "Akademiya", "Automaton", "Seven Pillars"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Eleazar:
    def __init__(self):
        self.name = "Eleazar"
        self.type = "Support"
        self.element = "Dendro"
        self.tag = "Abyssal", "Seven Pillars"
        self.cost = 4
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Irminsul:
    def __init__(self):
        self.name = "Irminsul"
        self.type = "Support"
        self.element = "Dendro"
        self.tag = "Elemental", "Akademiya", "Celestial"
        self.cost = 8
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Corrupted_Data:
    def __init__(self):
        self.name = "Corrupted Data"
        self.type = "Support"
        self.element = "Dendro"
        self.tag = "Automaton", "Seven Pillars"
        self.cost = 2
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Crimmson_Moon_Marrow:
    def __init__(self):
        self.name = "Crimson Moon Marrow"
        self.type = "Weapon"
        self.element = "Pyro"
        self.tag = "Moonsign", "Frostmoon", "Abyssal", "Crimson Moon Dynasty"
        self.cost = 4
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Eternal_Moon_Marrow:
    def __init__(self):
        self.name = "Eternal Moon Marrow"
        self.type = "Weapon"
        self.element = "Dendro"
        self.tag = "Moonsign", "Frostmoon"
        self.cost = 6
       
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Artificial_Moon_Marrow:
    def __init__(self):
        self.name = "Artificial Moon Marrow"
        self.type = "Weapon"
        self.element = "Anemo"
        self.tag = "Moonsign", "Automaton"
        self.cost = 8
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Dark_Side_of_the_Moon:
    def __init__(self):
        self.name = "Dark Side of the Moon"
        self.type = "Support"
        self.element = "Hydro"
        self.tag = "Dragon", "Frostmoon", "Moonsign"
        self.cost = 6
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Kuuhenki:
    def __init__(self):
        self.name = "Kuuhenki"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Moonsign", "Frostmoon"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Luonnotar:
    def __init__(self):
        self.name = "Luonnotar"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Moonsign", "Frostmoon"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Trilunar_Authority:
    def __init__(self):
        self.name = "Trilunar Authority"
        self.type = "Support"
        self.element = "Omini"
        self.tag = "Moonsign", "Frostmoon"
        self.cost = 8
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Krupp:
    def __init__(self):
        self.name = "Krupp"
        self.type = "Character"
        self.element = "Anemo"
        self.tag = "Fatui", "Authomaton", "Moonsign"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Primal_Construct_Reshaper:
    def __init__(self):
        self.name = "Primal Construct: Reshaper"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Authomaton", "Seven Pillars"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Replicators_Keysttone:
    def __init__(self):
        self.name = "Replicator's Keystone"
        self.type = "Support"
        self.element = "Dendro"
        self.tag = "Authomaton", "Seven Pillars"
        self.cost = 1
       
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Moon_Fragments:
    def __init__(self):
        self.name = "Moon Fragments"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Moonsign", "Frostmoon"
        self.cost = 2
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Forged_Primal_Lights:
    def __init__(self):
        self.name = "Forged Primal Lights"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Authomathon", "Seven Pillars"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Ashru:
    def __init__(self):
        self.name = "Ashru"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Agent" "Seven Pillars", "Moonsign"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Chessboard_of_Secrets:
    def __init__(self):
        self.name = "Chessboard of Secrets"
        self.type = "Support"
        self.element = "Dendro"
        self.tag = "Agent", "Moonsign", "Seven Pillars"
        self.cost = 6
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Bennu:
    def __init__(self):
        self.name = "Bennu"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Authomaton", "Seven Pillars"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Tenoch:
    def __init__(self):
        self.name = "Tenoch"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Heroes"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Enjou:
    def __init__(self):
        self.name = "Enjou"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Abyssal", "Heroes"
        self.cost = 6
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Mare_Jivari:
    def __init__(self):
        self.name = "Meré Jivari"
        self.type = "Support"
        self.element = "Pyro"
        self.tag = "Heroes", "Abyssal"
        self.cost = 2
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Alhaitham:
    def __init__(self):
        self.name = "Alhaitham"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Akademiya", "Seven Pillars"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Ninianne_of_the_Lake:
    def __init__(self):
        self.name = "Ninianne of the Lake"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Oceanid", "Elemntal"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Idiya:
    def __init__(self):
        self.name = "Idiya"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Oceanid", "Hexerei", "Elemental"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Sanhaj:
    def __init__(self):
        self.name = "Sanhaj"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Masters of the Night Wind", "Heroes"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Rilai:
    def __init__(self):
        self.name = "Rilai"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Masters of the Night Wind", "Heroes"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Papar:
    def __init__(self):
        self.name = "Papar"
        self.type = "Character"
        self.element = "Electro"
        self.tag = "Heroes"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Endora:
    def __init__(self):
        self.name = "endora"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Oceanid", "Elemental"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Sigewinne:
    def __init__(self):
        self.name = "Sigewinne"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Melusine", "Warden", "Alchemy"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Hydro_Mimic_Boar:
    def __init__(self):
        self.name = "Hydro Mimic Boar"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Oceanid", "Elemental"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Hydro_Mimic_Crab:
    def __init__(self):
        self.name = "Hydro Mimic Crab"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Oceanid", "Elemental"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Water_From_the_Primordial_Sea:
    def __init__(self):
        self.name = "Water From the Primordial Sea"
        self.type = "Support"
        self.element = "Hydro"
        self.tag = "Oceanid", "Elemental"
        self.cost = 2
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class All_Devouring_Narwhal:
    def __init__(self):
        self.name = "All Devouring Narwhal"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Abyssal", "Elemental"
        self.cost = 8
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Skirk:
    def __init__(self):
        self.name = "Skirk"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Abyssal"
        self.cost = 8
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Tartaglia:
    def __init__(self):
        self.name = "Tartaglia"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Fatui", "Abyssal"
        self.cost = 6
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Surtalogi:
    def __init__(self):
        self.name = "Surtalogi"
        self.type = "Character"
        self.element = "Electro"
        self.tag = "Abyssal", "Sinner"
        self.cost = 6
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Oratrice:
    def __init__(self):
        self.name = "OPratrice Mecanique d'Analyse Cardinale"
        self.type = "Support"
        self.element = "Hydro"
        self.tag = "Court of Fontaine", "Celestial"
        self.cost = 4
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Folcalors:
    def __init__(self):
        self.name = "Folcalors"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Oceanid", "Celestial", "Court of Fontaine"
        self.cost = 8
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Sinners_Finale:
    def __init__(self):
        self.name = "Sinner's FFinale"
        self.type = "Support"
        self.element = "Hydro"
        self.tag = "Court of Fontaine"
        self.cost = 6
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Neuvillette:
    def __init__(self):
        self.name = "Neuvillette"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Dragon", "Court of Fontaine", "Melusine"
        self.cost = 6
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Sedene:
    def __init__(self):
        self.name = "Sedene"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Melusine", "Court of Fontaine", "Alchemy"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Blathine:
    def __init__(self):
        self.name = "Blathine"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Melusine", "Court of Fontaine", "Alchemy"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Memere:
    def __init__(self):
        self.name = "Memere"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Melusine", "Narzissenkreuz", "Alchemy"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Seymour:
    def __init__(self):
        self.name = "Seymour"
        self.type = "Character"
        self.element = "Electro"
        self.tag = "Authomaton", "Narzissenkreuz", "Court of Fontaine"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class HunterSeeker:
    def __init__(self):
        self.name = "Hunter-Seeker"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Dragon", "Authomaton"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Overseer_Device:
    def __init__(self):
        self.name = "Overseer Device"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Dragon", "Authomaton"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class PSSMON:
    def __init__(self):
        self.name = "P.S.S.M.O.N"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Dragon", "Moonsign", "Frostmoon", "Authomaton"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Throne_of_the_Primal_Fire:
    def __init__(self):
        self.name = "Throne of the Primal Fire"
        self.type = "Support"
        self.element = "Hydro"
        self.tag = "Heroes", "Masters of the Night Wind"
        self.cost = 4
       
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class NinNin:
    def __init__(self):
        self.name = "NinNin"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Moonsign", "Frostmoon", "Dragon"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Kukulkan:
    def __init__(self):
        self.name = "Kukulkan"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Dragon"
        self.cost = 6
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Holawaqa_Ngoubou:
    def __init__(self):
        self.name = "Holawaqa Ngoubou"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Dragon", "Flowerfaether Clan"
        self.cost = 6
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Kinich:
    def __init__(self):
        self.name = "Kinich"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Heroes", "Dragon", "Scions of the Canopy"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Ajaw:
    def __init__(self):
        self.name = "Ajaw"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Dragon", "Authomaton", "Heroes", "Scions of the Canopý"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Huitzilopochtli:
    def __init__(self):
        self.name = "Huitzilopochtli"
        self.type = "Support"
        self.element = "Pyro"
        self.tag = "Dragon"
        self.cost = 15
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Moonheart_Gap:
    def __init__(self):
        self.name = "Moonheart Gap"
        self.type = "Support"
        self.element = "Hydro"
        self.tag = "Moonsign", "Frostmoon"
        self.cost = 4
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Baby_Geo_Vishap:
    def __init__(self):
        self.name = "Baby Geo Vishap"
        self.type = "Character"
        self.element = "Geo"
        self.tag = "Dragon"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Primordial_Geo_Vishap:
    def __init__(self):
        self.name = "Primordial Geo Vishap"
        self.type = "Character"
        self.element = "Geo"
        self.tag = "Dragon"
        self.cost = 6
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Azdaha:
    def __init__(self):
        self.name = "Azdaha"
        self.type = "Character"
        self.element = "Geo"
        self.tag = "Dragon"
        self.cost = 8
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Silver_White_Tree:
    def __init__(self):
        self.name = "Silver White Tree"
        self.type = "Support"
        self.element = "Dendro"
        self.tag = "Elemental", "Celestial"
        self.cost = 4
       
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Four_Winds_Temple:
    def __init__(self):
        self.name = "Four Winds' Temple"
        self.type = "Support"
        self.element = "Anemo"
        self.tag = "Four Winds"
        self.cost = 2
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Stormterrors_LAir:
    def __init__(self):
        self.name = "Stormterror's Lair"
        self.type = "Support"
        self.element = "Anemo"
        self.tag = "Dragon", "Four Winds"
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Baby_Qucusaurus:
    def __init__(self):
        self.name = "Baby Qucusaurus"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Dragon", "Flowerfaether Clan"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Hydro_Slime:
    def __init__(self):
        self.name = "Hydro Slime"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Elemental"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Eye_of_the_Storm:
    def __init__(self):
        self.name = "Eye of the Storm"
        self.type = "Character"
        self.element = "Anemo"
        self.tag = "Elemental"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Ruin_Hunter:
    def __init__(self):
        self.name = "Ruin Hunter"
        self.type = "Character"
        self.element = "Omni"
        self.tag = "Abyssal", "Authomaton"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Pyro_Frostnight_Scion:
    def __init__(self):
        self.name = "P`yro Frostnight Scion"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Monsign", "WildLif"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Vilemina:
    def __init__(self):
        self.name = "Vilemina"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Fatui", "Frostmoon", "Moonsign", "WildLife"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Electro_Lawachurl:
    def __init__(self):
        self.name = "Electro Lawachurl"
        self.type = "Character"
        self.element = "Electro"
        self.tag = "Hilichurl"
        self.cost = 8
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Hydro_Hilichurl_Rogue:
    def __init__(self):
        self.name = "Hydro Hilichurl Rogue"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Hilichurl"
        self.cost = 6
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Fisher_of_the_Hidden_Depths:
    def __init__(self):
        self.name = "Fisher of the Hidden Depths"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Abyssal", "Wild Hunt", "Moonsign"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Scout_Landcruiser:
    def __init__(self):
        self.name = "Scout LAndcruiser"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Fatui", "Authomaton"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Oprichnik_Cannoneer:
    def __init__(self):
        self.name = "Oprichnik Cannoneer"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Fatui"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Knuckle_Duckle:
    def __init__(self):
        self.name = "Knuckle Duckle"
        self.type = "Character"
        self.element = "Electro"
        self.tag = "Authomaton", "Moonsign"
        self.cost = 6
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Radiant_Lunapod:
    def __init__(self):
        self.name = "Radiant Lunapod"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Frostmoon", "Moonsign", "WildLife"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Foul_Legacy:
    def __init__(self):
        self.name = "Foul Legacy"
        self.type = "Support"
        self.element = "Electro"
        self.tag = "Abyssal"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Flying_Serpent:
    def __init__(self):
        self.name = "Flying Serpernt"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Seven Pillars", "WildLife"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Khuuvaki:
    def __init__(self):
        self.name = "Khuuvaki"
        self.type = "Support"
        self.element = "Hydro"
        self.tag = "Frostmoon", "Moonsign"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Alchemical_Granade:
    def __init__(self):
        self.name = "Alchemical Granade"
        self.type = "Support"
        self.element = "Hydro"
        self.tag = "Treasure Hoarders", "Alchemy"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Gravedigger:
    def __init__(self):
        self.name = "Gravedigger"
        self.type = "Character"
        self.element = "Geo"
        self.tag = "Treasure Hoarder"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Coppelius_and_Coppelia:
    def __init__(self):
        self.name = "Coppelia and Colppelius"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Court of Fontaine", "Authomaton"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Viliana:
    def __init__(self):
        self.name = "Viliana"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Fae"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Mr_Nine:
    def __init__(self):
        self.name = "Mr. Nine"
        self.type = "Character"
        self.element = "Anemo"
        self.tag = "Hexerei", "Celestial"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Millelith:
    def __init__(self):
        self.name = "Millelith"
        self.type = "Character"
        self.element = "geo"
        self.tag = "Liyue Qixing"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Golden_House:
    def __init__(self):
        self.name = "Golden House"
        self.type = "Support"
        self.element = "geo"
        self.tag = "Liyue Qixing"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Rifthound:
    def __init__(self):
        self.name = "Rifthound"
        self.type = "Character"
        self.element = "Geo"
        self.tag = "Alchemy", "Abyssal"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Mooncarver:
    def __init__(self):
        self.name = "Mooncarver"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Adepti", "WildLife"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Elynas_Spirit:
    def __init__(self):
        self.name = "Elynas Spirit"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Melusine", "Abyssal", "Alchemy"
        self.cost = 6
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Dendro_Slime:
    def __init__(self):
        self.name = "Dendro Slime"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Elemental"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Large_Dendro_Slime:
    def __init__(self):
        self.name = "Large Dendro Slime"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Elemental"
        self.cost = 2
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Thundering_Manifestation:
    def __init__(self):
        self.name = "Thundering Manifestation"
        self.type = "Character"
        self.element = "Electro"
        self.tag = "Elemental", "Youkai"
        self.cost = 4
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Kapatcir:
    def __init__(self):
        self.name = "Kapatcir"
        self.type = "Character"
        self.element = "Electro"
        self.tag = "Celestial", "Youkai"
        self.cost = 6
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Boatman:
    def __init__(self):
        self.name = "Boatman"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Frostmoon", "Moonsign"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Moon_Chariot:
    def __init__(self):
        self.name = "Moon Chariot"
        self.type = "Support"
        self.element = "Hydro"
        self.tag =  "Frostmoon", "Moonsign"
        self.cost = 2
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Sabzerus_Festival:
    def __init__(self):
        self.name = "Sabzerus Festival"
        self.type = "Support"
        self.element = "Dendro"
        self.tag = "Akademiya"
        self.cost = 4
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

class Knight_of_Flowers:
    def __init__(self):
        self.name = "Knight of Flowers"
        self.type = "Character"
        self.element = "Dendro"
        self.tag = "Akademiya"
        self.cost = 2
        self.power = 200
        self.hp = 200
        
        self.passive = "When played, Destroy a total of 10 cost from your field or hand to play units up to 10 cost from hand, deck or discard pile."

set2 = [Rhinedottir, Bakunawa, Baby_Rifthound, Belyi_Tsar, Durin, The_Primordial_Human,Aksinya,The_Shadow_Realm, Subject_01, Durin_Remains, Sucrose, Alchemy_Bench, Timaeus, Elemental_Gemstones, Tranmutation_Circle, Imortal_Construct, Chimeric_Armored_Beast, Chimeric_Burrowbeast, Chimeric_Horned_Bear, Banndersnatch, Crystalflies, Venessa, Dvalin, Corrupted_Tears, Pale_furred_Wolf, Razor, Alpha_Wolf, Wolfs_Gravestone, Jean, Lisa, Kaeya, Amber, Hertha, Mika, Il_Dottore_Omega_Builda, Apep,  Guardian_of_the_Oasis, Zandik, Il_Dottore_27, Diluc, Crepus, Forbidden_Knowladge_Capsule, Faruzan, Eleazar, Irminsul, Corrupted_Data, Crimmson_Moon_Marrow, Eternal_Moon_Marrow, Artificial_Moon_Marrow, Dark_Side_of_the_Moon, Kuuhenki, Luonnotar, Trilunar_Authority, Krupp, Primal_Construct_Reshaper, Replicators_Keysttone, Moon_Fragments, Forged_Primal_Lights, Ashru, Chessboard_of_Secrets, Bennu, Tenoch, Enjou, Mare_Jivari, Alhaitham, Ninianne_of_the_Lake, Idiya, Sanhaj, Rilai, Papar, Endora, Sigewinne, Hydro_Mimic_Boar, Hydro_Mimic_Crab, Water_From_the_Primordial_Sea, All_Devouring_Narwhal, Skirk, Tartaglia, Surtalogi, Oratrice, Folcalors, Sinners_Finale, Neuvillette, Sedene, Blathine, Memere, Seymour, HunterSeeker, Overseer_Device, PSSMON, Throne_of_the_Primal_Fire, NinNin, Kukulkan, Holawaqa_Ngoubou, Kinich, Ajaw, Huitzilopochtli, Moonheart_Gap, Baby_Geo_Vishap, Primordial_Geo_Vishap, Azdaha, Silver_White_Tree, Four_Winds_Temple, Stormterrors_LAir, Baby_Qucusaurus, Hydro_Slime, Eye_of_the_Storm, Ruin_Hunter, Pyro_Frostnight_Scion, Vilemina, Electro_Lawachurl, Hydro_Hilichurl_Rogue, Fisher_of_the_Hidden_Depths, Scout_Landcruiser, Oprichnik_Cannoneer, Knuckle_Duckle, Radiant_Lunapod, Foul_Legacy, Flying_Serpent, Khuuvaki, Alchemical_Granade, Gravedigger, Coppelius_and_Coppelia, Viliana, Mr_Nine, Millelith, Golden_House, Rifthound, Mooncarver, Elynas_Spirit, Dendro_Slime, Large_Dendro_Slime, Thundering_Manifestation, Kapatcir, Moon_Chariot, Sabzerus_Festival, Knight_of_Flowers]