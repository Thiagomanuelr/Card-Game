
# Celestial Deck

class Aether:
    def __init__(self):
        self.name = "Aether"
        self.type = "Character"
        self.element = "Omni"
        self.tag = "Celestial"
        self.cost = 4
        self.power = 300
        self.hp = 400
        self.r = "C"
        self.passive = "Omni Strike: Aether can change elements by copying an ally element once they are played. When a *Celestial card is played, Aether gains +100 power for 1 combat."

class Pyro_Seelie_Guide:
    def __init__(self):
        self.name = "Pyro Seelie Guide"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Celestial"
        self.cost = 1
        self.power = 100
        self.hp = 200
        self.r = "C"
        self.passive = "reveal the next three cards in your deck, choose one pyro card to add to your hand, and add the other two to your deck bottom."

class Paimon:
    def __init__(self):
        self.name = "Paimon"
        self.type = "Character"
        self.element = "Omni"
        self.tag = "Celestial"
        self.cost = 1
        self.power = 50
        self.hp = 100
        self.r = "C"
        self.passive = "Draw 1  at the start of combat"

class Hexaiphanes_Blade:
    def __init__(self):
        self.name = "Hexaiphanes Blade"
        self.type = "Weapon"
        self.element = "Omni"
        self.tag = "Celestial"
        self.cost = 6
        self.r = "SR"
        
        self.passive = "When equipped, increase the power of your character by 50 and grant them an additional attack per turn."

class Statue_of_the_Seven:
    def __init__(self):
        self.name = "Statue of the Seven"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Celestial"
        self.cost = 4
        self.duration = "combat"
        self.r = "C"
        
        self.passive = "At the start of combat, heal your character HP increase by 200."

class Nihilita:
    def __init__(self):
        self.name = "Nihilita"
        self.type = "Character"
        self.element = "Geo"
        self.tag = "Celestial"
        self.cost = 6
        self.power = 550
        self.hp = 350
        self.r = "SR"
        self.passive = "Disable one of the enemy's spells per combat"

class Domain_Keeper:
    def __init__(self):
        self.name = "Domain Keeper"
        self.type = "Character"
        self.element = "Geo"
        self.tag = "Celestial"
        self.cost = 2
        self.power = 100
        self.hp = 450
        self.r = "R"
        self.passive = "When Domain Keeper is in play, all Geo cards in your hand cost 1 less cost to play."

class Celestial_Nail:
    def __init__(self):
        self.name = "Celestial Nail"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Celestial"
        self.cost = 8
        self.duration = "Cast"
        self.r = "R"
        self.passive = "When activated, clear all enemy spells from the field and deal 200 damage to all enemy characters."

class Celestia:
    def __init__(self):
            self.name = "Celestia"
            self.type = "Support"
            self.element = "Omni"
            self.tag = "Celestial"
            self.cost = 8
            self.duration = "combat"
            self.r = "R"
            self.passive = "While in combat, all *Celestial cards +200atq +100hp, +1 cost per turn"

class Celestial_Envoy:
    def __init__(self):
        self.name = "Celestial Envoy"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Celestial"
        self.cost = 1
        self.power = 150
        self.hp = 300
        self.r = "C"
        self.passive = "When Celestial Envoy is in the field, when a card in your field is destroyed, destroy Celestial Envoy instead."

class Fake_Sky:
    def __init__(self):
        self.name = "Fake Sky"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Celestial"
        self.cost = 4
        self.duration = "3 turns"
        
        self.passive = "-1 cost per turn for the enemy player for 3 turns."

class Purification:
    def __init__(self):
        self.name = "Purification"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Celestial"
        self.cost = 2
        self.duration = "Cast"
        
        self.passive = "disable an enemy spell"

class Spaceship:
    def __init__(self):
        self.name = "Spaceship"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Celestial"
        self.cost = 6
        self.duration = "Cast"
        
        self.passive = "When activated, discard all cards in your hand and draw 5 new cards. Destroy this card after use."

class Elemental_Conversion:
    def __init__(self):
        self.name = "Elemental Conversion"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Celestial", "Abyssal"
        self.cost = 2
        self.duration = "Cast"
        
        self.passive = "When activated, change the element of one of your cost cards to any element in the deck."

class Leylines:
    def __init__(self):
        self.name = "Leylines"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Celestial", "Elemental"
        self.cost = 2
        self.duration = "combat"
        
        self.passive = "Discard one, +1 cost"

class Istoria:
    def __init__(self):
        self.name = "Istoria"
        self.type = "Character"
        self.element = "Geo"
        self.tag = "Celestial"
        self.cost = 1
        self.power = 100
        self.hp = 200
        self.passive = "While in combat, all *Celestial cards in your hand cost 1 less cost to play, the effect doesn't stack. When Istoria is destroyed, draw 1 card."

class Ursa_the_Drake:
    def __init__(self):
        self.name = "Ursa, the Drake"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Celestial", "Dragon"
        self.cost = 4
        self.power = 600
        self.hp = 300
        self.passive = "Discard one card from your hand to destroy an enemy character with 400 or less HP. This effect can only be used once per combat."



cartas = [Aether, Pyro_Seelie_Guide, Paimon, Hexaiphanes_Blade, Statue_of_the_Seven, Nihilita, Domain_Keeper, 
          Celestial_Nail, Celestia, Celestial_Envoy, Fake_Sky, Purification, Spaceship, Elemental_Conversion, Leylines, Istoria, Ursa_the_Drake]

# Fae Deck

class Anastasia:
    def __init__(self):
        self.name = "Anastasia"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Fae", "Fatui", "Stellar"
        self.cost = 8
        self.power = 700
        self.hp = 500
        self.passive = "When Anastasia is in play, all Cryo cards in your hand cost 1 less cost to play. Binds 2 enemy characters for 2 turn."


class Jack_Frost:
    def __init__(self):
        self.name = "Jack Frost"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Fae"
        self.cost = 1
        self.power = 100
        self.hp = 300
        self.passive = "When played, search for a *Fae card in your deck."

class Jack_Frost_Chief:
    def __init__(self):
        self.name = "Jack Frost Chief"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Fae"
        self.cost = 2
        self.power = 200
        self.hp = 350
        self.passive = "While in combat, all *Cryo cards hp increase by 100."

class Snegovik_Guard:
    def __init__(self):
        self.name = "Snegovik Guard"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Fae"
        self.cost = 4
        self.power = 400
        self.hp = 400
        self.passive = "When Snegovik Guard is in play, when a *Fae card is destroyed, draw 1 card."

class Snegurochka_Cryomancer:
    def __init__(self):
        self.name = "Snegurochka Cryomancer"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Fae"
        self.cost = 2
        self.power = 400
        self.hp = 200
        self.passive = "Cryo Support cards cost 1 less cost to play."

class Pavlina:
    def __init__(self):
        self.name = "Pavlina"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Fae"
        self.cost = 6
        self.power = 550
        self.hp = 400
        self.passive = "Start of the combat: increase all cryo *Fae cards power by 150. When destroyed, bind 1 enemy character for 2 turns."

class Snow_Giant:
    def __init__(self):
        self.name = "Snow Giant"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Fae"
        self.cost = 6
        self.power = 350
        self.hp = 600
        self.passive = "Enemies can olny atack Snow Giant, if they have 2 or more characters in play. When destroyed, draw 1 card."

class Vesna:
    def __init__(self):
        self.name = "Vesna"
        self.type = "Character"
        self.element = "Anemo"
        self.tag = "Fae", "Stellar"
        self.cost = 4
        self.power = 450
        self.hp = 350
        self.passive = "Can attack twice per turn. When Swirl or StellarSwirl are played, draw 1 card."

class Rogue_Vila:
    def __init__(self):
        self.name = "Rogue Vila"
        self.type = "Character"
        self.element = "Anemo"
        self.tag = "Fae"
        self.cost = 2
        self.power = 300
        self.hp = 250
        self.passive = "Piercing"

class Royal_Guard_Druzhna:
    def __init__(self):
        self.name = "Royal Guard Druzhna"
        self.type = "Character"
        self.element = "Anemo"
        self.tag = "Fae"
        self.cost = 1
        self.power = 200
        self.hp = 200
        self.passive = "When played, search for a *Fae card in your deck."

class Belyi_Tsars_Wish:
    def __init__(self):
        self.name = "Belyi Tsar's Wish"
        self.type = "Support"
        self.element = "Cryo"
        self.tag = "Fae"
        self.cost = 6
        self.duration = "Combat"
        
        self.passive = "When activated, discard a *Fae card from your hand to draw Anastasya from your deck."

class Kresnik_Torch:
    def __init__(self):
        self.name = "Kresnik Torch"
        self.type = "Support"
        self.element = "Cryo"
        self.tag = "Fatui"
        self.cost = 4
        self.duration = "Cast"
        
        self.passive = "give one extra cost per turn."

