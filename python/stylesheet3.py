stylesheet = """
 /*QMainWindow {
		    background-image: linear-gradient(45deg, #030637, #3C0753, #720455, #910A67) !important;
            font-family: "Poppins", sans-serif !important;
            font-weight: 400 !important;
            font-size: 14px !important;
 }*/
 QMainWindow {
		    background-color: #FF70AB;
            font-family: "Poppins", sans-serif !important;
            font-weight: 400 !important;
            font-size: 14px !important;
 }
    QPushButton {
        background-color: #720455; /* Change button background color */
        color: white; /* Change button text color */
        border-radius: 10px; /* Change button border radius */
        border: 1px solid #030637; /* Change button border color */
        padding: 10px; /* Change button padding */
    }
    QPushButton:hover {
        background-color: #910A67; /* Change button background color on hover */
    }
    QPushButton:pressed{
        background-color : #3C0753;
    }
    QToolBar {
        background-color: #910A67; /* Change toolbar background color */
    }
    QToolButton {
        background-color: transparent; /* Make tool buttons transparent */
    }
    QLineEdit {
        background-color: #910A67; /* Change line edit background color */
        font-family: "Poppins";
        border: 1px solid #ccc; /* Change line edit border color */
        color: #ccc;
    }
    QLineEdit:hover {
        /* Styles when QLineEdit is hovered */
        background-color: #FFD0EC;
        color: #000;
    }
    QLineEdit:focus {
        /* Styles when QLineEdit is focused */
        background-color: #FFD0EC;
        color: #000;
    }
    QLineEdit:selected {
        /* Styles when text in QLineEdit is selected */
        background-color: #910A67;
    }

    QTabBar::tab {
        background-color: #720455; /* Tab background color */
        color: #ffffff; /* Tab text color */
        padding: 8px;
        border-top-left-radius: 4px; /* Rounded corners for tabs */
        border-top-right-radius: 4px;
    }

    QTabBar::tab:selected {
        background-color: #3C0753; /* Background color for selected tab */
    }

    QTabBar::tab:hover {
        background-color: #910A67; /* Background color for hovered tab */
    }
    QTabBar::tab {
        border:0;
    }

QMenuBar {
	background-color: #c34daa;
    border-width:0px;
}
QTabWidget {
	background-color: #c34daa;
    border-width:0px;
}
QTabWidget::pane {
	background-color: #c34daa;
    border-width:0px;
}


    * {
        font-family: "Poppins", sans-serif; /* Ensure the font family is set correctly */
    }
"""
