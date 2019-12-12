from PyQt5 import QtCore, QtGui, QtWidgets
from database_tmp import Db #importing database.py
from home import Ui_MainWindow

sign = 0

class block(QtWidgets.QWidget):
    def setupblock(self, QWidget, name):
        self.box = QtWidgets.QVBoxLayout(QWidget)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.box.setSpacing(0)
        self.toInput = QtWidgets.QLineEdit()
        # self.toInput = MyLineEdit()
        self.toInput.setPlaceholderText(name)
        self.toInput.setFont(QtGui.QFont(QtGui.QFont("Times", 24, QtGui.QFont.Bold)))
        self.toInput.setObjectName(name)
        self.box.addWidget(self.toInput)
        self.box.setStretchFactor(self.toInput, 5)

        hbox = QtWidgets.QHBoxLayout()
        hbox.setContentsMargins(0, 5, 0, 0)
        hbox.setSpacing(0)
        error = QtWidgets.QLabel()
        jpg2 = QtGui.QPixmap("Pic/error.png")
        error.resize(18, 18)
        error.setPixmap(jpg2.scaled(error.size(), aspectRatioMode= QtCore.Qt.KeepAspectRatio))
        error.setObjectName("Error")
        error.setVisible(False)
        hbox.addWidget(error)
        hbox.setStretchFactor(error, 1)
        # hbox.addStretch(1)

        prompt = QtWidgets.QLabel()
        prompt.resize(200, 50)
        if name.endswith("Again"):
            prompt.setText("You should confirm your password")
        else:
            prompt.setText(name + " cannot be empty")
        prompt.setObjectName("Prompt")
        prompt.setFont(QtGui.QFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold)))
        prompt.setVisible(False)
        hbox.addWidget(prompt)
        hbox.setStretchFactor(prompt, 19)
        hbox.setObjectName("Container")
        self.box.addLayout(hbox)