class Eye_of_Graeae:
    def __init__(self):
        self.name = "Eye of Graeae"
        self.type = "Support"
        self.element = "Cryo"
        self.tag = "Fae", "Stellar"
        self.cost = 1
        self.duration = "Cast"
        
        self.passive = "When activated, gives one character card *piercing."

class Imperial_March:
    def __init__(self):
        self.name = "Imperial March"
        self.type = "Support"
        self.element = "Anemo"
        self.tag = "Fae", "Fatui"
        self.cost = 2
        self.duration = "3 turns"
        
        self.passive = "Play an anemo *Fae card from your deck. That card receives +100 power and +100 hp for 3 turns."

class Mistilteinn:
    def __init__(self):
        self.name = "Mistilteinn"
        self.type = "Support"
        self.element = "Cryo"
        self.tag = "Fatui", "Stellar"
        self.cost = 15
        self.duration = "Combat"
        
        self.passive = "When equipped, Destroy all enemy characters with 400 or less HP. Than, increase the power and hp of the equiped character by 100 for each destroyed enemy."

class FrostBite:
    def __init__(self):
        self.name = "FrostBite"
        self.type = "Support"
        self.element = "Cryo"
        self.tag = "Fae"
        self.cost = 6
        self.duration = "Combat"
        
        self.passive = "When played: stun an enemy character for 1 turn. For the rest of the combat, stunned and binded characters receive -200 hp."





# Abyss Deck

class Lumine:
    def __init__(self):
        self.name = "Lumine"
        self.type = "Character"
        self.element = "Omni"
        self.tag = "Abyssal"
        self.cost = 4
        self.power = 400
        self.hp = 300
        self.passive = "Abyssal Strike: Lumine can change elements by equipping specific elemental cost cards, for each card that goes to the disdcard pile, Lumine gains 100 power for 1  turn."

class Cryo_Abyss_Mage:
    def __init__(self):
        self.name = "Cryo Abyss Mage"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Abyssal"
        self.cost = 1
        self.power = 200
        self.hp = 150
        self.passive = "When played, search for a *Abyssal card in your deck. Than shuffle your deck."

class Hydro_Abyss_Mage:
    def __init__(self):
        self.name = "Hydro Abyss Mage"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Abyssal"
        self.cost = 1
        self.power = 100
        self.hp = 300
        self.passive = "when destroyed or discarded, bind an enemy character for 1 turn."

class Caribert:
    def __init__(self):
        self.name = "Caribert"
        self.type = "Character"
        self.element = "Omni"
        self.tag = "Abyssal", "Hilichurl"
        self.cost = 2
        self.power = 400
        self.hp = 100
        self.passive = "When played, play a *Abyssal card from your deck."

class Chlothar:
    def __init__(self):
        self.name = "Chlothar"
        self.type = "Character"
        self.element = "Omni"
        self.tag = "Abyssal", "Khaenri'ah"
        self.cost = 1
        self.power = 100
        self.hp = 200
        self.passive = "When destroyed or discarded, draw 1 card. If Chlothar is played from the discard pile, play an Abyss Herald from the deck. Than shuffle your deck."

class Cryo_Abyss_Herald:
    def __init__(self):
        self.name = "Cryo Abyss Herald"
        self.type = "Character"
        self.element = "Cryo"
        self.tag = "Abyssal"
        self.cost = 6
        self.power = 550
        self.hp = 400
        self.passive = "When played, discard a card from your hand to get piercing."

class Hydro_Abyss_Herald:
    def __init__(self):
        self.name = "Hydro Abyss Herald"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Abyssal"
        self.cost = 6
        self.power = 400
        self.hp = 550
        self.passive = "When played, discard a card from your hand to bind an enemy character for 1 turn."

class Transcending_Fate:
    def __init__(self):
        self.name = "Transcending Fate"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Abyssal"
        self.cost = 4
        self.duration = "Combat"
        
        self.passive = "When activated, discard a card from your hand to play a *Abyssal card from your discard pile."

class Loom_of_Fate:
    def __init__(self):
        self.name = "Loom of Fate"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Abyssal"
        self.cost = 6
        self.duration = "once"
        
        self.passive = "Play a *Abyssal card from your discard pile. Than, discard a card from your hand to play a *Abyssal card from your deck."

class Tenebrous_Mimiflora:
    def __init__(self):
        self.name = "Tenebrous Mimiflora"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Abyssal"
        self.cost = 2
        self.power = 300
        self.hp = 300
        self.passive = "When played, destroy this card to play a *Abyssal card from your discard pile or hand."

class Abyssal_Rift:
    def __init__(self):
        self.name = "Abyssal Rift"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Abyssal"
        self.cost = 4
        self.duration = "once"
        
        self.passive = "When activated, return a card from the field to the hand. Than, play a card *Abyssal card up to 4 cost from your deck."

class Sinners_Blessing:
    def __init__(self):
        self.name = "Sinner's Blessing"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Abyssal", "Khaenri'ah"
        self.cost = 2
        self.duration = "once"
        
        self.passive = "destroy a 4 cost or less card from the field to play an 6 or more cost *Abyssal card from your discard pile. Than."

class Defield_Statue:
    def __init__(self):
        self.name = "Defiled Statue"
        self.type = "Character"
        self.element = "Omni"
        self.tag = "Abyssal"
        self.cost = 6
        self.power = 0
        self.hp = 600
        self.passive = "Increase the power of all *Abyssal cards other than this one by 50 per card in the discard pile."

class Ruin_Guard:
    def __init__(self):
        self.name = "Ruin Guard"
        self.type = "Character"
        self.element = "Omni"
        self.tag = "Khaenri'ah", "Automaton"
        self.cost = 4
        self.power = 400
        self.hp = 500
        self.passive = "When played, destroy a card with 2 or less cost from the enemy's field."

class Corrupted_Blood:
    def __init__(self):
        self.name = "Corrupted Blood"
        self.type = "Support"
        self.element = "Omni"
        self.tag = "Abyssal"
        self.cost = 2
        self.duration = "once"
        
        self.passive = "When activated, destroy a card from your field. Than, play a *Abyssal card with the same cost from your discard pile."

class Ruin_Destroyer_Serpent:
    def __init__(self):
        self.name = "Ruin Destroyer Serpent"
        self.type = "Character"
        self.element = "Omni"
        self.tag = "Khaenri'ah", "Automaton"
        self.cost = 1
        self.power = 300
        self.hp = 100
        self.passive = "When destroyed, draw 1 card."

class Elynas:
    def __init__(self):
        self.name = "Elynas"
        self.type = "Character"
        self.element = "Hydro"
        self.tag = "Abyssal"
        self.cost = 8
        self.power = 600
        self.hp = 400
        self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

abyssDeck = [Lumine, Cryo_Abyss_Mage, Hydro_Abyss_Mage, Caribert, Chlothar, Cryo_Abyss_Herald, Hydro_Abyss_Herald, Elemental_Conversion, Transcending_Fate, Loom_of_Fate, Tenebrous_Mimiflora, Abyssal_Rift, Sinners_Blessing, Defield_Statue, Ruin_Guard, Corrupted_Blood, Ruin_Destroyer_Serpent, Elynas]

deck2 = [card_class() for card_class in abyssDeck]
#ST01

class Albedo:
    def __init__(self):
        self.name = "Albedo"
        self.type = "Character"
        self.element = "Geo"
        self.tag = "Knights of Favonius", "Hexerei", "Alchemy"
        self.cost = 4
        self.power = 350
        self.hp = 350
        self.passive = "On play, use Transmutation to play a character from the discard pile or hand"

