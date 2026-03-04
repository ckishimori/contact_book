from textual.app import App
from textual.screen import Screen
from textual.containers import Grid, Horizontal, Vertical
from textual.widgets import (
    Button,
    DataTable,
    Footer,
    Header,
    Label,
    Static,
)

class ContactsApp(App):
    CSS_PATH = "textual_app.tcss"
    BINDINGS = [
        ("q", "quit", "Quit")
    ]
    def compose(self):
        yield Header()
        contacts_list = DataTable(classes="contacts-list")
        contacts_list.focus()
        contacts_list.add_columns("Name", "Phone", "Email")
        contacts_list.cursor_type = "row"
        contacts_list.zebra_stripes = True
        add_button = Button("Add", variant="success", id="add")
        add_button.focus()
        buttons_panel = Vertical(
            add_button,
            Button("Delete", variant="warning", id="delete"),
            Static(classes="separator"),
            Button("Clear All", variant="error", id="clear"),
            classes="buttons-panel",
        )
        yield Horizontal(contacts_list, buttons_panel)
        yield Footer()

    def on_mount(self):
        self.title = "Textual Contact Book"
#       self.sub_title = "A Contacts Book App With Textual & Python"

def main():
    app = ContactsApp()
    app.run()

if __name__ == "__main__":
    main()