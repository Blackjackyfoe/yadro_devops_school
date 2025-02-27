from fastapi import APIRouter, Depends
from app.config import settings
from app.models.models import CurrencyQueryParams, CurrencyResponse
import requests
from app.services.parserXml2Json import parseXML
from app.services.requestCBR import requestCBR
from app.services.validateData import validateData

from xml.etree import ElementTree
import os
from datetime import datetime

router = APIRouter(prefix="/info")

@router.get("/currency", response_model=CurrencyResponse)
async def get_currency_info(query: CurrencyQueryParams = Depends()):
    """
    Endpoint for retrieving exchange rates from the Central Bank of Russia.
    Query Parameters:

        -currency: Optional (ISO 4217, e.g., USD). If not specified, returns all exchange rates.
        -date: Optional (format YYYY-MM-DD). If not specified, the current date is used.

    Returns JSON:

        -service: "currency"
        -data: { "USD": 33.4013, "EUR": 40.1234, ... } (if no errors)
        -error: A string describing the error, if something went wrong.
    """

    try:
        dt = validateData(query.date) if query.date else datetime.now()
    except ValueError as e:
        return CurrencyResponse(service="currency", error=str(e))


    try:
        xml_data = requestCBR(dt)
    except ConnectionError as e:
        return CurrencyResponse(service="currency", error=str(e))


    try:
        currencies = parseXML(xml_data)
    except ValueError as e:
        return CurrencyResponse(service="currency", error=str(e))

    if query.currency:
        currency_upper = query.currency.upper()
        if currency_upper not in currencies:
            return CurrencyResponse(
                service="currency",
                error=f"Currency '{query.currency}' not found for date {dt.strftime('%Y-%m-%d')}"
            )
        data = {currency_upper: currencies[currency_upper]}
    else:
        data = currencies

    return CurrencyResponse(
        service="currency",
        data=data
    )