class Klee:
    def __init__(self):
        self.name = "Klee"
        self.type = "Character"
        self.element = "Pyro"
        self.tag = "Knights of Favonius", "Hexerei"
        self.cost = 2
        self.power = 300
        self.hp = 200
        self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Nicole:
    def __init__(self):
            self.name = "Nicole"
            self.type = "Character"
            self.element = "Pyro"
            self.tag = "Hexerei", "Celestial"
            self.cost = 8
            self.power = 550
            self.hp = 650
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Mona:
    def __init__(self):
            self.name = "Mona"
            self.type = "Character"
            self.element = "Hydro"
            self.tag = "Hexerei", "Astrology"
            self.cost = 4
            self.power = 300
            self.hp = 400
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Prune:
    def __init__(self):
            self.name = "Prune"
            self.type = "Character"
            self.element = "Anemo"
            self.tag = "Hexerei"
            self.cost = 1
            self.power = 250
            self.hp = 150
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Dodoco:
    def __init__(self):
            self.name = "Dodoco"
            self.type = "Character"
            self.element = "Pyro"
            self.tag ="Hexerei"
            self.cost = 1
            self.power = 150
            self.hp = 250
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Dodocannon:
    def __init__(self):
            self.name = "Dodocannon"
            self.type = "Character"
            self.element = "Pyro"
            self.tag = "Hexerei", "Automaton"
            self.cost = 4
            self.power = 300
            self.hp = 400
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Witches_Tea_Party:
    def __init__(self):
            self.name = "Witches' Tea Party"
            self.type = "Support"
            self.element = "Omni"
            self.tag ="Hexerei"
            self.cost = 2
           
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Dodocomunicator:
    def __init__(self):
            self.name = "Dodocomunicator"
            self.type = "Support"
            self.element = "Pyro"
            self.tag ="Hexerei"
            self.cost = 1
            
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Fischl:
    def __init__(self):
            self.name = "Fischl"
            self.type = "Character"
            self.element = "Electro"
            self.tag ="Hexerei", "Adventure's Guild", "Fairy Tale"
            self.cost = 2
            self.power = 350
            self.hp = 150
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Magic_Bubble:
    def __init__(self):
            self.name = "Magic Bubble"
            self.type = "Support"
            self.element = "Omni"
            self.tag ="Hexerei"
            self.cost = 4
           
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Venti:
    def __init__(self):
            self.name = "Venti"
            self.type = "Character"
            self.element = "Anemo"
            self.tag = "Knights of Favonius", "Hexerei", "Church of Favonius", "Celestial"
            self.cost = 8
            self.power = 550
            self.hp = 450
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Mini_Durin:
    def __init__(self):
            self.name = "Mini Durin"
            self.type = "Character"
            self.element = "Pyro"
            self.tag = "Hexerei", "Fairy Tale", "Dragon"
            self.cost = 1
            self.power = 150
            self.hp = 250
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Imaginarium_Theather:
    def __init__(self):
            self.name = "Imaginarium Theather"
            self.type = "Support"
            self.element = "Omni"
            self.tag ="Hexerei", "Fairy Tale"
            self.cost = 6
            
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Wolfy:
    def __init__(self):
            self.name = "Wolfy"
            self.type = "Character"
            self.element = "Omni"
            self.tag = "Hexerei", "Fairy Tale"
            self.cost = 1
            self.power = 50
            self.hp = 350
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Witches_Homework:
    def __init__(self):
            self.name = "Witch's Homework"
            self.type = "Support"
            self.element = "Omni"
            self.tag ="Hexerei"
            self.cost = 4
           
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class The_Boar_Princess:
    def __init__(self):
            self.name = "The Boar Princess"
            self.type = "Support"
            self.element = "Omni"
            self.tag = "Hexerei", "Fairy Tale"
            self.cost = 2
            
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Xiao:
    def __init__(self):
            self.name = "Xiao"
            self.type = "Character"
            self.element = "Anemo"
            self.tag = "Adepti", "Yaksha"
            self.cost = 6
            self.power = 550
            self.hp = 350
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Zhongli:
    def __init__(self):
            self.name = "Zhongli"
            self.type = "Character"
            self.element = "Geo"
            self.tag = "Adepti", "Celestial"
            self.cost = 8
            self.power = 350
            self.hp = 650
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Cloud_Retainer:
     def __init__(self):
             self.name = "Cloud Retainer"
             self.type = "Character"
             self.element = "Anemo"
             self.tag = "Adepti"
             self.cost = 2
             self.power = 150
             self.hp = 350
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Xianyun:
     def __init__(self):
             self.name = "Xianyun"
             self.type = "Character"
             self.element = "Anemo"
             self.tag = "Adepti"
             self.cost = 6
             self.power = 450
             self.hp = 450
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Yanfei:
     def __init__(self):
             self.name = "Yanfei"
             self.type = "Character"
             self.element = "Pyro"
             self.tag = "Adepti", "Liyue Qixing"
             self.cost = 1
             self.power = 200
             self.hp = 200
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Bosacius:
     def __init__(self):
             self.name = "Bosacius"
             self.type = "Character"
             self.element = "Electro"
             self.tag = "Adepti", "Yaksha"
             self.cost = 6
             self.power = 500
             self.hp = 400
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Solitary_Suanni:
     def __init__(self):
             self.name = "Solitary Suanni"
             self.type = "Character"
             self.element = "Anemo"
             self.tag = "Adepti"
             self.cost = 4
             self.power = 400
             self.hp = 300
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Xuanwen_Beast:
     def __init__(self):
             self.name = "Xuanwen Beast"
             self.type = "Character"
             self.element = "Anemo"
             self.tag = "Adepti"
             self.cost = 1
             self.power = 250
             self.hp = 150
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Xiangling:
     def __init__(self):
             self.name = "Xiangling"
             self.type = "Character"
             self.element = "Pyro"
             self.tag = "Adepti"
             self.cost = 1
             self.power = 150
             self.hp = 250
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Guoba:
     def __init__(self):
             self.name = "Guoba"
             self.type = "Character"
             self.element = "Pyro"
             self.tag = "Adepti"
             self.cost = 1
             self.power = 200
             self.hp = 200
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Seal_of_Permission:
     def __init__(self):
             self.name = "Seal of Permission"
             self.type = "Support"
             self.element = "Omni"
             self.tag = "Adepti"
             self.cost = 2
             
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Guili_Assembly:
     def __init__(self):
             self.name = "Guili Assembly"
             self.type = "Support"
             self.element = "Omni"
             self.tag = "Adepti"
             self.cost = 4
            
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Karma:
     def __init__(self):
             self.name = "Karma"
             self.type = "Weapon"
             self.element = "Omni"
             self.tag = "Adepti"
             self.cost = 2
             
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Guizhong_Balista:
     def __init__(self):
             self.name = "Guizhong Balista"
             self.type = "Weapon"
             self.element = "Geo"
             self.tag = "Adepti"
             self.cost = 6
             
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Zibai:
     def __init__(self):
             self.name = "Zibai"
             self.type = "Character"
             self.element = "Geo"
             self.tag = "Adepti", "Celestial", "Moonsign"
             self.cost = 8
             self.power = 600
             self.hp = 400
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Raiden_Ei:
     def __init__(self):
             self.name = "Raiden Ei"
             self.type = "Character"
             self.element = "Electro"
             self.tag = "Youkai", "Shogunate", "Celestial"
             self.cost = 8
             self.power = 700
             self.hp = 300
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Kappa:
     def __init__(self):
             self.name = "Kappa"
             self.type = "Character"
             self.element = "Hydro"
             self.tag = "Youkai"
             self.cost = 1
             self.power = 80
             self.hp = 320
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Kujou_Sara:
     def __init__(self):
             self.name = "Kujou Sara"
             self.type = "Character"
             self.element = "Electro"
             self.tag = "Youkai", "Shogunate"
             self.cost = 4
             self.power = 350
             self.hp = 350
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Yae_Miko:
     def __init__(self):
             self.name = "Yae Miko"
             self.type = "Character"
             self.element = "Electro"
             self.tag = "Youkai", "Shrine Maiden", "Shogunate"
             self.cost = 6
             self.power = 550
             self.hp = 350
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Sasayuri:
     def __init__(self):
             self.name = "Sasayuri"
             self.type = "Character"
             self.element = "Electro"
             self.tag = "Youkai", "Shogunate"
             self.cost = 6
             self.power = 450
             self.hp = 450
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Red_Oni:
     def __init__(self):
             self.name = "Red Oni"
             self.type = "Character"
             self.element = "Geo"
             self.tag = "Youkai"
             self.cost = 1
             self.power = 250
             self.hp = 150
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Arataki_Itto:
     def __init__(self):
             self.name = "Arataki Itto"
             self.type = "Character"
             self.element = "Geo"
             self.tag = "Youkai", "Resistence"
             self.cost = 4
             self.power = 450
             self.hp = 250
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Blue_Oni:
     def __init__(self):
             self.name = "Blue Oni"
             self.type = "Character"
             self.element = "Hydro"
             self.tag = "Youkai"
             self.cost = 1
             self.power = 150
             self.hp = 250
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Ginkaku:
     def __init__(self):
             self.name = "Ginkaku"
             self.type = "Character"
             self.element = "Anemo", "Electro"
             self.tag = "Youkai"
             self.cost = 1
             self.power = 200
             self.hp = 200
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Bake_Danuke:
     def __init__(self):
             self.name = "Bake-Danuke"
             self.type = "Character"
             self.element = "Electro"
             self.tag = "Youkai"
             self.cost = 1
             self.power = 150
             self.hp = 250
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Ioroi:
     def __init__(self):
             self.name = "Ioroi"
             self.type = "Character"
             self.element = "Geo"
             self.tag = "Youkai"
             self.cost = 4
             self.power = 100
             self.hp = 500
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Kitsune_Statue:
     def __init__(self):
             self.name = "Kitsune Statue"
             self.type = "Support"
             self.element = "Electro"
             self.tag = "Youkai", "Shrine Maiden"
             self.cost = 2
             
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Toukabou_Shigure:
     def __init__(self):
             self.name = "Toukabou Shigure"
             self.type = "Weapon"
             self.element = "Electro", "Anemo"
             self.tag = "Youkai"
             self.cost = 2
             
             self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Kamen:
    def __init__(self):
            self.name = "Kamen"
            self.type = "Character"
            self.element = "Electro"
            self.tag = "Youkai"
            self.cost = 2
            self.power = 300
            self.hp = 200
            self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Mussou_no_Hitotachi:
     def __init__(self):
                 self.name = "Mussou no Hitotachi"
                 self.type = "Support"
                 self.element = "Electro"
                 self.tag = "Youkai", "Shogunate"
                 self.cost = 6
                 
                 self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Aaru:
     def __init__(self):
                 self.name = "Aaru"
                 self.type = "Support"
                 self.element = "Dendro"
                 self.tag = "Seven Pillars"
                 self.cost = 8
                 
                 self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Golden_Slumber:
     def __init__(self):
                 self.name = "Golden Slumber"
                 self.type = "Support"
                 self.element = "Dendro"
                 self.tag = "Seven Pillars"
                 self.cost = 6
                 
                 self.passive = "When played, destroy all 4 or less cost cards from the field. While in the field, all *Abyssal cards have +200 power."

