# Edit-RDKB-Banner
A utility application made to run on windows computers where the banner from the RDKB homepage is scrapped and turned into an editable object

## Making your own changes to the banner
For live pulling from the website you will need the gecko(Firefox) driver which is firefox running in the background to surf the web

### Dependecies
The packaged application requires nothing else, however, if you want to make changes to the application the python libraries used are:
- PySimpleGUI
  - `pip install pysimplegui`
- Selenium
  - `pip install selenium`
- bs4(Beautiful Soup 4)
  - `pip install beautifulsoup4`
- Packaged with auto-py-to-exe(Auto Py to Exe)
  - Install `pip install auto-py-to-exe`
  - Run to package `auto-py-to-exe` or `python -m auto_py_to_exe`

## Using the Application
While previous versions saved locally exclusively, this and future versions pull from the web so that the version that you are editing is the same as the one on the website.

Typical Use:
1. Launch the application
2. **Select** the section you would like to edit from the drop-down menu and press **switch**, the UI will tell you which section you are currently editing.
3. Change the **fields** and they will change what is on the page
4. Press copy to clipboard to **copy** the html code to your **clipboard**
5. Go to the website, edit the front banner, and **paste** the html code into the **source**
6. If the changes are good, then you can save the html code to your local machine by pressing the **save** or **save and exit** buttons
  (While this was required on past versions, this current version pulls from the live site and creates a copy to edit locally in memory. You should only save after you are sure that the changes do not break the banner. This feature is now primarily for backup purposes)
