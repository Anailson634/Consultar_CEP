import sys
from GUI import *
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox

class Root(QMainWindow, Ui_Covid_19):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.pushButton.clicked.connect(self.search)
        self.Help.clicked.connect(self.HelpMe)



    def search(self):
            import requests
            
            if len(self.Cep.text()) != 8:
                self.Caract_popup(f'Você informou um CEP com {len(self.Cep.text())} caracteres. sô cera válido com 8 caracteres!', 
                'Menos de 8 caracteres' if len(self.Cep.text()) < 8 else 'Maior que 8 caracteres')
            else:
                try:
                    web = requests.get(f'https://viacep.com.br/ws/{self.Cep.text()}/json/')
                    Dic = web.json()

                    self.CEP.setText(f"CEP: {Dic['cep']}")
                    self.lgd.setText(f"Logradouro: {Dic['logradouro']}")
                    self.cpl.setText(f"Complemento: {Dic['complemento']}")
                    self.uf.setText(f"Bairro: {Dic['bairro']}")
                    self.bairro.setText(f"localidade: {Dic['localidade']}")
                    self.ddd.setText(f"uf: {Dic['uf']}")
                    self.ibge.setText(f"Ibge: {Dic['ibge']}")
                    self.gia.setText(f"Gia: {Dic['gia']}")
                    self.local.setText(f"DDD: {Dic['ddd']}")
                    
                except:
                    self.Caract_popup('CEP inálido!', 'O CEP que você informou não existe!')
    
    def HelpMe(self):
    	self.Caract_popup('CEP verdadeiro!, e não pode conter nenhum caractere especial como "-"', 'Ajuda')
    	
    def Caract_popup(self, text, title):
        pop = QMessageBox()
        pop.setWindowTitle(title)
        pop.setText(text)

        pop.exec_()
        

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Root()
    app.show()
    qt.exec_()