class Nahida:
     def __init__(self):
                 self.name = "Nahida"
                 self.type = "Character"
                 self.element = "Dendro"
                 self.tag = "Seven Pillars", "Akademiya"
                 self.cost = 8
                 self.power = 600
                 self.hp = 400
                 self.passive = "When played, Draw 2 cards, Spells have their cost reduced by 2."

class Thoth:
     def __init__(self):
                 self.name = "Thoth"
                 self.type = "Character"
                 self.element = "Dendro"
                 self.tag = "Seven Pillars", "Moonsign"
                 self.cost = 6
                 self.power = 500
                 self.hp = 300
                 self.passive = "When played, Draw 2 cards, Spells have their cost reduced by 2."

class Nefer:
        def __init__(self):
                    self.name = "Nefer"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "Seven Pillars", "Agent", "Moonsign"
                    self.cost = 4
                    self.power = 400
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Cyno:
        def __init__(self):
                    self.name = "Cyno"
                    self.type = "Character"
                    self.element = "Electro"
                    self.tag = "Seven Pillars", "Akademiya"
                    self.cost = 6
                    self.power = 400
                    self.hp = 400
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Sethos:
        def __init__(self):
                    self.name = "Sethos"
                    self.type = "Character"
                    self.element = "Electro"
                    self.tag = "Seven Pillars"
                    self.cost = 4
                    self.power = 300
                    self.hp = 300
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Temple_of_Silence:
        def __init__(self):
                    self.name = "Temple of Silence"
                    self.type = "Support"
                    self.element = "Electro"
                    self.tag = "Seven Pillars"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class ASIMON:
        def __init__(self):
                    self.name = "A.S.I.M.O.N"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "Automaton", "Seven Pillars"
                    self.cost = 4
                    self.power = 300
                    self.hp = 400
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Volture:
        def __init__(self):
                    self.name = "Volture"
                    self.type = "Character"
                    self.element = "Pyro"
                    self.tag = "WildLife"
                    self.cost = 1
                    self.power = 200
                    self.hp = 100
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Primal_Construct_repulsor:
        def __init__(self):
                    self.name = "Primal Construct Repulsor"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "Automaton", "Seven Pillars"
                    self.cost = 1
                    self.power = 150
                    self.hp = 150
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Primal_Construct_prospector:
        def __init__(self):
                    self.name = "Primal Construct Prospector"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "Automaton", "Seven Pillars"
                    self.cost = 1
                    self.power = 100
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Forbidden_Knowledge:
        def __init__(self):
                    self.name = "Forbidden Knowlagde"
                    self.type = "Support"
                    self.element = "Dendro"
                    self.tag = "Seven Pillars", "Abyssal"
                    self.cost = 6
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Dehya:
        def __init__(self):
                    self.name = "Dehya"
                    self.type = "Character"
                    self.element = "Pyro"
                    self.tag = "Seven Pillars", "Mercenary"
                    self.cost = 4
                    self.power = 300
                    self.hp = 400
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Eremite:
        def __init__(self):
                    self.name = "Eremite"
                    self.type = "Character"
                    self.element = "Electro"
                    self.tag = "Mercenary"
                    self.cost = 1
                    self.power = 200
                    self.hp = 100
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Sandrone:
        def __init__(self):
                    self.name = "Sandrone"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Automaton", "Fatui", "Narzissenkreuz", "Stellar"
                    self.cost = 4
                    self.power = 350
                    self.hp = 350
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Ineffa:
        def __init__(self):
                    self.name = "Ineffa"
                    self.type = "Character"
                    self.element = "Electro"
                    self.tag = "Automaton", "Dragon", "Moonsign"
                    self.cost = 2
                    self.power = 200
                    self.hp = 300
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Aino:
        def __init__(self):
                    self.name = "Aino"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "Automaton", "Moonsign"
                    self.cost = 1
                    self.power = 50
                    self.hp = 250
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Freminet:
        def __init__(self):
                    self.name = "Freminet"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Automaton", "Fatui", "House of the Hearth", "Aekhe"
                    self.cost = 2
                    self.power = 250
                    self.hp = 150
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Recon_Log_Mek:
        def __init__(self):
                    self.name = "Recon Log Mek"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Automaton", "Aekhe", "Court of Fontaine"
                    self.cost = 1
                    self.power = 150
                    self.hp = 150
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Underwater_Survey_Mek:
        def __init__(self):
                    self.name = "Underwater Survey Mek"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "Automaton", "Aekhe", "Court of Fontaine"
                    self.cost = 1
                    self.power = 100
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Suppression_Specialist_Mek:
        def __init__(self):
                    self.name = "Suppression Specialist Mek"
                    self.type = "Character"
                    self.element = "Electro"
                    self.tag = "Automaton", "Aekhe", "Court of Fontaine"
                    self.cost = 4
                    self.power = 300
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Storm_Landcruiser:
        def __init__(self):
                    self.name = "Pyro Storm Landcruiser"
                    self.type = "Character"
                    self.element = "Pyro"
                    self.tag = "Automaton", "Fatui"
                    self.cost = 1
                    self.power = 200
                    self.hp = 100
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Mechaniozed_Fortress:
        def __init__(self):
                    self.name = "Mechaniozed Fortress"
                    self.type = "Character"
                    self.element = "Pyro"
                    self.tag = "Automaton", "Fatui"
                    self.cost = 6
                    self.power = 350
                    self.hp = 650
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Fontaine_Research_Institute:
        def __init__(self):
                    self.name = "Fontaine Research Institute"
                    self.type = "Support"
                    self.element = "Hydro"
                    self.tag = "Automaton", "Court of Fontaine"
                    self.cost = 4
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Scrap_Robots:
        def __init__(self):
                    self.name = "Scrap Robots"
                    self.type = "Character"
                    self.element = "Electro"
                    self.tag = "Automaton"
                    self.cost = 1
                    self.power = 100
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Pulonia:
        def __init__(self):
                    self.name = "Pulonia"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Automaton", "Fatui", "Narzissenkreuz"
                    self.cost = 8
                    self.power = 500
                    self.hp = 500
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Fagio:
        def __init__(self):
                    self.name = "Fagio"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Automaton", "Fatui", "Narzissenkreuz"
                    self.cost = 8
                    self.power = 600
                    self.hp = 400
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class World_Formula:
        def __init__(self):
                    self.name = "World Formula"
                    self.type = "Support"
                    self.element = "Cryo"
                    self.tag = "Narzissenkreuz"
                    self.cost = 6
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Garde:
        def __init__(self):
                    self.name = "Garde"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "Court of Fontaine"
                    self.cost = 1
                    self.power = 200
                    self.hp = 100
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Citlali:
        def __init__(self):
                    self.name = "Citlali"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Heroes", "Masters of the Night Wind", "Astrology"
                    self.cost = 6
                    self.power = 350
                    self.hp = 350
                    self.passive = "This card can't be removed by spells. When played, Reveal the 4 cards from the top of your deck, then, draw one Masters of the Night Wind card. If this card is revealed in the deck, play this card without paying the cost."

class Mavuika:
        def __init__(self):
                    self.name = "Mavuika"
                    self.type = "Character"
                    self.element = "Pyro"
                    self.tag = "Heroes", "Celestial"
                    self.cost = 8
                    self.power = 700
                    self.hp = 300
                    self.passive = "When played, Deals 500 damage to all enemy cards. Heroes cards have thei power increased by 150."

