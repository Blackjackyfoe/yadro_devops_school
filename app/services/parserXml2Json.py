import xml.etree.ElementTree as ET


def parseXML(xml_data: str) -> dict:
    """Parses XML response from CBR and extracts currency rates."""
    try:
        root = ET.fromstring(xml_data)
        currencies = {}
        for valute in root.findall("Valute"):
            char_code = valute.find("CharCode").text
            value_str = valute.find("Value").text.replace(",", ".")
            try:
                currencies[char_code] = round(float(value_str), 4)
            except ValueError:
                continue
        return currencies
    except ET.ParseError:
        raise ValueError("Failed to parse XML from CBR. The response format might have changed.")