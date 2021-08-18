import PySimpleGUI as sg
from bs4 import BeautifulSoup
import htmlparser as hp
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# The theme for the appearance of the application
sg.theme("reddit")
mobile = False
live = True

# Path for the gecko driver
driver_path = "geckodriver.exe"


if live is True:
    # Gets the banner for editing from the website
    opt = Options()
    opt.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=driver_path, options=opt)
    driver.get("https://rdkb.com/")
    primary_grid = driver.find_elements_by_id("primary-grid")[0]
    in_file = primary_grid.get_attribute("outerHTML")
    driver.quit()
    soup = BeautifulSoup(in_file, 'html.parser')
else:
    # Gets the banner for editing from file
    with open("FT_Banner.html") as in_file:
        soup = BeautifulSoup(in_file, 'html.parser')
        in_file.close()
edit_obj = hp.Editable(soup)


def shorten_sub(text: str, length=26):
    """
    Shortens the text to the given length and truncates it with a ellipse
    :param text: The text to shorten
    :param length: The length of the shortened text+3
    :return:
    """
    if mobile:
        if len(text) >= length:
            return text[:length-1] + "..."
        else:
            return text
    else:
        return text


def absolute_to_relative(path):
    """
    Takes a file path from the web server and turns it to a relative url
    :param path: The path of the file, ex: X:\\Portals\\0\\EnvironmentalServices\\images\\Normal-02.png
    :return: The relative path
    """
    path = path.replace("\\", "/")
    try:
        path = path[path.find("Portals")-1:]
    except Exception:
        print("Could not find image in portals")
    return path


def update_panel(dropdown_value: str, values: dict):
    """
    Updates the given panel for the banner
    :param dropdown_value: The panel the app is currently trying
    :param values:
    :return:
    """
    if dropdown_value == "Main":
        header, text, image = values["header"], shorten_sub(values["text"]), values["img"]
        hp.update_main(edit_obj, header, text, image)
    elif dropdown_value == "News":
        header, text, image = values["header"], shorten_sub(values["text"]), values["img"]
        hp.update_news(edit_obj, header, text, image)
    elif dropdown_value == "Water":
        header, text, image = values["header"], shorten_sub(values["text"]), values["img"]
        hp.update_water(edit_obj, header, text, image)
    elif dropdown_value == "Meeting":
        header, text, image = values["header"], shorten_sub(values["text"]), values["img"]
        hp.update_meeting(edit_obj, header, text, image)
    elif dropdown_value == "About":
        header, text, image = values["header"], shorten_sub(values["text"]), values["img"]
        hp.update_about(edit_obj, header, text, image)
    elif dropdown_value == "Opportunities":
        header, text, image = values["header"], shorten_sub(values["text"]), values["img"]
        hp.update_opp(edit_obj, header, text, image)
    elif dropdown_value == "Blue":
        text, link = values["text"], values["link"]
        hp.update_blue(edit_obj, link, text)


def get_layout(name="Main"):
    sub_layout = [[]]
    if name in ["Main", "News", "Water", "About", "Opportunities", "Meeting"]:
        sub_layout = [[sg.Text(f"Editing {name}", font=("Helvetica", 20))],
                      [sg.Text("Header", size=(12, None)), sg.Input(key="header")],
                      [sg.Text("Sub-Text", size=(12, None)), sg.Input(key="text")],
                      [sg.FilesBrowse("Image", target="img", size=(12, None)), sg.Input(key="img")]]
    if name == "Blue":
        sub_layout = [[sg.Text(f"Editing {name}", font=("Helvetica", 20))],
                      [sg.Text("Link", size=(12, None)), sg.Input(key="link")],
                      [sg.Text("Text", size=(12, None)), sg.Input(key="text")]]
    return [
        [sg.Button("Switch", key="ref"),
         sg.Combo(values=["Main", "News", "Water", "About", "Blue", "Meeting", "Opportunities"], key="opt"),
         sg.Image(filename=f"images/{name}.png")],
        [sg.Text("_"*60)],
        [sg.Column(layout=sub_layout, key="col")],
        [sg.Button("Exit", key="ext", button_color="red"), sg.Button("Save & Exit", key="save&ext"),
         sg.Button("Save", key="save"), sg.Button("Copy to Clipboard", key="copy")]]


if __name__ == "__main__":
    layout = get_layout()
    window = sg.Window(title="Edit Main", layout=layout, grab_anywhere=True, font="IBM-Plex-Sans",
                       icon="BannerIcon.ico")
    name = "Main"
    while True:
        event, value = window.read()
        if event == "save&ext":
            update_panel(name, value)
            edit_obj.export()
            break

        if event == "ref":
            print("Refreshed")
            dv = value["opt"]
            update_panel(name, value)
            if len(dv) != 0:
                name = dv
                layout = get_layout(name)
                last_loc = window.current_location()
                window.close()
                window = sg.Window(title=f"Edit {name}", layout=layout, location=last_loc,
                                   grab_anywhere=True, font="IBM-Plex-Sans", icon="BannerIcon.ico")

        if event == "save":
            update_panel(name, value)
            edit_obj.export()
            print(edit_obj)

        if event == "copy":
            update_panel(name, value)
            print(edit_obj)
            sg.clipboard_set(edit_obj)

        if event == sg.WINDOW_CLOSED or event == "ext":
            break

    window.close()