class Ororon:
        def __init__(self):
                    self.name = "Ororon"
                    self.type = "Character"
                    self.element = "Electro"
                    self.tag = "Heroes", "Masters of the Night Wind", "Astrology"
                    self.cost = 2
                    self.power = 300
                    self.hp = 100
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one Masters of the Night Wind card. When this is in the discard pile, once per turn, gain one cost."

class Capitano:
        def __init__(self):
                    self.name = "Capitano"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Masters of the Night Wind", "Fatui"
                    self.cost = 8
                    self.power = 500
                    self.hp = 500
                    self.passive = "For each spell card in the discard pile, increase power by 50. If this card is revealed in the deck, draw this card. If this card is sent to the discard pile, after one turn, draw this card."

class Iktomissaurus:
        def __init__(self):
                    self.name = "Iktomissaurus"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Dragon", "Masters of the Night Wind"
                    self.cost = 2
                    self.power = 200
                    self.hp = 300
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Tlapo:
        def __init__(self):
                    self.name = "Tlapo"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Dragon", "Masters of the Night Wind"
                    self.cost = 4
                    self.power = 300
                    self.hp = 300
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one Masters of the Night Wind card. This card can be played by paying 1 less cost to diseable a spell."

class Biram:
        def __init__(self):
                    self.name = "Biram"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Heroes", "Masters of the Night Wind", "Astrology"
                    self.cost = 4
                    self.power = 300
                    self.hp = 300
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Nightkingdom:
        def __init__(self):
                    self.name = "Nightkingdom"
                    self.type = "Support"
                    self.element = "Omni"
                    self.tag = "Heroes"
                    self.cost = 6
                    self.passive = "While active, you can put a card in the discard pile in the bottom of the deck to negate a spell."

class Acient_Name:
        def __init__(self):
                    self.name = "Acient Name"
                    self.type = "Support"
                    self.element = "Omni"
                    self.tag = "Heroes"
                    self.cost = 2
                    self.passive = "When played, increase a Heroes card power and hp by 50. When the card this card was used is destroyed, after one turn, draw that card again without the effect of this card ."

class Wyob:
        def __init__(self):
                    self.name = "Cryo Wyob Manifestation"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Heroes", "Celestial", "Masters of the Night Wind"
                    self.cost = 6
                    self.power = 400
                    self.hp = 400
                    self.passive = "When played, search for an Ancient Name and than draw it. While in the discard pile, negate one spell per turn."

class Obsidian_Pillar:
        def __init__(self):
                    self.name = "Obsidian Pillar"
                    self.type = "Support"
                    self.element = "Omni"
                    self.tag = "Heroes"
                    self.cost = 4
                    self.passive = "While active, reveal the top card of your deck."

class Nightsoul_Blessing:
        def __init__(self):
                    self.name = "Nightsoul Blessing"
                    self.type = "Support"
                    self.element = "Omni"
                    self.tag = "Heroes"
                    self.cost = 2
                    self.passive = "When played, choose a Heroes card to attack again."

class Name_Fishing:
        def __init__(self):
                    self.name = "Name Fishing"
                    self.type = "Support"
                    self.element = "Omni"
                    self.tag = "Heroes"
                    self.cost = 4
                    self.passive = "When played, search for an Ancient Name and then draw it."

class Ode_of_Ressurection:
        def __init__(self):
                    self.name = "Ode of Ressurection"
                    self.type = "Support"
                    self.element = "Omni"
                    self.tag = "Heroes"
                    self.cost = 8
                    self.passive = "All Heroes characters that are destroyed go back to the field with the effect of Nightsoul Blessing. This effect duration is 3 turns."

class Spiritspeaker_Warrior:
        def __init__(self):
                    self.name = "Spiritspeaker Warrior"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Heroes", "Masters of the Night Wind"
                    self.cost = 1
                    self.power = 200
                    self.hp = 100
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Iktomisaurus_Warrior:
        def __init__(self):
                    self.name = "Iktomisaurus Warrior"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Heroes", "Masters of the Night Wind"
                    self.cost = 1
                    self.power = 250
                    self.hp = 50
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Spiritspeaker_State:
        def __init__(self):
                    self.name = "Spiritspeaker State"
                    self.type = "Support"
                    self.element = "Cryo"
                    self.tag = "Heroes", "Masters of the Night Wind"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Nightspirit_Graffiti:
        def __init__(self):
                    self.name = "Nightspirit Graffiti"
                    self.type = "Support"
                    self.element = "Cryo"
                    self.tag = "Heroes", "Masters of the Night Wind"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Phlogistum:
        def __init__(self):
                    self.name = "Phlogistum"
                    self.type = "Support"
                    self.element = "Pyro"
                    self.tag = "Heroes", "Dragon"
                    self.cost = 4
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Baby_Iktomisaurus:
        def __init__(self):
                    self.name = "Baby Iktomisaurus"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Dragons", "Masters of the Night Wind"
                    self.cost = 1
                    self.power = 200
                    self.hp = 100
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Lauma:
        def __init__(self):
                    self.name = "Lauma"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "WildLife", "Moonsign", "Frostmoon"
                    self.cost = 4
                    self.power = 300
                    self.hp = 300
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Columbina:
        def __init__(self):
                    self.name = "Columbina"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "WildLife", "Moonsign", "Frostmoon", "Fatui"
                    self.cost = 8
                    self.power = 500
                    self.hp = 500
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Collei:
        def __init__(self):
                    self.name = "Collei"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "WildLife", "Celestial", "Seven Pillars"
                    self.cost = 1
                    self.power = 250
                    self.hp = 50
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Tighnari:
        def __init__(self):
                    self.name = "Tighnari"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "WildLife", "Seven Pillars"
                    self.cost = 2
                    self.power = 300
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Radiant_Moonfly:
        def __init__(self):
                    self.name = "Radiant Moonfly"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "WildLife", "Moonsign"
                    self.cost = 6
                    self.power = 350
                    self.hp = 250
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Juvenille_Leshy:
        def __init__(self):
                    self.name = "Juvenille Leshy"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "WildLife", "Fae"
                    self.cost = 1
                    self.power = 150
                    self.hp = 150
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Elder_Leshy:
        def __init__(self):
                    self.name = "Elder Leshy"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "WildLife", "Fae"
                    self.cost = 4
                    self.power = 300
                    self.hp = 400
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Radiant_Bladehorn:
        def __init__(self):
                    self.name = "Radiant Bladehorn"
                    self.type = "Character"
                    self.element = "Anemo"
                    self.tag = "WildLife", "Moonsign"
                    self.cost = 2
                    self.power = 300
                    self.hp = 100
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Dualblaze_Ibis:
        def __init__(self):
                    self.name = "Dualblaze Ibis"
                    self.type = "Character"
                    self.element = "Anemo"
                    self.tag = "WildLife", "Moonsign"
                    self.cost = 1
                    self.power = 150
                    self.hp = 150
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Fluffahog:
        def __init__(self):
                    self.name = "Fluffahog"
                    self.type = "Character"
                    self.element = "Anemo"
                    self.tag = "WildLife"
                    self.cost = 1
                    self.power = 100
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Blunthorn_Rhino:
        def __init__(self):
                    self.name = "Blunthorn Rhino"
                    self.type = "Character"
                    self.element = "Anemo"
                    self.tag = "WildLife", "Moonsign"
                    self.cost = 1
                    self.power = 200
                    self.hp = 100
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."    

