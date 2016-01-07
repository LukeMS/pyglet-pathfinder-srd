import json


class PygletEncodedText(object):
    blue = "{color (63, 63, 255, 223)}"
    white = "{color (223,223,255, 223)}"
    light_gray = "{color (160,160,160, 223)}"

    tab_size = 8
    color = light_gray
    title_color = white

    regular = (
        """{font_name 'Fontin'}{.align "left"}{bold False}{font_size 12}""" +
        """{italic False}""" + color
    )
    par = paragraph = (
        "\n\n" +
        (" " * tab_size) +
        regular
    )
    t1 = title1 = title_1 = (
        """{font_name 'Fontin'}{.align "center"}{bold True}{font_size 28}""" +
        """{italic True}{indent 0}""" + title_color
    )
    t2 = title2 = title_2 = (
        """{font_size 6}""" +
        "\n\n" + "\n\n" +
        """{font_name 'Fontin'}{.align "center"}{bold True}{font_size 14}""" +
        """{italic False}""" + title_color
    )
    t3 = title3 = title_3 = (
        """{font_size 4}""" +
        "\n\n" + "\n\n" +
        (" " * tab_size) +
        """{font_name 'Fontin'}{.align "left"}{bold True}{font_size 12}""" +
        """{italic True}""" + title_color
    )
    table = (
        "\n\n" +
        """{font_name 'Courier New'}{.align "center"}{bold True}"""
    )
    credits = (
        "\n\n" +
        t3 + ("#" * 12) +
        "\n\n" +
        t3 + "Section 15 - Copyright Notice" +
        color +
        par +
        "\n\n"
    )

    def style(self, format, string=''):
        if format == 't1':
            result = (
                getattr(self, format) +
                "~~ {} ~~".format(string) +
                "\n\n" + getattr(self, 'regular')
            )
        elif format == 't1-':
            result = (
                getattr(self, 't1') +
                "~~~ {} ~~~".format(string)
            )
        elif format == 't2':
            result = (
                getattr(self, format) +
                "> {} <".format(string) +
                "\n\n" + getattr(self, 'regular')
            )
        elif format in ['blue']:
            result = (
                getattr(self, format) +
                string +
                getattr(self, 'regular')
            )

        else:
            result = getattr(self, format) + string
        return result

pyglet_encoded_text_shortcut = PygletEncodedText()


def style(format, string=''):
    return pyglet_encoded_text_shortcut.style(format, string)

DISCLAIMER = {
    "disclaimer": (
        style('t1', "Caves & Lizards") +
        ("\n\n" * 2) +
        style('t1', "DISCLAIMER") +
        style('par') +
        """This game's core rules are built upon Open Game Content (OGC). This game is not published, endorsed, or specifically approved by the OGC's copyright owners. The use of the OGC relies only on the license granted by the Open Game License (OGL) itself.""" +
        style('par') +
        style('par') +
        """The full OGL and the OGC as in the official (or community maintained, when specified) System Reference Document are available through the "Open Game Content" option in the "Main Menu" (or during the game, at any time, by pressing the F1 key).""" +
        style('par') +
        style('par') +
        """The game art (graphics, sound, etc.) is used under varying licenses. A complete list with each of the multimedia resource's credits and license is available through the "Credits" (for simple textual information) or the "Art Gallery" options on the "Main Menu".""" +
        style('par') +
        style('par') +
        """The game and its source code is released under GNU GPL v3.""" +

        style('par') +
        style('credits') +
        """Original game concept and design by: Lucas Siqueira"""
    )
}
