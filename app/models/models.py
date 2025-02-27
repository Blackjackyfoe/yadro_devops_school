from pydantic import BaseModel, Field
from typing import Optional, Dict

class CurrencyQueryParams(BaseModel):
    currency: Optional[str] = Field(
        None,
        example="USD",
        description="The currency follows the ISO 4217 standard. If the parameter is not provided, return all available currencies from the Central Bank of Russia along with their exchange rates against the Russian ruble."
    )
    date: Optional[str] = Field(
        None,
        example="2016-01-06",
        description="The date follows the YYYY-MM-DD format. If not provided, the current date is used."
    )

class CurrencyResponse(BaseModel):
    service: str = Field("currency")
    data: Optional[Dict[str, float]] = Field(default=None)
    error: Optional[str] = Field(
        default=None,
        description="Description of an error."
    )