class Fuzzbadge:
        def __init__(self):
                    self.name = "Fuzzbadge"
                    self.type = "Character"
                    self.element = "Anemo"
                    self.tag = "WildLife", "Moonsign"
                    self.cost = 1
                    self.power = 150
                    self.hp = 150
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Rimehorn_Deer:
        def __init__(self):
                    self.name = "Rimehorn Deer"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "WildLife", "Moonsign"
                    self.cost = 2
                    self.power = 300
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Wrath_of_the_Forest:
        def __init__(self):
                    self.name = "Wrath of the Forest"
                    self.type = "Support"
                    self.element = "Dendro"
                    self.tag = "WildLife", "Moonsign"
                    self.cost = 4
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Moonglow_Fireflly:
        def __init__(self):
                    self.name = "Moonglow Firefly"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "WildLife", "Moonsign"
                    self.cost = 1
                    self.power = 100
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Winter_Icelea:
        def __init__(self):
                    self.name = "Winter Icelea"
                    self.type = "Support"
                    self.element = "Dendro"
                    self.tag = "WildLife", "Moonsign"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Frostmoon_Priest:
        def __init__(self):
                    self.name = "Frostmoon Priest"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "WildLife", "Moonsign", "Frostmoon"
                    self.cost = 2
                    self.power = 200
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Imprision:
        def __init__(self):
                    self.name = "Imprision"
                    self.type = "Support"
                    self.element = "Dendro"
                    self.tag = "WildLife"
                    self.cost = 4
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Moon_Prayer:
        def __init__(self):
                    self.name = "Moon Prayer"
                    self.type = "Support"
                    self.element = "Hydro"
                    self.tag = "WildLife", "Moonsign", "Frostmoon"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Nastya:
        def __init__(self):
                    self.name = "Nastya"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "WildLife", "Fae"
                    self.cost = 2
                    self.power = 100
                    self.hp = 300
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Pierro:
        def __init__(self):
                    self.name = "Pierro"
                    self.type = "Character"
                    self.element = "Electro"
                    self.tag = "Fatui", "Astrology"
                    self.cost = 6
                    self.power = 500
                    self.hp = 300
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Lumi:
        def __init__(self):
                    self.name = "Lumi"
                    self.type = "Character"
                    self.element = "Geo"
                    self.tag = "Fae", "Adventure", "Moonsign"
                    self.cost = 4
                    self.power = 400
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Linnea:
        def __init__(self):
                    self.name = "Linnea"
                    self.type = "Character"
                    self.element = "Geo"
                    self.tag = "Fae", "Adventure", "Moonsign"
                    self.cost = 2
                    self.power = 300
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Vodyanitsa:
        def __init__(self):
                    self.name = "Vodyanitsa"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "Fae", "Rebel"
                    self.cost = 4
                    self.power = 400
                    self.hp = 300
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Siren_Song:
        def __init__(self):
                    self.name = "Siren Song"
                    self.type = "Support"
                    self.element = "Hydro"
                    self.tag = "Fae"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Flins:
        def __init__(self):
                    self.name = "Flins"
                    self.type = "Character"
                    self.element = "Electro"
                    self.tag = "Fae", "Lightkeeper", "Moonsign"
                    self.cost = 6
                    self.power = 500
                    self.hp = 400
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Hilichurl_Warrior:
        def __init__(self):
                    self.name = "Hilichurl Warrior"
                    self.type = "Character"
                    self.element = "Geo"
                    self.tag = "Hilichurl"
                    self.cost = 1
                    self.power = 200
                    self.hp = 100
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Hilichurl_Shooter:   
        def __init__(self):
                    self.name = "Hilichurl Shooter"
                    self.type = "Character"
                    self.element = "Pyro"
                    self.tag = "Hilichurl"
                    self.cost = 1
                    self.power = 150
                    self.hp = 150
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Mitachurl_BlazingAxe:
        def __init__(self):
                    self.name = "Mitachurl Blazing Axe"
                    self.type = "Character"
                    self.element = "Pyro"
                    self.tag = "Hilichurl"
                    self.cost = 4
                    self.power = 400
                    self.hp = 300
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Hydro_Samachurl:
        def __init__(self):
                    self.name = "Hydro Samachurl"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "Hilichurl"
                    self.cost = 2
                    self.power = 200
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Ella_Musk:
        def __init__(self):
                    self.name = "Ella Musk"
                    self.type = "Character"
                    self.element = "Electro"
                    self.tag = "Hilichurl"
                    self.cost = 1
                    self.power = 150
                    self.hp = 150
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Hilichurl_Camp:
        def __init__(self):
                    self.name = "Hilichurl Camp"
                    self.type = "Support"
                    self.element = "Geo"
                    self.tag = "Hilichurl"
                    self.cost = 4
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Curse_of_Wilderness:
        def __init__(self):
                    self.name = "Curse of Wilderness"
                    self.type = "Support"
                    self.element = "Omni"
                    self.tag = "Hilichurl", "Celestial"
                    self.cost = 8
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Geo_Lawachurl:
        def __init__(self):
                    self.name = "Geo Lawachurl"
                    self.type = "Character"
                    self.element = "Geo"
                    self.tag = "Hilichurl"
                    self.cost = 8
                    self.power = 600
                    self.hp = 400
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Pyro_Slime:
        def __init__(self):
                    self.name = "Pyro Slime"
                    self.type = "Character"
                    self.element = "Pyro"
                    self.tag = "Elemental"
                    self.cost = 1
                    self.power = 100
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Unusual_Hilichurl:
        def __init__(self):
                    self.name = "Unusual Hilichurl"
                    self.type = "Character"
                    self.element = "Omni"
                    self.tag = "Hilichurl"
                    self.cost = 2
                    self.power = 200
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Final_Rest:
        def __init__(self):
                    self.name = "Final Rest"
                    self.type = "Support"
                    self.element = "Omni"
                    self.tag = "Hilichurl"
                    self.cost = 6
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Churlcric:
        def __init__(self):
                    self.name = "Churldric"
                    self.type = "Character"
                    self.element = "Geo"
                    self.tag = "Hilichurl"
                    self.cost = 8
                    self.power = 500
                    self.hp = 500
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Explosive_Barrel:
        def __init__(self):
                    self.name = "Explosive Barrel"
                    self.type = "Support"
                    self.element = "Pyro"
                    self.tag = "Hilichurl", "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Totem:
        def __init__(self):
                    self.name = "Totem"
                    self.type = "Support"
                    self.element = "Omni"
                    self.tag = "Hilichurl"
                    self.cost = 4
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Furina:
        def __init__(self):
                    self.name = "Furina"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "Court of Fontaine", "Celestial", "Oceanid"
                    self.cost = 2
                    self.power = 100
                    self.hp = 300
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Gentilhome_Usher:
        def __init__(self):
                    self.name = "Gentilhome Usher"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "Court of Fontaine", "Oceanid", "WildLife"
                    self.cost = 2
                    self.power = 200
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Surintendante_Chevalmarin:
        def __init__(self):
                    self.name = "Surintendante Chevalmarin"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "Court of Fontaine", "Oceanid", "WildLife"
                    self.cost = 1
                    self.power = 150
                    self.hp = 150
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Mademoiselle_Crabaletta:
        def __init__(self):
                    self.name = "Mademoiselle Crabaletta"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "Court of Fontaine", "Oceanid", "WildLife"
                    self.cost = 4
                    self.power = 200
                    self.hp = 300
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Hydro_Tulpa:
        def __init__(self):
                    self.name = "Hydro Tulpa"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "Oceanid", "Elemental"
                    self.cost = 6
                    self.power = 400
                    self.hp = 400
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Oceanid:
        def __init__(self):
                    self.name = "Oceanid"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "Oceanid", "Elemental"
                    self.cost = 6
                    self.power = 300
                    self.hp = 500
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Hydro_Eidolon:
        def __init__(self):
                    self.name = "Hydro Eidolon"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "Oceanid", "Elemental"
                    self.cost = 1
                    self.power = 100
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Fountain_of_Lucine:
        def __init__(self):
                    self.name = "Fountain of Lucine"
                    self.type = "Support"
                    self.element = "Hydro"
                    self.tag = "Oceanid", "Court of Fontaine"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Koholasaurus:
        def __init__(self):
                    self.name = "Koholasaurus"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "Dragon", "People of the Springs"
                    self.cost = 4
                    self.power = 300
                    self.hp = 400
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Youg_Koholasaurus:
        def __init__(self):
                    self.name = "Young Koholasaurus"
                    self.type = "Character"
                    self.element = "Hydro"
                    self.tag = "Dragon", "People of the Springs"
                    self.cost = 1
                    self.power = 150
                    self.hp = 150
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Qucusaurus:
        def __init__(self):
                    self.name = "Qucusaurus"
                    self.type = "Character"
                    self.element = "Pyro"
                    self.tag = "Dragon", "Flowerfeather Clan"
                    self.cost = 2
                    self.power = 250
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Geo_Vishap:
        def __init__(self):
                    self.name = "Geo Vishap"
                    self.type = "Character"
                    self.element = "Geo"
                    self.tag = "Dragon"
                    self.cost = 4
                    self.power = 300
                    self.hp = 400
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Dottore_20:
        def __init__(self):
                    self.name = "Il Dottore Segment 20"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "Fatui", "Automaton", "Moonsign"
                    self.cost = 4
                    self.power = 400
                    self.hp = 300
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Arabalika:
        def __init__(self):
                    self.name = "Arabalika"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "Aranara", "WildLife"
                    self.cost = 2
                    self.power = 300
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Aranyaka:
        def __init__(self):
                    self.name = "Aranyaka"
                    self.type = "Support"
                    self.element = "Dendro"
                    self.tag = "Aranara", "WildLife"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Arama:
        def __init__(self):
                    self.name = "Arama"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "Aranara", "WildLife"
                    self.cost = 1
                    self.power = 200
                    self.hp = 100
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Ying_ier:
        def __init__(self):
                    self.name = "Ying'ier"
                    self.type = "Character"
                    self.element = "Dendro"
                    self.tag = "Liyue Qixing", "Alchemy"
                    self.cost = 1
                    self.power = 150
                    self.hp = 150
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one *Alchemy card and put the others on the bottom."

