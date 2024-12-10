import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Dict

from GerarNumeros import SorteadorMegaSena

class MegaSenaGeneratorApp:
    """
    A GUI application for generating Mega-Sena lottery number combinations.
    
    Provides an interface to select generation method, number of combinations,
    and display the results with basic analysis.
    """
    
    def __init__(self, master: tk.Tk):
        """
        Initialize the Mega-Sena Generator application.
        
        Args:
            master (tk.Tk): The main window of the application
        """
        self.master = master
        self._setup_window()
        
        self.generator = SorteadorMegaSena()
        self._create_widgets()

    def _setup_window(self) -> None:
        """Configure the main application window."""
        self.master.title("Gerador de Números da Mega-Sena")
        self.master.geometry("600x700")
        self.master.resizable(False, False)
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 12))
        self.style.configure("TButton", font=("Arial", 12))
        self.style.configure("TRadiobutton", font=("Arial", 10))

    def _create_widgets(self) -> None:
        """Create and layout all GUI widgets."""
        self._create_method_selection()
        
        self._create_combinations_selection()
        
        self._create_generate_button()
        
        self._create_results_display()

    def _create_method_selection(self) -> None:
        """Create radio buttons for number generation method."""
        ttk.Label(
            self.master, 
            text="Escolha o Método de Geração:", 
            style="TLabel"
        ).pack(pady=10)
        
        self.method_var = tk.StringVar(value="mixed")
        methods = [
            ("Números Mais Frequentes", "most_frequent"),
            ("Números Menos Frequentes", "least_frequent"),
            ("Método Misto", "mixed"),
            ("Aleatório", "random")
        ]
        
        for label, method in methods:
            ttk.Radiobutton(
                self.master, 
                text=label, 
                variable=self.method_var, 
                value=method,
                style="TRadiobutton"
            ).pack(pady=5)

    def _create_combinations_selection(self) -> None:
        """Create spinbox for selecting number of combinations."""
        ttk.Label(
            self.master, 
            text="Número de Combinações:", 
            style="TLabel"
        ).pack(pady=10)
        
        self.num_combinations_var = tk.IntVar(value=5)
        num_combinations_spinbox = ttk.Spinbox(
            self.master, 
            from_=1, 
            to=10, 
            textvariable=self.num_combinations_var, 
            width=5
        )
        num_combinations_spinbox.pack(pady=5)

    def _create_generate_button(self) -> None:
        """Create the generate combinations button."""
        generate_button = ttk.Button(
            self.master, 
            text="Gerar Combinações", 
            command=self._generate_and_display
        )
        generate_button.pack(pady=20)

    def _create_results_display(self) -> None:
        """Create the results display area with scrollbar."""
        self.results_frame = ttk.Frame(self.master)
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

    def _generate_and_display(self) -> None:
        """
        Generate lottery number combinations and display results.
        
        Handles the generation process, including error handling 
        and result display.
        """
        self.results_text.delete(1.0, tk.END)
        
        method = self.method_var.get()
        num_combinations = self.num_combinations_var.get()
        
        try:
            combinations = self.generator.generate_combinations(
                method=method, 
                num_combinations=num_combinations
            )
            
            analysis = self.generator.analyze_combinations(combinations)
            
            self._display_results(method, num_combinations, combinations, analysis)
        
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def _display_results(
        self, 
        method: str, 
        num_combinations: int, 
        combinations: List[List[int]], 
        analysis: Dict[str, any]
    ) -> None:
        """
        Format and display the generated combinations and analysis.
        
        Args:
            method (str): Generation method used
            num_combinations (int): Number of combinations generated
            combinations (List[List[int]]): Generated number combinations
            analysis (Dict[str, any]): Analysis of the generated combinations
        """
        self.results_text.insert(tk.END, f"Método: {method}\n")
        self.results_text.insert(tk.END, f"Número de Combinações: {num_combinations}\n\n")
        
        self.results_text.insert(tk.END, "Combinações Geradas:\n")
        for idx, combo in enumerate(combinations, 1):
            self.results_text.insert(tk.END, f"{idx}. {combo}\n")
        
        self.results_text.insert(tk.END, "\nAnálise das Combinações:\n")
        self.results_text.insert(tk.END, 
            f"Total de Combinações Únicas: {analysis['unique_combinations']}\n\n"
        )
        
        self.results_text.insert(tk.END, "Frequência dos Números:\n")
        sorted_frequency = sorted(
            analysis['frequency_analysis'].items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        for num, freq in sorted_frequency:
            self.results_text.insert(tk.END, f"Número {num}: {freq} vezes\n")

def main():
    """
    Main entry point for the Mega-Sena Generator application.
    """
    root = tk.Tk()
    app = MegaSenaGeneratorApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()