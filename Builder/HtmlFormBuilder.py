from html import escape

from Builder.AbstractFormBuilder import AbstractFormBuilder


class HtmlFormBuilder(AbstractFormBuilder):
    def __index__(self):
        self.title = 'HtmlFormBuilder'
        self.items = {}

    def add_title(self, title):
        super().add_title(escape(title))

    def add_lable(self, text, row, column, **kwargs):
        self.items[(row, column)] = ('<td><label for="{}">{}:</label></td>').format(kwargs["target"], escape(text))

    def add_entry(self, variable, row, column, **kwargs):
        html = """<td><input name="{}" type="{}" /></td>""".format(variable, kwargs.get("kind", "text"))
        self.items[(row, column)] = html

    def form(self):
        html = ["<!doctype html>\n<html><head><title>{}</title></head>"
                "<body>".format(self.title), '<form><table border ="0">']
        thisRow = None
        for key, value in sorted(self.items.items()):
            row, column = key
            if thisRow is None:
                html.append(" <tr>")
            elif thisRow != row:
                html.append(" </tr>\n  <tr>")
                thisRow = row
                html.append("    " + value)
            html.append(("  </tr>\n</table></form></body>"))
        return "\n".join(html)
