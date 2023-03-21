import os
import sys
from os import listdir
from os.path import isfile, join, isdir
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtGui import QMovie

class copy():

    def __init__(self):
        # iniciando a tela
        self.option_window = uic.loadUi('telas/tela_opcao.ui')
        self.option_window.setWindowTitle('Opcão - COMPARTILHADO')

        # atribuindo os clicks dos botões
        self.option_window.btn_entrar_copy_arquivos.clicked.connect(self.copy_file_window)
        self.option_window.btn_entrar_copy_pastas.clicked.connect(self.copy_folder_window)

        self.option_window.btn_entrar_del_arquivos.clicked.connect(self.del_file_window)
        self.option_window.btn_entrar_del_pastas.clicked.connect(self.del_folder_window)

        self.option_window.btn_entrar_ren_arquivos.clicked.connect(self.ren_file_window)
        self.option_window.btn_entrar_ren_pastas.clicked.connect(self.ren_folder_window)

        self.option_window.setWindowFlags(self.option_window.windowFlags() & QtCore.Qt.CustomizeWindowHint)
        self.option_window.setWindowFlags(self.option_window.windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)

        self.option_window.btn_sair.clicked.connect(self.close_window)
        self.option_window.show()

    #####################################################################################################
    #####################################################################################################

    # função para abrir a tela principal dnv
    def main_window_copy_file(self):
        # fechando a tela que já estava aberta e abrindo a main dnv
        self.option_window.show()
        self.file_window_copy.hide()
        # self.net_use()

    # função para abrir a tela principal dnv
    def main_window_copy_folder(self):
        # fechando a tela que já estava aberta e abrindo a main dnv
        self.option_window.show()
        self.folder_window_copy.hide()
        # self.net_use()

    # função para abrir a tela principal dnv
    def main_window_del_file(self):
        # fechando a tela que já estava aberta e abrindo a main dnv
        self.option_window.show()
        self.file_window_del.hide()
        # self.net_use()

    # função para abrir a tela principal dnv
    def main_window_del_folder(self):
        # fechando a tela que já estava aberta e abrindo a main dnv
        self.option_window.show()
        self.folder_window_del.hide()
        # self.net_use()

    # função para abrir a tela principal dnv
    def main_window_ren_file(self):
        # fechando a tela que já estava aberta e abrindo a main dnv
        self.option_window.show()
        self.file_window_ren.hide()
        # self.net_use()

    # função para abrir a tela principal dnv
    def main_window_ren_folder(self):
        # fechando a tela que já estava aberta e abrindo a main dnv
        self.option_window.show()
        self.folder_window_ren.hide()
        # self.net_use()

    #####################################################################################################
    #####################################################################################################

        # função para abrir a tela
        def copy_file_window(self):
            # iniciando a tela
            self.file_window = uic.loadUi('telas/tela_caminho_arquivos.ui')
            self.file_window.setWindowTitle('Copiar arquivos - COMPARTILHADO')

            # atribuindo o click ao botão
            self.file_window.btn_entrar_arquivo.clicked.connect(self.copy_file_func)
            self.file_window.btn_voltar_arquivo.clicked.connect(self.main_window_file)
            self.file_window.btn_explorador_arquivo.clicked.connect(self.open_explorer)

            self.file_window.setWindowFlags(self.file_window.windowFlags() & QtCore.Qt.CustomizeWindowHint)
            self.file_window.setWindowFlags(self.file_window.windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)

            self.file_window.show()
            self.option_window.hide()

    #####################################################################################################
    #####################################################################################################

    # função para abrir a tela
    def copy_file_window(self):
        # iniciando a tela
        self.file_window_copy = uic.loadUi('telas/tela_copiar_arquivos.ui')
        self.file_window_copy.setWindowTitle('Copiar arquivos - COMPARTILHADO')

        # atribuindo o click ao botão
        self.file_window_copy.btn_entrar.clicked.connect(self.copy_file_func)
        self.file_window_copy.btn_voltar.clicked.connect(self.main_window_copy_file)
        self.file_window_copy.btn_explorador_arquivo.clicked.connect(self.open_explorer)

        self.file_window_copy.setWindowFlags(self.file_window_copy.windowFlags() & QtCore.Qt.CustomizeWindowHint)
        self.file_window_copy.setWindowFlags(self.file_window_copy.windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)

        self.file_window_copy.show()
        self.option_window.hide()

    # função para abrir a tela
    def copy_folder_window(self):

        # iniciando a tela
        self.folder_window_copy = uic.loadUi('telas/tela_copiar_pastas.ui')
        self.folder_window_copy.setWindowTitle('Copiar pastas e arquivos - COMPARTILHADO')

        # atribuindo o click ao botão
        self.folder_window_copy.btn_entrar.clicked.connect(self.copy_folder_func)
        self.folder_window_copy.btn_voltar.clicked.connect(self.main_window_copy_folder)
        self.folder_window_copy.btn_explorador_arquivo.clicked.connect(self.open_explorer)
        self.folder_window_copy.setWindowFlags(self.folder_window_copy.windowFlags() & QtCore.Qt.CustomizeWindowHint)
        self.folder_window_copy.setWindowFlags(self.folder_window_copy.windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)

        self.folder_window_copy.show()
        self.option_window.hide()

    # função para abrir a tela
    def del_file_window(self):
        # iniciando a tela
        self.file_window_del = uic.loadUi('telas/tela_deletar_arquivo.ui')
        self.file_window_del.setWindowTitle('Deletar arquivo - COMPARTILHADO')

        # atribuindo o click ao botão
        self.file_window_del.btn_entrar.clicked.connect(self.del_file_func)
        self.file_window_del.btn_voltar.clicked.connect(self.main_window_del_file)
        self.file_window_del.btn_explorador_arquivo.clicked.connect(self.open_explorer)

        self.file_window_del.setWindowFlags(self.file_window_del.windowFlags() & QtCore.Qt.CustomizeWindowHint)
        self.file_window_del.setWindowFlags(self.file_window_del.windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)

        self.file_window_del.show()
        self.option_window.hide()

    # função para abrir a tela
    def del_folder_window(self):
        # iniciando a tela
        self.folder_window_del = uic.loadUi('telas/tela_deletar_pasta.ui')
        self.folder_window_del.setWindowTitle('Deletar pasta - COMPARTILHADO')

        # atribuindo o click ao botão
        self.folder_window_del.btn_entrar.clicked.connect(self.del_folder_func)
        self.folder_window_del.btn_voltar.clicked.connect(self.main_window_del_folder)
        self.folder_window_del.btn_explorador_arquivo.clicked.connect(self.open_explorer)
        self.folder_window_del.setWindowFlags(self.folder_window_del.windowFlags() & QtCore.Qt.CustomizeWindowHint)
        self.folder_window_del.setWindowFlags(self.folder_window_del.windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)

        self.folder_window_del.show()
        self.option_window.hide()

    # função para abrir a tela
    def ren_file_window(self):
        # iniciando a tela
        self.file_window_ren = uic.loadUi('telas/tela_renomear_arquivo.ui')
        self.file_window_ren.setWindowTitle('Renomear arquivo - COMPARTILHADO')

        # atribuindo o click ao botão
        self.file_window_ren.btn_entrar.clicked.connect(self.ren_file_func)
        self.file_window_ren.btn_voltar.clicked.connect(self.main_window_ren_file)
        self.file_window_ren.btn_explorador_arquivo.clicked.connect(self.open_explorer)

        self.file_window_ren.setWindowFlags(self.file_window_ren.windowFlags() & QtCore.Qt.CustomizeWindowHint)
        self.file_window_ren.setWindowFlags(self.file_window_ren.windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)

        self.file_window_ren.show()
        self.option_window.hide()

    # função para abrir a tela
    def ren_folder_window(self):
        # iniciando a tela
        self.folder_window_ren = uic.loadUi('telas/tela_renomear_pasta.ui')
        self.folder_window_ren.setWindowTitle('Renomear pasta - COMPARTILHADO')

        # atribuindo o click ao botão
        self.folder_window_ren.btn_entrar.clicked.connect(self.ren_folder_func)
        self.folder_window_ren.btn_voltar.clicked.connect(self.main_window_ren_folder)
        self.folder_window_ren.btn_explorador_pasta.clicked.connect(self.open_explorer)

        self.folder_window_ren.setWindowFlags(self.folder_window_ren.windowFlags() & QtCore.Qt.CustomizeWindowHint)
        self.folder_window_ren.setWindowFlags(self.folder_window_ren.windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)

        self.folder_window_ren.show()
        self.option_window.hide()

    # função para o popup
    def popup_window(self, data="", tAlert=""):

        self.popup = uic.loadUi("telas/tela_popup.ui")
        self.popup.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.popup.btn_sair_popup.clicked.connect(self.close_window)
        color = ''

        if tAlert == 'success':
            self.popup.certo.show()
            self.popup.erro.hide()
            self.popup.alert.hide()
            self.popup.btn_sair_popup.show()
            color = 'rgb(0, 170, 0)'

        elif tAlert == 'alert':
            self.popup.certo.hide()
            self.popup.erro.hide()
            self.popup.alert.show()
            self.popup.btn_sair_popup.show()
            color = 'rgb(255, 170, 0)'

        elif tAlert == 'danger':
            self.popup.certo.hide()
            self.popup.erro.show()
            self.popup.alert.hide()
            self.popup.btn_sair_popup.show()
            color = 'rgb(255, 0, 0)'

        else:
            self.popup.certo.hide()
            self.popup.erro.hide()
            self.popup.alert.hide()

        self.popup.info.setStyleSheet(f"color: {color}")
        self.popup.info.setText(data)
        self.popup.show()

    #####################################################################################################
    #####################################################################################################

    # função para copiar arquivos
    def copy_file_func(self):
        path_file = self.file_window_copy.txt_entrada_arquivo.text()
        path_direct_file = self.file_window_copy.txt_saida_arquivo.text()
        file_name_copy = self.file_window_copy.txt_nome_arquivo.text()
        user = "br" + "\\" + "tparca"
        password = "timeconexao20@@"


        if (os.path.exists(path_file) and os.path.exists(path_direct_file)):
            files = [f for f in listdir(path_file) if isfile(join(path_file, f))]
            if files == []:
                print(f'Não existem arqvos nesta pasta: {path_file}')
                self.file_window_copy.hide()
                self.popup_window('Arquivo(s) inexistente(s)', 'alert')
            else:
                print(f'Arquivos encontrados: {files}')
                try:
                    script_robo_file = f"psexec -u \"{user}\" -p \"{password}\" cmd /k \"\"C:/DCAP_COMPARTILHADO/file/copy_file.bat\" \"usuario\" \"senha\" \"{path_file}\" \"{path_direct_file}\" \"{file_name_copy}\"\""
                    os.system(script_robo_file)
                    self.file_window_copy.hide()
                except:
                    print('Não foi possível copiar os arquivos')
                    self.file_window_copy.hide()
                    self.popup_window('Erro ao copiar o arquivo', 'danger')

        else:
            print("Diretório Inexistente")
            self.file_window_copy.hide()
            self.popup_window('Diretório inexistente ', 'danger')

    # função para copiar pastas
    def copy_folder_func(self):
        path_folder = self.folder_window_copy.txt_entrada_pasta.text()
        path_direct_folder = self.folder_window_copy.txt_saida_pasta.text()
        user = "br" + "\\" + "tparca"
        password = "timeconexao20@@"


        if (os.path.exists(path_folder) and os.path.exists(path_direct_folder)):
            folders = [f for f in listdir(path_folder) if isdir(join(path_folder, f))]

            if folders == []:
                print(f'Não existem pastas no seguinte diretório: {path_folder}')
                self.folder_window_copy.hide()
                self.popup_window('Pasta não encontrada', 'alert')
            else:
                try:
                    script_robo_folder = f"psexec -u \"{user}\" -p \"{password}\" cmd /k \"\"C:/DCAP_COMPARTILHADO/folder/copy_folder.bat\" \"usuario\" \"senha\" \"{path_folder}\" \"{path_direct_folder} \"\""
                    os.system(script_robo_folder)
                    self.file_window_copy.hide()
                except:
                    print('Não foi possível copiar a(s) pasta(s)')
                    self.folder_window_copy.hide()
                    self.popup_window('Erro ao copiar', 'danger')
        else:
            print("Diretório Inexistente")
            self.folder_window_copy.hide()
            self.popup_window('Diretório inexistente', 'danger')

    # função para deletar arquivos
    def del_file_func(self):
        path_file_del = self.file_window_del.txt_entrada_del_arquivo.text()
        file_name = self.file_window_del.txt_entrada_del_nome_arquivo.text()
        user = "br" + "\\" + "tparca"
        password = "timeconexao20@@"

        if (os.path.exists(path_file_del)):
            files = [f for f in listdir(path_file_del) if isfile(join(path_file_del, f))]

            if files == []:
                print(f'Não existem arquivos no seguinte diretório: {path_file_del}')
                self.folder_window.hide()
                self.popup_window('Arquivo não encontrado', 'alert')
            else:
                try:
                    file_name = path_file_del + "\\" + file_name
                    script_del_file = f"psexec -u \"{user}\" -p \"{password}\" cmd /k \"\"C:/DCAP_COMPARTILHADO/file/del_file.bat\" \"usuario\" \"senha\" \"{file_name}\"\""
                    os.system(script_del_file)
                    self.file_window_del.hide()
                    self.popup_window('Deletado com sucesso', 'success')
                except:
                    print('Não foi possível deletar o(s) arquivo(s)')
                    self.popup_window('Erro ao deletar', 'danger')
        else:
            print("Diretório Inexistente")
            self.popup_window('Diretório inexistente', 'danger')

    # função para deletar pastas
    def del_folder_func(self):
        path_folder_del = self.folder_window_del.txt_entrada_del_pasta.text()
        user = "br" + "\\" + "tparca"
        password = "timeconexao20@@"

        if (os.path.exists(path_folder_del)):
            try:
                script_del_folder = f"psexec -u \"{user}\" -p \"{password}\" cmd /k \"\"C:/DCAP_COMPARTILHADO/folder/del_folder.bat\" \"usuario\" \"senha\" \"{path_folder_del}\"\""
                os.system(script_del_folder)
                self.folder_window_del.hide()
                self.popup_window('Deletado com sucesso', 'success')
            except:
                print("Não foi possível concluír a operação.")
                self.folder_window_del.hide()
                self.popup_window('Erro ao deletar', 'danger')
        else:
            print("Diretório Inexistente")
            self.file_window_del.hide()
            self.popup_window('Diretório inexistente', 'danger')

    # função para renomear um arquivo
    def ren_file_func(self):
        path_file_ren = self.file_window_ren.txt_caminho_arquivo.text()
        file_name = self.file_window_ren.txt_nome_atual_arquivo.text()
        new_file_name = self.file_window_ren.txt_nome_novo_arquivo.text()
        user = "br" + "\\" + "tparca"
        password = "timeconexao20@@"


        if (os.path.exists(path_file_ren)):
            files = [f for f in listdir(path_file_ren) if isfile(join(path_file_ren, f))]
            if files == []:
                print(f'Não existem arquivos nesta pasta: {path_file_ren}')
                self.file_window.hide()
                self.popup_window('Arquivo(s) inexistente(s)', 'alert')
            else:
                try:
                    script_ren_file = f"psexec -u \"{user}\" -p \"{password}\" cmd /k \"\"C:/DCAP_COMPARTILHADO/file/ren_file.bat\" \"usuario\" \"senha\" \"{path_file_ren}\" \"{file_name}\" \"{new_file_name}\"\""
                    os.system(script_ren_file)
                    self.file_window_ren.hide()
                    self.popup_window('Renomeado com sucesso', 'success')
                except:
                    print('Não foi possível renomear o(s) arquivo(s)')
                    self.file_window_ren.hide()
                    self.popup_window('Erro ao renomear', 'danger')
        else:
            print("Diretório Inexistente")
            self.file_window_ren.hide()
            self.popup_window('Diretório inexistente', 'danger')

    # função para renomear pastas
    def ren_folder_func(self):
        path_folder_ren = self.folder_window_ren.txt_caminho_pasta.text()
        folder_name = self.folder_window_ren.txt_nome_atual_pasta.text()
        new_folder_name = self.folder_window_ren.txt_nome_novo_pasta.text()
        user = "br" + "\\" + "tparca"
        password = "timeconexao20@@"

        if (os.path.exists(path_folder_ren)):
            try:
                script_robo_folder = f"psexec -u \"{user}\" -p \"{password}\" cmd /k \"\"C:/DCAP_COMPARTILHADO/folder/ren_folder.bat\" \"usuario\" \"senha\" \"{path_folder_ren}\" \"{folder_name}\" \"{new_folder_name} \"\""
                os.system(script_robo_folder)
                self.folder_window_ren.hide()
                self.popup_window('Renomeado com sucesso', 'success')
            except:
                print('Não foi possível renomear a(s) pasta(s)')
                self.folder_window_ren.hide()
                self.popup_window('Erro ao renomear', 'danger')
        else:
            print("Diretório Inexistente")
            self.folder_window_ren.hide()
            self.popup_window('Diretório inexistente', 'danger')


    #####################################################################################################
    #####################################################################################################

    # função para abrir o explorador de arquivos
    def open_explorer(self):
        script_open_explorer = "start explorer"
        os.system(script_open_explorer)

    #####################################################################################################
    #####################################################################################################

    # função para fechar a tela
    def close_window(self):
        sys.exit()

    def net_use(self):
        script_net_use = "start C:/DCAP_COMPARTILHADO/script_ca/net_use.bat"
        os.system(script_net_use)

    #####################################################################################################
    ####################################################################################################

# chamando a função main
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    c = copy()
    sys.exit(app.exec_())