class Ui_Dialog2(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Signup")
        Dialog.setFixedSize(1200, 720)
        Dialog.setStyleSheet("QDialog{\n"
        "background-color:rgb(255, 255, 255);}\n}"
"QLineEdit{\n"
"background-color:rgb(255, 0, 0, 0); border: 1px solid #aaa; border-radius:4px;}\n"
"\n"
"QLabel{\n"
"color:#ff5b5b;}"
"\n"
"QPushButton{\n"
"background-color:#3487ff;background-image: qlineargradient(0deg,#398bff,#3083ff); color:rgb(255,255,255);}\n"
"")
        plane = QtWidgets.QHBoxLayout(Dialog)
        plane.setContentsMargins(0, 0, 0, 0)

        background = QtWidgets.QLabel()
        jpg = QtGui.QPixmap('Pic/signup.jpg')
        background.resize(510, 720)
        background.setPixmap(jpg.scaled(background.size(), aspectRatioMode= QtCore.Qt.KeepAspectRatio))
        background.setObjectName("Background")
        plane.addWidget(background)  
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.setContentsMargins(100, 0, 100, 100)
        vbox.setSpacing(0)
        
        icon = QtWidgets.QLabel()
        jpg1 = QtGui.QPixmap('Pic/Icon.jpg')
        icon.resize(350, 70)
        icon.setPixmap(jpg1.scaled(icon.size(), aspectRatioMode= QtCore.Qt.KeepAspectRatio))
        icon.setObjectName("Icon")
        icon.setAlignment(QtCore.Qt.AlignCenter)
        vbox.addWidget(icon)
        vbox.setStretchFactor(icon, 5)

        setblock = block()

        self.Username = QtWidgets.QWidget()
        setblock.setupblock(self.Username, "Username")
        self.UsernameInput = self.Username.findChild(QtWidgets.QLineEdit, "Username")
        self.UsernameInput.installEventFilter(self)
        vbox.addWidget(self.Username)
        vbox.addStretch(1)

        self.Nickname = QtWidgets.QWidget()
        setblock.setupblock(self.Nickname, "Nickname")
        self.NicknameInput = self.Nickname.findChild(QtWidgets.QLineEdit, "Nickname")
        self.NicknameInput.installEventFilter(self)
        vbox.addWidget(self.Nickname)
        vbox.addStretch(1)

        self.Password = QtWidgets.QWidget()
        setblock.setupblock(self.Password, "Password")
        self.PasswordInput = self.Password.findChild(QtWidgets.QLineEdit, "Password")
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput.installEventFilter(self)
        vbox.addWidget(self.Password)
        vbox.addStretch(1)

        self.Password2 = QtWidgets.QWidget()
        setblock.setupblock(self.Password2, "Password Again")
        self.PasswordInput2 = self.Password2.findChild(QtWidgets.QLineEdit, "Password Again")
        self.PasswordInput2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput2.installEventFilter(self)
        vbox.addWidget(self.Password2)
        vbox.addStretch(1.5)

        self.btnSignup = QtWidgets.QPushButton()
        self.btnSignup.setObjectName("btnSignup")
        ################## Signup button#########################
        self.btnSignup.clicked.connect(self.SignupButton)
        ###########################################################
        vbox.addWidget(self.btnSignup)
        vbox.setStretchFactor(self.btnSignup, 6)
        vbox.addStretch(0.5)

        ending = QtWidgets.QHBoxLayout()
        ending.setContentsMargins(0, 20, 0, 0)
        ending.setSpacing(0)
        ending.addStretch(2)

        self.btnBack = QtWidgets.QPushButton()
        self.btnBack.setObjectName("btnBack")
        self.btnBack.clicked.connect(self.BackButton)

        ending.addWidget(self.btnBack)
        ending.setStretchFactor(self.btnBack, 1)
        vbox.addLayout(ending)
        vbox.setStretchFactor(ending, 2)

        plane.addLayout(vbox)
        plane.setStretchFactor(vbox, 8)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def eventFilter(self, object, event):        
        layout = object.parentWidget()
        prompt = layout.findChild(QtWidgets.QLabel, "Prompt")
        error = layout.findChild(QtWidgets.QLabel, "Error")
        if event.type() == QtCore.QEvent.FocusIn:
            object.setStyleSheet("border:1px solid #549df8; border-radius:4px;}")
            prompt.setVisible(False)
            error.setVisible(False)

        elif event.type() == QtCore.QEvent.FocusOut:
            text = object.text()
            if len(text) == 0:
                object.setStyleSheet("border: 1px solid #ff5b5b; focus{\nborder:1px solid #549df8;}\n")
                prompt.setVisible(True)
                error.setVisible(True)
            else:
                object.setStyleSheet("border: 1px solid #aaa; focus{\nborder:1px solid #549df8;}\n")

        return super(Ui_Dialog2, self).eventFilter(object, event)

    def BackButton(self):
        self.clearField()
        self.close()

    def SignupButton(self):
        username = self.UsernameInput.text()
        nickname = self.NicknameInput.text()
        password = self.PasswordInput.text()
        password2 = self.PasswordInput2.text()
        if self.checkFields(username,nickname,password,password2):
            return
        else:
            if(self.checkPassword(password,password2)):
                insertDb = Db()
                insertDb.insertTable(nickname,username,password)
                self.clearField()
            else:
                self.showMessage("Error","Passwords doesn't match")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Chatroom"))
        self.btnSignup.setText(_translate("Dialog", "Sign Up"))
        self.btnSignup.setFont(QtGui.QFont(QtGui.QFont("Times", 24, QtGui.QFont.Bold)))
        self.btnBack.setText(_translate("Dialog", "Back"))
        self.btnBack.setFont(QtGui.QFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold)))
        
    def checkFields(self,username,nickname,password,password2):
        if username=="":
            self.prompt(self.UsernameInput)
            return
        elif nickname=="":
            self.prompt(self.NicknameInput)
            return
        elif password== "":
            self.prompt(self.PasswordInput)
            return
        elif password2=="":
            self.prompt(self.PasswordInput2)
            return

    def prompt(self, object):
        layout = object.parentWidget()
        prompt = layout.findChild(QtWidgets.QLabel, "Prompt")
        error = layout.findChild(QtWidgets.QLabel, "Error")
        object.setStyleSheet("border: 1px solid #ff5b5b; focus{\nborder:1px solid #549df8;}\n")
        prompt.setVisible(True)
        error.setVisible(True)

    def hide(self, object):
        object.setText(None)
        layout = object.parentWidget()
        prompt = layout.findChild(QtWidgets.QLabel, "Prompt")
        error = layout.findChild(QtWidgets.QLabel, "Error")
        object.setStyleSheet("border: 1px solid #aaa; focus{\nborder:1px solid #549df8;}\n")
        prompt.setVisible(False)
        error.setVisible(False)

    ############## check if password1 and password2 matches #############
    def checkPassword(self,password1, password2):
        return password1 == password2

    ##################### clear fields ##################
    def clearField(self):
        self.hide(self.UsernameInput)
        self.hide(self.NicknameInput)
        self.hide(self.PasswordInput)
        self.hide(self.PasswordInput2)

