from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)

    # Título
    pdf.set_font("Helvetica", "B", 36)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 60, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    # Imagen de la camiseta centrada
    img_width = 190
    x = (210 - img_width) / 2
    pdf.image("shirtificate.png", x=x, y=75, w=img_width)

    # Nombre del usuario encima de la camiseta
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(140)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
