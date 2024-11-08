# Footer
        self.footer_frame = ttk.Frame(master)
        self.footer_frame.pack(side=BOTTOM, fill=X, pady=(10, 0))

        footer_label = ttk.Label(self.footer_frame, text="Created By : ", font=("Helvetica", 12))
        footer_label.pack(side=LEFT, padx=5)

        link_label = ttk.Label(self.footer_frame, text="Aditya Nalawade", font=("Helvetica", 12, "underline"), foreground="#CBFC01")
        link_label.pack(side=LEFT)

        link_label2 = ttk.Label(self.footer_frame, text="GitHub", font=("Helvetica", 12, "underline"), foreground="#CBFC01")
        link_label2.pack(side=LEFT, padx=5)
        link_label2.bind("<Button-1>", self.open_link2)

        link_label3 = ttk.Label(self.footer_frame, text="Mail", font=("Helvetica", 12, "underline"), foreground="#CBFC01")
        link_label3.pack(side=LEFT, padx=5)
        link_label3.bind("<Button-1>", self.open_link3)

        link_label.bind("<Button-1>", self.open_link)

    def open_link(self, event):
        webbrowser.open("https://www.linkedin.com/in/aditya-nalawade-a4b081297?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")

    def open_link2(self, event):
        webbrowser.open("https://github.com/Adiiiicodes")

    def open_link3(self, event):
        webbrowser.open("adityacodes8@gmail.com")
