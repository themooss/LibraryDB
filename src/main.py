import customtkinter

from models.library import Library

l = Library()


class ScrollableDataFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)  # Для label
        self.grid_columnconfigure(0, weight=1)  # Для label

        self.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        self.label = customtkinter.CTkLabel(self, text="Scrollable Data Frame Content")
        self.label.grid(row=0, column=5, padx=20, pady=20, sticky="nsew")

        for i in range(1, 20):
            customtkinter.CTkLabel(self, text=f"Item {i} in Scrollable Frame").grid(row=i, column=0, padx=20, pady=5,
                                                                                    sticky="w")


class InteractionFrame(customtkinter.CTkFrame):

    def __init__(self, master, scrollable_data_frame_object=ScrollableDataFrame, **kwargs):
        super().__init__(master=master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.scrollable_data_frame_object = scrollable_data_frame_object

        self.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        def add_data_callback():
            print('add')
            l.add_content(
                {'writer': 'АЭС.Пушкин', 'title': 'Капитанская дочка', 'pages': 70, 'time_to_read': 120, 'cost': 120})
            print(l)

        add_button = customtkinter.CTkButton(self, text=f'Добавить', command=add_data_callback).grid(row=0, column=0,
                                                                                                     padx=20, pady=5,
                                                                                                     sticky="w")


class CRUDInteractionFrame(customtkinter.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        sort_button = customtkinter.CTkButton(self, text=f'Сортировать').grid(row=0, column=0, padx=20, pady=5,
                                                                              sticky="w")
        update_button = customtkinter.CTkButton(self, text=f'Обновить').grid(row=1, column=0, padx=20, pady=5,
                                                                             sticky="w")
        delete_button = customtkinter.CTkButton(self, text=f'Удалить').grid(row=2, column=0, padx=20, pady=5,
                                                                            sticky="w")


class App(customtkinter.CTk):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'LibraryDB'
        self.geometry('1024x768')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.scrollable_data_frame = ScrollableDataFrame(master=self, corner_radius=12,
                                                         fg_color='#2A2A29', border_width=2, border_color='#222222')
        self.scrollable_data_frame.grid(row=0, column=0, sticky='nsew')

        self.crud_interaction_frame = CRUDInteractionFrame(master=self, corner_radius=12, fg_color='#2A2A29',
                                                           border_width=2, border_color='#222222')
        self.crud_interaction_frame.grid(row=1, column=0, sticky='nsew')

        self.interaction_frame = InteractionFrame(master=self, corner_radius=12, fg_color='#2A2A29',
                                                  border_width=2, border_color='#222222'
                                                  )
        self.interaction_frame.grid(row=1, column=1, sticky='nsew')



if __name__ == "__main__":
    app = App()
    app.mainloop()
