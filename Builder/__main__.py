from Builder.HtmlFormBuilder import HtmlFormBuilder
from Builder.TkFormBuilder import TkFormBuilder


def create_login_form(builder):
    builder.add_titile("Login")
    builder.add_lable("Username", 0, 0, target="username")
    builder.add_entry("username", 0, 1)
    builder.add_lable("Password", 1, 0, target="password")
    builder.add_entry("password", 1, 1, kind="password")
    builder.add_button("Login", 2, 0)
    builder.add_button("Cancel", 2, 1)
    return builder.form()


def main():
    htmlForm = create_login_form(HtmlFormBuilder())
    htmlForm.save()

    tkForm = create_login_form(TkFormBuilder())
    tkForm.save()


if __name__ == '__main__':
    main()
