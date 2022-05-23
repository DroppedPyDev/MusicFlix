from typing import Dict, List
from config import admins


admins: Dict[int, List[int]] = {}


def set(chat_id: int, admins_: List[int]):
    admins[chat_id] = admins_


def get(chat_id: int) -> List[int]:
    if chat_id in admins:
        return admins[chat_id]
    return []

# എന്താടാ മോനെ അടിച്ചു അടിച്ചു മാറ്റാൻ വന്നതാണോ? നാണം വേണം കേട്ടോ കുറച്ച് 😜😹.
# എന്തായാലും എടുത്തു bug ആരികും മുഴുവൻ നോക്കി ഒക്കെ add ആക്ക് കേട്ടോ 🤭
