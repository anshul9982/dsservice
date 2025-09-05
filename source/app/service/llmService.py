from typing import Optional
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field
from .ExpenseSchema import ExpenseSchema
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv, dotenv_values
import os


class LLMService:
    def __init__(self):
        load_dotenv()
        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an expert extraction algorithm."
                    "Only extract the required information and respond in JSON format."
                    "If the information is not present, respond with null values."
                    "Do not add any additional information."
                    "If the message is not a bank transaction SMS, respond with null values."
                ),
                (
                    "human", "{text}"
                )
            ]
        )

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash-latest",
            temperature=0,
        )
        self.runnable = self.prompt | self.llm.with_structured_output(schema=ExpenseSchema)

    def runLLM(self, message):
        return self.runnable.invoke({"text": message})