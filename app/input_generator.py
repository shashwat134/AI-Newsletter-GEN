from datetime import datetime

COLOR_PRIMARY = "#2F72FF"
COLOR_TEXT = "#333333"
COLOR_BACKGROUND = "#F4F7F6"
COLOR_WHITE = "#FFFFFF"

def generate_html_email(data: dict) -> str:
    today = datetime.now().strftime("%d %B %Y")
    code_id = datetime.now().strftime("#NEWS-%Y-%m-%d")
    html = f"""
    <!DOCTYPE html><html><body><h1>{data.get('headline','')}</h1></body></html>
    """
    return html