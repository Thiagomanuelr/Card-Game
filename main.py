import json
import random
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
from pathlib import Path
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk

from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageTk

from Cartas2 import set2
from cartas import deck, deck2, st01_cards

st02_cards = set2
ST01_CARD_NAMES = {card_class().name for card_class in st01_cards}
ST02_CARD_NAMES = {card_class().name for card_class in st02_cards}
SET_CARD_NAMES = ST01_CARD_NAMES | ST02_CARD_NAMES

CARD_RARITIES = {
    "Albedo": "R", "Klee": "R", "Nicole": "UR", "Mona": "R",
    "Prune": "R", "Dodoco": "R", "Dodocannon": "C",
    "Witches' Tea Party": "SR", "Dodocomunicator": "R", "Fischl": "SR",
    "Magic Bubble": "R", "Venti": "SR", "Mini Durin": "R",
    "Imaginarium Theather": "UR", "Wolfy": "C", "Witch's Homework": "R",
    "The Boar Princess": "C", "Xiao": "R", "Zhongli": "UR",
    "Cloud Retainer": "C", "Xianyun": "R", "Yanfei": "C",
    "Bosacius": "SR", "Solitary Suanni": "R", "Xuanwen Beast": "C",
    "Xiangling": "C", "Guoba": "C", "Seal of Permition": "C",
    "Guili Assembly": "C", "Karma": "C", "Guizhong Balista": "R",
    "Zibai": "UR", "Raiden Ei": "UR", "Kappa": "C", "Kujou Sara": "R",
    "Yae Miko": "SR", "Sasayuri": "R", "Red Oni": "C",
    "Arataki Itto": "R", "Blue Oni": "C", "Ginkaku": "C",
    "Bake-Danuke": "C", "Ioroi": "R", "Kitsune Statue": "C",
    "Toukabou Shigure": "C", "Kamen": "C", "Mussou no Hitotachi": "SR",
    "Aaru": "R", "Golden Slumber": "R", "Nahida": "UR", "Toth": "R",
    "Nefer": "SR", "Cyno": "R", "Sethos": "C", "Temple of Silence": "R",
    "A.S.I.M.O.N": "R", "Volture": "C", "Primal Construct repulsor": "C",
    "Primal Construct prospector": "C", "Forbidden Knowlagde": "R", "Dehya": "C",
    "Eremite": "C", "Sandrone": "UR", "Ineffa": "R", "Aino": "C",
    "Freminet": "C", "Recon Log Mek": "C", "Underwater Survey Mek": "C",
    "Suppression Specialist Mek": "R", "Storm Landcruiser": "C",
    "Mechaniozed Fortress": "SR", "Fontaine Research Institute": "C",
    "Scrap Robots": "C", "Pulonia": "SR", "Fagio": "UR", "World Formula": "SR",
    "Garde": "C", "Citlali": "SR", "Mavuika": "UR", "Ororon": "C",
    "Capitano": "UR", "Iktomissaurus": "C", "Tlapo": "R", "Biram": "C",
    "Nightkingdom": "UR", "Acient Name": "R", "Wyob": "R", "Obsidian Pillar": "C",
    "Nightsoul Blessing": "R", "Name Fishing": "R", "Ode of Ressurection": "SR",
    "Spiritspeaker Warrior": "C", "Iktomisaurus Warrior": "C",
    "Spiritspeaker State": "C", "Nightspirit Graffiti": "C", "Phlogistum": "C",
    "Baby Iktomisaurus": "C", "Lauma": "SR", "Columbina": "UR", "Collei": "C",
    "Tighnari": "C", "Radiant Moonfly": "SR", "Juvenille Leshy": "C",
    "Elder Leshy": "C", "Radiant Bladehorn": "R", "Dualblaze Ibis": "C",
    "Fluffahog": "C", "Blunthorn Rhino": "C", "Fuzzbadge": "C",
    "Rimehorn Deer": "R", "Wrath of the Forest": "UR", "Moonglow Fireflly": "C",
    "Winter Icelea": "C", "Frostmoon Priest": "C", "Imprision": "R",
    "Moon Prayer": "SR", "Nastya": "C", "Pierro": "UR", "Lumi": "R",
    "Linnea": "C", "Vodyanitsa": "R", "Siren Song": "R", "Flins": "UR",
    "Hilichurl Warrior": "C", "Hilichurl Shooter": "C", "Mitachurl BlazingAxe": "C",
    "Hydro Samachurl": "R", "Ella Musk": "C", "Hilichurl Camp": "R",
    "Curse of Wilderness": "SR", "Geo Lawachurl": "C", "Pyro Slime": "C",
    "Unusual Hilichurl": "SR", "Final Rest": "R", "Churlcric": "SR",
    "Explosive Barrel": "C", "Totem": "C", "Furina": "SR",
    "Gentilhome Usher": "C", "Surintendante Chevalmarin": "C",
    "Mademoiselle Crabaletta": "C", "Hydro Tulpa": "SR", "Oceanid": "C",
    "Hydro Eidolon": "C", "Fountain of Lucine": "C", "Koholasaurus": "C",
    "Youg Koholasaurus": "C", "Qucusaurus": "C", "Geo Vishap": "C",
    "Dottore 20": "R", "Arabalika": "C", "Aranyaka": "R", "Arama": "C",
    "Ying ier": "C", "Knowladge Capsule": "C", "Debt Collector": "R",
    "Oprichnik Line Trooper": "C", "Frost Operative": "R", "Odette": "C",
    "Arlecchino": "UR", "Knight Patroller": "C", "Umbrellafinch": "C",
    "Jahoda": "C", "Anemo Sigil": "SR", "Hydro Sigil": "SR", "Pyro Sigil": "SR",
    "Electro Sigil": "SR", "Geo Sigil": "SR", "Dendro Sigil": "SR",
    "Cryo Sigil": "SR", "Elemental Ressonance": "R", "Leyline Overflow": "C",
    "Polar Star Edict Mandate": "SR", "Anastasia": "UR", "Jack Frost": "C",
    "Jack Frost Chief": "C", "Snegovik Guard": "C", "Snegurochka Cryomancer": "C",
    "Pavlina": "SR", "Snow Giant": "SR", "Vesna": "R", "Rogue Vila": "C",
    "Royal Guard Druzhna": "C", "Belyi Tsar's Wish": "SR", "Kresnik Torch": "C",
    "Eye of Graeae": "C", "Imperial March": "R", "Mistilteinn": "UR", "FrostBite": "C",
}


