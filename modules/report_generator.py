import requests
import os

class ReportGenerator:
    def __init__(self, save_directory):
        self.save_directory = save_directory

    def create_report(self, username, user_data, repositories, include_languages=False):
        report = f"Relatório do usuário {username}:\n\n"
        report += f"Nome: {user_data['name']}\n"
        report += f"Perfil: {user_data['html_url']}\n"
        report += f"Número de repositórios públicos: {user_data['public_repos']}\n"
        report += f"Número de seguidores: {user_data['followers']}\n"
        report += f"Número de usuários seguidos: {user_data['following']}\n\n"
        
        if include_languages:
            report += "Lista de Repositórios:\n"
            for repo in repositories:
                report += f"- {repo['name']}: {repo['html_url']}\n"
                repo_languages = self.get_repo_languages(repo['languages_url'])
                report += "  Linguagens utilizadas: "
                if repo_languages:
                    report += ", ".join(repo_languages)
                else:
                    report += "N/A"
                report += "\n"
        
        save_path = os.path.join(self.save_directory, f"{username}.txt")
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(report)
    
    def get_repo_languages(self, languages_url):
        response = requests.get(languages_url)
        if response.status_code != 200:
            return None
        languages_data = response.json()
        return list(languages_data.keys())
