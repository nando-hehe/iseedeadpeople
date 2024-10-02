import random

def quiz():
    questions = [
        ("The function or CI code to load a view is:", "$this->load->view", ["$this->load->view", "$this->view->load", "$this->load_view()", "view.load"]),
        ("Andi Gutmans was the inventor of PHP.", "False", ["True", "False"]),
        ("The function or CI code to show or call the client-side 'non-existing page' error is:", "show_404()", ["show_404()", "error_404()", "404_error()", "404()"]),
        ("PHP runs on various platforms operating system such as Apache and IIS.", "False", ["True", "False"]),
        ("PHP version currently in use on most websites and included several new features such as support for object-oriented programming.", "5", ["4", "5", "7", "8"]),
        ("The first URI segment in CI refers to:", "controller", ["controller", "method", "class", "function"]),
        ("Who is the inventor of PHP?", "Rasmus Lerdorf", ["Rasmus Lerdorf", "Andi Gutmans", "James Gosling", "Larry Wall"]),
        ("The page that displays a message that the requested page was not found is called:", "Error 404", ["Error 404", "Page not found", "404 Not Found", "Missing Page"]),
        ("What year did PHP begin its development?", "1994", ["1993", "1994", "1995", "1996"]),
        ("It is a URI Component that serves as persistent location-independent identifiers.", "URN", ["URL", "URN", "URI", "IP"]),
        ("It refers to the horizontal dimension of the grid system in CI.", "rows", ["columns", "rows", "cells", "divs"]),
        ("It's a JavaScript library that makes web scripting easier.", "JQuery", ["Angular", "React", "Vue", "JQuery"]),
        ("Null keywords should be written in:", "Uppercase", ["Lowercase", "Uppercase", "CamelCase", "PascalCase"]),
        ("It is a function that overrides the normal behavior in which the URI determines which function is called, allowing you to define your own function routing rules.", "//_remap()", ["//_remap()", "remap_uri()", "//override_uri()", "//redefine_uri()"]),
        ("Element can be placed onto a web page in a pre-checked fashion by setting the checked attribute.", "Checkbox", ["Radio Button", "Dropdown", "Text Box", "Checkbox"]),
        ("Form Helper method or code to return an HTML password input type.", "form_password()", ["form_input()", "form_password()", "input_password()", "password_form()"]),
        ("Other term used for Option buttons?", "Radio Buttons", ["Checkbox", "Toggle Button", "Select", "Radio Buttons"]),
        ("CI method or code to load the form validation library.", "$this->load->library('form_validation')", ["$this->load->library('form_validation')", "$this->load_form_validation()", "load_form_validation()", "form_library()"]),
        ("Form Helper method or code to return an HTML button.", "form_button()", ["form_button()", "button_form()", "button()", "input_button()"]),
        ("It is a line that is not read/executed as part of the program.", "comment", ["method", "statement", "comment", "parameter"]),
        ("Query Builder class method that inserts a record on the database.", "$this->db->insert()", ["$this->db->insert()", "db_insert()", "insert_db()", "db.insert()"]),
        ("Query Builder or Active Record pattern in CI replaces the traditional query string in PHP coding.", "True", ["True", "False"]),
        ("Defines a multi-line text input control.", "//<textarea> tag", ["//<textarea> tag", "<input>", "<form>", "<textarea>"]),
        ("`row_array()` fetches the data as a single row and `result_array()` fetches the data as a multi-dimensional array.", "True", ["True", "False"]),
        ("The person that introduced MVC.", "Trygve Reenskaug", ["Andi Gutmans", "Rasmus Lerdorf", "Trygve Reenskaug", "James Gosling"]),
        ("This helper file contains functions that assist in working with forms.", "Form", ["HTML", "Form", "CSS", "Validation"]),
        ("A cart library method that displays the total number of items in the cart.", "total_items()", ["total_cart()", "total_items()", "item_total()", "cart_total()"]),
        ("A configuration variable contains full URL to the controller class/function containing your pagination.", "base_url", ["base_url", "config_url", "url_base", "route_url"]),
        ("Form Helper method or code to return an HTML checkbox input type.", "form_checkbox()", ["form_checkbox()", "input_checkbox()", "checkbox_form()", "form_input()"]),
        ("One of the main points of interaction between a user and a web site or application. They allow users to send data to the website.", "HTML Forms", ["JavaScript", "HTML Forms", "CSS", "PHP"]),
        ("A variable declared outside a function.", "Global", ["Local", "Global", "Parameter", "Static"]),
        ("PHP variables start with what symbol?", "$", ["$", "&", "#", "*"]),
        ("CI function code to load the database class.", "$this->load->database();", ["$this->load->database();", "$this->database->load();", "load_database();", "db_load();"]),
        ("CI method or code to set an error message in form validation.", "$this->form_validation->set_message()", ["$this->form_validation->set_message()", "set_error_message()", "$this->validation->error_message()", "form_error_message()"]),
        ("A variable declared within a function.", "Local", ["Local", "Global", "Static", "Instance"]),
        ("Form Helper method or code to return an HTML button.", "form_button()", ["form_button()", "button_form()", "form_btn()", "input_btn()"]),
        ("The `__construct()` method executes when a class is created or instantiated.", "True", ["True", "False"]),
        ("CI method or code to set an error message in form validation.", "$this->form_validation->set_message()", ["$this->form_validation->set_message()", "set_error_message()", "$this->validation->error_message()", "form_error_message()"]),
        ("File that will automatically route the `index.php` next to the Controller.", ".htaccess", [".htaccess", "index.php", "controller.php", "routes.php"]),
        ("Variables that can be accessed anywhere on the web application because they are stored on the browser.", "superglobal", ["global", "superglobal", "local", "static"]),
        ("It can be said as the entry point of the application.", "Controller", ["Model", "View", "Helper", "Controller"]),
        ("Organization that sponsors CI.", "Ellislab", ["Ellislab", "Oracle", "Microsoft", "Zend"]),
        ("Method will execute codes once the class is created or instantiated.", "__construct", ["__construct", "__invoke", "__create", "__init"]),
        ("You can display the error 404 page by using what function?", "show_404()", ["show_404()", "display_404()", "error_404()", "404_error()"]),
        ("Function that fetches the data as a single row array.", "row_array()", ["row_array()", "fetch_single_row()", "single_row()", "get_single_row()"]),
        ("Variables are session variables that expire with a given time limit.", "Tempdata", ["Tempdata", "Superglobals", "Local Variables", "Static Variables"]),
        ("Function that fetches the data as a multi-dimensional array.", "result_array()", ["result_array()", "multi_array()", "fetch_array()", "get_multi_array()"]),
        ("What function can be used to access session variables on webpages?", "Session_start()", ["Session_start()", "Start_session()", "Session_open()", "Open_session()"])
    ]
    
    random.shuffle(questions)

    score = 0
    total_questions = len(questions)

    for i, (question, correct_answer, choices) in enumerate(questions):
        print(f"\nQuestion {i+1}: {question}")
        for j, choice in enumerate(choices):
            print(f"{j+1}. {choice}")
        
        answer = input("Please enter the number of your choice: ")
        
        if answer.isdigit() and 1 <= int(answer) <= len(choices):
            if choices[int(answer)-1] == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {correct_answer}\n")
        else:
            print("Invalid input. Please enter a valid choice number.")
    
    print(f"Quiz completed! Your final score is {score}/{total_questions}.")

quiz()
