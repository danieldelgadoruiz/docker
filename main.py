import reactpy
# from reactpy import component, html, use_state
# from reactpy.backend.fastapi import configure
# from fastapi import FastAPI


# @reactpy.component
# def Calculator():
#     state, set_state = use_state({
#         "num1": "",
#         "num2": "",
#         "operation": "",
#         "result": ""
#     })

#     def handle_number_change(e, num):
#         new_state = state.copy()
#         new_state[num] = e["target"]["value"]
#         set_state(new_state)

#     def handle_operation_change(e):
#         new_state = state.copy()
#         new_state["operation"] = e["target"]["value"]
#         set_state(new_state)

#     async def handle_calculate(e):
#         try:
#             num1 = float(state["num1"])
#             num2 = float(state["num2"])
#             operation = state["operation"]
            
#             result = None
#             if operation == "+":
#                 result = num1 + num2
#             elif operation == "-":
#                 result = num1 - num2
#             elif operation == "*":
#                 result = num1 * num2
#             elif operation == "/":
#                 if num2 != 0:
#                     result = num1 / num2
#                 else:
#                     new_state = state.copy()
#                     new_state["result"] = "Error: División por cero"
#                     set_state(new_state)
#                     return
            
#             if result is not None:
#                 new_state = state.copy()
#                 new_state["result"] = str(round(result, 2))
#                 set_state(new_state)
                
#         except ValueError:
#             new_state = state.copy()
#             new_state["result"] = "Error: Ingrese números válidos"
#             set_state(new_state)
#         except Exception as error:
#             new_state = state.copy()
#             new_state["result"] = f"Error: {str(error)}"
#             set_state(new_state)

#     return html.div(
#         {
#             "class": "min-h-screen bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center p-4"
#         },
#         html.div(
#             {
#                 "class": "w-full max-w-md bg-white bg-opacity-90 backdrop-blur-xl rounded-3xl shadow-2xl p-8 transform hover:scale-105 transition-all duration-300 border-t-8 border-purple-500"
#             },
#             html.h2(
#                 {
#                     "class": "text-4xl font-bold mb-8 text-center bg-gradient-to-r from-purple-600 to-pink-600 text-transparent bg-clip-text"
#                 },
#                 "Calculadora"
#             ),
#             html.div(
#                 {"class": "space-y-6"},
#                 html.input({
#                     "type": "number",
#                     "value": state["num1"],
#                     "on_change": lambda e: handle_number_change(e, "num1"),
#                     "class": "w-full p-5 border-2 border-purple-300 rounded-2xl focus:border-purple-500 focus:ring-4 focus:ring-purple-200 transition-all outline-none text-xl shadow-inner bg-gray-50",
#                     "placeholder": "Primer número"
#                 }),
#                 html.select(
#                     {
#                         "value": state["operation"],
#                         "on_change": handle_operation_change,
#                         "class": "w-full p-5 border-2 border-purple-300 rounded-2xl focus:border-purple-500 focus:ring-4 focus:ring-purple-200 transition-all outline-none text-xl bg-gray-50 shadow-inner"
#                     },
#                     html.option({"value": ""}, "🔢 Operación"),
#                     html.option({"value": "+"}, "➕ Suma"),
#                     html.option({"value": "-"}, "➖ Resta"),
#                     html.option({"value": "*"}, "✖️ Multiplicar"),
#                     html.option({"value": "/"}, "➗ Dividir")
#                 ),
#                 html.input({
#                     "type": "number",
#                     "value": state["num2"],
#                     "on_change": lambda e: handle_number_change(e, "num2"),
#                     "class": "w-full p-5 border-2 border-purple-300 rounded-2xl focus:border-purple-500 focus:ring-4 focus:ring-purple-200 transition-all outline-none text-xl shadow-inner bg-gray-50",
#                     "placeholder": "Segundo número"
#                 }),
#                 html.button(
#                     {
#                         "on_click": handle_calculate,
#                         "class": "w-full p-5 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-2xl font-bold text-xl shadow-lg hover:shadow-2xl transform transition-all hover:-translate-y-1 active:translate-y-0 hover:from-purple-700 hover:to-pink-700"
#                     },
#                     "✨ Calcular"
#                 ),
#                 html.div(
#                     {
#                         "class": "mt-8 p-6 bg-gradient-to-br from-purple-100 to-pink-100 rounded-2xl shadow-inner"
#                     },
#                     html.p(
#                         {"class": "text-2xl font-bold text-center"},
#                         ["Resultado: ", 
#                          html.span(
#                             {
#                                 "class": "text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-pink-600"
#                             },
#                             state["result"] or "..."
#                         )]
#                     )
#                 )
#             )
#         )
#     )

# # Configuración del servidor
# app = FastAPI()
# configure(app, Calculator)

import reactpy
from reactpy import component, html, use_state
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

styles = {
    "container": {
        "display": "flex",
        "flexDirection": "column",
        "alignItems": "center",
        "padding": "20px",
        "backgroundColor": "#f0f0f0",
        "borderRadius": "10px",
        "maxWidth": "400px",
        "margin": "20px auto"
    },
    "input": {
        "margin": "10px",
        "padding": "5px",
        "borderRadius": "5px",
        "border": "1px solid #ccc",
        "width": "200px"
    },
    "button": {
        "backgroundColor": "#4CAF50",
        "color": "white",
        "padding": "10px 20px",
        "border": "none",
        "borderRadius": "5px",
        "cursor": "pointer",
        "margin": "10px"
    },
    "result": {
        "fontSize": "20px",
        "fontWeight": "bold",
        "color": "#333",
        "marginTop": "15px"
    }
}

@reactpy.component
def Calculator():
    num1, set_num1 = use_state("")
    num2, set_num2 = use_state("")
    result, set_result = use_state("")
    operation, set_operation = use_state("add")

    async def handle_calculate(e):
        try:
            n1 = float(num1)
            n2 = float(num2)
            if operation == "add":
                set_result(str(n1 + n2))
            elif operation == "subtract":
                set_result(str(n1 - n2))
            elif operation == "multiply":
                set_result(str(n1 * n2))
            elif operation == "divide":
                set_result(str(n1 / n2) if n2 != 0 else "Error: División por cero")
        except ValueError:
            set_result("Error: Ingrese números válidos")

    return html.div(
        {"style": styles["container"]},
        html.input({
            "type": "number",
            "value": num1,
            "on_change": lambda e: set_num1(e["target"]["value"]),
            "style": styles["input"],
            "placeholder": "Primer número"
        }),
        html.select(
            {
                "value": operation,
                "on_change": lambda e: set_operation(e["target"]["value"]),
                "style": styles["input"]
            },
            html.option({"value": "add"}, "+"),
            html.option({"value": "subtract"}, "-"),
            html.option({"value": "multiply"}, "×"),
            html.option({"value": "divide"}, "÷")
        ),
        html.input({
            "type": "number",
            "value": num2,
            "on_change": lambda e: set_num2(e["target"]["value"]),
            "style": styles["input"],
            "placeholder": "Segundo número"
        }),
        html.button(
            {
                "on_click": handle_calculate,
                "style": styles["button"]
            },
            "Calcular"
        ),
        html.div(
            {"style": styles["result"]},
            f"Resultado: {result}" if result else ""
        )
    )

app = FastAPI()
configure(app, Calculator)