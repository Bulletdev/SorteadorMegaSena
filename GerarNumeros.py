from typing import List, Dict, Literal
import random
from collections import Counter

class SorteadorMegaSena:
    """
    A class for generating and analyzing Mega-Sena lottery number combinations.
    
    This class provides methods to generate number combinations based on 
    historical draw data, with different selection strategies.
    """
    
    MIN_NUMBER = 1
    MAX_NUMBER = 60
    COMBINATION_SIZE = 6

    def __init__(self, historical_results: List[List[int]] = None):
        """
        Initialize the number generator with historical draw results.
        
        Args:
            historical_results (List[List[int]], optional): Past lottery draw numbers. 
            Defaults to end-of-year draws from 2009 to 2023.
        """
        if historical_results is None:
            historical_results = [
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
        
        self._validate_historical_results(historical_results)
        
        all_numbers_flat = [num for results in historical_results for num in results]
        
        number_counts = Counter(all_numbers_flat)
        
        self.most_frequent_numbers = [
            num for num, count in number_counts.most_common(self.COMBINATION_SIZE)
        ]
        
        self.least_frequent_numbers = [
            num for num, count in number_counts.most_common()[:-7:-1]
        ]
        
        self.all_numbers = list(range(self.MIN_NUMBER, self.MAX_NUMBER + 1))

    def _validate_historical_results(self, results: List[List[int]]) -> None:
        """
        Validate the historical results to ensure they meet the expected criteria.
        
        Args:
            results (List[List[int]]): Historical draw numbers to validate
        
        Raises:
            ValueError: If the historical results are invalid
        """
        for draw in results:
            if len(draw) != self.COMBINATION_SIZE:
                raise ValueError(f"Each draw must have exactly {self.COMBINATION_SIZE} numbers")
            
            if any(num < self.MIN_NUMBER or num > self.MAX_NUMBER for num in draw):
                raise ValueError(f"Numbers must be between {self.MIN_NUMBER} and {self.MAX_NUMBER}")
            
            if len(set(draw)) != len(draw):
                raise ValueError("No duplicate numbers allowed in a single draw")

    def generate_combinations(
        self, 
        method: Literal['most_frequent', 'least_frequent', 'mixed', 'random'] = 'mixed', 
        num_combinations: int = 5
    ) -> List[List[int]]:
        """
        Generate lottery number combinations using specified strategy.
        
        Args:
            method (str): Strategy for number selection
            num_combinations (int): Number of combinations to generate
        
        Returns:
            List of number combinations
        
        Raises:
            ValueError: If an invalid method is provided
        """
        if num_combinations < 1:
            raise ValueError("Number of combinations must be at least 1")
        
        method_map = {
            'most_frequent': self._generate_most_frequent_combination,
            'least_frequent': self._generate_least_frequent_combination,
            'mixed': self._generate_mixed_combination,
            'random': self._generate_random_combination
        }
        
        if method not in method_map:
            raise ValueError(f"Invalid method. Choose from {list(method_map.keys())}")
        
        return [
            sorted(method_map[method]())
            for _ in range(num_combinations)
        ]

    def _generate_most_frequent_combination(self) -> List[int]:
        """Generate a combination using the most frequent numbers"""
        return random.sample(self.most_frequent_numbers, self.COMBINATION_SIZE)

    def _generate_least_frequent_combination(self) -> List[int]:
        """Generate a combination using the least frequent numbers"""
        return random.sample(self.least_frequent_numbers, self.COMBINATION_SIZE)

    def _generate_mixed_combination(self) -> List[int]:
        """Generate a mixed combination of most and least frequent numbers"""
        combination = (
            random.sample(self.most_frequent_numbers, self.COMBINATION_SIZE // 2) + 
            random.sample(self.least_frequent_numbers, self.COMBINATION_SIZE // 2)
        )
        random.shuffle(combination)
        return combination

    def _generate_random_combination(self) -> List[int]:
        """Generate a completely random combination"""
        return random.sample(self.all_numbers, self.COMBINATION_SIZE)

    def analyze_combinations(self, combinations: List[List[int]]) -> Dict[str, any]:
        """
        Provide basic analysis of generated combinations.
        
        Args:
            combinations (List[List[int]]): List of number combinations to analyze
        
        Returns:
            Dictionary with analysis details
        """
        if not combinations:
            return {
                'total_combinations': 0,
                'unique_combinations': 0,
                'frequency_analysis': {}
            }
        
        analysis = {
            'total_combinations': len(combinations),
            'unique_combinations': len(set(tuple(combo) for combo in combinations)),
            'frequency_analysis': {}
        }
        
        all_numbers_generated = [num for combo in combinations for num in combo]
        
        for num in range(self.MIN_NUMBER, self.MAX_NUMBER + 1):
            count = all_numbers_generated.count(num)
            if count > 0:
                analysis['frequency_analysis'][num] = count
        
        return analysis