class Knowladge_Capsule:
        def __init__(self):
                    self.name = "Knowledge Capsule"
                    self.type = "Support"
                    self.element = "Dendro"
                    self.tag = "Akademiya"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Debt_Collector:
        def __init__(self):
                    self.name = "Debt Collector"
                    self.type = "Character"
                    self.element = "Pyro"
                    self.tag = "Fatui"
                    self.cost = 2
                    self.power = 300
                    self.hp = 100
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Oprichnik_Line_Trooper:
        def __init__(self):
                    self.name = "Oprichnik Line Trooper"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Fatui"
                    self.cost = 1
                    self.power = 200
                    self.hp = 100
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Frost_Operative:
        def __init__(self):
                    self.name = "Frost Operative"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Fatui", "House of the Hearth"
                    self.cost = 4
                    self.power = 400
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Odette:
        def __init__(self):
                    self.name = "Odette"
                    self.type = "Character"
                    self.element = "Cryo"
                    self.tag = "Fatui", "Rebel"
                    self.cost = 2
                    self.power = 300
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Arlecchino:
        def __init__(self):
                    self.name = "Arlecchino"
                    self.type = "Character"
                    self.element = "Pyro"
                    self.tag = "Fatui", "House of the Hearth", "Frostmoon"
                    self.cost = 8
                    self.power = 600
                    self.hp = 400
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Knight_Patroller:
        def __init__(self):
                    self.name = "Knight Patroller"
                    self.type = "Character"
                    self.element = "Anemo"
                    self.tag = "Knights of Favonius"
                    self.cost = 1
                    self.power = 100
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Umbrellafinch:
        def __init__(self):
                    self.name = "Umbrellafinch"
                    self.type = "Character"
                    self.element = "Anemo"
                    self.tag = "WildLife"
                    self.cost = 1
                    self.power = 200
                    self.hp = 100
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Jahoda:
        def __init__(self):
                    self.name = "Jahoda"
                    self.type = "Character"
                    self.element = "Anemo"
                    self.tag = "Agent", "Moonsign", "Treasure Hoarders"
                    self.cost = 2
                    self.power = 300
                    self.hp = 200
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Anemo_Sigil:
        def __init__(self):
                    self.name = "Anemo Sigil"
                    self.type = "Support"
                    self.element = "Anemo"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Hydro_Sigil:
        def __init__(self):
                    self.name = "Hydro Sigil"
                    self.type = "Support"
                    self.element = "Hydro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Pyro_Sigil:
        def __init__(self):
                    self.name = "Pyro Sigil"
                    self.type = "Support"
                    self.element = "Pyro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Electro_Sigil:
        def __init__(self):
                    self.name = "Electro Sigil"
                    self.type = "Support"
                    self.element = "Electro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Geo_Sigil:
        def __init__(self):
                    self.name = "Geo Sigil"
                    self.type = "Support"
                    self.element = "Geo"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Dendro_Sigil:
        def __init__(self):
                    self.name = "Dendro Sigil"
                    self.type = "Support"
                    self.element = "Dendro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Cryo_Sigil:
        def __init__(self):
                    self.name = "Cryo Sigil"
                    self.type = "Support"
                    self.element = "Cryo"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Elemental_Ressonance:
        def __init__(self):
                    self.name = "Elemental Ressonance"
                    self.type = "Support"
                    self.element = "Omni"
                    self.tag = "Elemental"
                    self.cost = 4
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Leyline_Overflow:
        def __init__(self):
                    self.name = "Leyline Overflow"
                    self.type = "Support"
                    self.element = "Omni"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Aggravate:
        def __init__(self):
                    self.name = "Aggravate"
                    self.type = "Reaction"
                    self.element = "electro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Spread:
        def __init__(self):
                    self.name = "Spread"
                    self.type = "Reaction"
                    self.element = "Dendro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Vaporize:
        def __init__(self):
                    self.name = "Vaporize"
                    self.type = "Reaction"
                    self.element = "Hydro", "Pyro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Melt:
        def __init__(self):
                    self.name = "Melt"
                    self.type = "Reaction"
                    self.element = "Cryo", "Pyro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Freeze:
        def __init__(self):
                    self.name = "Freeze"
                    self.type = "Reaction"
                    self.element = "Cryo", "Hydro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Overload:
        def __init__(self):
                    self.name = "Overload"
                    self.type = "Reaction"
                    self.element = "Pyro", "Electro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Superconduct:
        def __init__(self):
                    self.name = "Superconduct"
                    self.type = "Reaction"
                    self.element = "Cryo", "Electro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Swirl:
        def __init__(self):
                    self.name = "Swirl"
                    self.type = "Reaction"
                    self.element = "Anemo", "Elemental"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Crystallize:
        def __init__(self):
                    self.name = "Crystallize"
                    self.type = "Reaction"
                    self.element = "Geo", "Elemental"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Bloom:
        def __init__(self):
                    self.name = "Bloom"
                    self.type = "Reaction"
                    self.element = "Dendro", "Elemental"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Burgeon:
        def __init__(self):
                    self.name = "Burgeon"
                    self.type = "Reaction"
                    self.element = "Dendro", "Elemental"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Hyperbloom:
        def __init__(self):
                    self.name = "Hyperbloom"
                    self.type = "Reaction"
                    self.element = "Dendro", "Elemental"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Electro_Charged:
         def __init__(self):
                    self.name = "Electro-Charged"
                    self.type = "Reaction"
                    self.element = "Electro", "Hydro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Shatter:
         def __init__(self):
                    self.name = "Shatter"
                    self.type = "Reaction"
                    self.element = "Cryo", "Geo", "Hydro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Rimegrass:
         def __init__(self):
                    self.name = "Rimegrass"
                    self.type = "Reaction"
                    self.element = "Dendro", "Cryo"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Lunar_Charged:
         def __init__(self):
                    self.name = "Lunar Charged"
                    self.type = "Reaction"
                    self.element = "Electro", "Hydro"
                    self.tag = "Elemental", "Moonsign"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Lunar_Bloom:
         def __init__(self):
                    self.name = "Lunar Bloom"
                    self.type = "Reaction"
                    self.element = "Dendro", "Hydro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Lunar_Crystalize:
         def __init__(self):
                    self.name = "Lunar Crystalize"
                    self.type = "Reaction"
                    self.element = "Geo", "Hydro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Stellar_Swirl:
         def __init__(self):
                    self.name = "Stellar Swirl"
                    self.type = "Reaction"
                    self.element = "Anemo", "Cryo"
                    self.tag = "Elemental", "Stellar"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Stellar_Conduct: 
         def __init__(self):
                    self.name = "Stellar Conduct"
                    self.type = "Reaction"
                    self.element = "Electro", "Cryo"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Burning: 
         def __init__(self):
                    self.name = "Burning"
                    self.type = "Reaction"
                    self.element = "Pyro", "Dendro"
                    self.tag = "Elemental"
                    self.cost = 2
                    self.passive = "When played, Reveal the 3 cards from the top of your deck, then, draw one of them and put the others on the bottom."

class Polar_Star_Edict_Mandate:
         def __init__(self):
                    self.name = "Polar Star Edict Mandate"
                    self.type = "Support"
                    self.element = "Omni"
                    self.tag = "Stellar"
                    self.cost = 4
                    self.passive = "When played, increase the power of all *Stellar cards in your field by 200."
 

















