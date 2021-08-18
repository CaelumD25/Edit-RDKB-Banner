from bs4 import BeautifulSoup


def update_main(edit_obj, header, txt, img):
    edit_obj.set_main_header(header)
    edit_obj.set_main_text(txt)
    edit_obj.set_main_img(img)


def update_news(edit_obj, header, txt, img):
    edit_obj.set_news_header(header)
    edit_obj.set_news_text(txt)
    edit_obj.set_news_img(img)


def update_water(edit_obj, header, txt, img):
    edit_obj.set_water_header(header)
    edit_obj.set_water_text(txt)
    edit_obj.set_water_img(img)


def update_about(edit_obj, header, txt, img):
    edit_obj.set_about_header(header)
    edit_obj.set_about_text(txt)
    edit_obj.set_about_img(img)


def update_opp(edit_obj, header, txt, img):
    edit_obj.set_opp_header(header)
    edit_obj.set_opp_text(txt)
    edit_obj.set_opp_img(img)


def update_meeting(edit_obj, header, txt, img):
    edit_obj.set_meeting_header(header)
    edit_obj.set_meeting_text(txt)
    edit_obj.set_meeting_img(img)


def update_blue(edit_obj, link, txt):
    edit_obj.set_blue_link(link)
    edit_obj.set_blue_text(txt)


class Editable:
    def __init__(self, soup):
        self.soup = soup
        # All of the tags from the html file, if these break then the id in the HTML document do not match
        self.news_header_tag = self.soup.select("#news-header")[0]
        self.news_text_tag = self.soup.select("#news-text")[0]
        self.news_img_tag = self.soup.select("#news-img")[0]

        self.water_header_tag = self.soup.select("#water-header-tag")[0]
        self.water_text_tag = self.soup.select("#water-text-tag")[0]
        self.water_img_tag = self.soup.select("#water-img-tag")[0]

        self.opp_header_tag = self.soup.select("#opp-img-tag")[0]
        self.opp_text_tag = self.soup.select("#opp-text-tag")[0]
        self.opp_img_tag = self.soup.select("#opp-img-tag")[0]

        self.blue_text_tag = self.soup.select("#blue-text-tag")[0]
        self.blue_link_tag = self.soup.select("#blue-link-tag")[0]

        self.meeting_header_tag = self.soup.select("#meeting-header-tag")[0]
        self.meeting_text_tag = self.soup.select("#meeting-text-tag")[0]
        self.meeting_img_tag = self.soup.select("#meeting-img-tag")[0]

        self.about_header_tag = self.soup.select("#about-header-tag")[0]
        self.about_text_tag = self.soup.select("#about-text-tag")[0]
        self.about_img_tag = self.soup.select("#about-img-tag")[0]

        self.main_header_tag = self.soup.select("#main-header-tag")[0]
        self.main_text_tag = self.soup.select("#main-text-tag")[0]
        self.main_img_tag = self.soup.select("#main-img-tag")[0]

        self.br = BeautifulSoup("<br />", "html.parser")

    def __str__(self):
        return str(self.soup.prettify())

    def __repr__(self):
        return str(self.soup)

    def set_main_header(self, txt):
        if len(txt) != 0:
            self.main_header_tag.string = txt

    def set_main_text(self, txt):
        if len(txt) != 0:
            self.main_text_tag.string = txt

    def set_main_img(self, img):
        if len(img) != 0:
            self.main_img_tag["src"] = img

    def set_about_header(self, txt):
        if len(txt) != 0:
            self.about_header_tag.string = txt

    def set_about_text(self, txt):
        if len(txt) != 0:
            self.about_text_tag.string = txt

    def set_about_img(self, img):
        if len(img) != 0:
            self.about_img_tag["src"] = img

    def set_meeting_header(self, txt):
        if len(txt) != 0:
            self.meeting_header_tag.string = txt

    def set_meeting_text(self, txt):
        if len(txt) != 0:
            self.meeting_text_tag.string = txt

    def set_meeting_img(self, img):
        if len(img) != 0:
            self.meeting_img_tag["src"] = img

    def set_opp_header(self, txt):
        if len(txt) != 0:
            self.opp_header_tag.string = txt

    def set_opp_text(self, txt):
        if len(txt) != 0:
            self.opp_text_tag.string = txt

    def set_opp_img(self, img):
        if len(img) != 0:
            self.opp_img_tag["src"] = img

    def set_water_header(self, txt):
        if len(txt) != 0:
            self.water_header_tag.string = txt

    def set_water_text(self, txt):
        if len(txt) != 0:
            self.water_text_tag.string = txt

    def set_water_img(self, img):
        if len(img) != 0:
            self.water_img_tag["src"] = img

    def set_news_header(self, txt):
        if len(txt) != 0:
            self.news_header_tag.string = txt

    def set_news_text(self, txt):
        if len(txt) != 0:
            self.news_text_tag.string = txt

    def set_news_img(self, img):
        if len(img) != 0:
            self.news_img_tag["src"] = img

    def set_blue_link(self, link):
        if len(link) != 0:
            self.blue_link_tag["href"] = link

    def set_blue_text(self, txt):
        if len(txt) != 0:
            self.blue_text_tag.string = txt
            self.blue_text_tag.insert(0, self.br)

    def export(self):
        """
        Exports the soup
        :return: Nothing
        """
        with open("FT_Banner.html", "w") as out_file:
            out_file.write(str(self.soup))
        out_file.close()



