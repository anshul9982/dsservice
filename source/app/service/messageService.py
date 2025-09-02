from ..utilis.messageUtil import MessageUtil
from .llmService import LLMService
class MessageService:
    def __init__(self):
        self.messageUtil = MessageUtil()
        self.llmService = LLMService()

    def process_message(self, message):
        if self.messageUtil.isBankSms(message):
            response = self.llmService.runLLM(message)
            return response
        else:
            return None