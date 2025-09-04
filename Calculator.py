import PySimpleGUI as sg
import sys
import os

def main():

    SCRIPT_DIR = os.path.dirname(os.path. abspath(__file__))
    IMAGES_DIR = SCRIPT_DIR

    init = [
        [sg.Text("WELCOME TO THE CALCULATOR APP!", font=("Arial", 30), text_color="orange")],
        [sg.Image(os.path.join(IMAGES_DIR, "8665100_calculator_icon.png"))]
    ]

    init_window = sg.Window("App Start", init, no_titlebar=True, auto_close=True, auto_close_duration=5)
    init_window.read()

    def main2():

        def restart():
            restart_option = sg.popup_yes_no("Would you like to restart?")
            
            while True:
                if restart_option in ("No", sg.WIN_CLOSED):
                    sg.popup_no_buttons("See you!", no_titlebar=True, auto_close=True, auto_close_duration=2.5)
                    break
                elif(restart_option == "Yes"):
                    sg.popup_no_buttons("Restarting...", no_titlebar=True, auto_close=True, auto_close_duration=3)
                    main2()
            sys.exit()
        
        def addition(a, b):
            return a+b
        
        def subtraction(a,b):
            return a-b
        
        def multiplication(a,b):
            return a*b
        
        def division(a,b):
            return a/b

        math_menu = [
            [sg.Text("Select what math problem you have below:")],
            [sg.Button("Addition"), sg.Button("Subtraction"), sg.Button("Multiplication"), sg.Button("Division"), sg.Button("Exit")]
        ]

        math_window = sg.Window("Math Menu", math_menu, resizable=True)

        while True:
            math_events, values = math_window.read()
            if math_events in ("Exit", sg.WIN_CLOSED):
                math_window.close()
                break
            elif(math_events == "Addition"):
                math_window.close()
                add_input = [
                    [sg.Text("Input your first value:"), sg.Input(key='-VALUE_A-', enable_events=True)],
                    [sg.Text("Input your second value:"), sg.Input(key='-VALUE_B-', enable_events=True)],
                    [sg.Text(key='-ANSWER-')],
                    [sg.Button("Submit", key='-SUBMIT-', bind_return_key=True, disabled=True), sg.Button("Cancel")]
                ]

                add_window = sg.Window("Addition", add_input, finalize=True, resizable=True)
                add_window['-SUBMIT-'].set_focus()

                while True:
                    add_events, values = add_window.read()
                    if(add_events == "Cancel" or add_events == sg.WIN_CLOSED):
                        add_window.close()
                        break
                    
                    if add_events in ('-VALUE_A-', '-VALUE_B-'):
                        if values['-VALUE_A-'].strip() and values['-VALUE_B-'].strip():
                            add_window['-SUBMIT-'].update(disabled=False)
                        else:
                            add_window['-SUBMIT-'].update(disabled=True)

                    elif(add_events == '-SUBMIT-'):                    
                        try:
                            a = float(values['-VALUE_A-'])
                            b = float(values['-VALUE_B-'])
                            c = addition(a,b)
                            answer = c
                            add_window['-ANSWER-'].update(answer)
                            add_window['-VALUE_A-'].update('')
                            add_window['-VALUE_B-'].update('')
                            add_window['-SUBMIT-'].update(disabled=True)
                        except ValueError:
                            sg.popup("Please enter valid numbers.", no_titlebar=True)
                            add_window['-VALUE_A-'].update('')
                            add_window['-VALUE_B-'].update('')
                            continue
                restart()

            elif(math_events == "Subtraction"):
                math_window.close()

                subtract_input = [
                    [sg.Text("Input your first value:"), sg.Input(key='-VALUE_A-', enable_events=True)],
                    [sg.Text("Input your second value:"), sg.Input(key='-VALUE_B-', enable_events=True)],
                    [sg.Text(key='-ANSWER-')],
                    [sg.Button("Submit", key='-SUBMIT-', bind_return_key=True, disabled=True), sg.Button("Cancel")]
                ]

                subtract_window = sg.Window("Subtraction", subtract_input, finalize=True, resizable=True)
                subtract_window['-SUBMIT-'].set_focus()

                while True:
                    subtract_events, values = subtract_window.read()
                    if subtract_events in ("Cancel", sg.WIN_CLOSED):
                        subtract_window.close()
                        break

                    elif subtract_events in ('-VALUE_A-', '-VALUE_B-'):
                        if values['-VALUE_A-'].strip() and values['-VALUE_B-'].strip():
                            subtract_window['-SUBMIT-'].update(disabled=False)
                        else:
                            subtract_window['-SUBMIT-'].update(disabled=True)
                    
                    elif(subtract_events == '-SUBMIT-'):
                        try:
                            a = float(values['-VALUE_A-'])
                            b = float(values['-VALUE_B-'])
                            c = subtraction(a,b)
                            answer = c
                            subtract_window['-ANSWER-'].update(answer)
                            subtract_window['-VALUE_A-'].update('')
                            subtract_window['-VALUE_B-'].update('')
                            subtract_window['-SUBMIT-'].update(disabled=True)
                        except ValueError:
                            sg.popup("Please enter valid numbers.", no_titlebar=True)
                            subtract_window['-VALUE_A-'].update('')
                            subtract_window['-VALUE_B-'].update('')
                            continue
                restart()

            elif(math_events == "Multiplication"):
                math_window.close()

                multi_input = [
                    [sg.Text("Enter your first value:"), sg.Input(key='-VALUE_A-', enable_events=True)],
                    [sg.Text("Enter your second value:"), sg.Input(key='-VALUE_B-', enable_events=True)],
                    [sg.Text(key='-ANSWER-')],
                    [sg.Button("Submit", key='-SUBMIT-', disabled=True, bind_return_key=True), sg.Button("Cancel")]
                ]

                multi_window = sg.Window("Multiplication", multi_input, finalize=True, resizable=True)
                multi_window['-SUBMIT-'].set_focus()

                while True:
                    multi_events, values = multi_window.read()
                    if(multi_events == "Cancel" or multi_events == sg.WIN_CLOSED):
                        multi_window.close()
                        break

                    elif multi_events in ('-VALUE_A-', '-VALUE_B-'):
                        if values['-VALUE_A-'].strip() and values['-VALUE_B-'].strip():
                            multi_window['-SUBMIT-'].update(disabled=False)
                        else:
                            multi_window['-SUBMIT-'].update(disabled=True)

                    elif(multi_events == '-SUBMIT-'):
                            try:
                                a = float(values['-VALUE_A-'])
                                b = float(values['-VALUE_B-'])
                                c = multiplication(a,b)
                                answer = c
                                multi_window['-ANSWER-'].update(answer)
                                multi_window['-VALUE_A-'].update('')
                                multi_window['-VALUE_B-'].update('')
                                multi_window['-SUBMIT-'].update(disabled=True)
                            except ValueError:
                                sg.popup("Please enter valid numbers.", no_titlebar=True)
                                multi_window['-VALUE_A-'].update('')
                                multi_window['-VALUE_B-'].update('')
                                continue
        
                restart()

            elif(math_events == "Division"):
                math_window.close()

                division_input = [
                    [sg.Text("Input your first value:"), sg.Input(key='-VALUE_A-', enable_events=True)],
                    [sg.Text("Enter your second value:"), sg.Input(key='-VALUE_B-', enable_events=True)],
                    [sg.Text(key='-ANSWER-')],
                    [sg.Button("Submit", key='-SUBMIT-', bind_return_key=True, disabled=True), sg.Button("Cancel")]
                ]

                division_window = sg.Window("Division", division_input, finalize=True, resizable=True)
                division_window['-SUBMIT-'].set_focus()

                while True:
                    division_events, values = division_window.read()
                    if division_events in ("Cancel", sg.WIN_CLOSED):
                        division_window.close()
                        break
                    
                    elif division_events in ('-VALUE_A-', '-VALUE_B-'):
                        if values['-VALUE_A-'].strip() and values['-VALUE_B-'].strip():
                            division_window['-SUBMIT-'].update(disabled=False)
                        else:
                            division_window['-SUBMIT-'].update(disabled=True)
                    
                    elif(division_events == '-SUBMIT-'):
                        try:
                            a = float(values['-VALUE_A-'])
                            b = float(values['-VALUE_B-'])
                            c = division(a,b)
                            answer = c
                            division_window['-ANSWER-'].update(answer)
                            division_window['-VALUE_A-'].update('')
                            division_window['-VALUE_B-'].update('')
                            division_window['-SUBMIT-'].update(disabled=True)
                        except ValueError:
                            sg.popup("Please enter valid numbers.", no_titlebar=True)
                            division_window['-VALUE_A-'].update('')
                            division_window['-VALUE_B-'].update('')
                            continue

                restart()

        sys.exit()

    main2()

main()