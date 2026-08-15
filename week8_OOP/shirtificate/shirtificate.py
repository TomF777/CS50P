"""
Implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf
with these specifications:

- The orientation of the PDF should be Portrait.
- The format of the PDF should be A4, which is 210mm wide by 297mm tall.
- The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
- The shirt’s image should be centered horizontally.
- The user’s name should be on top of the shirt, in white text.

All other details we leave to you.
You’re even welcome to add borders, colors, and lines.
No need to wrap long names across multiple lines.


requires:
pip install fpdf2
"""

from fpdf import FPDF


class PDF(FPDF):

    def set_cs50_name(self, cs50_name):
        self.cs50_name = cs50_name

    def header(self):

        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=20)

        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C", center=True)


    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-200)

        # Setting font: helvetica italic 8
        self.set_font("helvetica", style="B", size=16)
        self.set_text_color(255,255,255)

        # Printing user name:
        self.cell(0, 10, f"{self.cs50_name} took CS50", align="C", center=True)



if __name__ == "__main__":

    cs50_name = input("Name: ")

    # Instantiation of inherited class
    pdf = PDF(orientation="portrait", format="A4")
    pdf.set_cs50_name(cs50_name)
    pdf.add_page()
    pdf.image("./shirtificate.png", x=0, y=50)
    pdf.set_auto_page_break(auto=False)

    pdf.output("shirtificate.pdf")
