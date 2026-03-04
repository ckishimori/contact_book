import flet as ft
from database import create_table, add_contact, get_contacts

def main(page: ft.Page):
    page.title = "Flet Contact Book"
    create_table() # Ensure the database table is created when the app starts

    # Input fields
    name_entry = ft.TextField(label="Name")
    phone_entry = ft.TextField(label="Phone")
    email_entry = ft.TextField(label="Email")
    
    # List view to display contacts
    contacts_list = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    def populate_contacts_list():
        contacts_list.controls.clear()
        contacts = get_contacts()
        for contact in contacts:
            contacts_list.controls.append(ft.Text(value=f"Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}"))
        page.update()

    def on_add_contact_click(e):
        name = name_entry.value
        phone = phone_entry.value
        email = email_entry.value
        if name and phone:
            add_contact(name, phone, email)
            name_entry.value = ""
            phone_entry.value = ""
            email_entry.value = ""
            populate_contacts_list()
        page.update()

    page.add(
        ft.Column(
            controls=[
                name_entry,
                phone_entry,
                email_entry,
                ft.ElevatedButton(content="Add Contact", on_click=on_add_contact_click),
                ft.Text("Contacts List:", size=20),
                contacts_list,
            ]
        )
    )
    
    populate_contacts_list()

if __name__ == "__main__":
    ft.app(target=main)