st01_cards = [
    Albedo,  # R
    Klee,  # R
    Nicole,  # UR
    Mona,  # R
    Prune,  # R
    Dodoco,  # R
    Dodocannon,  # C
    Witches_Tea_Party,  # SR
    Dodocomunicator,  # R
    Fischl,  # SR
    Magic_Bubble,  # R
    Venti,  # SR
    Mini_Durin,  # R
    Imaginarium_Theather,  # UR
    Wolfy,  # C
    Witches_Homework,  # R
    The_Boar_Princess,  # C
    Xiao,  # R
    Zhongli,  # UR
    Cloud_Retainer,  # C
    Xianyun,  # R
    Yanfei,  # C
    Bosacius,  # SR
    Solitary_Suanni,  # R
    Xuanwen_Beast,  # C
    Xiangling,  # C
    Guoba,  # C
    Seal_of_Permission,  # C
    Guili_Assembly,  # C
    Karma,  # C
    Guizhong_Balista,  # R
    Zibai,  # UR
    Raiden_Ei,  # UR
    Kappa,  # C
    Kujou_Sara,  # R
    Yae_Miko,  # SR
    Sasayuri,  # R
    Red_Oni,  # C
    Arataki_Itto,  # R
    Blue_Oni,  # C
    Ginkaku,  # C
    Bake_Danuke,  # C
    Ioroi,  # R
    Kitsune_Statue,  # C
    Toukabou_Shigure,  # C
    Kamen,  # C
    Mussou_no_Hitotachi,  # SR
    Aaru,  # R
    Golden_Slumber,  # R
    Nahida,  # UR
    Thoth,  # R
    Nefer,  # SR
    Cyno,  # R
    Sethos,  # C
    Temple_of_Silence,  # R
    ASIMON,  # R
    Volture,  # C
    Primal_Construct_repulsor,  # C
    Primal_Construct_prospector,  # C
    Forbidden_Knowledge,  # R
    Dehya,  # C
    Eremite,  # C
    Sandrone,  # UR
    Ineffa,  # R
    Aino,  # C
    Freminet,  # C
    Recon_Log_Mek,  # C
    Underwater_Survey_Mek,  # C
    Suppression_Specialist_Mek,  # R
    Storm_Landcruiser,  # C
    Mechaniozed_Fortress,  # SR
    Fontaine_Research_Institute,  # C
    Scrap_Robots,  # C
    Pulonia,  # SR
    Fagio,  # UR
    World_Formula,  # SR
    Garde,  # C
    Citlali,  # SR
    Mavuika,  # UR
    Ororon,  # C
    Capitano,  # UR
    Iktomissaurus,  # C
    Tlapo,  # R
    Biram,  # C
    Nightkingdom,  # UR
    Acient_Name,  # R
    Wyob,  # R
    Obsidian_Pillar,  # C
    Nightsoul_Blessing,  # R
    Name_Fishing,  # R
    Ode_of_Ressurection,  # SR
    Spiritspeaker_Warrior,  # C
    Iktomisaurus_Warrior,  # C
    Spiritspeaker_State,  # C
    Nightspirit_Graffiti,  # C
    Phlogistum,  # C
    Baby_Iktomisaurus,  # C
    Lauma,  # SR
    Columbina,  # UR
    Collei,  # C
    Tighnari,  # C
    Radiant_Moonfly,  # SR
    Juvenille_Leshy,  # C
    Elder_Leshy,  # C
    Radiant_Bladehorn,  # R
    Dualblaze_Ibis,  # C
    Fluffahog,  # C
    Blunthorn_Rhino,  # C
    Fuzzbadge,  # C
    Rimehorn_Deer,  # R
    Wrath_of_the_Forest,  # UR
    Moonglow_Fireflly,  # C
    Winter_Icelea,  # C
    Frostmoon_Priest,  # C
    Imprision,  # R
    Moon_Prayer,  # SR
    Nastya,  # C
    Pierro,  # UR
    Lumi,  # R
    Linnea,  # C
    Vodyanitsa,  # R
    Siren_Song,  # R
    Flins,  # UR
    Hilichurl_Warrior,  # C
    Hilichurl_Shooter,  # C
    Mitachurl_BlazingAxe,  # C
    Hydro_Samachurl,  # R
    Ella_Musk,  # C
    Hilichurl_Camp,  # R
    Curse_of_Wilderness,  # SR
    Geo_Lawachurl,  # C
    Pyro_Slime,  # C
    Unusual_Hilichurl,  # SR
    Final_Rest,  # R
    Churlcric,  # SR
    Explosive_Barrel,  # C
    Totem,  # C
    Furina,  # SR
    Gentilhome_Usher,  # C
    Surintendante_Chevalmarin,  # C
    Mademoiselle_Crabaletta,  # C
    Hydro_Tulpa,  # SR
    Oceanid,  # C
    Hydro_Eidolon,  # C
    Fountain_of_Lucine,  # C
    Koholasaurus,  # C
    Youg_Koholasaurus,  # C
    Qucusaurus,  # C
    Geo_Vishap,  # C
    Dottore_20,  # R
    Arabalika,  # C
    Aranyaka,  # R
    Arama,  # C
    Ying_ier,  # C
    Knowladge_Capsule,  # C
    Debt_Collector,  # R
    Oprichnik_Line_Trooper,  # C
    Frost_Operative,  # R
    Odette,  # C
    Arlecchino,  # UR
    Knight_Patroller,  # C
    Umbrellafinch,  # C
    Jahoda,  # C
    Anemo_Sigil,  # SR
    Hydro_Sigil,  # SR
    Pyro_Sigil,  # SR
    Electro_Sigil,  # SR
    Geo_Sigil,  # SR
    Dendro_Sigil,  # SR
    Cryo_Sigil,  # SR
    Elemental_Ressonance,  # R
    Leyline_Overflow,  # C
    Polar_Star_Edict_Mandate,  # SR
    Anastasia,  # UR
    Jack_Frost,  # C
    Jack_Frost_Chief,  # C
    Snegovik_Guard,  # C
    Snegurochka_Cryomancer,  # C
    Pavlina,  # SR
    Snow_Giant,  # SR
    Vesna,  # R
    Rogue_Vila,  # C
    Royal_Guard_Druzhna,  # C
    Belyi_Tsars_Wish,  # SR
    Kresnik_Torch,  # C
    Eye_of_Graeae,  # C
    Imperial_March,  # R
    Mistilteinn,  # UR
    FrostBite,  # C
]


ReactionSideDeck = [Aggravate, Spread, Vaporize, Melt, Freeze, Superconduct, Stellar_Conduct, Overload, Electro_Charged, Lunar_Charged, Lunar_Bloom, Lunar_Crystalize, Stellar_Swirl, Swirl, Crystallize, Burgeon, Bloom, Hyperbloom, Shatter, Rimegrass, Burning]  
     
     


from collections import Counter

costs = [cartas[i]().cost for i in range(len(cartas))]
cost_counts = Counter(costs)


deck = [
    cartas[0](), cartas[0](), cartas[0](),  # 3x Aether
    cartas[1](), cartas[1](), cartas[1](),  # 3x Pyro_Seelie_Guide
    cartas[2](), cartas[2](), cartas[2](),   # 3x Paimon
    cartas[3](), cartas[3](),  # 2x Hexaiphanes_Blade
    cartas[4](), cartas[4](),  # 2x Statue_of_the_Seven
    cartas[5](), cartas[5](),  # 2x Nihylita
    cartas[6](), cartas[6](), cartas[6](),  # 3x Domain_Keeper
    cartas[7](), cartas[7](),  # 2x Celestial_Nail
    cartas[8](),  # 1x Celestia
    cartas[9](), cartas[9](), cartas[9](),  # 3x Celestial_Envoy
    cartas[10](), cartas[10](),  # 2x   Fake_Sky
    cartas[11](), cartas[11](), cartas[11](),  # 3x Purification
    cartas[12](), cartas[12](),  # 2x Spaceship
    cartas[13](), cartas[13](), cartas[13](),  # 3x Elemental_Conversion
    cartas[14](), cartas[14](),  # 2x Leylines
    cartas[15](), cartas[15](),  # 3x Istoria
    cartas[16](), cartas[16](),  # 2x Dark_Dragon
    
]


deck2 = [
    abyssDeck[0](), abyssDeck[0](), abyssDeck[0](),  # 3x Lumine
    abyssDeck[1](), abyssDeck[1](), # 3x Cryo_Abyss_Mage
    abyssDeck[2](), abyssDeck[2](), abyssDeck[2](),  # 3x Hydro_Abyss_Mage
    abyssDeck[3](), abyssDeck[3](),  # 3x Caribert
    abyssDeck[4](), abyssDeck[4](),  # 3x Chlothar
    abyssDeck[5](), abyssDeck[5](), abyssDeck[5](),  # 3x Cryo_Abyss_Herald
    abyssDeck[6](), abyssDeck[6](),  # 2x Hydro_Abyss_Herald
    abyssDeck[7](), abyssDeck[7](), abyssDeck[7](),  # 3x Elemental_Conversion
    abyssDeck[8](), abyssDeck[8](),  # 3x Transcending_Fate
    abyssDeck[9](), abyssDeck[9](),  # 2x Loom_of_Fate
    abyssDeck[10](), abyssDeck[10](), abyssDeck[10](),  # 3x Tenebrous_Mimiflora
    abyssDeck[11](), abyssDeck[11](),  # 2x Abyssal_Rift
    abyssDeck[12](), abyssDeck[12](),  # 3x Sinner's_Blessing
    abyssDeck[13](), abyssDeck[13](),  # 2x Defiled_Statue
    abyssDeck[14](), abyssDeck[14](),  # 3x Ruin_Guard
    abyssDeck[15](), abyssDeck[15](),  # 2x Corrupted_Blood
    abyssDeck[16](), abyssDeck[16](),  # 3x Ruin_Destroyer_Serpent
    abyssDeck[17](),  # 2x Elynas  
    ]

