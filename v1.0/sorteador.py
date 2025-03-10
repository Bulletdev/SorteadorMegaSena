import random
import tkinter as tk
from tkinter import ttk
import itertools
from collections import Counter

class MegaSenaNumberGenerator:
    def __init__(self):
        # Números dos sorteios de fim de ano (31/12) de 2009 a 2024
        self.historical_results = [
            [01, 17, 19, 29, 50, 57],  # 2024
            [21, 24, 33, 41, 45, 56],  # 2023
            [4, 5, 10, 34, 58, 59],    # 2022
            [12, 15, 23, 32, 33, 46],  # 2021
            [17, 20, 22, 35, 41, 42],  # 2020
            [3, 35, 38, 40, 57, 58],   # 2019
            [5, 10, 12, 18, 25, 33],   # 2018
            [3, 6, 10, 17, 34, 37],    # 2017
            [5, 11, 22, 24, 51, 53],   # 2016
            [2, 18, 31, 42, 51, 56],   # 2015
            [1, 5, 11, 16, 20, 56],    # 2014
            [20, 30, 36, 38, 47, 53],  # 2013
            [14, 32, 33, 36, 41, 52],  # 2012
            [3, 4, 29, 36, 45, 55],    # 2011
            [2, 10, 34, 37, 43, 50],   # 2010
            [10, 27, 40, 46, 49, 58]   # 2009
            ]
        
        all_numbers_flat = [num for results in self.historical_results for num in results]
        
        number_counts = Counter(all_numbers_flat)
        
        self.most_frequent_numbers = [
            num for num, count in number_counts.most_common(6)
        ]
        
        self.least_frequent_numbers = [
            num for num, count in number_counts.most_common()[:-7:-1]
        ]
        
        self.all_numbers = list(range(1, 61))

    def generate_combinations(self, method='mixed', num_combinations=5):
        """
        Generate lottery number combinations using different strategies
        
        Args:
        - method: 'most_frequent', 'least_frequent', 'mixed', 'random'
        - num_combinations: number of combinations to generate
        
        Returns:
        List of number combinations
        """
        combinations = []
        for _ in range(num_combinations):
            if method == 'most_frequent':
                combination = self._generate_most_frequent_combination()
            elif method == 'least_frequent':
                combination = self._generate_least_frequent_combination()
            elif method == 'mixed':
                combination = self._generate_mixed_combination()
            elif method == 'random':
                combination = self._generate_random_combination()
            else:
                raise ValueError("Invalid method. Choose 'most_frequent', 'least_frequent', 'mixed', or 'random'.")
            
            combinations.append(sorted(combination))
        return combinations

    def _generate_most_frequent_combination(self):
        """Generate a combination using the most frequent numbers"""
        return random.sample(self.most_frequent_numbers, 6)

    def _generate_least_frequent_combination(self):
        """Generate a combination using the least frequent numbers"""
        return random.sample(self.least_frequent_numbers, 6)

    def _generate_mixed_combination(self):
        """Generate a mixed combination of most and least frequent numbers"""
        combination = (
            random.sample(self.most_frequent_numbers, 3) + 
            random.sample(self.least_frequent_numbers, 3)
        )
        random.shuffle(combination)
        return combination

    def _generate_random_combination(self):
        """Generate a completely random combination"""
        return random.sample(self.all_numbers, 6)

    def analyze_combinations(self, combinations):
        """
        Provide basic analysis of generated combinations
        
        Args:
        - combinations: List of number combinations
        
        Returns:
        Dictionary with analysis details
        """
        analysis = {
            'total_combinations': len(combinations),
            'unique_combinations': len(set(tuple(combo) for combo in combinations)),
            'frequency_analysis': {}
        }
        
        all_numbers_generated = [num for combo in combinations for num in combo]
        
        for num in range(1, 61):
            count = all_numbers_generated.count(num)
            if count > 0:
                analysis['frequency_analysis'][num] = count
        
        return analysis

class MegaSenaGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerador de Números da Mega-Sena")
        self.master.geometry("600x700")
        
        self.generator = MegaSenaNumberGenerator()
        
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 12))
        self.style.configure("TButton", font=("Arial", 12))
        
        ttk.Label(master, text="Escolha o Método de Geração:", style="TLabel").pack(pady=10)
        
        self.method_var = tk.StringVar(value="mixed")
        methods = [
            ("Números Mais Frequentes", "most_frequent"),
            ("Números Menos Frequentes", "least_frequent"),
            ("Método Misto", "mixed"),
            ("Aleatório", "random")
        ]
        
        for label, method in methods:
            ttk.Radiobutton(
                master, 
                text=label, 
                variable=self.method_var, 
                value=method
            ).pack(pady=5)
        
        ttk.Label(master, text="Número de Combinações:", style="TLabel").pack(pady=10)
        self.num_combinations_var = tk.IntVar(value=5)
        num_combinations_spinbox = ttk.Spinbox(
            master, 
            from_=1, 
            to=10, 
            textvariable=self.num_combinations_var, 
            width=5
        )
        num_combinations_spinbox.pack(pady=5)
        
        generate_button = ttk.Button(
            master, 
            text="Gerar Combinações", 
            command=self.generate_and_display
        )
        generate_button.pack(pady=20)
        
        self.results_frame = ttk.Frame(master)
        self.results_frame.pack(pady=10, expand=True, fill=tk.BOTH)
        
        self.results_text = tk.Text(
            self.results_frame, 
            height=15, 
            width=50, 
            font=("Courier", 12)
        )
        self.results_text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        
        scrollbar = ttk.Scrollbar(
            self.results_frame, 
            orient=tk.VERTICAL, 
            command=self.results_text.yview
        )
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.results_text.configure(yscrollcommand=scrollbar.set)

    def generate_and_display(self):
        """Gera combinações e exibe na interface"""
        self.results_text.delete(1.0, tk.END)
        
        method = self.method_var.get()
        num_combinations = self.num_combinations_var.get()
        
        try:
            combinations = self.generator.generate_combinations(
                method=method, 
                num_combinations=num_combinations
            )
            
            analysis = self.generator.analyze_combinations(combinations)
            
            self.results_text.insert(tk.END, f"Método: {method}\n")
            self.results_text.insert(tk.END, f"Número de Combinações: {num_combinations}\n\n")
            
            self.results_text.insert(tk.END, "Combinações Geradas:\n")
            for idx, combo in enumerate(combinations, 1):
                self.results_text.insert(tk.END, f"{idx}. {combo}\n")
            
            self.results_text.insert(tk.END, "\nAnálise das Combinações:\n")
            self.results_text.insert(tk.END, f"Total de Combinações Únicas: {analysis['unique_combinations']}\n\n")
            
            self.results_text.insert(tk.END, "Frequência dos Números:\n")
            sorted_frequency = sorted(
                analysis['frequency_analysis'].items(), 
                key=lambda x: x[1], 
                reverse=True
            )
            for num, freq in sorted_frequency:
                self.results_text.insert(tk.END, f"Número {num}: {freq} vezes\n")
        
        except Exception as e:
            self.results_text.insert(tk.END, f"Erro ao gerar combinações: {str(e)}")

def main():
    root = tk.Tk()
    app = MegaSenaGeneratorApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
