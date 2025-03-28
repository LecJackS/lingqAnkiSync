from .Converter import ConvertAnkiCardsToLingqs, ConvertLingqsToAnkiCards
from .AnkiHandler import CreateNotesFromCards, GetAllCardsInDeck, GetAllDeckNames
from .LingqApi import LingqApi
from .Config import Config
from typing import List

class ActionHandler:
    def __init__(self, addonManager):
        self.config = Config(addonManager)

    def ImportLingqsToAnki(self, deckName:str, import_knowns: bool) -> int:
        apiKey = self.GetApiKey()
        languageCode = self.GetLanguageCode()
        statusToInterval = self.config.GetStatusToInterval()

        lingqs = LingqApi(apiKey, languageCode, import_knowns).GetLingqs()
        cards = ConvertLingqsToAnkiCards(lingqs, statusToInterval)
        return CreateNotesFromCards(cards, deckName)

    def SyncLingqStatusToLingq(self, deckName) -> int:
        apiKey = self.config.GetApiKey()
        languageCode = self.config.GetLanguageCode()
        statusToInterval = self.config.GetStatusToInterval()
        
        cards = GetAllCardsInDeck(deckName)
        lingqs = ConvertAnkiCardsToLingqs(cards, statusToInterval)
        return LingqApi(apiKey, languageCode).SyncStatusesToLingq(lingqs)

    def SetConfigs(self, apiKey, languageCode):
        self.config.SetApiKey(apiKey)
        self.config.SetLanguageCode(languageCode)

    def GetDeckNames(self) -> List:
        return GetAllDeckNames()

    def GetApiKey(self) -> str:
        return self.config.GetApiKey()

    def GetLanguageCode(self) -> str:
        return self.config.GetLanguageCode()