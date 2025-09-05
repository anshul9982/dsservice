from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Optional

class ExpenseSchema(BaseModel):
    amount: Optional[str] = Field(title="expense", description="The amount of the transaction in INR")
    transaction_type: Optional[str] = Field(title="transaction_type", description="The type of transaction, either 'debit' or 'credit'")
    date: Optional[str] = Field(title= "date", description="The date of the transaction in YYYY-MM-DD format")
    time: Optional[str] = Field(title="time", description="The time of the transaction in HH:MM format")
    merchant: Optional[str] = Field(title="merchant", description="The name of the merchant or payee")
    balance: Optional[float] = Field(title="balance", description="The remaining account balance after the transaction in INR")
    currency: Optional[str] = Field("INR", description="The currency of the transaction, default is INR")
    description: Optional[str] = Field(title="description", description="A description of the transaction, if available")
