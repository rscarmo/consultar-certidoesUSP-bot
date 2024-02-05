from typing import Optional
from PySide6.QtCore import Qt, QEvent
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import json

import shutil
from os.path import abspath, dirname, join
import os
import time
import sys

from ui_frmCertidoes import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QKeySequenceEdit
from PySide6.QtGui import QIcon

from pycpfcnpj import cpfcnpj

PATH = dirname(abspath(__file__)) + '\\'

settings = {
       "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }

prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings),
        #  'download.default_directory': PATH,
}

# self.CNPJ = '48371694000108'

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

class WindowCertidoes (QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        # Desabilitar botão de maximizar e fixar o tamanho da janela
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint) 
        self.setFixedSize(self.size())    

        self.cbTodas.stateChanged.connect(self.HabilitaDesabilita)
        self.btConsultar.clicked.connect(self.ConsultarClick)

        self.txtCNPJ.setInputMask('99.999.999/9999-99')
        self.txtCNPJ.setFocus()

        my_icon = QIcon()
        my_icon.addFile(PATH + 'certidoes.ico')
        self.setWindowIcon(my_icon)
        
    def event(self, event:QEvent):
        if (event.type() == QEvent.KeyPress) and \
        (event.key() in (Qt.Key.Key_Enter, Qt.Key.Key_Return)):
            self.ConsultarClick()
        return super().event(event)

    def HabilitaDesabilita(self, state):
        if state == 0:
            self.cbTodas.checkState()
            self.cbCND.setChecked(False)
            self.cbCRF.setChecked(False)
            self.cbCADIN.setChecked(False)
            self.cbE_Sancoes.setChecked(False) 
            self.cbApenados.setChecked(False)
            self.cbCEIS.setChecked(False)
        else:
            self.cbCND.setChecked(True)
            self.cbCRF.setChecked(True)
            self.cbCADIN.setChecked(True)
            self.cbE_Sancoes.setChecked(True)
            self.cbApenados.setChecked(True)
            self.cbCEIS.setChecked(True) 

    def ConsultarClick(self):
        self.CNPJ = self.txtCNPJ.text().replace('.', '').replace('/', '').replace('-', '')
        if self.CNPJ != '' and cpfcnpj.validate(self.CNPJ):
            if self.cbCND.isChecked():
                self.CND()
            if self.cbCRF.isChecked():
                self.CRF()
            if self.cbCADIN.isChecked():
                self.CADIN()                    
            if self.cbE_Sancoes.isChecked():
                self.Sancoes()                    
            if self.cbApenados.isChecked():
                self.Apenados()                    
            if self.cbCEIS.isChecked():
                self.CEIS()                    
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("CNPJ inválido.")
            # msg.setInformativeText('CNPJ inválido.')
            msg.setWindowTitle("Error")
            msg.exec_()        

    def CND(self):
    ### CND ###
        chrome_options = uc.ChromeOptions()
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_argument('--kiosk-printing')

        driver = uc.Chrome(chrome_options)
        driver.implicitly_wait(10)
        # driver.minimize_window()
        wait = WebDriverWait(driver, 10)

        Problema = False
        try:
            driver.get("https://solucoes.receita.fazenda.gov.br/servicos/certidaointernet/pj/emitir")
            wait.until(expected_conditions.visibility_of_element_located((By.ID, 'NI')))
            time.sleep(0.5)
            driver.find_element(By.ID, 'NI').send_keys(self.CNPJ)

            driver.find_element(By.ID, 'validar').click()

            driver.find_element(By.LINK_TEXT, 'Consulta de certidão e emissão de 2ª via').click()
            driver.find_element(By.ID, 'validar').click()
          
            driver.find_element(By.XPATH, '//*[@id="resultado"]/table/tbody/tr[1]/td[7]/a').click()

            download_wait(get_download_path(), 10)
            time.sleep(0.5)
            shutil.move(get_download_path() + '\\Certidao-' + self.CNPJ + '.pdf', get_download_path() + '\\CND - ' + self.CNPJ + '.pdf')
        except:
            Problema = True
            # print('Site está fora do ar.')

        if not Problema:
            driver.close()

    def CRF(self):
    ### CRF ###
        chrome_options2 = uc.ChromeOptions()

        chrome_options2.add_experimental_option('prefs', prefs)
        # chrome_options2.add_argument('--kiosk-printing')

        driver2 = uc.Chrome(chrome_options2)
        driver2.implicitly_wait(10)
        wait2 = WebDriverWait(driver2, 10)


        try:
            driver2.get("https://consulta-crf.caixa.gov.br/consultacrf/pages/consultaEmpregador.jsf")
            wait2.until(expected_conditions.visibility_of_element_located((By.ID, 'mainForm:txtInscricao1')))
            time.sleep(0.5)
            driver2.find_element(By.ID, 'mainForm:txtInscricao1').send_keys(self.CNPJ)
            
            # time.sleep(1)
            # shutil.move(PATH + 'Consulta Regularidade do Empregador.pdf', PATH + 'CND - ' + self.CNPJ + '.pdf')
        except:
            # try:
            #     time.sleep(1)
            #     shutil.move(get_download_path() + '\\Consulta Regularidade do Empregador.pdf', PATH + 'CND - ' + self.CNPJ + '.pdf')            
            # except:
            pass

    def CADIN(self):
    ### CADIN ###
        chrome_options3 = uc.ChromeOptions()

        chrome_options3.add_experimental_option('prefs', prefs)
        # chrome_options3.add_argument('--kiosk-printing')

        driver3 = uc.Chrome(chrome_options3)
        driver3.implicitly_wait(10)
        wait3 = WebDriverWait(driver3, 10)

        try:
            driver3.get('https://www.fazenda.sp.gov.br/cadin_estadual/pages/publ/cadin.aspx')
            driver3.find_element(By.PARTIAL_LINK_TEXT, 'Consulta Inscritos CADIN').click()
            try:
                driver3.switch_to.frame(driver3.find_element(By.ID, 'fbs'))
            except:
                driver3.find_element(By.PARTIAL_LINK_TEXT, 'Consulta Inscritos CADIN').click()
                driver3.switch_to.frame(driver3.find_element(By.ID, 'fbs'))

            wait3.until(expected_conditions.visibility_of_element_located((By.ID, 'ctl00_pageBody_tbDocto')))
            time.sleep(0.5)
            driver3.find_element(By.ID, 'ctl00_pageBody_tbDocto').send_keys(self.CNPJ)
        except:
            # print('Site está fora do ar.')
            pass

    def Sancoes(self):
    ### SANÇÕES ###
        chrome_options4 = uc.ChromeOptions()

        chrome_options4.add_experimental_option('prefs', prefs)
        chrome_options4.add_argument('--kiosk-printing')

        driver4 = uc.Chrome(chrome_options4)
        # driver4.minimize_window()
        driver4.implicitly_wait(10)
        wait4 = WebDriverWait(driver4, 10)


        Problema2 = False
        try:
            driver4.get('https://www.bec.sp.gov.br/Sancoes_ui/aspx/ConsultaAdministrativaFornecedor.aspx')

            wait4.until(expected_conditions.visibility_of_element_located((By.ID, 'txtCNPJCPF')))

            driver4.find_element(By.ID, 'txtCNPJCPF').send_keys(self.CNPJ)
            driver4.find_element(By.ID, 'ctl00_ContentPlaceHolder1_btnBuscar').click()
            driver4.find_element(By.ID, 'ctl00_ContentPlaceHolder1_btnImprimir').click()
            time.sleep(1)
            driver4.switch_to.alert.accept()
            
            download_wait(get_download_path(), 12)
            time.sleep(3)
            shutil.move(get_download_path() + '\\E-Sanções.pdf', get_download_path() + '\\E-Sanções - ' + self.CNPJ + '.pdf')
        except:
            # print('Site está fora do ar')
            Problema2 =True

        if not Problema2:
            driver4.close()

    def Apenados(self):
    ### Apenados ###
        chrome_options5 = uc.ChromeOptions()

        chrome_options5.add_experimental_option('prefs', prefs)
        chrome_options5.add_argument('--kiosk-printing')

        driver5 = uc.Chrome(chrome_options5)
        driver5.implicitly_wait(10)
        # driver5.minimize_window()
        wait5 = WebDriverWait(driver5, 10)

        Problema3 = False
        try: 
            driver5.get('https://www4.tce.sp.gov.br/apenados/publico/#/publicas/impedimento')
            wait5.until(expected_conditions.visibility_of_element_located((By.ID, 'cnpj')))
            time.sleep(0.5)
            driver5.find_element(By.ID, 'cnpj').send_keys(self.CNPJ, Keys.ENTER)
            driver5.find_element(By.PARTIAL_LINK_TEXT, 'pdf').click()

            download_wait(get_download_path(), 10)
            shutil.move(get_download_path() + '\\ImpedimentosContratoLicitacao.pdf', get_download_path() + '\\Apenados - ' + self.CNPJ + '.pdf')    
        except:
            # print('Site está fora do ar')
            Problema3 =True

        if not Problema3:
            driver5.close()

    def CEIS(self):
    ### CEIS ###
        chrome_options6 = uc.ChromeOptions()

        chrome_options6.add_experimental_option('prefs', prefs)
        chrome_options6.add_argument('--kiosk-printing')

        Problema4 = False
        try: 
            driver6 = uc.Chrome(chrome_options6)
            driver6.implicitly_wait(10)
            # driver6.minimize_window()
            wait6 = WebDriverWait(driver6, 10)

            driver6.get('https://portaldatransparencia.gov.br/sancoes/consulta?ordenarPor=nomeSancionado&direcao=asc')
            driver6.find_element(By.XPATH, '/html/body/main/div[2]/div/div[1]/div/div/ul/li[6]/div/button').click()
            time.sleep(0.5)
            driver6.find_element(By.ID, 'token-input-cpfCnpj').send_keys(self.CNPJ, Keys.ENTER)
            driver6.find_element(By.XPATH, '/html/body/main/div[2]/div/div[1]/div/div/ul/li[6]/div/div/div/div[2]/input[2]').click()
            driver6.find_element(By.XPATH, '/html/body/main/div[2]/div/div[2]/section/div/p/button[1]').click()
            driver6.find_element(By.XPATH, '/html/body/main/div[2]/div/div[2]/div[2]/ul/li[1]/a').click()
            # NÃO SALVA NO LUGAR CERTO SABE DEUS PORQUE, ENTÃO...
            # wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/main/div[2]/div/div[2]/div[2]/ul/li[1]/a')))
            download_wait(get_download_path(), 6)
            shutil.move(get_download_path() + '\\Detalhamento das Sanções Vigentes - Portal da transparência.pdf', get_download_path() + '\\CEIS - ' + self.CNPJ + '.pdf')

        except:
            Problema4 =True

        if not Problema4:
            driver6.close()   

def download_wait(directory, timeout, nfiles=None):
    """
    Wait for downloads to finish with a specified timeout.

    Args
    ----
    directory : str
        The path to the folder where the files will be downloaded.
    timeout : int
        How many seconds to wait until timing out.
    nfiles : int, defaults to None
        If provided, also wait for the expected number of files.

    """
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(1)
        dl_wait = False
        files = os.listdir(directory)
        if nfiles and len(files) != nfiles:
            dl_wait = True

        for fname in files:
            if fname.endswith('.crdownload'):
                dl_wait = True

        seconds += 1
    return seconds
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = WindowCertidoes()
    mainWindow.show()
    app.exec()

