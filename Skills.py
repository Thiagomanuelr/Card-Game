# Boss Cards for Celestial Deck

import inspect

import cartas as card_data


class CardSkill:
    def __init__(self, card=None):
        self.card = card if card is not None else self.card_class()
        self.name = getattr(self, "skill_name", self.card.name)
        self.skill_number = self.number
        self.energy_cost = 1
        self.description = getattr(self.card, "passive", "")


class AetherSkill(CardSkill):
    card_class = card_data.Aether

    def _deal_damage(self, target, multiplier, element=None, player=None):
        if not hasattr(target, "hp"):
            raise TypeError("O alvo precisa ter um atributo 'hp'.")
        

        damage = int(self.card.power * multiplier)
        target.hp = max(0, target.hp - damage)
        result = {"damage": damage, "element": element}

        if element is not None:
            target.last_damage_element = element

        if self.generates_elemental_energy:
            if isinstance(player, dict):
                player["elemental_energy"] = player.get("elemental_energy", 0) + 1
            else:
                player.elemental_energy = getattr(player, "elemental_energy", 0) + 1
            result["elemental_energy_generated"] = 1

        return result


class AetherSlash(AetherSkill):
    number = 1
    skill_name = "Aether Slash"
    generates_elemental_energy = False

    def use(self, target):
        return self._deal_damage(target, 0.5)


class AetherElementalPulse(AetherSkill):
    number = 2
    skill_name = "Aether Elemental Pulse"
    generates_elemental_energy = False
    elements = {"Pyro", "Hydro", "Cryo", "Electro", "Dendro", "Anemo", "Geo"}

    def use(self, target, element):
        if element not in self.elements:
            raise ValueError(f"Elemento inválido: {element}")
        return self._deal_damage(target, 0.8, element=element)


class AetherRegen(AetherSkill):
    number = 3
    skill_name = "Aether Regen"
    generates_elemental_energy = True

    def use(self, target, player=None):
        return self._deal_damage(target, 0.5, element="Elemental", player=player)


CUSTOM_CARD_SKILLS = {
    card_data.Aether: (AetherSlash, AetherElementalPulse, AetherRegen),
}


def _build_card_skill_classes():
    skill_classes = {}
    seen_cards = set()

    for candidate in vars(card_data).values():
        if not inspect.isclass(candidate) or candidate.__module__ != card_data.__name__:
            continue

        try:
            card = candidate()
        except TypeError:
            continue

        if not hasattr(card, "name") or not hasattr(card, "cost") or candidate in seen_cards:
            continue

        seen_cards.add(candidate)
        if candidate in CUSTOM_CARD_SKILLS:
            skill_classes[candidate] = CUSTOM_CARD_SKILLS[candidate]
            continue

        skill_count = min(max(int(card.cost), 0), 4)
        card_skills = []

        for skill_number in range(1, skill_count + 1):
            skill_class_name = f"{candidate.__name__}Skill{skill_number}"
            skill_class = type(
                skill_class_name,
                (CardSkill,),
                {"card_class": candidate, "number": skill_number},
            )
            globals()[skill_class_name] = skill_class
            card_skills.append(skill_class)

        skill_classes[candidate] = tuple(card_skills)

    return skill_classes


CARD_SKILL_CLASSES = _build_card_skill_classes()


def get_card_skills(card):
    """Return the skill instances associated with a card or card class."""
    card_class = card if inspect.isclass(card) else type(card)
    card_instance = card() if inspect.isclass(card) else card
    return [skill_class(card_instance) for skill_class in CARD_SKILL_CLASSES[card_class]]




