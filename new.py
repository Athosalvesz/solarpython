import random

class SolarOptimizer:
    def __init__(self):
  
        self.log_file = "solar_optimizer.log"
        self.historia_geracao = []
        self.historia_consumo = []

    def simular_valor(self, minimo, maximo):
        """Gera um valor aleatório de energia entre o mínimo e máximo especificados."""
        return round(random.uniform(minimo, maximo), 2)

    def simular_geracao_energia(self):
        """Simula a energia solar gerada (em kWh) para um dia e armazena na história."""
        gerado = self.simular_valor(0, 10)
        self.historia_geracao.append(gerado)
        return gerado

    def simular_consumo_energia(self):
        """Simula o consumo de energia (em kWh) para um dia e armazena na história."""
        consumido = self.simular_valor(5, 15)
        self.historia_consumo.append(consumido)
        return consumido

    def otimizar_uso_energia(self, gerado, consumido):
        """
        Fornece recomendações de otimização baseado no balanço
        entre energia gerada e consumida.
        """
        if gerado >= consumido:
            recomendacao = "Eficiência ótima: uso de energia solar adequado."
        else:
            deficit = consumido - gerado
            recomendacao = f"Reduza o consumo em {deficit:.2f} kWh ou aumente a geração."
        return recomendacao

    def sugerir_economia_energia(self):
        """Sugere formas genéricas de economizar energia."""
        dicas = [
            "Desligue aparelhos quando não estiverem em uso.",
            "Utilize lâmpadas de LED.",
            "Otimize o uso de ar condicionado.",
            "Utilize eletrodomésticos eficientes.",
            "Aproveite a luz natural durante o dia.",
        ]
        return random.sample(dicas, 3) 
    def formatar_dicas_economia(self):
        """Formata as dicas em um layout de lista."""
        dicas = self.sugerir_economia_energia()
        return "\n".join(f"- {dica}" for dica in dicas)

    def calcular_media(self, valores):
        """Retorna a média de uma lista de valores."""
        return sum(valores) / len(valores) if valores else 0

    def salvar_log(self, apartamento_id, dia, gerado, consumido, recomendacao):
        """Salva métricas e recomendações em um arquivo de log."""
        try:
            with open(self.log_file, 'a') as file:
                file.write(f"Apartamento ID: {apartamento_id}, Dia: {dia}, Gerado: {gerado}, Consumido: {consumido}, Recomendações: {recomendacao}\n")
        except IOError as e:
            print(f"Erro ao salvar log: {e}")

    def mostrar_estatisticas(self):
        """Exibe estatísticas de energia gerada e consumida."""
        if self.historia_geracao and self.historia_consumo:
            media_geracao = self.calcular_media(self.historia_geracao)
            media_consumo = self.calcular_media(self.historia_consumo)
            print(f"Média gerada: {media_geracao:.2f} kWh | Média consumida: {media_consumo:.2f} kWh")
        else:
            print("Sem dados para exibir estatísticas.")

    def rodar(self):
        """Executa a simulação principal do otimizador."""
        while True:
            apartamento_id = input("\nPor favor, insira o ID do apartamento que deseja verificar: ").strip()
            
            dia = input("Simular geração e consumo para qual dia? ").strip()
            print(f"\nSimulando para o apartamento ID: {apartamento_id}, dia: {dia}")

            gerado = self.simular_geracao_energia()
            consumido = self.simular_consumo_energia()
            print(f"\nGerado: {gerado} kWh | Consumido: {consumido} kWh")

            recomendacao = self.otimizar_uso_energia(gerado, consumido)
            print(f"Recomendação:\n{recomendacao}\n{'='*40}")

            
            resposta = input("Gostaria de receber dicas sobre economia de energia? (s/n): ").strip().lower()
            if resposta == 's':
                dicas = self.formatar_dicas_economia()
                print(f"Dicas de economia de energia:\n{dicas}\n{'='*40}")

            self.salvar_log(apartamento_id, dia, gerado, consumido, recomendacao)
            self.mostrar_estatisticas()

        
            if input("Simular outro dia? (s/n): ").strip().lower() != 's':
                print("Simulação encerrada.")
                break

if __name__ == "__main__":

    SolarOptimizer().rodar()
