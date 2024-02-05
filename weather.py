from requests_html import HTMLSession

def get_weather(query="pune"):
    # Set up an HTML session
    session = HTMLSession()

    # Define the URL with the weather query
    url = f"https://www.google.com/search?q=weather+{query}&sca_esv=599077546&rlz=1C1VDKB_enIN1064IN1064&sxsrf=ACQVn09maDF0lRAnRjrHKyuOEJRTIi4exw%3A1705484542903&ei=_qCnZYTcNrqQnesPn7KF4A8&ved=0ahUKEwiE0-WCkeSDAxU6SGcHHR9ZAfwQ4dUDCBA&uact=5&oq=weather+pune&gs_lp=Egxnd3Mtd2l6LXNlcnAiDHdlYXRoZXIgcHVuZTIPECMYgAQYigUYJxhGGIACMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMhkQABiABBiKBRhGGIACGJcFGIwFGN0E2AEBSMEkUK4DWOoccAF4AZABAJgBwAOgAYMVqgEJMC4yLjguMC4xuAEDyAEA-AEBwgIKEAAYRxjWBBiwA8ICEBAAGIAEGIoFGEMYyQMYsAPCAg0QABiABBiKBRhDGLADwgIKECMYgAQYigUYJ8ICEBAAGIAEGBQYhwIYsQMYgwHCAgoQABiABBiKBRhDwgIQEAAYgAQYFBiHAhixAxjJA8ICCBAAGIAEGLEDwgILEAAYgAQYsQMYgwHCAhMQABiABBgUGIcCGLEDGIMBGMkDwgILEAAYgAQYigUYkgPCAgsQABiABBiKBRiRAsICDhAAGIAEGIoFGLEDGIMB4gMEGAAgQYgGAZAGCroGBggBEAEYEw&sclient=gws-wiz-serp"

    # Make the request with a specific user agent
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    response = session.get(url, headers=headers)

    # Extract weather information from the HTML response
    temperature = response.html.find('span#wob_tm', first=True).text
    unit = "°C"
    description = response.html.find('span#wob_dc', first=True).text

    # Return the formatted weather information with unit
    return f"{temperature} {unit} {description}"

