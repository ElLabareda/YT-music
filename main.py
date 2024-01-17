from pytube import YouTube
from PyQt5 import uic, QtWidgets
import music_main
import vid_main



def funcao_principal():
    url = entrada.lineEdit.text()

    if entrada.radioButton.isChecked():
       music_main.download_audio(url)
        


    elif entrada.radioButton_2.isChecked():
        vid_main.download_video(url)
        


app = QtWidgets.QApplication([])
entrada = uic.loadUi("entrada.ui")
entrada.pushButton_login.clicked.connect(funcao_principal)



entrada.show()
app.exec()
