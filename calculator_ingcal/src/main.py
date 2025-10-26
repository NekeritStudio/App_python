import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Calorías"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 30
    page.bgcolor = "#1f416e"

    # Text field of the result
    number_calculate = ft.TextField(
        label="Resultado",
        text_align=ft.TextAlign.CENTER,
        read_only=True,
        width=200,
    )

    # Text field user enter
    user_calories = ft.TextField(
        label="Calorías del usuario",
        text_align=ft.TextAlign.CENTER,
        width=200,
    )

    # Text field default number
    number_default = ft.TextField(
        label="Valor base",
        value="1600",
        text_align=ft.TextAlign.CENTER,
        width=200,
        read_only=True,
    )

    # Calculate function
    def calculate(e):
        try:
            value = float(user_calories.value)
            result = value / 1600
            number_calculate.value = f"{result:.2f}"
            user_calories.error_text = None
        except ValueError:
            user_calories.error_text = "El valor debe ser númerico"
            number_calculate.value = ""
        page.update()

    # Button
    calc = ft.ElevatedButton(
        text="Calcular",
        on_click=calculate,
        width=200,
        bgcolor="#1c284b"
    )

    # Container "enter"
    enter = ft.Container(
        content=ft.Column(
            [
                user_calories,
                ft.Divider(height=10, thickness=1, color= "#658eff"),
                number_default,
                calc,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
        expand= 1,
        bgcolor="#2c4383",
        padding=20,
        border_radius=10,
    )

    # Container "outpot"
    outpot = ft.Container(
        content=ft.Column(
            [number_calculate],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand= 1,
        bgcolor="#2c4383",
        padding=20,
        border_radius=10,
    )

    # First Container "calculator"
    calculator = ft.Container(
        content=ft.Row(
            [
                enter,
                outpot,
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand= True,
        border_radius=15,
        padding=20,
    )

    page.add(calculator)

ft.app(target=main)
