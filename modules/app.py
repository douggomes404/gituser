# modules/app.py
import os
from modules.github_api import GithubAPI
from modules.report_generator import ReportGenerator

class ReportApp:
    def __init__(self):
        self.save_directory = "./relatorio/"
        self.github_api = GithubAPI()

    def run(self):
        username = input("Digite o nome de usuário do GitHub: ")
        
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)
        
        user_data = self.github_api.get_user_data(username)
        if user_data is None:
            print("Erro ao obter dados do usuário.")
            return
        
        repositories = self.github_api.get_user_repositories(username)
        
        include_languages = input("Deseja incluir informações detalhadas dos repositórios? Responda com 'sim' ou 'não': ")
        include_languages = include_languages.lower() == "sim"
        
        report_generator = ReportGenerator(self.save_directory)
        report_generator.create_report(username, user_data, repositories, include_languages)
        print(f"Relatório salvo em {self.save_directory}{username}.txt")

if __name__ == "__main__":
    app = ReportApp()
    app.run()