class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(1200, 720)
        Dialog.setStyleSheet("QDialog{\n"
        "background-color:rgb(255, 255, 255);}\n}"
"QLineEdit{\n"
"background-color:rgb(255, 0, 0, 0); border: 2px solid #aaa; border-radius:4px}\n"
"\n"
"QLabel{\n"
"color:#ff5b5b;}"
"\n"
"QPushButton{\n"
"background-color:#3487ff;background-image: qlineargradient(0deg,#398bff,#3083ff); color:rgb(255,255,255);}\n"
"")
        plane = QtWidgets.QHBoxLayout(Dialog)
        plane.setContentsMargins(0, 0, 0, 0)

        background = QtWidgets.QLabel()
        jpg = QtGui.QPixmap('Pic/signin.jpg')
        background.resize(510, 720)
        background.setPixmap(jpg.scaled(background.size(), aspectRatioMode= QtCore.Qt.KeepAspectRatio))
        background.setObjectName("Background")
        plane.addWidget(background)
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.setContentsMargins(100, 70, 100, 100)
        vbox.setSpacing(0)

        icon = QtWidgets.QLabel()
        jpg1 = QtGui.QPixmap('Pic/Icon.jpg')
        icon.resize(350, 70)
        icon.setPixmap(jpg1.scaled(icon.size(), aspectRatioMode= QtCore.Qt.KeepAspectRatio))
        icon.setObjectName("Icon")
        icon.setAlignment(QtCore.Qt.AlignCenter)
        vbox.addWidget(icon)
        vbox.setStretchFactor(icon, 5)

        setblock = block()

        self.Username = QtWidgets.QWidget()
        setblock.setupblock(self.Username, "Username")
        self.UsernameInput = self.Username.findChild(QtWidgets.QLineEdit, "Username")
        self.UsernameInput.installEventFilter(self)
        vbox.addWidget(self.Username)
        vbox.addStretch(1)

        self.Password = QtWidgets.QWidget()
        setblock.setupblock(self.Password, "Password")
        self.PasswordInput = self.Password.findChild(QtWidgets.QLineEdit, "Password")
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput.installEventFilter(self)
        vbox.addWidget(self.Password)
        vbox.addStretch(1.5)

        self.btnSignin = QtWidgets.QPushButton()
        self.btnSignin.setObjectName("btnSignin")
        ################## Signup button#########################
        self.btnSignin.clicked.connect(self.SigninCheck)
        ###########################################################
        vbox.addWidget(self.btnSignin)
        vbox.setStretchFactor(self.btnSignin, 6)
        vbox.addStretch(0.5)

        ending = QtWidgets.QHBoxLayout()
        ending.setContentsMargins(0, 20, 0, 0)
        ending.setSpacing(0)
        ending.addStretch(2)

        self.btnSignup = QtWidgets.QPushButton()
        self.btnSignup.setObjectName("btnSignup")
        self.btnSignup.clicked.connect(self.SignupButton)
        ending.addWidget(self.btnSignup)
        ending.setStretchFactor(self.btnSignup, 1)
        vbox.addLayout(ending)
        vbox.setStretchFactor(ending, 2)

        plane.addLayout(vbox)
        plane.setStretchFactor(vbox, 8)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def eventFilter(self, object, event):        
        layout = object.parentWidget()
        prompt = layout.findChild(QtWidgets.QLabel, "Prompt")
        error = layout.findChild(QtWidgets.QLabel, "Error")
        if event.type() == QtCore.QEvent.FocusIn:
            object.setStyleSheet("border:1px solid #549df8; border-radius:4px;}")
            prompt.setVisible(False)
            error.setVisible(False)

        elif event.type() == QtCore.QEvent.FocusOut:
            text = object.text()
            if len(text) == 0:
                object.setStyleSheet("border: 1px solid #ff5b5b; focus{\nborder:1px solid #549df8;}\n")
                prompt.setVisible(True)
                error.setVisible(True)
            else:
                object.setStyleSheet("border: 1px solid #aaa; focus{\nborder:1px solid #549df8;}\n")

        return super(Ui_Dialog, self).eventFilter(object, event)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Chatroom"))
        self.btnSignin.setText(_translate("Dialog", "Sign in"))
        self.btnSignin.setFont(QtGui.QFont(QtGui.QFont("Times", 24, QtGui.QFont.Bold)))
        self.btnSignup.setText(_translate("Dialog", "Sign Up"))
        self.btnSignup.setFont(QtGui.QFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold)))
        
    def welcomePage(self):
        self.homWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.homWindow)
        self.homWindow.show()
        
    def SigninCheck(self):
        username = self.UsernameInput.text()
        password = self.PasswordInput.text()
        if self.checkFields(username,password):
            return
        
        getDb = Db()        
        result = getDb.SigninCheck(username,password)
        if(result):
            self.welcomePage()
            self.clearField()
            print(result)
        else:
            print("password wrong")
            self.showMessage("Warning","Invalid Username and Password")
    
    def checkFields(self,username,password):
        if username=="":
            self.prompt(self.UsernameInput)
            return
        elif password== "":
            self.prompt(self.PasswordInput)
            return

    def prompt(self, object):
        layout = object.parentWidget()
        prompt = layout.findChild(QtWidgets.QLabel, "Prompt")
        error = layout.findChild(QtWidgets.QLabel, "Error")
        object.setStyleSheet("border: 1px solid #ff5b5b; focus{\nborder:1px solid #549df8;}\n")
        prompt.setVisible(True)
        error.setVisible(True)

    def hide(self, object):
        object.setText(None)
        layout = object.parentWidget()
        prompt = layout.findChild(QtWidgets.QLabel, "Prompt")
        error = layout.findChild(QtWidgets.QLabel, "Error")
        object.setStyleSheet("border: 1px solid #aaa; focus{\nborder:1px solid #549df8;}\n")
        prompt.setVisible(False)
        error.setVisible(False)

    def SignupButton(self):   
        self.clearField()
        self.close()
                
    def clearField(self):
        self.hide(self.UsernameInput)
        self.hide(self.PasswordInput)

class Dialog(Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        # self.btnSignup.clicked.connect(self.close)

class Dialog2(Ui_Dialog2):
    def __init__(self, parent=None):
        super(Dialog2, self).__init__(parent)
        self.setupUi(self)
        # self.btnBack.clicked.connect(self.close)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window1 = Dialog()
    Window2 = Dialog2()
    # ui = Ui_Dialog2()
    # ui.setupUi(Dialog)

    # Dialog2 = QtWidgets.QDialog()
    # ui2 = Ui_Dialog()
    # ui2.setupUi(Dialog2)
    
    Window1.btnSignup.clicked.connect(Window2.show)
    Window2.btnBack.clicked.connect(Window1.show)
    Window1.show()

    sys.exit(app.exec_())