class CardBrowser(tk.Tk):
    CARD_WIDTH = 340
    CARD_HEIGHT = 515
    IMAGE_WIDTH = 304
    IMAGE_HEIGHT = 270
    CORNER_RADIUS = 16
    WEAPON_POWER_BONUS = 50
    WEAPON_HP_BONUS = 50
    PHASE_DRAW_COUNT = 5
    PURCHASE_AREA_LIMIT = 10
    MAX_MATCH_PHASES = 18
    BOSS_PHASE_INTERVAL = 6

    ELEMENT_COLORS = {
        "Pyro": "#ff7043",
        "Hydro": "#4da3ff",
        "Cryo": "#7bdff2",
        "Electro": "#af7ac5",
        "Dendro": "#7dcea0",
        "Anemo": "#73d6b5",
        "Geo": "#f4d03f",
        "Omni": "#ffffff",
    }

    IMAGE_FILES = {
        "Abyssal Rift": "Abyssal Rift.bmp",
        "Aether": "Aether.png",
        "Anastasia": "Anastasya.bmp",
        "Albedo": "Albedo.bmp",
        "Belyi Tsar's Wish": "Tsar's Final Wish.bmp",
        "Caribert": "Caribert.jpg",
        "Celestial Envoy": "Clestial Envoy.bmp",
        "Celestial Nail": "CelestialNail.png",
        "Chlothar": "Chlothar.webp",
        "Corrupted Blood": "Corrupted blood.webp",
        "Cryo Abyss Herald": "Cryo Abyss Herald.bmp",
        "Cryo Abyss Mage": "Cryo Abyss Mage.bmp",
        "Hydro Abyss Herald": "Hydro Abyss Herald.bmp",
        "Hydro Abyss Mage": "Hydro Abyss Mage.bmp",
        "Ursa, the Drake": "Ursa, the Drake.bmp",
        "Defiled Statue": "Defieled Statue.bmp",
        "Elemental Conversion": "Elemental Conversion.bmp",
        "Elynas": "Elynas.jpg",
        "Fake Sky": "False Sky.bmp",
        "Fischl": "Fischl.bmp",
        "FrostBite": "Frostbite.bmp",
        "Hexaiphanes Blade": "Hexaiphanes blade.png",
        "Eye of Graeae": "Eye of Graeae.bmp",
        "Imperial March": "Imperial March.bmp",
        "Istoria": "Istoria.bmp",
        "Jack Frost": "Jack Frost.bmp",
        "Jack Frost Chief": "Jack Frost Thief.bmp",
        "Klee": "Klee.bmp",
        "Kresnik Torch": "Kresnik Torch.bmp",
        "Leylines": "Ley Lines.bmp",
        "Loom of Fate": "Loom of Fate.bmp",
        "Lumine": "Lumine.bmp",
        "Mona": "Mona.bmp",
        "Mistilteinn": "Mistilteinn.bmp",
        "Nicole": "Nicole.bmp",
        "Nihilita": "Nihilita.png",
        "Paimon": "Paimon.png",
        "Pavlina": "Pavlina.bmp",
        "Prune": "Prune.bmp",
        "Purification": "Purification.bmp",
        "Pyro Seelie Guide": "Pyro Seelie.png",
        "Ruin Destroyer Serpent": "Ruin Destroyer.bmp",
        "Ruin Guard": "Ruin Guard.bmp",
        "Royal Guard Druzhna": "Druzhna.jpg",
        "Sinner's Blessing": "Sinnes's Blessing.bmp",
        "Snegovik Guard": "Snegovik Guard.bmp",
        "Snegurochka Cryomancer": "Snegurochka.jpg",
        "Snow Giant": "Snow Giant.jpg",
        "Spaceship": "Spaceship.bmp",
        "Vesna": "Vesna.jpg",
        "Rogue Vila": "Vila.bmp",
        "Tenebrous Mimiflora": "Tenebrous Mimiflora.jpg",
        "Transcending Fate": "Transcending Fate.bmp",
        "Dodoco": "Dodoco.bmp",
        "Dodocannon": "Dodocannon.bmp",
        "Dodocomunicator": "Dodocomunicator.bmp",
        "Magic Bubble": "Magic Bubble.bmp",
        "Mini Durin": "Mini-Durin.bmp",
        "Witches' Tea Party": "Witches Tea Party.bmp",
        "Witch's Homework": "Witch's Homework.png",
        "Wolfy": "Wolfy.png",
        "The Boar Princess": "The Boar Princess.png",
        "Xiao": "Xiao.png",
        "Zhongli": "Zhongli.png",
        "Cloud Retainer": "Cloud Retainer.png",
        "Xianyun": "Xianyun.png",
        "Yanfei": "Yanfei.png",
        "Bosacius": "Bosacius.png",
        "Solitary Suanni": "Solitary Suanni.png",
        "Xiangling": "Xiangling.png",
        "Guoba": "Guoba.png",
        "Guili Assembly": "Guili Assembly.png",
        "Karma": "KArma.png",
        "Guizhong Balista": "Guizhong Balista.png",
        "Zibai": "Zibai.png",
        "Freminet": "Freminet.bmp",
        "Pierro": "Pierro.bmp",
        "Odette": "odette.bmp",
        "Arlecchino": "Arlecchino.bmp",
        "Imaginarium Theather": "Imaginarium Theater.png",
        "Xuanwen Beast": "Xuawen Beast.png",
        "Seal of Permission": "Seal of Permission.png",
        "Mechaniozed Fortress": "Mechanized Fortress.bmp",
        "Pyro Storm Landcruiser": "Pyro Storm Landcruiser.bmp",
        "Aaru": "Aaru.png",
        "Aino": "Aino.png",
        "Acient Name": "Ancient Name.png",
        "Arataki Itto": "Arataki Itto.bmp",
        "A.S.I.M.O.N": "ASIMON.png",
        "Baby Iktomisaurus": "Baby Iktomisaurus.png",
        "Bake-Danuke": "Bake-Danuke.png",
        "Biram": "Biram.png",
        "Blue Oni": "Blue Oni.bmp",
        "Capitano": "Capitano.png",
        "Celestia": "Celestia.png",
        "Citlali": "Citlali.png",
        "Cyno": "Cyno.png",
        "Dehya": "Dehya.png",
        "Domain Keeper": "Domain Keeper.png",
        "Eremite": "Eremite.png",
        "Fagio": "Fagio.png",
        "Debt Collector": "Fatui Debt Collector.bmp",
        "Frost Operative": "Fatui Frost Opperative.bmp",
        "Oprichnik Line Trooper": "Fatui Oprichnik.bmp",
        "Fontaine Research Institute": "Fontaine Research Institute.png",
        "Forbidden Knowlagde": "Forbidden Knowledge.png",
        "Garde": "Gardes.png",
        "Ginkaku": "Ginkaku.bmp",
        "Golden Slumber": "Golden Slumber.png",
        "Iktomisaurus Warrior": "Iktomisaurus Warrior.png",
        "Iktomissaurus": "Iktomisaurus.png",
        "Ineffa": "Ineffa.png",
        "Ioroi": "Ioroi.png",
        "Kamen": "Kamen.png",
        "Kappa": "Kappa.bmp",
        "Kitsune Statue": "Kitsune Statue.bmp",
        "Kujou Sara": "Kujou Sara.bmp",
        "Mavuika": "Mavuika.png",
        "Mussou no Hitotachi": "Mussou no Hitotachi.png",
        "Nahida": "Nahida.png",
        "Name Fishing": "Name Fishing.png",
        "Nefer": "Nefer.png",
        "Nightkingdom": "Night Kingdom.png",
        "Nightsoul Blessing": "Nightsoul Blessing.png",
        "Nightspirit Graffiti": "Nightspirit graffiti.png",
        "Obsidian Pillar": "Obsidian Pillar.png",
        "Ode of Ressurection": "Ode of Ressuraction.png",
        "Ororon": "Ororon.png",
        "Phlogistum": "phlogistum.png",
        "Primal Construct Prospector": "Primal Constroct Prospector.png",
        "Primal Construct Repulsor": "Primal Construct Repulsor.png",
        "Pulonia": "Pulonna.png",
        "Raiden Ei": "Raiden.bmp",
        "Recon Log Mek": "Recon Log Mek.png",
        "Red Oni": "Red Oni.bmp",
        "Sandrone": "Sandrone.png",
        "Sasayuri": "Sasayuri.bmp",
        "Scrap Robots": "Scrap Robots.png",
        "Sethos": "Sethos.png",
        "Spiritspeaker State": "Spiritspeaker state.png",
        "Spiritspeaker Warrior": "Spiritspeaker Warrior.png",
        "Statue of the Seven": "Statue of the Seven.png",
        "Suppression Specialist Mek": "Supression specialist mek.png",
        "Temple of Silence": "Temple of Silence.png",
        "Tlapo": "Tlapo.png",
        "Churldric": "Churlcric.png",
        "Il Dottore Segment 20": "Il Dottore 20.png",
        "Toukabou Shigure": "Toukago Shigure.png",
        "Underwater Survey Mek": "Underwater Survey Mek.png",
        "Venti": "Venti.bmp",
        "Volture": "Volture.png",
        "World Formula": "World Formula.png",
        "Cryo Wyob Manifestation": "Wyob.png",
        "Yae Miko": "Yae Miko.bmp",
    }

    def __init__(self):
        super().__init__()
        self.title("Celestial Deck | Card Browser")
        self.geometry("1120x760")
        self.minsize(720, 520)
        self.state("zoomed")
        self.configure(bg="#10141b")

        # Caminho do arquivo JSON para persistência
        self.save_file = Path(__file__).parent / "decks_salvos.json"

        # Decks base fixos do jogo
        self.base_decks = {"deck": deck, "deck2": deck2}
        self.decks = dict(self.base_decks)
        self.base_collection_cards = list(
            {card.name: card for card in deck + deck2}.values()
        )
        self.base_collection_names = {
            card.name for card in self.base_collection_cards
        }

        # Mapeamento global de cartas por nome para reconstituição dos decks salvos
        self.card_registry = {
            card.name: card
            for d in self.base_decks.values()
            for card in d
        }
        self.card_registry.update(
            {card.name: card for card in deck2}
        )
        self.card_registry.update(
            {card_class().name: card_class() for card_class in st01_cards}
        )
        self.card_registry.update(
            {card_class().name: card_class() for card_class in st02_cards}
        )
        store_card_map = {
            card_class().name: card_class() for card_class in st01_cards
        }
        self.store_cards = list(store_card_map.values())
        self.store_available = list(self.store_cards)
        self.store_names = {card.name for card in self.store_cards}
        self.collection = []

        # Carrega os decks criados pelo usuário
        self._load_custom_decks()

        self.image_dir = Path(__file__).parent / "Imagens"
        self.menu_image_dir = Path(__file__).parent / "Imagens Menu"
        self.image_cache = {}
        self.menu_image_cache = {}
        self.menu_action_image_cache = {}
        self.play_image_cache = {}
        self.menu_action_base_image = None
        self.image_futures = {}
        self.image_executor = ThreadPoolExecutor(max_workers=4)
        self.background_frames = []
        self.background_future = None
        self.background_frames_loaded = False
        self.background_photo = None
        self.menu_backgrounds = []
        self.home_canvas = None
        self.home_background_item = None
        self.home_image_items = []
        self.play_canvas = None
        self.play_background_item = None
        self.play_image_items = []
        self.play_container = None
        self.background_frame_index = 0
        self.background_label = tk.Label(
            self, bg="#10141b", bd=0, highlightthickness=0
        )
        self.background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.background_label.lower()
        self._load_background_gif()

        self.card_view_id = 0
        self.card_data = []
        self.canvas = None
        self.deck_list_canvas = None
        self.card_image_items = {}
        self.show_collection_counts = False

        self.search_text = tk.StringVar()
        self.type_filter = tk.StringVar(value="All types")
        self.rarity_filter = tk.StringVar(value="All rarities")
        self.cost_filter = tk.StringVar(value="All costs")
        self.count_text = tk.StringVar()

        self._build_style()
        self.bind_all("<MouseWheel>", self._on_mousewheel)
        self.bind_all("<Button-4>", self._on_mousewheel)
        self.bind_all("<Button-5>", self._on_mousewheel)
        self.search_text.trace_add("write", self._refresh_cards)
        self.type_filter.trace_add("write", self._refresh_cards)
        self.rarity_filter.trace_add("write", self._refresh_cards)
        self.cost_filter.trace_add("write", self._refresh_cards)
        self._show_home()

    def _load_background_gif(self):
        background_path = self.image_dir / "BG-gif.gif"
        if not background_path.exists():
            return
        try:
            with Image.open(background_path) as gif:
                self.background_frames.append(gif.convert("RGB").copy())
        except (OSError, ValueError):
            self.background_frames.clear()
            return

        if self.background_frames:
            self.background_future = self.image_executor.submit(
                self._decode_background_frames,
                background_path,
            )
            self._animate_background()

    @staticmethod
    def _decode_background_frames(background_path):
        frames = []
        try:
            with Image.open(background_path) as gif:
                gif.seek(1)
                while True:
                    frames.append(gif.convert("RGB").copy())
                    try:
                        gif.seek(gif.tell() + 1)
                    except EOFError:
                        break
        except (OSError, ValueError, EOFError):
            return []
        return frames

    def _animate_background(self):
        if not self.background_frames or not self.winfo_exists():
            return
        if self.background_future is not None:
            if self.background_future.done() and not self.background_frames_loaded:
                try:
                    self.background_frames.extend(self.background_future.result())
                except (OSError, ValueError):
                    pass
                self.background_frames_loaded = True
        photo = self._background_photo(
            self.background_frames[self.background_frame_index]
        )
        self.background_label.configure(image=photo)
        if self.home_canvas is not None and self.home_background_item is not None:
            self.home_canvas.itemconfigure(
                self.home_background_item,
                image=photo,
            )
        active_backgrounds = []
        for label in self.menu_backgrounds:
            if label.winfo_exists():
                label.configure(image=photo)
                active_backgrounds.append(label)
        self.menu_backgrounds = active_backgrounds
        self.background_frame_index = (
            self.background_frame_index + 1
        ) % len(self.background_frames)
        self.after(100, self._animate_background)

    def _add_menu_background(self, parent):
        label = tk.Label(parent, bg="#10141b", bd=0, highlightthickness=0)
        label.place(relx=0, rely=0, relwidth=1, relheight=1)
        label.lower()
        if self.background_photo is not None:
            label.configure(image=self.background_photo)
        self.menu_backgrounds.append(label)
        return label

    def _background_photo(self, frame):
        width = max(self.winfo_width(), 1)
        height = max(self.winfo_height(), 1)
        target_width = width + 20
        target_height = height + 20
        fitted = ImageOps.fit(
            frame,
            (target_width, target_height),
            method=Image.Resampling.LANCZOS,
        )
        left = (target_width - width) // 2
        top = (target_height - height) // 2
        fitted = fitted.crop((left, top, left + width, top + height))
        self.background_photo = ImageTk.PhotoImage(fitted)
        return self.background_photo

    # --- PERSISTÊNCIA DE DADOS ---
    def _save_custom_decks(self):
        """Salva apenas os decks personalizados criados pelo usuário em arquivo JSON."""
        custom_decks = {}
        for deck_name, cards in self.decks.items():
            if deck_name not in self.base_decks:
                # Salva uma lista contendo o nome de cada carta no deck
                custom_decks[deck_name] = [card.name for card in cards]
        custom_decks["_collection"] = self.collection

        try:
            with open(self.save_file, "w", encoding="utf-8") as f:
                json.dump(custom_decks, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Erro ao salvar decks: {e}")

    def _load_custom_decks(self):
        """Lê o arquivo JSON e reconstrói os objetos de carta dos decks salvos."""
        if not self.save_file.exists():
            return

        try:
            with open(self.save_file, "r", encoding="utf-8") as f:
                saved_data = json.load(f)

            saved_collection = saved_data.get("_collection", [])
            self.collection = [
                name
                for name in saved_collection
                if name in self.card_registry
            ]
            for deck_name, card_names in saved_data.items():
                if deck_name in {"_collection", "_store_available", "deck2"}:
                    continue
                if deck_name not in self.base_decks:
                    reconstructed_deck = []
                    for name in card_names:
                        if name in self.card_registry:
                            reconstructed_deck.append(self.card_registry[name])
                    self.decks[deck_name] = reconstructed_deck
        except (IOError, json.JSONDecodeError) as e:
            print(f"Erro ao carregar decks salvos: {e}")

    # --- GERENCIAMENTO DE DECKS ---
    def _delete_custom_deck(self, deck_name):
        if deck_name in self.decks and deck_name not in self.base_decks:
            del self.decks[deck_name]
            self._save_custom_decks()  # Atualiza o arquivo ao deletar
        self._show_decks()

    def _create_builder_deck(self):
        if not self.builder_cards:
            self.builder_status.set(
                "Adicione pelo menos uma carta antes de criar o deck."
            )
            return
        deck_name = self.builder_name.get().strip() or "Meu Deck"
        if deck_name.lower() in {
            k.lower() for k in self.base_decks.keys()
        }:
            self.builder_status.set("Esse nome pertence a um deck pré-criado.")
            return

        created_deck = []
        for card, amount in self.builder_cards.items():
            created_deck.extend([card] * amount)

        self.decks[deck_name] = created_deck
        self._save_custom_decks()  # Salva em disco imediatamente
        self._open_deck(deck_name)

    # --- CANVAS E UI ---
    def _draw_rounded_rectangle(self, x1, y1, x2, y2, radius=10, **kwargs):
        points = [
            x1 + radius,
            y1,
            x2 - radius,
            y1,
            x2,
            y1,
            x2,
            y1 + radius,
            x2,
            y2 - radius,
            x2,
            y2,
            x2 - radius,
            y2,
            x1 + radius,
            y2,
            x1,
            y2,
            x1,
            y2 - radius,
            x1,
            y1 + radius,
            x1,
            y1,
        ]
        return self.canvas.create_polygon(points, smooth=True, **kwargs)

    def _clear_screen(self):
        self._hide_match_card_preview()
        self.card_view_id += 1
        self.image_futures.clear()
        self.card_image_items.clear()
        self.home_canvas = None
        self.home_background_item = None
        self.home_image_items = []
        self.play_canvas = None
        self.play_background_item = None
        self.play_image_items = []
        self.play_container = None
        self.deck_list_canvas = None
        for child in self.winfo_children():
            if child is self.background_label:
                continue
            child.destroy()
        self.canvas = None

    def _show_home(self):
        self._clear_screen()
        page = ttk.Frame(self, style="App.TFrame", padding=0)
        page.pack(fill="both", expand=True)
        self.home_canvas = tk.Canvas(
            page,
            bg="#10141b",
            bd=0,
            highlightthickness=0,
        )
        self.home_canvas.pack(fill="both", expand=True)
        self.home_canvas.bind("<Configure>", self._position_home_images)
        if self.background_photo is not None:
            self.home_background_item = self.home_canvas.create_image(
                0,
                0,
                image=self.background_photo,
                anchor="nw",
            )

        logo = self._load_menu_image("Logo.png")
        if logo is not None:
            logo_item = self.home_canvas.create_image(
                0,
                0,
                image=logo,
                anchor="n",
                tags=("menu_logo",),
            )
            self.home_image_items.append((logo_item, logo, None))

        for filename, command in (
            ("Botão Jogar.png", self._show_play),
            ("Botão Decks.png", self._show_decks),
            ("Botão Opções.png", self._show_options),
        ):
            image = self._load_menu_image(filename)
            if image is None:
                continue
            item = self.home_canvas.create_image(
                0,
                0,
                image=image,
                anchor="n",
                tags=("menu_button",),
            )
            self.home_canvas.tag_bind(
                item,
                "<Button-1>",
                lambda event, callback=command: callback(),
            )
            self.home_canvas.tag_bind(
                item,
                "<Enter>",
                lambda event: self.home_canvas.configure(cursor="hand2"),
            )
            self.home_canvas.tag_bind(
                item,
                "<Leave>",
                lambda event: self.home_canvas.configure(cursor=""),
            )
            self.home_image_items.append((item, image, None))
        self._position_home_images()

    def _position_home_images(self, event=None):
        if self.home_canvas is None or not self.home_image_items:
            return
        canvas_width = self.home_canvas.winfo_width()
        canvas_height = self.home_canvas.winfo_height()
        if canvas_width <= 1 or canvas_height <= 1:
            return

        total_height = sum(image.height() for _, image, _ in self.home_image_items)
        total_height += 28 + 5 * (len(self.home_image_items) - 1)
        current_y = max((canvas_height - total_height) // 2, 10)
        center_x = canvas_width // 2
        for index, (item, image, _) in enumerate(self.home_image_items):
            self.home_canvas.coords(item, center_x, current_y)
            current_y += image.height()
            if index == 0:
                current_y += 28
            else:
                current_y += 5

    def _load_menu_image(self, filename):
        if filename in self.menu_image_cache:
            return self.menu_image_cache[filename]
        image_path = self.menu_image_dir / filename
        if not image_path.exists():
            return None
        try:
            with Image.open(image_path) as image:
                resized_image = image.convert("RGBA")
                for point in (
                    (0, 0),
                    (resized_image.width - 1, 0),
                    (0, resized_image.height - 1),
                    (resized_image.width - 1, resized_image.height - 1),
                ):
                    ImageDraw.floodfill(
                        resized_image,
                        point,
                        (0, 0, 0, 0),
                        thresh=16,
                    )
                max_size = (360, 220) if filename == "Logo.png" else (300, 100)
                resized_image.thumbnail(max_size, Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(resized_image)
        except (OSError, ValueError):
            return None
        self.menu_image_cache[filename] = photo
        return photo

    def _menu_button(self, parent, image_filename, command, row):
        image = self._load_menu_image(image_filename)
        button = tk.Button(
            parent,
            image=image,
            command=command,
            bg="#10141b",
            activebackground="#354254",
            relief="flat",
            bd=0,
            highlightthickness=0,
            cursor="hand2",
        )
        button.image = image
        button.grid(row=row, column=0, pady=5)

    def _show_decks(self):
        self._clear_screen()
        page = ttk.Frame(self, style="App.TFrame", padding=0)
        page.pack(fill="both", expand=True)
        self._add_menu_background(page)
        tk.Button(page, text="<  VOLTAR", command=self._show_home).pack(
            anchor="w"
        )
        ttk.Label(page, text="DECKS", style="Title.TLabel").pack(
            anchor="w", pady=(36, 4)
        )
        ttk.Label(
            page,
            text="Escolha um deck para consultar suas cartas",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(0, 30))

        action_menu = tk.Frame(page, bg="#10141b")
        action_menu.pack(anchor="w", pady=(0, 12))
        self._deck_action_button(
            action_menu, "CRIAR DECK", self._show_deck_builder, 0
        )
        self._deck_action_button(
            action_menu, "TODAS AS CARTAS", self._open_all_cards, 1
        )
        self._deck_action_button(action_menu, "LOJA", self._show_store, 2)

        deck_list = tk.Frame(page, bg="#10141b")
        deck_list.pack(fill="both", expand=True)
        self.deck_list_canvas = tk.Canvas(
            deck_list,
            bg="#10141b",
            highlightthickness=0,
        )
        scrollbar = ttk.Scrollbar(
            deck_list,
            orient="vertical",
            command=self.deck_list_canvas.yview,
        )
        self.deck_list_canvas.configure(yscrollcommand=scrollbar.set)
        self.deck_list_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        deck_rows = tk.Frame(self.deck_list_canvas, bg="#10141b")
        deck_rows_window = self.deck_list_canvas.create_window(
            (0, 0),
            window=deck_rows,
            anchor="nw",
        )
        deck_rows.bind(
            "<Configure>",
            lambda event: self.deck_list_canvas.configure(
                scrollregion=self.deck_list_canvas.bbox("all")
            ),
        )
        self.deck_list_canvas.bind(
            "<Configure>",
            lambda event: self.deck_list_canvas.itemconfigure(
                deck_rows_window, width=event.width
            ),
        )

        for name, current_deck in self.decks.items():
            deck_row = tk.Frame(deck_rows, bg="#10141b")
            deck_row.pack(anchor="w", pady=5)
            tk.Button(
                deck_row,
                text=f"{name.upper()}    {len(current_deck)} cartas",
                command=lambda selected=name: self._open_deck(selected),
                width=30,
                anchor="w",
                bg="#10141b",
                fg="#f5f1e8",
                activebackground="#354254",
                activeforeground="#ffffff",
                relief="flat",
                bd=0,
                padx=18,
                pady=14,
                font=("Segoe UI", 12, "bold"),
                cursor="hand2",
            ).pack(side="left")

            if name not in self.base_decks:
                tk.Button(
                    deck_row,
                    text="EXCLUIR",
                    command=lambda selected=name: self._delete_custom_deck(
                        selected
                    ),
                ).pack(side="left", padx=(8, 0), ipady=11)

    def _deck_action_button(self, parent, text, command, row):
        image = self._load_menu_action_image(text)
        button = tk.Button(
            parent,
            image=image,
            command=command,
            bg="#10141b",
            activebackground="#10141b",
            relief="flat",
            bd=0,
            highlightthickness=0,
            cursor="hand2",
        )
        button.image = image
        button.grid(row=row, column=0, pady=5)

    def _load_menu_action_image(self, text):
        if text in self.menu_action_image_cache:
            return self.menu_action_image_cache[text]
        image_path = self.menu_image_dir / "Botão Jogar.png"
        try:
            if self.menu_action_base_image is None:
                with Image.open(image_path) as image:
                    self.menu_action_base_image = image.convert("RGBA")
                for point in (
                    (0, 0),
                    (self.menu_action_base_image.width - 1, 0),
                    (0, self.menu_action_base_image.height - 1),
                    (
                        self.menu_action_base_image.width - 1,
                        self.menu_action_base_image.height - 1,
                    ),
                ):
                    ImageDraw.floodfill(
                        self.menu_action_base_image,
                        point,
                        (0, 0, 0, 0),
                        thresh=16,
                    )
            styled_image = self.menu_action_base_image.copy()
            draw = ImageDraw.Draw(styled_image)
            draw.rectangle((650, 180, 1520, 545), fill="#06265c")
            font_size = 170
            font_path = "C:/Windows/Fonts/arialbd.ttf"
            while font_size > 70:
                font = ImageFont.truetype(font_path, font_size)
                if draw.textbbox((0, 0), text, font=font)[2] <= 800:
                    break
                font_size -= 10
            draw.text(
                (1085, 365),
                text,
                font=font,
                anchor="mm",
                fill="#f5cf70",
                stroke_width=5,
                stroke_fill="#4d260d",
            )
            styled_image.thumbnail((300, 100), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(styled_image)
        except (OSError, ValueError):
            return None
        self.menu_action_image_cache[text] = photo
        return photo

    def _show_store(self, purchased_cards=None):
        self._clear_screen()
        page = ttk.Frame(self, style="App.TFrame", padding=0)
        page.pack(fill="both", expand=True)
        self._add_menu_background(page)
        tk.Button(page, text="<  DECKS", command=self._show_decks).pack(
            anchor="w"
        )
        ttk.Label(page, text="LOJA", style="Title.TLabel").pack(
            anchor="w", pady=(36, 8)
        )
        ttk.Label(
            page,
            text="Compre cartas para adicionar à sua coleção",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(0, 22))

        collection_counts = Counter(self.collection)
        available_cards = [
            (card, 3 - collection_counts[card.name])
            for card in self.store_available
        ]

        store_button = tk.Button(
            page,
            text="",
            command=self._buy_random_card,
            image=self._get_store_image(),
            width=240,
            height=320,
            anchor="center",
            justify="center",
            bg="#ADD8E6",
            fg="#f5f1e8",
            activebackground="#9ac8d6",
            activeforeground="#ffffff",
            relief="ridge",
            overrelief="groove",
            bd=6,
            highlightthickness=4,
            highlightbackground="#78aebb",
            highlightcolor="#e6f7fb",
            padx=0,
            pady=10,
            font=("Segoe UI", 13, "bold"),
            cursor="hand2",
        )
        store_button.pack(anchor="center", pady=(20, 0))

        reset_button = tk.Button(
            page,
            text="RESETAR LOJA",
            command=self._reset_store,
            width=28,
            bg="#354254",
            fg="#ffffff",
            activebackground="#4a5c73",
            activeforeground="#ffffff",
            relief="flat",
            bd=0,
            padx=18,
            pady=9,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
        )
        reset_button.pack(anchor="center", pady=(10, 0))

        if purchased_cards is not None:
            self._show_purchased_cards(purchased_cards)
            return

        list_frame = tk.Frame(page, bg="#10141b")
        list_frame.pack(fill="both", expand=True, pady=(24, 0))
        tk.Label(
            list_frame,
            text="CARTAS DA COLEÇÃO",
            bg="#10141b",
            fg="#b9c4d0",
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", pady=(0, 8))
        remaining_list = tk.Listbox(
            list_frame,
            bg="#10141b",
            fg="#f5f1e8",
            selectbackground="#354254",
            selectforeground="#ffffff",
            highlightthickness=0,
            relief="flat",
            bd=0,
            font=("Segoe UI", 11),
            height=8,
        )
        remaining_scroll = ttk.Scrollbar(
            list_frame, orient="vertical", command=remaining_list.yview
        )
        remaining_list.configure(yscrollcommand=remaining_scroll.set)
        remaining_list.pack(side="left", fill="both", expand=True)
        remaining_scroll.pack(side="right", fill="y")
        for card, remaining in available_cards:
            remaining_list.insert(
                "end", f"{card.name}    ({remaining}/3 disponíveis)"
            )

        if not available_cards:
            remaining_list.insert("end", "Nenhuma carta disponível")

    def _show_purchased_cards(self, cards):
        self._clear_screen()
        self.show_collection_counts = False
        page = ttk.Frame(self, style="App.TFrame", padding=0)
        page.pack(fill="both", expand=True)
        self._add_menu_background(page)
        tk.Button(page, text="<  LOJA", command=self._show_store).pack(
            anchor="w"
        )
        ttk.Label(page, text="VOCÊ RECEBEU", style="Title.TLabel").pack(
            anchor="center", pady=(18, 2)
        )
        ttk.Label(
            page,
            text=f"{len(cards)} cartas foram adicionadas à coleção",
            style="Subtitle.TLabel",
        ).pack(anchor="center", pady=(0, 12))

        card_area = ttk.Frame(page, style="App.TFrame")
        card_area.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(card_area, bg="#10141b", highlightthickness=0)
        scrollbar = ttk.Scrollbar(
            card_area, orient="vertical", command=self.canvas.yview
        )
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.canvas.bind(
            "<Configure>",
            lambda event: self._refresh_purchased_cards(cards),
        )
        self.card_data = list(cards)
        self.search_text.set("")
        self.type_filter.set("All types")
        self.after_idle(lambda: self._refresh_purchased_cards(cards))
        page.after(3000, self._show_store)

    def _refresh_purchased_cards(self, cards):
        if not self.canvas or not self.canvas.winfo_exists():
            return
        canvas_width = max(self.canvas.winfo_width(), self.CARD_WIDTH)
        pad_x = 16
        pad_y = 16
        cols = max(1, (canvas_width - pad_x) // (self.CARD_WIDTH + pad_x))
        total_grid_width = cols * self.CARD_WIDTH + (cols - 1) * pad_x
        start_x = max(pad_x, (canvas_width - total_grid_width) // 2)
        self.card_view_id += 1
        self.card_image_items.clear()
        self.canvas.delete("all")
        for index, card in enumerate(cards):
            col = index % cols
            row = index // cols
            x = start_x + col * (self.CARD_WIDTH + pad_x)
            y = pad_y + row * (self.CARD_HEIGHT + pad_y)
            self._draw_card_on_canvas(
                card, x, y, self.CARD_WIDTH, self.CARD_HEIGHT
            )
        total_rows = (len(cards) + cols - 1) // cols
        total_height = total_rows * (self.CARD_HEIGHT + pad_y) + pad_y
        self.canvas.configure(scrollregion=(0, 0, canvas_width, total_height))

    def _buy_random_card(self):
        collection_counts = Counter(self.collection)
        available_cards = [
            card
            for card in self.store_available
            if collection_counts[card.name] < 3
        ]
        if not available_cards:
            return

        purchased_cards = []
        available_by_rarity = {}
        for card in available_cards:
            rarity = self._card_rarity(card)
            available_by_rarity.setdefault(rarity, []).append(card)

        target_counts = {
            "UR": random.randint(0, 1),
            "SR": random.randint(1, 2),
            "R": random.randint(2, 3),
        }
        for rarity, target in target_counts.items():
            cards = available_by_rarity.get(rarity, [])
            random.shuffle(cards)
            purchased_cards.extend(cards[:target])
            del cards[:target]

        remaining_cards = [
            card
            for cards in available_by_rarity.values()
            for card in cards
            if card not in purchased_cards
        ]
        random.shuffle(remaining_cards)
        remaining_cards.sort(
            key=lambda card: 0 if self._card_rarity(card) == "C" else 1
        )
        package_size = min(10, len(available_cards))
        purchased_cards.extend(
            remaining_cards[: package_size - len(purchased_cards)]
        )

        for purchased_card in purchased_cards:
            self.collection.append(purchased_card.name)

        collection_counts.update(card.name for card in purchased_cards)
        self.store_available = [
            card
            for card in self.store_available
            if collection_counts[card.name] < 3
        ]
        self._save_custom_decks()
        self._show_store(purchased_cards)

    def _get_store_image(self):
        image_path = self.image_dir / "ST01.jpg"
        if not image_path.exists():
            return None
        try:
            image = Image.open(image_path).convert("RGB")
            image = ImageOps.fit(
                image, (240, 320), method=Image.Resampling.LANCZOS
            )
            self.store_button_image = ImageTk.PhotoImage(image)
            return self.store_button_image
        except (OSError, ValueError):
            return None

    def _reset_store(self):
        self.collection = [
            name for name in self.collection if name not in self.store_names
        ]
        self.store_available = list(self.store_cards)
        random.shuffle(self.store_available)
        self._save_custom_decks()
        self._show_store()

    def _show_deck_builder(self, deck_name=None):
        self._clear_screen()
        self.builder_cards = {}
        if deck_name in self.decks:
            cards_by_name = {}
            for card in self.decks[deck_name]:
                cards_by_name[card.name] = cards_by_name.get(card.name, 0) + 1
            self.builder_cards = {
                self.card_registry[name]: amount
                for name, amount in cards_by_name.items()
                if name in self.card_registry
            }
        self.builder_buttons = {}
        self.builder_status = tk.StringVar(
            value="Escolha cartas para montar seu deck."
        )

        page = ttk.Frame(self, style="App.TFrame", padding=0)
        page.pack(fill="both", expand=True)
        self._add_menu_background(page)
        tk.Button(page, text="<  DECKS", command=self._show_decks).pack(
            anchor="w"
        )
        ttk.Label(page, text="CRIADOR DE DECK", style="Title.TLabel").pack(
            anchor="w", pady=(22, 3)
        )
        ttk.Label(
            page,
            text="Máximo de 3 elementos diferentes. Omni não conta para o limite.",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(0, 14))

        content = tk.Frame(page, bg="#10141b")
        content.pack(fill="both", expand=True)

        catalog = tk.Frame(content, bg="#181e28", padx=14, pady=14)
        catalog.pack(side="left", fill="both", expand=True, padx=(0, 8))
        ttk.Label(
            catalog, text="CARTAS DISPONÍVEIS", style="Toolbar.TLabel"
        ).pack(anchor="w", pady=(0, 8))

        catalog_toolbar = tk.Frame(catalog, bg="#181e28")
        catalog_toolbar.pack(fill="x", pady=(0, 8))
        self.builder_search = tk.StringVar()
        self.builder_search.trace_add(
            "write", lambda *_: self._refresh_builder_catalog()
        )
        ttk.Entry(
            catalog_toolbar,
            textvariable=self.builder_search,
            style="Search.TEntry",
            width=24,
        ).pack(side="left", ipady=4, padx=(0, 8))
        self.builder_type = tk.StringVar(value="All types")
        ttk.Combobox(
            catalog_toolbar,
            textvariable=self.builder_type,
            values=["All types"] + sorted(
                {card.type for card in self._all_cards()}
            ),
            state="readonly",
            style="Filter.TCombobox",
            width=13,
        ).pack(side="left", padx=(0, 8))
        self.builder_tag = tk.StringVar(value="All tags")
        ttk.Combobox(
            catalog_toolbar,
            textvariable=self.builder_tag,
            values=["All tags"] + self._available_tags(),
            state="readonly",
            style="Filter.TCombobox",
            width=18,
        ).pack(side="left")
        self.builder_cost = tk.StringVar(value="All costs")
        ttk.Combobox(
            catalog_toolbar,
            textvariable=self.builder_cost,
            values=["All costs"] + [
                str(cost)
                for cost in sorted({card.cost for card in self._all_cards()})
            ],
            state="readonly",
            style="Filter.TCombobox",
            width=10,
        ).pack(side="left", padx=(8, 0))
        self.builder_type.trace_add(
            "write", lambda *_: self._refresh_builder_catalog()
        )
        self.builder_tag.trace_add(
            "write", lambda *_: self._refresh_builder_catalog()
        )
        self.builder_cost.trace_add(
            "write", lambda *_: self._refresh_builder_catalog()
        )

        catalog_canvas = tk.Canvas(catalog, bg="#181e28", highlightthickness=0)
        catalog_scroll = ttk.Scrollbar(
            catalog, orient="vertical", command=catalog_canvas.yview
        )
        catalog_canvas.configure(yscrollcommand=catalog_scroll.set)
        catalog_canvas.pack(side="left", fill="both", expand=True)
        catalog_scroll.pack(side="right", fill="y")
        self.canvas = catalog_canvas
        self.card_image_items = {}
        self.card_data = self._all_cards()
        self.builder_card_regions = []
        catalog_canvas.bind(
            "<Configure>", lambda _: self._refresh_builder_catalog()
        )
        catalog_canvas.bind("<Button-1>", self._on_builder_card_click)

        summary = tk.Frame(content, bg="#10141b", padx=16, pady=14, width=310)
        summary.pack(side="right", fill="y")
        summary.pack_propagate(False)

        ttk.Label(summary, text="SEU DECK", style="Toolbar.TLabel").pack(
            anchor="w"
        )
        ttk.Label(summary, text="NOME DO DECK", style="Toolbar.TLabel").pack(
            anchor="w", pady=(12, 5)
        )
        self.builder_name = tk.StringVar(value=deck_name or "Meu Deck")
        tk.Entry(summary, textvariable=self.builder_name, width=28).pack(
            fill="x", ipady=5
        )
        tk.Button(
            summary, text="CRIAR DECK", command=self._create_builder_deck
        ).pack(fill="x", pady=(10, 12))

        info_canvas = tk.Canvas(summary, bg="#10141b", highlightthickness=0)
        info_scroll = ttk.Scrollbar(
            summary, orient="vertical", command=info_canvas.yview
        )
        info_inner = tk.Frame(info_canvas, bg="#10141b")
        info_window = info_canvas.create_window(
            (0, 0), window=info_inner, anchor="nw"
        )

        info_canvas.configure(yscrollcommand=info_scroll.set)
        info_canvas.pack(side="left", fill="both", expand=True)
        info_scroll.pack(side="right", fill="y")

        info_inner.bind(
            "<Configure>",
            lambda _: info_canvas.configure(
                scrollregion=info_canvas.bbox("all")
            ),
        )
        info_canvas.bind(
            "<Configure>",
            lambda e: info_canvas.itemconfigure(info_window, width=e.width),
        )

        self.builder_summary = tk.Label(
            info_inner,
            text="",
            bg="#10141b",
            fg="#cbd3dc",
            font=("Consolas", 10),
            justify="left",
            anchor="nw",
        )
        self.builder_summary.pack(fill="x", pady=(12, 18))

        self.builder_selected_frame = tk.Frame(info_inner, bg="#10141b")
        self.builder_selected_frame.pack(fill="x", pady=(0, 12))

        ttk.Label(
            summary,
            textvariable=self.builder_status,
            style="Subtitle.TLabel",
            wraplength=275,
        ).pack(anchor="w")
        ttk.Label(
            summary,
            text="Clique em uma carta para adicionar cópias. O limite acompanha sua coleção.",
            style="Subtitle.TLabel",
            wraplength=275,
        ).pack(anchor="w", side="bottom")

        self._refresh_builder_catalog()
        self._refresh_builder()

    def _available_tags(self):
        tags = set()
        for card in self._all_cards():
            card_tags = card.tag if isinstance(card.tag, tuple) else (card.tag,)
            tags.update(tag for tag in card_tags if tag)
        return sorted(tags, key=str.lower)

    def _refresh_builder_catalog(self):
        if not hasattr(self, "canvas") or not self.canvas:
            return
        if not self.canvas.winfo_exists():
            return

        query = self.builder_search.get().strip().lower()
        selected_type = self.builder_type.get()
        selected_tag = self.builder_tag.get()
        selected_cost = self.builder_cost.get()
        visible_cards = [
            card
            for card in self._all_cards()
            if (
                not query
                or query in card.name.lower()
                or query in getattr(card, "element", "").lower()
            )
            and (selected_type == "All types" or card.type == selected_type)
            and (
                selected_tag == "All tags"
                or selected_tag
                in (
                    card.tag
                    if isinstance(card.tag, tuple)
                    else (card.tag,)
                )
            )
            and (
                selected_cost == "All costs"
                or card.cost == int(selected_cost)
            )
        ]

        self.card_view_id += 1
        self.card_image_items.clear()
        self.canvas.delete("all")
        self.builder_card_regions = []

        canvas_width = max(self.canvas.winfo_width(), self.CARD_WIDTH)
        pad_x = 16
        pad_y = 16
        cols = max(1, (canvas_width - pad_x) // (self.CARD_WIDTH + pad_x))
        total_grid_width = cols * self.CARD_WIDTH + (cols - 1) * pad_x
        start_x = max(pad_x, (canvas_width - total_grid_width) // 2)

        for index, card in enumerate(visible_cards):
            col = index % cols
            row = index // cols
            x = start_x + col * (self.CARD_WIDTH + pad_x)
            y = pad_y + row * (self.CARD_HEIGHT + pad_y)
            self._draw_card_on_canvas(
                card, x, y, self.CARD_WIDTH, self.CARD_HEIGHT
            )
            self.builder_card_regions.append(
                (x, y, x + self.CARD_WIDTH, y + self.CARD_HEIGHT, card)
            )
            amount = self.builder_cards.get(card, 0)
            limit = self._card_copy_limit(card)
            self.canvas.create_oval(
                x + 12, y + self.CARD_HEIGHT - 42,
                x + 72, y + self.CARD_HEIGHT - 12,
                fill="#354254", outline="#f5f1e8", width=1
            )
            self.canvas.create_text(
                x + 42, y + self.CARD_HEIGHT - 27,
                text=f"{amount}/{limit}", fill="#ffffff",
                font=("Segoe UI", 9, "bold")
            )

        total_rows = (len(visible_cards) + cols - 1) // cols
        total_height = total_rows * (self.CARD_HEIGHT + pad_y) + pad_y
        self.canvas.configure(scrollregion=(0, 0, canvas_width, total_height))

    def _on_builder_card_click(self, event):
        click_x = self.canvas.canvasx(event.x)
        click_y = self.canvas.canvasy(event.y)
        for x1, y1, x2, y2, card in self.builder_card_regions:
            if x1 <= click_x <= x2 and y1 <= click_y <= y2:
                self._toggle_builder_card(card)
                self._refresh_builder_catalog()
                return

    def _unique_cards(self):
        return list(self.card_registry.values())

    def _all_cards(self):
        collection_counts = Counter(self.collection)
        cards = {card.name: card for card in self.base_collection_cards}
        cards.update(
            {
                card.name: card
                for card in self.store_cards
                if collection_counts[card.name] > 0
            }
        )
        return list(cards.values())

    def _card_copy_limit(self, card):
        if card.name in self.store_names:
            return min(self.collection.count(card.name), 3)
        return 3

    def _card_rarity(self, card):
        return CARD_RARITIES.get(card.name, getattr(card, "r", "C"))

    def _toggle_builder_card(self, card):
        selected_elements = {
            item.element
            for item in self.builder_cards
            if item.element != "Omni"
        }
        if (
            card not in self.builder_cards
            and card.element != "Omni"
            and card.element not in selected_elements
            and len(selected_elements) >= 3
        ):
            self.builder_status.set(
                f"Limite atingido: {card.element} seria o 4º elemento."
            )
            return
        amount = self.builder_cards.get(card, 0)
        copy_limit = self._card_copy_limit(card)
        if amount >= copy_limit:
            self.builder_status.set(
                f"Limite atingido: você possui {copy_limit} cópia(s) de {card.name}."
            )
            return
        self.builder_cards[card] = amount + 1
        self.builder_status.set(
            f"{card.name}: {amount + 1}/{copy_limit} cópias."
        )
        self._refresh_builder()

    def _refresh_builder(self):
        types, costs, elements = {}, {}, {}
        for card, amount in self.builder_cards.items():
            types[card.type] = types.get(card.type, 0) + amount
            costs[card.cost] = costs.get(card.cost, 0) + amount
            elements[card.element] = elements.get(card.element, 0) + amount

        for card, button in self.builder_buttons.items():
            copy_limit = self._card_copy_limit(card)
            button.configure(
                text=f"{card.name}  [{card.element}]  ({self.builder_cards.get(card, 0)}/{copy_limit})"
            )

        for child in self.builder_selected_frame.winfo_children():
            child.destroy()

        for card, amount in self.builder_cards.items():
            row = tk.Frame(self.builder_selected_frame, bg="#10141b")
            row.pack(fill="x", pady=2)
            ttk.Label(
                row, text=f"{card.name} x{amount}", style="Subtitle.TLabel"
            ).pack(side="left", fill="x", expand=True)
            tk.Button(
                row,
                text="REMOVER",
                command=lambda selected=card: self._remove_builder_card(
                    selected
                ),
            ).pack(side="right")

        lines = [f"TOTAL: {sum(self.builder_cards.values())}", "", "TYPES"]
        lines.extend(
            f"{name}: {count}" for name, count in sorted(types.items())
        )
        lines.append("\nCUSTOS")
        lines.extend(
            f"Custo {cost}: {count}" for cost, count in sorted(costs.items())
        )
        lines.append("\nELEMENTOS")
        lines.extend(
            f"{name}: {count}" for name, count in sorted(elements.items())
        )
        self.builder_summary.configure(text="\n".join(lines))

    def _remove_builder_card(self, card):
        if card not in self.builder_cards:
            return
        if self.builder_cards[card] == 1:
            del self.builder_cards[card]
        else:
            self.builder_cards[card] -= 1
        self.builder_status.set(
            f"{card.name}: {self.builder_cards.get(card, 0)}/{self._card_copy_limit(card)} cópias."
        )
        self._refresh_builder()

    def _open_all_cards(self):
        self._clear_screen()
        self.show_collection_counts = True
        self.card_data = sorted(
            self._all_cards(),
            key=lambda card: (card.cost, card.name.lower()),
        )
        self.search_text.set("")
        self.type_filter.set("All types")
        self.rarity_filter.set("All rarities")
        self.cost_filter.set("All costs")

        self._build_header("Todas as cartas")
        self._build_card_area()
        self._refresh_cards()

    def _show_play(self):
        self._clear_screen()
        page = ttk.Frame(self, style="App.TFrame", padding=0)
        page.pack(fill="both", expand=True)
        self._add_menu_background(page)
        tk.Button(
            page,
            text="<  MENU INICIAL",
            command=self._show_home,
            bg="#10141b",
            fg="#f5f1e8",
            activebackground="#354254",
            activeforeground="#ffffff",
            relief="flat",
            bd=0,
            padx=16,
            pady=10,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
        ).place(x=24, y=18)
        self.play_container = page
        page.bind("<Configure>", self._position_play_images)

        modes = [
            ("Mondstadt", "Mondstadt.png"),
            ("Liyue", "Liyue.png"),
            ("Inazuma", "Inazuma.png"),
            ("Sumeru", "Sumeru.png"),
            ("Fontaine", "FontaineSem título.png"),
            ("Natlan", "Natlan.png"),
            ("Snezhnaya", "Snezhnaya.png"),
        ]

        for mode_number, (mode_name, image_filename) in enumerate(modes, start=1):
            mode_image = self._load_play_image(image_filename)
            if mode_image is None:
                continue
            item = tk.Label(
                page,
                image=mode_image,
                bg="#10141b",
                bd=0,
                highlightthickness=0,
                cursor="hand2",
            )
            item.image = mode_image
            item.bind(
                "<Button-1>",
                lambda event, number=mode_number, name=mode_name: self._show_deck_selection(
                    number, name
                ),
            )
            self.play_image_items.append((item, mode_image))
        self._position_play_images()

    def _position_play_images(self, event=None):
        if self.play_container is None or not self.play_image_items:
            return
        canvas_width = self.play_container.winfo_width()
        canvas_height = self.play_container.winfo_height()
        if canvas_width <= 1 or canvas_height <= 1:
            return

        gap = 6
        image_width = self.play_image_items[0][1].width()
        total_width = image_width * len(self.play_image_items)
        total_width += gap * (len(self.play_image_items) - 1)
        start_x = max((canvas_width - total_width) // 2, 0)
        image_height = self.play_image_items[0][1].height()
        start_y = max((canvas_height - image_height) // 2, 0)
        for index, (item, _) in enumerate(self.play_image_items):
            item.place(
                x=start_x + index * (image_width + gap),
                y=start_y,
                width=image_width,
                height=image_height,
            )

    def _load_play_image(self, filename):
        if filename in self.play_image_cache:
            return self.play_image_cache[filename]
        image_path = Path(__file__).parent / "Botões jogar" / filename
        if not image_path.exists():
            return None
        try:
            with Image.open(image_path) as image:
                play_image = image.convert("RGBA")
                play_image = ImageOps.fit(
                    play_image,
                    (150, 520),
                    method=Image.Resampling.LANCZOS,
                )
                photo = ImageTk.PhotoImage(play_image)
        except (OSError, ValueError):
            return None
        self.play_image_cache[filename] = photo
        return photo

    def _show_deck_selection(self, mode_number, mode_name):
        self._clear_screen()
        page = ttk.Frame(self, style="App.TFrame", padding=0)
        page.pack(fill="both", expand=True)
        self._add_menu_background(page)

        tk.Button(page, text="<  VOLTAR", command=self._show_play).pack(
            anchor="w"
        )
        ttk.Label(page, text="ESCOLHA SEU DECK", style="Title.TLabel").pack(
            anchor="center", pady=(28, 4)
        )
        ttk.Label(
            page,
            text=f"Escolha um deck para jogar em {mode_name}",
            style="Subtitle.TLabel",
        ).pack(anchor="center", pady=(0, 24))

        deck_menu = tk.Frame(page, bg="#10141b")
        deck_menu.pack(anchor="center")
        for deck_name, cards in self.decks.items():
            deck_button = tk.Button(
                deck_menu,
                text=f"{deck_name.upper()}    ({len(cards)} cartas)",
                command=lambda selected=deck_name: self._select_play_deck(
                    mode_number, mode_name, selected
                ),
                width=32,
                bg="#10141b",
                fg="#f5f1e8",
                activebackground="#354254",
                activeforeground="#ffffff",
                relief="flat",
                bd=0,
                padx=18,
                pady=10,
                font=("Segoe UI", 11, "bold"),
                cursor="hand2",
            )
            deck_button.pack(pady=4)

    def _select_play_deck(self, mode_number, mode_name, deck_name):
        selected_cards = [type(card)() for card in self.decks[deck_name]]
        random.shuffle(selected_cards)
        opponent_options = [
            name for name in self.decks if name != deck_name
        ] or [deck_name]
        opponent_deck_name = random.choice(opponent_options)
        opponent_cards = [
            type(card)() for card in self.decks[opponent_deck_name]
        ]
        random.shuffle(opponent_cards)

        self.match_mode = f"{mode_number:02d} - {mode_name}"
        self.match_deck_name = deck_name
        self.match_opponent_deck_name = opponent_deck_name
        self.match_opponent_deck_cards = opponent_cards
        self.match_coins = 3
        self.match_opponent_coins = 3
        self.match_phase = 1
        self.match_turn_count = 0
        self.match_phase_state = "preparation"
        self.match_turn_owner = "player"
        self.match_hand_locked = False
        self.match_attacked_cards = set()
        self.match_discard_pile = []
        self.match_destroyed_cards = []
        self.match_combat_bonuses = {}
        self.match_bound_opponents = {}
        self.match_enemy_spells_disabled = 0
        self.match_combat_coin_bonus = 0
        self.match_enemy_cost_modifier = 0
        self.match_enemy_cost_turns = 0
        self.match_defeats = 0
        self.match_win_streak = 0
        self.match_pending_coin_reward = 0
        self.match_player_hp = 80
        self.match_character_cards = []
        self.match_destroyed_player_cards = []
        self.match_support_cards = []
        self.match_purchase_cards = selected_cards[:self.PHASE_DRAW_COUNT]
        self.match_draw_pile = selected_cards[self.PHASE_DRAW_COUNT:]
        self.match_opponent_character_cards = self._choose_starting_opponent_cards()
        self.match_opponent_reserve_cards = []
        self.match_opponent_support_cards = []
        starting_cards = set(id(card) for card in self.match_opponent_character_cards)
        remaining_opponent_cards = [
            card for card in opponent_cards if id(card) not in starting_cards
        ]
        self.match_opponent_purchase_cards = remaining_opponent_cards[:5]
        self.match_opponent_draw_pile = remaining_opponent_cards[5:]
        self._opponent_play_support_cards()
        self._show_match()

    def _choose_starting_opponent_cards(self):
        candidates = [
            card for card in self.match_opponent_deck_cards
            if getattr(card, "type", "") == "Character"
            and 1 <= int(getattr(card, "cost", 0)) <= 2
        ]
        for first_index, first_card in enumerate(candidates):
            first_tags = getattr(first_card, "tag", ())
            first_tags = {first_tags} if isinstance(first_tags, str) else set(first_tags)
            for second_card in candidates[first_index + 1:]:
                second_tags = getattr(second_card, "tag", ())
                second_tags = (
                    {second_tags}
                    if isinstance(second_tags, str)
                    else set(second_tags)
                )
                if first_tags & second_tags:
                    return [first_card, second_card]
        if len(candidates) == 1:
            return [candidates[0], type(candidates[0])()]
        return candidates[:2]

    def _show_match(self):
        self._clear_screen()
        page = ttk.Frame(self, style="App.TFrame", padding=0)
        page.pack(fill="both", expand=True)
        self._add_menu_background(page)

        header = tk.Frame(page, bg="#10141b")
        header.pack(fill="x", padx=24, pady=(16, 8))
        tk.Button(
            header,
            text="<  SAIR DA PARTIDA",
            command=lambda: self._show_deck_selection(
                int(self.match_mode[:2]), self.match_mode[5:]
            ),
            bg="#10141b",
            fg="#f5f1e8",
            activebackground="#354254",
            activeforeground="#ffffff",
            relief="flat",
            bd=0,
            cursor="hand2",
            font=("Segoe UI", 10, "bold"),
        ).pack(side="left")
        self.match_status_label = tk.Label(
            header,
            text="Prepare seu campo e comece o combate.",
            bg="#10141b",
            fg="#b8c2d1",
            font=("Segoe UI", 10),
        )
        self.match_status_label.pack(side="left", padx=20)
        actions = tk.Frame(header, bg="#10141b")
        actions.pack(side="right", padx=(12, 0))
        self.match_phase_button = tk.Button(
            actions,
            text="COMEÇAR COMBATE",
            command=self._start_combat,
            bg="#8f493f",
            fg="#ffffff",
            activebackground="#b35d50",
            activeforeground="#ffffff",
            relief="flat",
            bd=0,
            padx=12,
            pady=7,
            font=("Segoe UI", 9, "bold"),
            cursor="hand2",
        )
        self.match_phase_button.pack(side="left", padx=3)
        self.match_deck_label = tk.Label(
            actions,
            bg="#181e28",
            fg="#f4d03f",
            padx=12,
            pady=7,
            font=("Segoe UI", 9, "bold"),
        )
        self.match_deck_label.pack(side="left", padx=3)
        self._update_deck_indicator()
        self.match_lock_button = tk.Button(
            actions,
            command=self._toggle_hand_lock,
            fg="#ffffff",
            activeforeground="#ffffff",
            relief="flat",
            bd=0,
            padx=12,
            pady=7,
            font=("Segoe UI", 9, "bold"),
            cursor="hand2",
        )
        self.match_lock_button.pack(side="left", padx=3)
        self._update_hand_lock_button()
        tk.Button(
            actions,
            text="DESCARTE",
            command=self._show_discard_pile,
            bg="#354254",
            fg="#ffffff",
            activebackground="#4b5d73",
            activeforeground="#ffffff",
            relief="flat",
            bd=0,
            padx=12,
            pady=7,
            font=("Segoe UI", 9, "bold"),
            cursor="hand2",
        ).pack(side="left", padx=3)
        tk.Label(
            header,
            text=(
                f"{self.match_mode}   |   {self.match_deck_name.upper()} "
                f"VS {self.match_opponent_deck_name.upper()}"
            ),
            bg="#10141b",
            fg="#f5f1e8",
            font=("Segoe UI", 16, "bold"),
        ).pack(side="right")
        self.match_coins_label = tk.Label(
            header,
            text=(
                f"FASE {self.match_phase}  |  TURNO {self.match_turn_count}"
                f"  |  MOEDAS: {self.match_coins}"
            ),
            bg="#10141b",
            fg="#f4d03f",
            font=("Segoe UI", 13, "bold"),
        )
        self.match_coins_label.pack(side="right", padx=(0, 24))
        self.match_hp_label = tk.Label(
            header,
            text=(
                f"VIDA: {self.match_player_hp}  |  "
                f"OPONENTE: {len(self.match_opponent_character_cards)} MONSTROS"
                f" / {len(self.match_opponent_reserve_cards)} RESERVA"
            ),
            bg="#10141b",
            fg="#f5f1e8",
            font=("Segoe UI", 10, "bold"),
        )
        self.match_hp_label.pack(side="right", padx=(0, 18))

        self.match_canvas = tk.Canvas(
            page,
            bg="#10141b",
            bd=0,
            highlightthickness=0,
        )
        self.match_canvas.pack(fill="both", expand=True, padx=24, pady=(0, 20))
        self.match_canvas.bind("<Configure>", self._draw_match_board)
        self.match_canvas.bind("<ButtonPress-1>", self._start_card_drag)
        self.match_canvas.bind("<B1-Motion>", self._move_card_drag)
        self.match_canvas.bind("<ButtonRelease-1>", self._finish_card_drag)
        self.match_canvas.bind("<Motion>", self._show_match_card_preview)
        self.match_canvas.bind("<Leave>", self._hide_match_card_preview)
        self._draw_match_board()

    def _draw_match_board(self, event=None):
        if not hasattr(self, "match_canvas") or not self.match_canvas.winfo_exists():
            return

        canvas = self.match_canvas
        canvas.delete("all")
        self.match_card_photos = []
        self.match_purchase_regions = []
        self.match_card_regions = []
        self.match_character_regions = []
        self.match_opponent_regions = []
        self.match_field_regions = {}
        width = max(canvas.winfo_width(), 720)
        height = max(canvas.winfo_height(), 460)
        side_padding = 10
        row_gap = 16
        label_height = 28
        available_height = height - 5 * label_height - 4 * row_gap - 20
        row_height = max(70, available_height // 5)

        rows = (
            (
                "* CAMPO DE SUPORTE/SPELL DO OPONENTE "
                f"({len(self.match_opponent_support_cards)}/6)",
                self.match_opponent_support_cards,
            ),
            (
                "* CAMPO DE CARTAS DO OPONENTE "
                f"(RESERVA: {len(self.match_opponent_reserve_cards)})",
                self.match_opponent_character_cards,
            ),
            ("* CAMPO DE CARTAS DE PERSONAGEM", self.match_character_cards),
            ("* CAMPO DE CARTAS DE SUPORTE", self.match_support_cards),
            (
                "* MÃO DO JOGADOR (CARTAS DISPONÍVEIS)  |  "
                f"DECK: {len(self.match_draw_pile)}",
                self.match_purchase_cards,
            ),
        )
        current_y = 10
        for title, cards in rows:
            canvas.create_rectangle(
                side_padding,
                current_y,
                width - side_padding,
                current_y + label_height,
                fill="#e8ecf2",
                outline="#111111",
                width=2,
            )
            canvas.create_text(
                width / 2,
                current_y + label_height / 2,
                text=title,
                fill="#111111",
                font=("Segoe UI", 11, "bold"),
            )
            self._draw_match_cards(
                cards,
                side_padding,
                current_y + label_height + 4,
                width - side_padding * 2,
                row_height - label_height - 4,
                field_name=(
                    "opponent_support" if cards is self.match_opponent_support_cards
                    else "opponent" if cards is self.match_opponent_character_cards
                    else "character" if cards is self.match_character_cards
                    else "support" if cards is self.match_support_cards
                    else "purchase"
                ),
            )
            if cards is self.match_character_cards or cards is self.match_support_cards:
                self.match_field_regions[
                    "character" if cards is self.match_character_cards else "support"
                ] = (
                    side_padding,
                    current_y + label_height + 4,
                    width - side_padding,
                    current_y + row_height,
                )
            current_y += row_height + row_gap

    def _draw_match_cards(self, cards, x, y, width, height, field_name):
        canvas = self.match_canvas
        slot_count = (
            6
            if cards is not self.match_purchase_cards
            else self.PURCHASE_AREA_LIMIT
        )
        slot_gap = 8
        slot_width = max(72, (width - slot_gap * (slot_count - 1)) // slot_count)
        card_height = max(48, height)
        for index in range(slot_count):
            card_x = x + index * (slot_width + slot_gap)
            card_y = y
            canvas.create_rectangle(
                card_x,
                card_y,
                card_x + slot_width,
                card_y + card_height,
                fill="#202936",
                outline="#8090a5",
                width=1,
            )
            if index >= len(cards):
                canvas.create_text(
                    card_x + slot_width / 2,
                    y + card_height / 2,
                    text="vazio",
                    fill="#8090a5",
                    font=("Segoe UI", 9),
                )
                continue

            card = cards[index]
            self.match_card_regions.append(
                (card_x, card_y, card_x + slot_width, card_y + card_height, card)
            )
            if field_name == "character":
                self.match_character_regions.append(
                    (card_x, card_y, card_x + slot_width, card_y + card_height, card)
                )
            elif field_name == "opponent":
                self.match_opponent_regions.append(
                    (card_x, card_y, card_x + slot_width, card_y + card_height, card)
                )
            if field_name == "purchase":
                self.match_purchase_regions.append(
                    (card_x, card_y, card_x + slot_width, card_y + card_height, card)
                )
            card_type = getattr(card, "type", "Carta").upper()
            card_cost = max(
                0,
                int(getattr(card, "cost", 0))
                + (
                    self.match_enemy_cost_modifier
                    if field_name in ("opponent", "opponent_support")
                    else 0
                ),
            )
            equipment_count = len(getattr(card, "equipped_weapons", []))
            canvas.create_text(
                card_x + 6,
                card_y + 8,
                text=card.name,
                fill="#f5f1e8",
                font=("Segoe UI", 8, "bold"),
                anchor="nw",
                width=slot_width - 12,
            )
            canvas.create_text(
                card_x + 6,
                card_y + 25,
                text=f"{card_type}  |  CUSTO: {card_cost}",
                fill="#f4d03f",
                font=("Segoe UI", 7, "bold"),
                anchor="nw",
                width=slot_width - 12,
            )
            image = self._prepare_match_card_image(
                card, slot_width - 8, card_height - 30
            )
            if image is not None:
                photo = ImageTk.PhotoImage(image)
                self.match_card_photos.append(photo)
                canvas.create_image(
                    card_x + slot_width / 2,
                    y + 4,
                    image=photo,
                    anchor="n",
                )
            canvas.create_text(
                card_x + slot_width / 2,
                y + card_height - 14,
                text=(
                    f"{card.name}\n{card_type}  |  CUSTO: {card_cost}"
                    + (
                        f"\nARMAS: {equipment_count}"
                        if equipment_count
                        else ""
                    )
                ),
                fill="#f5f1e8",
                font=("Segoe UI", 8, "bold"),
                width=slot_width - 8,
            )

    def _show_match_card_preview(self, event):
        card = next(
            (
                card
                for x1, y1, x2, y2, card in self.match_card_regions
                if x1 <= event.x <= x2 and y1 <= event.y <= y2
            ),
            None,
        )
        if card is None:
            self._hide_match_card_preview()
            return

        preview = getattr(self, "match_preview_window", None)
        if preview is None or not preview.winfo_exists():
            preview = tk.Toplevel(self)
            preview.overrideredirect(True)
            preview.configure(bg="#10141b")
            self.match_preview_window = preview
            self.match_preview_card = None

        if self.match_preview_card is not card:
            for child in preview.winfo_children():
                child.destroy()

            panel = tk.Frame(
                preview,
                bg="#e8ecf2",
                bd=2,
                relief="solid",
                padx=10,
                pady=10,
            )
            panel.pack()
            image = self._prepare_match_card_image(card, 220, 150)
            if image is not None:
                photo = ImageTk.PhotoImage(image)
                image_label = tk.Label(panel, image=photo, bg="#181d26")
                image_label.image = photo
                image_label.pack(fill="x")

            element = getattr(card, "element", "")
            card_type = getattr(card, "type", "Carta")
            tags = getattr(card, "tag", "")
            if not isinstance(tags, str):
                tags = " / ".join(tags)
            stats = []
            if hasattr(card, "power"):
                stats.append(f"DP {card.power}")
            if hasattr(card, "hp"):
                stats.append(f"HP {card.hp}")
            if hasattr(card, "duration"):
                stats.append(f"DUR {card.duration}")

            tk.Label(
                panel,
                text=card.name,
                bg="#e8ecf2",
                fg="#202936",
                font=("Segoe UI", 12, "bold"),
                wraplength=220,
            ).pack(anchor="w", pady=(8, 2))
            tk.Label(
                panel,
                text=(
                    f"{card_type.upper()}  |  ELEMENTO: {element}\n"
                    f"CUSTO: {getattr(card, 'cost', 0)}  |  "
                    f"RARIDADE: {self._card_rarity(card)}\n"
                    f"TAGS: {tags}"
                ),
                bg="#e8ecf2",
                fg="#3b4352",
                font=("Segoe UI", 8, "bold"),
                justify="left",
                wraplength=220,
            ).pack(anchor="w")
            tk.Label(
                panel,
                text=f"PASSIVA:\n{getattr(card, 'passive', 'Sem passiva')}",
                bg="#dce2ec",
                fg="#2b3240",
                font=("Segoe UI", 8),
                justify="left",
                anchor="nw",
                wraplength=220,
                padx=6,
                pady=6,
            ).pack(fill="x", pady=(8, 4))
            tk.Label(
                panel,
                text="   ".join(stats) or f"TIPO: {card_type.upper()}",
                bg="#e8ecf2",
                fg="#10141b",
                font=("Segoe UI", 8, "bold"),
            ).pack(anchor="e")
            self.match_preview_card = card

        preview.update_idletasks()
        preview_width = preview.winfo_width()
        preview_height = preview.winfo_height()
        x = self.winfo_pointerx() + 18
        y = self.winfo_pointery() + 18
        if x + preview_width > self.winfo_screenwidth():
            x = self.winfo_pointerx() - preview_width - 18
        if y + preview_height > self.winfo_screenheight():
            y = self.winfo_pointery() - preview_height - 18
        preview.geometry(f"+{max(0, x)}+{max(0, y)}")
        preview.deiconify()
        preview.lift()

    def _hide_match_card_preview(self, event=None):
        preview = getattr(self, "match_preview_window", None)
        if preview is not None and preview.winfo_exists():
            preview.destroy()
        self.match_preview_window = None
        self.match_preview_card = None

    def _start_card_drag(self, event):
        if getattr(self, "match_phase_state", "preparation") == "combat":
            for x1, y1, x2, y2, card in self.match_character_regions:
                if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                    if self.match_turn_owner != "player":
                        self._show_match_status("Agora é o turno do oponente.")
                        return
                    if getattr(card, "attacks_this_turn", 0) >= (
                        1 + getattr(card, "extra_attacks", 0)
                    ):
                        self._show_match_status(
                            f"{card.name} já atacou neste turno."
                        )
                        return
                    self.match_selected_attacker = card
                    self._show_match_status(
                        f"{card.name} selecionado. Clique em um monstro inimigo."
                    )
                    return
            for x1, y1, x2, y2, card in self.match_opponent_regions:
                if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                    attacker = getattr(self, "match_selected_attacker", None)
                    if attacker is not None:
                        self._attack_character(attacker, card)
                    else:
                        self._show_match_status(
                            "Selecione primeiro um personagem do seu campo."
                        )
                    return
            return

        self.match_drag_card = None
        self.match_drag_item = None
        for x1, y1, x2, y2, card in self.match_purchase_regions:
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                self.match_drag_card = card
                self.match_drag_item = self.match_canvas.create_text(
                    event.x,
                    event.y,
                    text=card.name,
                    fill="#f4d03f",
                    font=("Segoe UI", 10, "bold"),
                    tags=("dragged_card",),
                )
                break

    def _move_card_drag(self, event):
        if self.match_drag_item is not None:
            self.match_canvas.coords(self.match_drag_item, event.x, event.y)

    def _finish_card_drag(self, event):
        if getattr(self, "match_phase_state", "preparation") != "preparation":
            self.match_drag_card = None
            self.match_drag_item = None
            return
        if self.match_drag_item is None or self.match_drag_card is None:
            return

        card = self.match_drag_card
        self.match_canvas.delete(self.match_drag_item)
        self.match_drag_item = None
        target = next(
            (
                field_name
                for field_name, (x1, y1, x2, y2) in self.match_field_regions.items()
                if x1 <= event.x <= x2 and y1 <= event.y <= y2
            ),
            None,
        )
        if target is None:
            self.match_drag_card = None
            return

        character_target = next(
            (
                field_card
                for x1, y1, x2, y2, field_card in self.match_character_regions
                if x1 <= event.x <= x2 and y1 <= event.y <= y2
            ),
            None,
        )
        target_cards = (
            self.match_character_cards
            if target == "character"
            else self.match_support_cards
        )
        card_cost = self._effective_card_cost(card)
        card_type = getattr(card, "type", "")
        if card_cost > self.match_coins:
            self._show_match_status(f"Você precisa de {card_cost} moedas para essa carta.")
        elif card_type == "Weapon":
            if target != "character" or character_target is None:
                self._show_match_status(
                    "Arraste uma arma sobre um personagem para equipá-la."
                )
            else:
                self._equip_weapon(character_target, card)
                self.match_purchase_cards.remove(card)
                self.match_coins -= card_cost
                self._update_match_header()
                self._show_match_status(
                    f"{card.name} equipada em {character_target.name}: "
                    f"+{self.WEAPON_POWER_BONUS} poder e "
                    f"+{self.WEAPON_HP_BONUS} HP."
                )
                self._draw_match_board()
        elif target == "character" and card_type != "Character":
            self._show_match_status("Somente personagens ou armas podem ir nesse campo.")
        elif target == "support" and getattr(card, "type", "") == "Character":
            self._show_match_status("Personagens não podem ir no campo de suporte.")
        elif target == "character" and character_target is not None:
            character_index = self.match_character_cards.index(character_target)
            self.match_character_cards[character_index] = card
            self.match_discard_pile.append(character_target)
            self.match_destroyed_cards.append(character_target)
            self._prepare_character_for_field(card)
            self.match_purchase_cards.remove(card)
            self.match_coins -= card_cost
            self._apply_play_passive(card)
            self._update_match_header()
            self._show_match_status(
                f"{card.name} substituiu {character_target.name}, que foi destruída."
            )
            self._draw_match_board()
        elif len(target_cards) >= 6:
            self._show_match_status("Esse campo já possui 6 cartas.")
        else:
            target_cards.append(card)
            if target == "character":
                self._prepare_character_for_field(card)
            self.match_purchase_cards.remove(card)
            self.match_coins -= card_cost
            self._apply_play_passive(card)
            self._update_match_header()
            self._show_match_status(f"{card.name} colocada no campo por {card_cost} moedas.")
            self._draw_match_board()
        self.match_drag_card = None

    def _prepare_character_for_field(self, card):
        if not hasattr(card, "base_power"):
            card.base_power = int(getattr(card, "power", 0))
        if not hasattr(card, "base_hp"):
            card.base_hp = int(getattr(card, "hp", 0))
        if not hasattr(card, "equipped_weapons"):
            card.equipped_weapons = []

    def _equip_weapon(self, character, weapon):
        self._prepare_character_for_field(character)
        character.equipped_weapons.append(weapon)
        character.power += self.WEAPON_POWER_BONUS
        character.hp += self.WEAPON_HP_BONUS
        if character.name == "Lumine":
            weapon_element = getattr(weapon, "element", "")
            if isinstance(weapon_element, str) and weapon_element:
                character.element = weapon_element
        if weapon.name == "Hexaiphanes Blade":
            character.extra_attacks = getattr(character, "extra_attacks", 0) + 1

    def _restore_destroyed_player_cards(self):
        for card in self.match_destroyed_player_cards:
            if len(self.match_character_cards) >= 6:
                break
            self._prepare_character_for_field(card)
            weapon_count = len(card.equipped_weapons)
            card.power = card.base_power + weapon_count * self.WEAPON_POWER_BONUS
            card.hp = card.base_hp + weapon_count * self.WEAPON_HP_BONUS
            self.match_character_cards.append(card)
        self.match_destroyed_player_cards.clear()

    @staticmethod
    def _card_tags(card):
        tags = getattr(card, "tag", ())
        return {tags} if isinstance(tags, str) else set(tags)

    def _effective_card_cost(self, card):
        cost = max(0, int(getattr(card, "cost", 0)))
        if (
            getattr(card, "element", "") == "Geo"
            and any(
                character.name == "Domain Keeper"
                for character in self.match_character_cards
            )
        ):
            cost -= 1
        if (
            "Celestial" in self._card_tags(card)
            and any(
                character.name == "Istoria"
                for character in self.match_character_cards
            )
        ):
            cost -= 1
        if (
            getattr(card, "element", "") == "Cryo"
            and any(
                character.name == "Anastasia"
                for character in self.match_character_cards
            )
        ):
            cost -= 1
        if (
            getattr(card, "type", "") == "Support"
            and getattr(card, "element", "") == "Cryo"
            and any(
                character.name == "Snegurochka Cryomancer"
                for character in self.match_character_cards
            )
        ):
            cost -= 1
        return max(0, cost)

    def _draw_cards(self, amount=1, predicate=None):
        drawn_cards = []
        for _ in range(amount):
            card = next(
                (
                    candidate
                    for candidate in self.match_draw_pile
                    if predicate is None or predicate(candidate)
                ),
                None,
            )
            if (
                card is None
                or len(self.match_purchase_cards) >= self.PURCHASE_AREA_LIMIT
            ):
                break
            self.match_draw_pile.remove(card)
            self.match_purchase_cards.append(card)
            drawn_cards.append(card)
        return drawn_cards

    def _draw_pyro_from_top_three(self, source_card=None):
        revealed_cards = self.match_draw_pile[:3]
        del self.match_draw_pile[:3]
        pyro_options = [
            card
            for card in revealed_cards
            if getattr(card, "element", "") == "Pyro"
        ]
        pyro_card = None
        if revealed_cards:
            can_take = (
                bool(pyro_options)
                and len(self.match_purchase_cards) < self.PURCHASE_AREA_LIMIT
            )
            pyro_card = self._show_revealed_cards(
                revealed_cards,
                pyro_options if can_take else [],
                source_card,
            )
        if pyro_card is not None:
            revealed_cards.remove(pyro_card)
            self.match_purchase_cards.append(pyro_card)
        self.match_draw_pile.extend(revealed_cards)
        self._update_match_header()
        return pyro_card

    def _show_revealed_cards(self, revealed_cards, selectable, source_card=None):
        """Mostra as cartas reveladas; retorna a carta escolhida entre as selecionáveis."""
        result = {"card": None}
        window = tk.Toplevel(self)
        window.title("Cartas reveladas")
        window.configure(bg="#10141b")
        window.transient(self)
        window.resizable(False, False)

        container = tk.Frame(window, bg="#10141b", padx=18, pady=18)
        container.pack(fill="both", expand=True)
        source_text = f"{source_card.name}: " if source_card is not None else ""
        if selectable:
            message = (
                f"{source_text}escolha uma carta Pyro para a mão. "
                "As outras vão para o fundo do deck."
            )
        else:
            message = (
                f"{source_text}nenhuma carta pode ser adicionada à mão. "
                "Todas vão para o fundo do deck."
            )
        tk.Label(
            container,
            text=message,
            bg="#10141b",
            fg="#f5f1e8",
            font=("Segoe UI", 12, "bold"),
            wraplength=560,
            justify="left",
        ).pack(anchor="w", pady=(0, 12))

        def choose(card):
            result["card"] = card
            window.destroy()

        cards_row = tk.Frame(container, bg="#10141b")
        cards_row.pack()
        for card in revealed_cards:
            can_choose = any(card is option for option in selectable)
            panel = tk.Frame(
                cards_row,
                bg="#202936",
                highlightthickness=2,
                highlightbackground="#f4d03f" if can_choose else "#8090a5",
                padx=8,
                pady=8,
            )
            panel.pack(side="left", padx=6)
            pil_image = self._prepare_match_card_image(card, 150, 130)
            if pil_image is not None:
                image = ImageTk.PhotoImage(pil_image)
                image_label = tk.Label(panel, image=image, bg="#202936")
                image_label.image = image
                image_label.pack()
            tk.Label(
                panel,
                text=card.name,
                bg="#202936",
                fg="#f5f1e8",
                font=("Segoe UI", 10, "bold"),
                wraplength=150,
            ).pack(pady=(6, 0))
            tk.Label(
                panel,
                text=(
                    f"{getattr(card, 'type', 'Carta')} | "
                    f"{getattr(card, 'element', '-')} | "
                    f"custo {getattr(card, 'cost', 0)}"
                ),
                bg="#202936",
                fg="#f4d03f",
                font=("Segoe UI", 8, "bold"),
            ).pack()
            if can_choose:
                tk.Button(
                    panel,
                    text="PEGAR",
                    command=lambda selected=card: choose(selected),
                    bg="#4d6f61",
                    fg="#ffffff",
                    activebackground="#638c7a",
                    activeforeground="#ffffff",
                    relief="flat",
                    bd=0,
                    padx=12,
                    pady=5,
                    font=("Segoe UI", 9, "bold"),
                    cursor="hand2",
                ).pack(pady=(6, 0))

        tk.Button(
            container,
            text="NÃO PEGAR NENHUMA" if selectable else "OK",
            command=window.destroy,
            bg="#354254",
            fg="#ffffff",
            activebackground="#4b5d73",
            activeforeground="#ffffff",
            relief="flat",
            bd=0,
            padx=12,
            pady=7,
            font=("Segoe UI", 9, "bold"),
            cursor="hand2",
        ).pack(anchor="e", pady=(12, 0))

        window.update_idletasks()
        x = self.winfo_rootx() + (self.winfo_width() - window.winfo_width()) // 2
        y = self.winfo_rooty() + (self.winfo_height() - window.winfo_height()) // 2
        window.geometry(f"+{max(x, 0)}+{max(y, 0)}")
        window.grab_set()
        window.focus_set()
        self.wait_window(window)
        return result["card"]

    def _choose_card_to_discard(self, options, source_card=None):
        """Abre um diálogo modal; retorna a carta escolhida ou None se cancelado."""
        result = {"card": None}
        window = tk.Toplevel(self)
        window.title("Escolha a carta para descartar")
        window.configure(bg="#10141b")
        window.transient(self)
        window.resizable(False, False)

        container = tk.Frame(window, bg="#10141b", padx=18, pady=18)
        container.pack(fill="both", expand=True)
        source_text = f"{source_card.name}: " if source_card is not None else ""
        tk.Label(
            container,
            text=f"{source_text}escolha uma carta da mão para descartar",
            bg="#10141b",
            fg="#f5f1e8",
            font=("Segoe UI", 12, "bold"),
            wraplength=380,
            justify="left",
        ).pack(anchor="w", pady=(0, 12))

        def choose(card):
            result["card"] = card
            window.destroy()

        for option in options:
            tk.Button(
                container,
                text=(
                    f"{option.name}  ({getattr(option, 'type', 'Carta')}, "
                    f"custo {getattr(option, 'cost', 0)})"
                ),
                command=lambda selected=option: choose(selected),
                bg="#354254",
                fg="#ffffff",
                activebackground="#4b5d73",
                activeforeground="#ffffff",
                relief="flat",
                bd=0,
                anchor="w",
                padx=12,
                pady=7,
                font=("Segoe UI", 10),
                cursor="hand2",
            ).pack(fill="x", pady=2)
        tk.Button(
            container,
            text="NÃO DESCARTAR",
            command=window.destroy,
            bg="#8f493f",
            fg="#ffffff",
            activebackground="#b35d50",
            activeforeground="#ffffff",
            relief="flat",
            bd=0,
            padx=12,
            pady=7,
            font=("Segoe UI", 9, "bold"),
            cursor="hand2",
        ).pack(anchor="e", pady=(12, 0))

        window.update_idletasks()
        x = self.winfo_rootx() + (self.winfo_width() - window.winfo_width()) // 2
        y = self.winfo_rooty() + (self.winfo_height() - window.winfo_height()) // 2
        window.geometry(f"+{max(x, 0)}+{max(y, 0)}")
        window.grab_set()
        window.focus_set()
        self.wait_window(window)
        return result["card"]

    def _discard_purchase_card(self, excluded_card=None):
        options = [
            candidate
            for candidate in self.match_purchase_cards
            if candidate is not excluded_card
        ]
        if not options:
            return None
        card = self._choose_card_to_discard(options, excluded_card)
        if card is None:
            return None
        self.match_purchase_cards.remove(card)
        self.match_discard_pile.append(card)
        for lumine in self.match_character_cards:
            if lumine.name == "Lumine":
                self._add_combat_bonus(lumine, power=100)
        return card

    def _destroy_enemy_character(self, card):
        if card in self.match_opponent_character_cards:
            self.match_opponent_character_cards.remove(card)
            self.match_destroyed_cards.append(card)
            self._summon_opponent_reserve_cards()

    def _summon_opponent_reserve_cards(self):
        while (
            len(self.match_opponent_character_cards) < 5
            and self.match_opponent_reserve_cards
        ):
            self.match_opponent_character_cards.append(
                self.match_opponent_reserve_cards.pop(0)
            )

    def _opponent_has_characters(self):
        return bool(
            self.match_opponent_character_cards
            or self.match_opponent_reserve_cards
        )

    def _boss_is_active(self):
        return any(
            getattr(card, "is_boss", False)
            for card in (
                self.match_opponent_character_cards
                + self.match_opponent_reserve_cards
            )
        )

    def _spawn_phase_boss(self):
        boss_candidates = [
            card
            for card in self.match_opponent_deck_cards
            if (
                getattr(card, "type", "") == "Character"
                and int(getattr(card, "cost", 0)) in {6, 8}
            )
        ]
        if not boss_candidates:
            boss_candidates = [
                card
                for card in self.base_decks["deck2"]
                if (
                    getattr(card, "type", "") == "Character"
                    and int(getattr(card, "cost", 0)) in {6, 8}
                )
            ]
        if not boss_candidates:
            raise RuntimeError(
                "Não há um personagem de custo 6 ou 8 disponível para o chefe."
            )

        boss = type(random.choice(boss_candidates))()
        boss.hp = int(getattr(boss, "hp", 0)) * 3 + 10 * self.match_turn_count
        boss.base_hp = boss.hp
        boss.is_boss = True
        boss.boss_phase = self.match_phase
        if len(self.match_opponent_character_cards) >= 5:
            displaced_card = self.match_opponent_character_cards.pop()
            self.match_opponent_reserve_cards.insert(0, displaced_card)
        self.match_opponent_character_cards.insert(0, boss)
        return boss

    def _begin_player_combat_turn(self):
        self.match_turn_count += 1
        self._apply_turn_cost_passives()
        self._update_match_header()
        return True

    def _destroy_player_character(self, card, restore_after_combat=True):
        if card not in self.match_character_cards:
            return False
        envoy = next(
            (
                candidate
                for candidate in self.match_character_cards
                if candidate is not card and candidate.name == "Celestial Envoy"
            ),
            None,
        )
        destroyed_card = envoy or card
        self.match_character_cards.remove(destroyed_card)
        self.match_destroyed_cards.append(destroyed_card)
        if restore_after_combat:
            self.match_destroyed_player_cards.append(destroyed_card)
        else:
            self.match_discard_pile.append(destroyed_card)
        self._on_player_character_destroyed(destroyed_card)
        return destroyed_card is card

    def _add_combat_bonus(self, card, power=0, hp=0):
        if not power and not hp:
            return
        bonus_power, bonus_hp = self.match_combat_bonuses.get(id(card), (0, 0))
        self.match_combat_bonuses[id(card)] = (
            bonus_power + power,
            bonus_hp + hp,
        )
        card.power += power
        card.hp += hp

    def _clear_combat_bonuses(self):
        cards = self.match_character_cards + self.match_destroyed_player_cards
        cards_by_id = {id(card): card for card in cards}
        for card_id, (power, hp) in self.match_combat_bonuses.items():
            card = cards_by_id.get(card_id)
            if card is not None:
                card.power -= power
                card.hp = max(0, card.hp - hp)
        self.match_combat_bonuses.clear()

    def _bind_enemy_character(self, turns=1):
        if not self.match_opponent_character_cards:
            return None
        target = max(
            self.match_opponent_character_cards,
            key=lambda card: int(getattr(card, "power", 0)),
        )
        self.match_bound_opponents[id(target)] = turns
        return target

    def _on_player_character_destroyed(self, card):
        if card.name in {"Istoria", "Chlothar", "Ruin Destroyer Serpent"}:
            self._draw_cards()
        if card.name == "Hydro Abyss Mage":
            self._bind_enemy_character()

    def _apply_play_passive(self, card):
        if card.name != "Aether" and "Celestial" in self._card_tags(card):
            for aether in self.match_character_cards:
                if aether.name == "Aether":
                    self._add_combat_bonus(aether, power=100)

        if card.name == "Pyro Seelie Guide":
            self._draw_pyro_from_top_three(card)
        elif card.name == "Jack Frost":
            self._draw_cards(
                predicate=lambda candidate: "Fae" in self._card_tags(candidate)
            )
        elif card.name == "Cryo Abyss Mage":
            self._draw_cards(
                predicate=lambda candidate: "Abyssal" in self._card_tags(candidate)
            )
        elif card.name == "Caribert":
            self._draw_cards(
                predicate=lambda candidate: "Abyssal" in self._card_tags(candidate)
            )
        elif card.name == "Tenebrous Mimiflora":
            self.match_character_cards.remove(card)
            self.match_discard_pile.append(card)
            replacement = next(
                (
                    candidate
                    for candidate in self.match_purchase_cards + self.match_discard_pile
                    if (
                        candidate is not card
                        and getattr(candidate, "type", "") == "Character"
                        and "Abyssal" in self._card_tags(candidate)
                    )
                ),
                None,
            )
            if replacement is not None and len(self.match_character_cards) < 6:
                if replacement in self.match_purchase_cards:
                    self.match_purchase_cards.remove(replacement)
                else:
                    self.match_discard_pile.remove(replacement)
                self._prepare_character_for_field(replacement)
                replacement.hp = replacement.base_hp
                self.match_character_cards.append(replacement)
        elif card.name == "Hydro Abyss Herald":
            if self._discard_purchase_card(card) is not None:
                self._bind_enemy_character()
        elif card.name == "Anastasia":
            for enemy in self.match_opponent_character_cards[:2]:
                self.match_bound_opponents[id(enemy)] = 2
        elif card.name == "Cryo Abyss Herald":
            if self._discard_purchase_card(card) is not None:
                card.piercing = True
        elif card.name == "Ruin Guard":
            target = next(
                (
                    enemy
                    for enemy in self.match_opponent_character_cards
                    if int(getattr(enemy, "cost", 0)) <= 2
                ),
                None,
            )
            if target is not None:
                self._destroy_enemy_character(target)
        elif card.name == "Elynas":
            for enemy in list(self.match_opponent_character_cards):
                if int(getattr(enemy, "cost", 0)) <= 4:
                    self._destroy_enemy_character(enemy)
        elif card.name == "Ursa, the Drake":
            if (
                not getattr(card, "ursa_used", False)
                and self._discard_purchase_card(card) is not None
            ):
                target = next(
                    (
                        enemy
                        for enemy in self.match_opponent_character_cards
                        if int(getattr(enemy, "hp", 0)) <= 400
                    ),
                    None,
                )
                if target is not None:
                    self._destroy_enemy_character(target)
                card.ursa_used = True
        elif card.name == "Celestial Nail":
            self.match_opponent_support_cards.clear()
            for enemy in list(self.match_opponent_character_cards):
                enemy.hp = max(0, int(getattr(enemy, "hp", 0)) - 200)
                if enemy.hp == 0:
                    self._destroy_enemy_character(enemy)
            self.match_discard_pile.append(card)
            self.match_support_cards.remove(card)
        elif card.name == "Fake Sky":
            self.match_enemy_cost_turns = 3
        elif card.name == "Elemental Conversion":
            target = next(
                (
                    candidate
                    for candidate in self.match_purchase_cards
                    if candidate is not card and hasattr(candidate, "element")
                ),
                None,
            )
            if target is not None:
                target.element = "Omni"
            self.match_discard_pile.append(card)
            self.match_support_cards.remove(card)
        elif card.name == "Purification":
            self.match_enemy_spells_disabled += 1
            self.match_discard_pile.append(card)
            self.match_support_cards.remove(card)
        elif card.name == "Spaceship":
            for hand_card in list(self.match_purchase_cards):
                self.match_purchase_cards.remove(hand_card)
                self.match_discard_pile.append(hand_card)
            self._draw_cards(5)
            self.match_discard_pile.append(card)
            self.match_support_cards.remove(card)
        elif card.name == "Leylines":
            if self._discard_purchase_card(card) is not None:
                self.match_coins += 1
            self.match_discard_pile.append(card)
            self.match_support_cards.remove(card)
        elif card.name == "Abyssal Rift":
            if self.match_opponent_character_cards:
                returned_card = self.match_opponent_character_cards.pop(0)
                self.match_opponent_draw_pile.append(returned_card)
                self._summon_opponent_reserve_cards()
            self._draw_cards(
                predicate=lambda candidate: (
                    "Abyssal" in self._card_tags(candidate)
                    and int(getattr(candidate, "cost", 0)) <= 4
                )
            )
            self.match_discard_pile.append(card)
            self.match_support_cards.remove(card)
        elif card.name in {"Transcending Fate", "Loom of Fate"}:
            if (
                card.name == "Transcending Fate"
                and self._discard_purchase_card(card) is None
            ):
                self.match_discard_pile.append(card)
                self.match_support_cards.remove(card)
                return
            revived_card = next(
                (
                    candidate
                    for candidate in self.match_discard_pile
                    if (
                        getattr(candidate, "type", "") == "Character"
                        and "Abyssal" in self._card_tags(candidate)
                    )
                ),
                None,
            )
            if revived_card is not None and len(self.match_character_cards) < 6:
                self.match_discard_pile.remove(revived_card)
                self._prepare_character_for_field(revived_card)
                revived_card.hp = revived_card.base_hp
                self.match_character_cards.append(revived_card)
            if card.name == "Loom of Fate":
                if self._discard_purchase_card(card) is not None:
                    self._draw_cards(
                        predicate=lambda candidate: (
                            "Abyssal" in self._card_tags(candidate)
                        )
                    )
            self.match_discard_pile.append(card)
            self.match_support_cards.remove(card)
        elif card.name == "Sinner's Blessing":
            sacrifice = next(
                (
                    character
                    for character in self.match_character_cards
                    if character is not card and int(getattr(character, "cost", 0)) <= 4
                ),
                None,
            )
            revived_card = next(
                (
                    candidate
                    for candidate in self.match_discard_pile
                    if (
                        getattr(candidate, "type", "") == "Character"
                        and "Abyssal" in self._card_tags(candidate)
                        and int(getattr(candidate, "cost", 0)) >= 6
                    )
                ),
                None,
            )
            if sacrifice is not None:
                self._destroy_player_character(
                    sacrifice,
                    restore_after_combat=False,
                )
            if revived_card is not None and len(self.match_character_cards) < 6:
                self.match_discard_pile.remove(revived_card)
                self._prepare_character_for_field(revived_card)
                revived_card.hp = revived_card.base_hp
                self.match_character_cards.append(revived_card)
            self.match_discard_pile.append(card)
            self.match_support_cards.remove(card)
        elif card.name == "Corrupted Blood":
            sacrifice = next(
                (
                    character
                    for character in self.match_character_cards
                    if character is not card
                ),
                None,
            )
            revived_card = None
            if sacrifice is not None:
                sacrifice_cost = int(getattr(sacrifice, "cost", 0))
                self._destroy_player_character(
                    sacrifice,
                    restore_after_combat=False,
                )
                revived_card = next(
                    (
                        candidate
                        for candidate in self.match_discard_pile
                        if (
                            getattr(candidate, "type", "") == "Character"
                            and "Abyssal" in self._card_tags(candidate)
                            and int(getattr(candidate, "cost", 0)) == sacrifice_cost
                        )
                    ),
                    None,
                )
            if revived_card is not None and len(self.match_character_cards) < 6:
                self.match_discard_pile.remove(revived_card)
                self._prepare_character_for_field(revived_card)
                revived_card.hp = revived_card.base_hp
                self.match_character_cards.append(revived_card)
            self.match_discard_pile.append(card)
            self.match_support_cards.remove(card)

    OPPONENT_STATIC_SPELLS = {"Statue of the Seven", "Celestia"}
    OPPONENT_CAST_SPELLS = {
        "Celestial Nail",
        "Purification",
        "Fake Sky",
        "Abyssal Rift",
    }
    OPPONENT_SUPPORT_LIMIT = 6

    def _opponent_play_support_cards(self):
        """O oponente baixa spells do próprio deck no campo de suporte/spell."""
        self.match_opponent_support_cards.clear()
        usable = self.OPPONENT_STATIC_SPELLS | self.OPPONENT_CAST_SPELLS
        pool = [
            type(card)()
            for card in self.match_opponent_deck_cards
            if getattr(card, "type", "") == "Support"
            and card.name in usable
        ]
        random.shuffle(pool)
        budget = 2 + self.match_phase
        for spell in pool:
            if len(self.match_opponent_support_cards) >= self.OPPONENT_SUPPORT_LIMIT:
                break
            cost = max(
                0, int(getattr(spell, "cost", 0)) + self.match_enemy_cost_modifier
            )
            if cost > budget:
                continue
            budget -= cost
            self.match_opponent_support_cards.append(spell)

    def _opponent_spell_negated(self, spell):
        """Purification do jogador anula uma spell do oponente por combate."""
        if self.match_enemy_spells_disabled <= 0:
            return False
        self.match_enemy_spells_disabled -= 1
        self.match_opponent_support_cards.remove(spell)
        return True

    def _apply_opponent_combat_start_passives(self):
        for spell in list(self.match_opponent_support_cards):
            if spell.name not in self.OPPONENT_STATIC_SPELLS:
                continue
            if self._opponent_spell_negated(spell):
                continue
            for enemy in self.match_opponent_character_cards:
                if spell.name == "Statue of the Seven":
                    enemy.hp += 200
                elif "Celestial" in self._card_tags(enemy):
                    enemy.power += 200
                    enemy.hp += 100

    def _cast_opponent_spells(self):
        """Ativa as spells de uso único do oponente no início do turno dele."""
        messages = []
        for spell in list(self.match_opponent_support_cards):
            if spell.name not in self.OPPONENT_CAST_SPELLS:
                continue
            if self._opponent_spell_negated(spell):
                messages.append(f"{spell.name} do oponente foi anulada.")
                continue
            if spell.name == "Celestial Nail":
                self.match_discard_pile.extend(self.match_support_cards)
                self.match_support_cards.clear()
                for character in list(self.match_character_cards):
                    character.hp = max(0, int(getattr(character, "hp", 0)) - 200)
                    if character.hp == 0:
                        self._destroy_player_character(character)
            elif spell.name == "Purification":
                if self.match_support_cards:
                    disabled = self.match_support_cards.pop(0)
                    self.match_discard_pile.append(disabled)
            elif spell.name == "Fake Sky":
                self.match_coins = max(0, self.match_coins - 1)
            elif spell.name == "Abyssal Rift":
                candidate = next(
                    (
                        card
                        for card in self.match_opponent_deck_cards
                        if getattr(card, "type", "") == "Character"
                        and "Abyssal" in self._card_tags(card)
                        and int(getattr(card, "cost", 0)) <= 4
                    ),
                    None,
                )
                if (
                    candidate is not None
                    and len(self.match_opponent_character_cards) < 5
                ):
                    self.match_opponent_character_cards.append(type(candidate)())
            self.match_opponent_support_cards.remove(spell)
            messages.append(f"Oponente ativou {spell.name}.")
        return messages

    def _apply_combat_start_passives(self):
        self._apply_opponent_combat_start_passives()
        for card in self.match_character_cards + self.match_support_cards:
            if card.name == "Paimon":
                self._draw_cards()
            elif card.name == "Statue of the Seven":
                for character in self.match_character_cards:
                    character.hp += 200
            elif card.name == "Celestia":
                for character in self.match_character_cards:
                    if "Celestial" in self._card_tags(character):
                        self._add_combat_bonus(character, power=200, hp=100)
            elif card.name == "Defiled Statue":
                bonus = 50 * len(self.match_discard_pile)
                for character in self.match_character_cards:
                    if character is not card and "Abyssal" in self._card_tags(character):
                        self._add_combat_bonus(character, power=bonus)
            elif card.name == "Elynas":
                for character in self.match_character_cards:
                    if character is not card and "Abyssal" in self._card_tags(character):
                        self._add_combat_bonus(character, power=200)

    def _apply_turn_cost_passives(self):
        cards_in_play = self.match_character_cards + self.match_support_cards
        coin_bonus = sum(
            1
            for card in cards_in_play
            if card.name in {"Celestia", "Kresnik Torch", "Ororon"}
        )
        if coin_bonus:
            self.match_coins += coin_bonus
            self.match_combat_coin_bonus += coin_bonus

        if self.match_enemy_cost_turns:
            self.match_enemy_cost_modifier -= 1
            self.match_enemy_cost_turns -= 1

    def _reset_player_attack_counts(self):
        for character in self.match_character_cards:
            character.attacks_this_turn = 0

    def _update_deck_indicator(self):
        if hasattr(self, "match_deck_label") and self.match_deck_label.winfo_exists():
            self.match_deck_label.configure(
                text=f"DECK: {len(self.match_draw_pile)}"
            )

    def _update_match_header(self):
        self._update_deck_indicator()
        if hasattr(self, "match_coins_label") and self.match_coins_label.winfo_exists():
            self.match_coins_label.configure(
                text=(
                    f"FASE {self.match_phase}  |  TURNO "
                    f"{self.match_turn_count}  |  "
                    f"MOEDAS: {self.match_coins}"
                )
            )
        if hasattr(self, "match_hp_label") and self.match_hp_label.winfo_exists():
            self.match_hp_label.configure(
                text=(
                    f"VIDA: {max(0, self.match_player_hp)}  |  "
                    f"OPONENTE: {len(self.match_opponent_character_cards)} MONSTROS"
                    f" / {len(self.match_opponent_reserve_cards)} RESERVA"
                )
            )
        if hasattr(self, "match_phase_button") and self.match_phase_button.winfo_exists():
            self.match_phase_button.configure(
                text=(
                    "COMEÇAR COMBATE"
                    if self.match_phase_state == "preparation"
                    else "ENCERRAR TURNO"
                ),
                command=(
                    self._start_combat
                    if self.match_phase_state == "preparation"
                    else self._end_combat_turn
                ),
            )

    def _show_discard_pile(self):
        window = tk.Toplevel(self)
        window.title("Cartas descartadas e destruídas")
        window.configure(bg="#10141b")
        window.geometry("430x460")
        window.transient(self)

        container = tk.Frame(window, bg="#10141b", padx=18, pady=18)
        container.pack(fill="both", expand=True)
        tk.Label(
            container,
            text="CARTAS DESCARTADAS E DESTRUÍDAS",
            bg="#10141b",
            fg="#f5f1e8",
            font=("Segoe UI", 13, "bold"),
        ).pack(anchor="w", pady=(0, 12))

        sections = (
            ("DESCARTADAS", self.match_discard_pile),
            ("DESTRUÍDAS NESTA PARTIDA", self.match_destroyed_cards),
            (
                "AGUARDANDO RETORNO AO CAMPO",
                self.match_destroyed_player_cards,
            ),
        )
        for title, cards in sections:
            tk.Label(
                container,
                text=f"{title} ({len(cards)})",
                bg="#10141b",
                fg="#f4d03f",
                font=("Segoe UI", 10, "bold"),
            ).pack(anchor="w", pady=(8, 2))
            content = (
                "\n".join(
                    f"- {card.name} ({getattr(card, 'type', 'Carta')})"
                    for card in cards
                )
                if cards
                else "Nenhuma carta."
            )
            tk.Label(
                container,
                text=content,
                bg="#181e28",
                fg="#cbd3dc",
                font=("Segoe UI", 9),
                justify="left",
                anchor="nw",
                wraplength=380,
                padx=10,
                pady=7,
            ).pack(fill="x")

        tk.Button(
            container,
            text="FECHAR",
            command=window.destroy,
            bg="#354254",
            fg="#ffffff",
            activebackground="#4b5d73",
            activeforeground="#ffffff",
            relief="flat",
            bd=0,
            padx=14,
            pady=7,
            font=("Segoe UI", 9, "bold"),
            cursor="hand2",
        ).pack(anchor="e", pady=(16, 0))

    def _update_hand_lock_button(self):
        locked = getattr(self, "match_hand_locked", False)
        self.match_lock_button.configure(
            text="MÃO TRAVADA" if locked else "TRAVAR MÃO",
            bg="#4d6f61" if locked else "#354254",
            activebackground="#638c7a" if locked else "#4b5d73",
        )

    def _toggle_hand_lock(self):
        self.match_hand_locked = not self.match_hand_locked
        self._update_hand_lock_button()
        self._show_match_status(
            "Mão travada: as cartas ficam na mão e nenhuma carta será comprada "
            "no próximo turno."
            if self.match_hand_locked
            else "Mão destravada."
        )

    def _refill_purchase_cards(self):
        while (
            len(self.match_purchase_cards) < self.PHASE_DRAW_COUNT
            and self.match_draw_pile
        ):
            self.match_purchase_cards.append(self.match_draw_pile.pop(0))

    def _refill_opponent_purchase_cards(self):
        while (
            len(self.match_opponent_purchase_cards) < 5
            and self.match_opponent_draw_pile
        ):
            self.match_opponent_purchase_cards.append(
                self.match_opponent_draw_pile.pop(0)
            )

    def _start_combat(self):
        if self.match_phase_state != "preparation":
            return
        if not self.match_character_cards:
            self._show_match_status(
                "Coloque pelo menos um personagem no campo antes de começar."
            )
            return

        self.match_phase_state = "combat"
        self.match_turn_owner = "player"
        self.match_attacked_cards.clear()
        self._reset_player_attack_counts()
        for character in self.match_character_cards:
            if character.name == "Ursa, the Drake":
                character.ursa_used = False
        self.match_selected_attacker = None
        self._apply_combat_start_passives()
        if not self._begin_player_combat_turn():
            return
        self._show_match_status(
            "Seu turno: selecione um personagem e depois um monstro inimigo."
        )
        self._draw_match_board()

    def _attack_character(self, attacker, defender):
        if self.match_phase_state != "combat":
            return
        if self.match_turn_owner != "player":
            self._show_match_status("Agora é o turno do oponente.")
            return
        if id(attacker) in self.match_attacked_cards:
            self._show_match_status(f"{attacker.name} já atacou neste turno.")
            return

        damage = max(0, int(getattr(attacker, "power", 0)))
        defender.hp = max(0, int(getattr(defender, "hp", 0)) - damage)
        self.match_attacked_cards.add(id(attacker))
        attacker.attacks_this_turn = getattr(attacker, "attacks_this_turn", 0) + 1
        self.match_selected_attacker = None
        if defender.hp == 0:
            defeated_boss = getattr(defender, "is_boss", False)
            self._destroy_enemy_character(defender)
            self._show_match_status(
                f"{attacker.name} destruiu {defender.name}."
            )
            if defeated_boss:
                if self.match_phase == self.MAX_MATCH_PHASES:
                    self._finish_match(
                        True,
                        "Você derrotou o chefe da fase 18 e venceu a partida!",
                    )
                else:
                    self._finish_combat(True)
                return

        else:
            self._show_match_status(
                f"{attacker.name} causou {damage} de dano em {defender.name}."
            )

        self._draw_match_board()
        if not self._opponent_has_characters():
            self._finish_combat(True)

    def _opponent_attack(self):
        self.match_turn_owner = "opponent"
        self.match_attacked_cards.clear()
        cast_messages = self._cast_opponent_spells()
        if cast_messages:
            self._show_match_status(" ".join(cast_messages))
        for attacker in list(self.match_opponent_character_cards):
            if not self.match_character_cards:
                break
            bound_turns = self.match_bound_opponents.get(id(attacker), 0)
            if bound_turns:
                self.match_bound_opponents[id(attacker)] = bound_turns - 1
                continue
            defender = min(
                self.match_character_cards,
                key=lambda card: int(getattr(card, "hp", 0)),
            )
            damage = max(0, int(getattr(attacker, "power", 0)))
            defender.hp = max(0, int(getattr(defender, "hp", 0)) - damage)
            self.match_attacked_cards.add(id(attacker))
            if defender.hp == 0:
                target_destroyed = self._destroy_player_character(defender)
                self._show_match_status(
                    (
                        f"{attacker.name} destruiu {defender.name}."
                        if target_destroyed
                        else f"{attacker.name} destruiu Celestial Envoy em vez de "
                        f"{defender.name}."
                    )
                )

        if not self.match_character_cards:
            if self._boss_is_active():
                self._finish_match(
                    False,
                    "Você perdeu para um chefe e a partida terminou.",
                )
                return
            self._finish_combat(False)
            return

        self._show_match_status(
            "Oponente atacou. Seu turno: selecione seus ataques."
        )
        self.match_turn_owner = "player"
        self.match_attacked_cards.clear()
        self._reset_player_attack_counts()
        if not self._begin_player_combat_turn():
            return
        self._draw_match_board()

    def _end_combat_turn(self):
        if self.match_phase_state != "combat":
            return
        if self.match_turn_owner != "player":
            return
        self._opponent_attack()

    def _finish_combat(self, player_won):
        self.match_phase_state = "transition"
        self.match_selected_attacker = None
        self.match_attacked_cards.clear()
        self._clear_combat_bonuses()
        self._update_match_header()
        if not player_won:
            self.match_win_streak = 0
            self.match_pending_coin_reward = 3
            self.match_defeats += 1
            damage = 15 + (self.match_phase - 1)
            self.match_player_hp -= damage
            if self.match_player_hp <= 0:
                self._finish_match(
                    False,
                    f"Você perdeu o combate e recebeu {damage} de dano. "
                    "Sua vida chegou a zero.",
                )
                return
            result = (
                f"Você perdeu o combate, recebeu {damage} de dano "
                "e ganhou 3 moedas."
            )
        else:
            self.match_defeats = 0
            self.match_win_streak += 1
            self.match_pending_coin_reward = self.match_win_streak
            result = (
                f"Você venceu o combate e ganhou "
                f"{self.match_pending_coin_reward} moedas de recompensa."
            )

        self._show_match_status(f"{result} Preparando a próxima fase...")
        self.after(700, self._start_next_phase)

    def _start_next_phase(self):
        self.match_phase += 1
        self.match_coins = (
            3
            + self.match_pending_coin_reward
            + self.match_combat_coin_bonus
        )
        self.match_pending_coin_reward = 0
        self.match_combat_coin_bonus = 0
        self._restore_destroyed_player_cards()
        self.match_opponent_character_cards = []
        self.match_opponent_reserve_cards = []
        self.match_opponent_support_cards.clear()
        self.match_enemy_spells_disabled = 0
        if self.match_hand_locked:
            # A trava vale apenas para esta troca de turno.
            self.match_hand_locked = False
            self._update_hand_lock_button()
        else:
            self.match_draw_pile.extend(self.match_purchase_cards)
            self.match_purchase_cards = []
            random.shuffle(self.match_draw_pile)
            self._refill_purchase_cards()

        opponent_pool = [
            type(card)() for card in self.match_opponent_deck_cards
            if getattr(card, "type", "") == "Character"
        ]
        random.shuffle(opponent_pool)
        required_cards = self.match_phase + 1
        if opponent_pool:
            phase_opponent_cards = [
                opponent_pool[index % len(opponent_pool)]
                for index in range(required_cards)
            ]
            self.match_opponent_character_cards = phase_opponent_cards[:5]
            self.match_opponent_reserve_cards = phase_opponent_cards[5:]
        boss = None
        if self.match_phase % self.BOSS_PHASE_INTERVAL == 0:
            boss = self._spawn_phase_boss()
        self._opponent_play_support_cards()
        self.match_opponent_purchase_cards = []
        self.match_opponent_draw_pile = []
        self.match_phase_state = "preparation"
        self.match_turn_owner = "player"
        self._update_match_header()
        phase_message = (
            f"Fase {self.match_phase}: oponente colocou "
            f"{len(self.match_opponent_character_cards)} monstros"
            f" e deixou {len(self.match_opponent_reserve_cards)} na reserva."
        )
        if boss is not None:
            phase_message += (
                f" {boss.name} apareceu como chefe com {boss.hp} HP."
            )
        self._show_match_status(f"{phase_message} Prepare seu campo.")
        self._draw_match_board()

    def _finish_match(self, player_won, message):
        self._show_match_status(message)
        self._draw_match_board()
        self.after(
            250,
            lambda: self._show_message(
                "VITÓRIA" if player_won else "DERROTA",
                f"{message}\n\nVocê pode voltar e iniciar uma nova partida.",
            ),
        )

    def _show_match_status(self, message):
        if hasattr(self, "match_status_label") and self.match_status_label.winfo_exists():
            self.match_status_label.configure(text=message)

    def _prepare_match_card_image(self, card, width, height):
        image_name = self._find_image_name_for_card(card.name)
        if not image_name:
            return None
        image_path = self.image_dir / image_name
        if not image_path.exists():
            return None
        try:
            with Image.open(image_path) as image:
                return ImageOps.fit(
                    image.convert("RGB"),
                    (max(1, width), max(1, height)),
                    method=Image.Resampling.LANCZOS,
                )
        except (OSError, ValueError):
            return None

    def _select_play_mode(self, mode_number, mode_name):
        self._show_message(
            mode_name,
            f"O modo {mode_number:02d} estará disponível em breve.",
        )

    def _show_options(self):
        self._show_message(
            "OPÇÕES", "As opções do jogo serão adicionadas aqui."
        )

    def _show_message(self, title, message):
        self._clear_screen()
        page = ttk.Frame(self, style="App.TFrame", padding=0)
        page.pack(fill="both", expand=True)
        self._add_menu_background(page)
        tk.Button(page, text="<  VOLTAR", command=self._show_home).pack(
            anchor="w"
        )
        ttk.Label(page, text=title, style="Title.TLabel").pack(
            anchor="w", pady=(36, 8)
        )
        ttk.Label(page, text=message, style="Subtitle.TLabel").pack(anchor="w")

    def _open_deck(self, deck_name):
        self._clear_screen()
        self.show_collection_counts = False
        self.card_data = list(self.decks[deck_name])
        self.search_text.set("")
        self.type_filter.set("All types")

        self._build_header(deck_name)
        self._build_card_area()
        self._refresh_cards()

    def _build_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("App.TFrame", background="#10141b")
        style.configure("Toolbar.TFrame", background="#181e28")
        style.configure(
            "Title.TLabel",
            background="#10141b",
            foreground="#f5f1e8",
            font=("Georgia", 24, "bold"),
        )
        style.configure(
            "Subtitle.TLabel",
            background="#10141b",
            foreground="#8e9aaa",
            font=("Segoe UI", 10),
        )
        style.configure(
            "Count.TLabel",
            background="#181e28",
            foreground="#b9c4d0",
            font=("Segoe UI", 10, "bold"),
        )
        style.configure(
            "Toolbar.TLabel",
            background="#181e28",
            foreground="#cbd3dc",
            font=("Segoe UI", 9),
        )
        style.configure(
            "Search.TEntry",
            fieldbackground="#242c38",
            foreground="#f5f1e8",
            insertcolor="#f5f1e8",
            borderwidth=0,
        )
        style.configure(
            "Filter.TCombobox",
            fieldbackground="#242c38",
            foreground="#f5f1e8",
            selectbackground="#354254",
            selectforeground="#f5f1e8",
        )

    def _build_header(self, deck_name):
        header = ttk.Frame(self, style="App.TFrame", padding=(28, 24, 28, 18))
        header.pack(fill="x")
        tk.Button(header, text="<  DECKS", command=self._show_decks).pack(
            anchor="w", pady=(0, 16)
        )
        ttk.Label(
            header, text=f"{deck_name.upper()} DECK", style="Title.TLabel"
        ).pack(anchor="w")
        ttk.Label(
            header,
            text="Browse every card and its combat effect",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(4, 0))
        if deck_name not in self.base_decks:
            tk.Button(
                header,
                text="EDITAR DECK",
                command=lambda: self._show_deck_builder(deck_name),
                bg="#4d6f61",
                fg="#ffffff",
                activebackground="#638c7a",
                activeforeground="#ffffff",
                relief="flat",
                bd=0,
                padx=14,
                pady=8,
                font=("Segoe UI", 10, "bold"),
                cursor="hand2",
            ).pack(anchor="w", pady=(12, 0))

        toolbar = ttk.Frame(self, style="Toolbar.TFrame", padding=(14, 10))
        toolbar.pack(fill="x", padx=28, pady=(0, 18))
        ttk.Label(toolbar, text="SEARCH", style="Toolbar.TLabel").pack(
            side="left", padx=(0, 8)
        )
        ttk.Entry(
            toolbar,
            textvariable=self.search_text,
            style="Search.TEntry",
            width=28,
        ).pack(side="left", ipady=5, padx=(0, 18))
        ttk.Label(toolbar, text="TYPE", style="Toolbar.TLabel").pack(
            side="left", padx=(0, 8)
        )

        types = ["All types"] + sorted({card.type for card in self.card_data})
        ttk.Combobox(
            toolbar,
            textvariable=self.type_filter,
            values=types,
            state="readonly",
            style="Filter.TCombobox",
            width=15,
        ).pack(side="left", ipady=3)
        ttk.Label(toolbar, text="RARITY", style="Toolbar.TLabel").pack(
            side="left", padx=(18, 8)
        )
        rarities = ["All rarities"] + [
            rarity
            for rarity in ("C", "R", "SR", "UR")
            if any(self._card_rarity(card) == rarity for card in self.card_data)
        ]
        ttk.Combobox(
            toolbar,
            textvariable=self.rarity_filter,
            values=rarities,
            state="readonly",
            style="Filter.TCombobox",
            width=13,
        ).pack(side="left", ipady=3)
        ttk.Label(toolbar, text="COST", style="Toolbar.TLabel").pack(
            side="left", padx=(18, 8)
        )
        costs = ["All costs"] + [
            str(cost) for cost in sorted({card.cost for card in self.card_data})
        ]
        ttk.Combobox(
            toolbar,
            textvariable=self.cost_filter,
            values=costs,
            state="readonly",
            style="Filter.TCombobox",
            width=10,
        ).pack(side="left", ipady=3)
        ttk.Label(
            toolbar, textvariable=self.count_text, style="Count.TLabel"
        ).pack(side="right", padx=8)

    def _build_card_area(self):
        container = ttk.Frame(self, style="App.TFrame")
        container.pack(fill="both", expand=True, padx=28, pady=(0, 24))

        self.canvas = tk.Canvas(container, bg="#10141b", highlightthickness=0)
        scrollbar = ttk.Scrollbar(
            container, orient="vertical", command=self.canvas.yview
        )

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.canvas.bind("<Configure>", lambda e: self._refresh_cards())

    def _on_mousewheel(self, event):
        scroll_canvas = self.deck_list_canvas or self.canvas
        if scroll_canvas and scroll_canvas.winfo_exists():
            if getattr(event, "num", None) == 4:
                amount = -3
            elif getattr(event, "num", None) == 5:
                amount = 3
            else:
                delta = getattr(event, "delta", 0)
                amount = int(-delta / 120)
                if amount == 0 and delta:
                    amount = -1 if delta > 0 else 1
            scroll_canvas.yview_scroll(amount, "units")

    @staticmethod
    def _normalize_card_name(value):
        if not value:
            return ""
        return "".join(ch.lower() for ch in value if ch.isalnum())

    def _find_image_name_for_card(self, card_name):
        if not card_name:
            return None

        exact_name = self.IMAGE_FILES.get(card_name)
        if exact_name:
            return exact_name

        normalized_name = self._normalize_card_name(card_name)
        direct_match = next(
            (
                image_name
                for mapped_name, image_name in self.IMAGE_FILES.items()
                if self._normalize_card_name(mapped_name) == normalized_name
            ),
            None,
        )
        if direct_match:
            return direct_match

        image_candidates = []
        for image_path in sorted(self.image_dir.iterdir()):
            if not image_path.is_file():
                continue
            image_stem = image_path.stem
            if self._normalize_card_name(image_stem) == normalized_name:
                return image_path.name

            stem_tokens = set(
                part for part in self._normalize_card_name(image_stem).split() if part
            )
            card_tokens = set(
                part for part in self._normalize_card_name(card_name).split() if part
            )
            if not stem_tokens or not card_tokens:
                continue
            common_tokens = stem_tokens & card_tokens
            if common_tokens:
                image_candidates.append((len(common_tokens), image_path.name))

        if image_candidates:
            best_score, best_name = max(image_candidates, key=lambda item: item[0])
            if best_score >= 1:
                return best_name

        return f"{card_name}.png"

    def _prepare_card_image(self, card):
        image_name = self._find_image_name_for_card(card.name)
        image_path = self.image_dir / image_name
        if not image_path.exists():
            return None
        try:
            image = Image.open(image_path).convert("RGB")
        except (OSError, ValueError):
            return None

        image_box = ImageOps.fit(
            image,
            (self.IMAGE_WIDTH, self.IMAGE_HEIGHT),
            method=Image.Resampling.LANCZOS,
        )
        return image_box

    def _refresh_cards(self, *_):
        if not self.canvas or not self.canvas.winfo_exists():
            return

        query = self.search_text.get().strip().lower()
        selected_type = self.type_filter.get()
        selected_rarity = self.rarity_filter.get()
        selected_cost = self.cost_filter.get()

        visible_cards = [
            card
            for card in self.card_data
            if (
                not query
                or query in card.name.lower()
                or query in getattr(card, "element", "").lower()
            )
            and (selected_type == "All types" or card.type == selected_type)
            and (
                selected_rarity == "All rarities"
                or self._card_rarity(card) == selected_rarity
            )
            and (
                selected_cost == "All costs"
                or str(card.cost) == selected_cost
            )
        ]

        self.count_text.set(
            f"{len(visible_cards)} of {len(self.card_data)} cards"
        )
        self.card_view_id += 1
        self.card_image_items.clear()
        self.canvas.delete("all")

        canvas_width = self.canvas.winfo_width()
        if canvas_width <= 1:
            canvas_width = 1000

        pad_x = 16
        pad_y = 16

        cols = max(1, (canvas_width - pad_x) // (self.CARD_WIDTH + pad_x))
        total_grid_width = cols * self.CARD_WIDTH + (cols - 1) * pad_x
        start_x = max(pad_x, (canvas_width - total_grid_width) // 2)

        for index, card in enumerate(visible_cards):
            col = index % cols
            row = index // cols

            x = start_x + col * (self.CARD_WIDTH + pad_x)
            y = pad_y + row * (self.CARD_HEIGHT + pad_y)

            self._draw_card_on_canvas(
                card, x, y, self.CARD_WIDTH, self.CARD_HEIGHT
            )

        total_rows = (len(visible_cards) + cols - 1) // cols
        total_height = total_rows * (self.CARD_HEIGHT + pad_y) + pad_y
        self.canvas.configure(
            scrollregion=(0, 0, canvas_width, total_height)
        )

    def _draw_formatted_text(self, x, y, max_width, text, fill_color):
        words = text.split()
        cursor_x = x
        cursor_y = y
        line_height = 14

        font_normal = tkfont.Font(family="Segoe UI", size=8, weight="normal")
        font_bold = tkfont.Font(family="Segoe UI", size=8, weight="bold")

        space_width = font_normal.measure(" ")

        for word in words:
            is_bold = word.startswith("*")
            clean_word = word.replace("*", "")

            current_font = font_bold if is_bold else font_normal
            word_width = current_font.measure(clean_word)

            if cursor_x + word_width > x + max_width and cursor_x > x:
                cursor_x = x
                cursor_y += line_height

            self.canvas.create_text(
                cursor_x,
                cursor_y,
                text=clean_word,
                fill=fill_color,
                font=current_font,
                anchor="nw",
            )

            cursor_x += word_width + space_width

    def _draw_card_on_canvas(self, card, x, y, width, height):
        element_name = getattr(card, "element", "")
        element_color = self.ELEMENT_COLORS.get(element_name, "#ffffff")

        self._draw_rounded_rectangle(
            x,
            y,
            x + width,
            y + height,
            radius=self.CORNER_RADIUS,
            fill="#e8ecf2",
            outline=element_color,
            width=2,
        )

        self.canvas.create_text(
            x + 18,
            y + 18,
            text=card.name.upper(),
            fill="#2b3240",
            font=("Segoe UI", 12, "bold"),
            anchor="nw",
            width=width - 110,
        )

        self.canvas.create_oval(
            x + width - 42,
            y + 14,
            x + width - 18,
            y + 38,
            fill="#d2d8e3",
            outline=element_color,
            width=1.5,
        )
        if element_name:
            self.canvas.create_text(
                x + width - 30,
                y + 26,
                text=element_name[0].upper(),
                fill=element_color,
                font=("Segoe UI", 9, "bold"),
            )

        self.canvas.create_rectangle(
            x + width - 70,
            y + 42,
            x + width - 18,
            y + 58,
            fill="#d2d8e3",
            outline="#c0c8d6",
        )
        self.canvas.create_text(
            x + width - 44,
            y + 50,
            text=card.type.upper(),
            fill="#3b4352",
            font=("Consolas", 7, "bold"),
        )

        img_x = x + (width - self.IMAGE_WIDTH) // 2
        img_y = y + 66

        self.canvas.create_rectangle(
            img_x,
            img_y,
            img_x + self.IMAGE_WIDTH,
            img_y + self.IMAGE_HEIGHT,
            fill="#181d26",
            outline="#3b4352",
        )

        img_item = self.canvas.create_image(img_x, img_y, anchor="nw")
        self.card_image_items[id(card)] = img_item
        self.after_idle(
            lambda: self._load_image_for_canvas(
                card, img_item, self.card_view_id
            )
        )

        cost_y = img_y + 12
        self.canvas.create_oval(
            x + 14,
            cost_y,
            x + 44,
            cost_y + 30,
            fill="#ffffff",
            outline=element_color,
            width=2,
        )
        self.canvas.create_text(
            x + 29,
            cost_y + 15,
            text=str(card.cost),
            fill="#10141b",
            font=("Segoe UI", 10, "bold"),
        )

        rarity_styles = {
            "C": ("#9ea7b0", "#10141b"),
            "R": ("#dcdde1", "#10141b"),
            "SR": ("#e6b800", "#10141b"),
            "UR": ("#1d4e62", "#ffffff"),
        }
        rarity_text = self._card_rarity(card).upper()
        rarity_bg, rarity_fg = rarity_styles.get(
            rarity_text, rarity_styles["C"]
        )

        self.canvas.create_rectangle(
            x + width - 42,
            cost_y + 4,
            x + width - 20,
            cost_y + 24,
            fill=rarity_bg,
            outline="",
        )
        self.canvas.create_text(
            x + width - 31,
            cost_y + 14,
            text=rarity_text,
            fill=rarity_fg,
            font=("Segoe UI", 7, "bold"),
        )

        tag_y = img_y + self.IMAGE_HEIGHT + 8
        tag_str = (
            card.tag if isinstance(card.tag, str) else " / ".join(card.tag)
        )
        tags = [t.strip().upper() for t in tag_str.split("/") if t.strip()]

        current_tag_x = x + 18
        for t in tags[:2]:
            tag_width = len(t) * 7 + 16
            self.canvas.create_rectangle(
                current_tag_x,
                tag_y,
                current_tag_x + tag_width,
                tag_y + 20,
                fill="#d2d8e3",
                outline="#c0c8d6",
            )
            self.canvas.create_text(
                current_tag_x + tag_width / 2,
                tag_y + 10,
                text=t,
                fill="#3b4352",
                font=("Consolas", 7, "bold"),
            )
            current_tag_x += tag_width + 8

        passive_y = tag_y + 24
        passive_height = 84
        self.canvas.create_rectangle(
            x + 18,
            passive_y,
            x + width - 18,
            passive_y + passive_height,
            fill="#dce2ec",
            outline="#c0c8d6",
        )

        self._draw_formatted_text(
            x + 24, passive_y + 6, width - 50, card.passive, "#2b3240"
        )

        footer_y = passive_y + passive_height + 4
        stats = []
        if hasattr(card, "power"):
            stats.append(f"DP {card.power}")
        if hasattr(card, "hp"):
            stats.append(f"HP {card.hp}")
        if hasattr(card, "duration"):
            stats.append(f"DUR {card.duration}")

        stats_text = (
            "   ".join(stats) if stats else f"TYPE: {card.type.upper()}"
        )

        self.canvas.create_text(
            x + 22,
            footer_y,
            fill="#6c7a8e",
            font=("Consolas", 8),
            anchor="nw",
        )

        self.canvas.create_text(
            x + width - 22,
            footer_y,
            text=stats_text,
            fill="#10141b",
            font=("Segoe UI", 9, "bold"),
            anchor="ne",
        )

        if self.show_collection_counts:
            store_names = {store_card.name for store_card in self.store_cards}
            copies = self._card_copy_limit(card)
            indicator_x = x + width - 34
            indicator_y = y + height - 34
            self.canvas.create_oval(
                indicator_x - 18,
                indicator_y - 18,
                indicator_x + 18,
                indicator_y + 18,
                fill="#354254",
                outline="#f5f1e8",
                width=2,
            )
            self.canvas.create_text(
                indicator_x,
                indicator_y,
                text=f"{copies}/3",
                fill="#ffffff",
                font=("Segoe UI", 8, "bold"),
            )

    def _load_image_for_canvas(self, card, image_item_id, view_id):
        if view_id != self.card_view_id or not self.canvas.winfo_exists():
            return

        if card.name in self.image_cache:
            photo = self.image_cache[card.name]
            if photo is not None:
                self.canvas.itemconfig(image_item_id, image=photo)
            return

        future = self.image_futures.get(card.name)
        if future is None:
            future = self.image_executor.submit(
                self._prepare_card_image, card
            )
            self.image_futures[card.name] = future

        self.after(
            30,
            lambda: self._finish_canvas_image_load(
                card, image_item_id, future, view_id
            ),
        )

    def _finish_canvas_image_load(self, card, image_item_id, future, view_id):
        if view_id != self.card_view_id or not self.canvas.winfo_exists():
            return

        if not future.done():
            self.after(
                30,
                lambda: self._finish_canvas_image_load(
                    card, image_item_id, future, view_id
                ),
            )
            return

        try:
            image = future.result()
        except Exception:
            image = None

        if image is None:
            self.image_cache[card.name] = None
            return

        photo = ImageTk.PhotoImage(image)
        self.image_cache[card.name] = photo
        self.canvas.itemconfig(image_item_id, image=photo)


if __name__ == "__main__":
    CardBrowser().mainloop()