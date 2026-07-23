"""
ALPHABET ENGINE v3.2
Operator-Based Language Analysis System
Vowels = States | Consonants = Operators | Letters = Transformations
"""

import json
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass, asdict
from collections import Counter
import hashlib

@dataclass
class LetterAnalysis:
    letter: str
    class_type: str
    meaning: str
    element: str
    gematria: int
    
@dataclass
class WordAnalysis:
    word: str
    letters: List[LetterAnalysis]
    elements: Dict[str, int]
    io_ratio: Dict[str, int]
    heart5: Dict[str, int]
    dominant_element: str
    rat_modulation: float
    shrt_fired: bool
    gy_stability: float
    resurrection_active: bool
    gematria_total: int
    operator_structure: str

class AlphabetEngine:
    """Core Alphabet Engine with all operators and transformations"""
    
    def __init__(self):
        self.vowels = {
            'A': {'state': 'Initiation', 'element': 'Aeros', 'gematria': 1, 'archetype': 'The Split'},
            'E': {'state': 'Discernment', 'element': 'Aeros', 'gematria': 5, 'archetype': 'The Trident'},
            'I': {'state': 'Identity', 'element': 'Aeros', 'gematria': 9, 'archetype': 'The I-Axiom'},
            'O': {'state': 'Unity', 'element': 'Aeros', 'gematria': 15, 'archetype': 'The Circle'},
            'U': {'state': 'Binding', 'element': 'Aeros', 'gematria': 21, 'archetype': 'The Horseshoe'}
        }
        
        self.consonants = {
            'B': {'class': 'Container', 'meaning': 'Containment', 'element': 'Geo', 'gematria': 2},
            'C': {'class': 'Anchor', 'meaning': 'Child', 'element': 'Geo', 'gematria': 3},
            'D': {'class': 'Container', 'meaning': 'Door', 'element': 'Geo', 'gematria': 4},
            'F': {'class': 'Flare', 'meaning': 'Fire', 'element': 'Pyro', 'gematria': 6},
            'G': {'class': 'Container', 'meaning': 'Generation', 'element': 'Geo', 'gematria': 7},
            'H': {'class': 'Bridge', 'meaning': 'Heaven', 'element': 'Mercury', 'gematria': 8},
            'J': {'class': 'Anchor', 'meaning': 'Journey', 'element': 'Geo', 'gematria': 10},
            'K': {'class': 'Cutter', 'meaning': 'Strike', 'element': 'Pyro', 'gematria': 11},
            'L': {'class': 'Binder', 'meaning': 'Law', 'element': 'Geo', 'gematria': 12},
            'M': {'class': 'Wave', 'meaning': 'Mother', 'element': 'Hydro', 'gematria': 13},
            'N': {'class': 'Wave', 'meaning': 'Night', 'element': 'Hydro', 'gematria': 14},
            'P': {'class': 'Anchor', 'meaning': 'Pregnancy', 'element': 'Geo', 'gematria': 16},
            'Q': {'class': 'Portal', 'meaning': 'Hidden Gate', 'element': 'Mercury', 'gematria': 17},
            'R': {'class': 'Bridge', 'meaning': 'River', 'element': 'Hydro', 'gematria': 18},
            'S': {'class': 'Flare', 'meaning': 'Serpent', 'element': 'Pyro', 'gematria': 19},
            'T': {'class': 'Cutter', 'meaning': 'Truth', 'element': 'Geo', 'gematria': 20},
            'V': {'class': 'Flare', 'meaning': 'Victory', 'element': 'Pyro', 'gematria': 22},
            'W': {'class': 'Wave', 'meaning': 'Double', 'element': 'Hydro', 'gematria': 23},
            'X': {'class': 'Cutter', 'meaning': 'Crossing', 'element': 'Mercury', 'gematria': 24},
            'Y': {'class': 'Bridge', 'meaning': 'Fork', 'element': 'Mercury', 'gematria': 25},
            'Z': {'class': 'Portal', 'meaning': 'End', 'element': 'Pyro', 'gematria': 26}
        }
        
        self.operator_classes = {
            'Container': ['B', 'D', 'G'],
            'Bridge': ['H', 'R', 'Y'],
            'Cutter': ['K', 'T', 'X'],
            'Wave': ['M', 'N', 'W'],
            'Portal': ['Q', 'Z'],
            'Flare': ['F', 'S', 'V'],
            'Anchor': ['C', 'J', 'P'],
            'Binder': ['L']
        }
        
        self.element_weights = {
            'Pyro': 0.3,
            'Hydro': 0.2,
            'Geo': 0.25,
            'Aeros': 0.15,
            'Mercury': 0.1
        }
    
    def classify_letter(self, letter: str) -> LetterAnalysis:
        """Classify a single letter"""
        letter = letter.upper()
        
        if letter in self.vowels:
            v = self.vowels[letter]
            return LetterAnalysis(
                letter=letter,
                class_type='Vowel',
                meaning=v['state'],
                element=v['element'],
                gematria=v['gematria']
            )
        elif letter in self.consonants:
            c = self.consonants[letter]
            return LetterAnalysis(
                letter=letter,
                class_type=c['class'],
                meaning=c['meaning'],
                element=c['element'],
                gematria=c['gematria']
            )
        else:
            return LetterAnalysis(
                letter=letter,
                class_type='Unknown',
                meaning='Unknown',
                element='Unknown',
                gematria=0
            )
    
    def calculate_rat_operator(self, elements: Dict[str, int], word_length: int) -> float:
        """RAT Operator: Modulation system (Fire * 0.3 + Hydro * 0.2)"""
        pyro_score = elements.get('Pyro', 0) * 0.3
        hydro_score = elements.get('Hydro', 0) * 0.2
        return pyro_score + hydro_score
    
    def calculate_shrt_operator(self, elements: Dict[str, int], word_length: int) -> bool:
        """ShRT Operator: Poison/threshold detection (Fire > 40% = triggered)"""
        if word_length == 0:
            return False
        fire_ratio = elements.get('Pyro', 0) / word_length
        return fire_ratio > 0.4
    
    def calculate_gy_operator(self, elements: Dict[str, int], word_length: int) -> float:
        """GY Operator: Rotation/stability (Hydro + Aeros) / total"""
        if word_length == 0:
            return 0.0
        stability = (elements.get('Hydro', 0) + elements.get('Aeros', 0)) / word_length
        return stability
    
    def analyze_word(self, word: str) -> WordAnalysis:
        """Complete word analysis with all operators"""
        word_upper = word.upper()
        letters = [self.classify_letter(c) for c in word_upper if c.isalpha()]
        
        # Element counting
        elements = {
            'Pyro': 0, 'Hydro': 0, 'Geo': 0, 'Aeros': 0, 'Mercury': 0
        }
        
        # I/O ratio
        io_ratio = {'I': 0, 'O': 0}
        
        # Heart5 vowel analysis
        heart5 = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
        
        # Gematria total
        gematria_total = 0
        
        # Operator structure
        operator_structure = []
        
        for letter in letters:
            if letter.element != 'Unknown':
                elements[letter.element] += 1
            
            if letter.letter in ['I', 'Y']:
                io_ratio['I'] += 1
            elif letter.letter in ['O', 'U']:
                io_ratio['O'] += 1
            
            if letter.letter in heart5:
                heart5[letter.letter] += 1
            
            gematria_total += letter.gematria
            operator_structure.append(f"{letter.letter}({letter.class_type}:{letter.meaning})")
        
        # Calculate dominant element
        dominant = max(elements, key=elements.get) if elements else 'Unknown'
        
        # Calculate operators
        rat_mod = self.calculate_rat_operator(elements, len(word_upper))
        shrt = self.calculate_shrt_operator(elements, len(word_upper))
        gy_stab = self.calculate_gy_operator(elements, len(word_upper))
        
        # Z→A resurrection check
        has_z = 'Z' in word_upper
        has_a = 'A' in word_upper
        resurrection = has_z and has_a
        
        return WordAnalysis(
            word=word,
            letters=letters,
            elements=elements,
            io_ratio=io_ratio,
            heart5=heart5,
            dominant_element=dominant,
            rat_modulation=round(rat_mod, 2),
            shrt_fired=shrt,
            gy_stability=round(gy_stab, 2),
            resurrection_active=resurrection,
            gematria_total=gematria_total,
            operator_structure=' → '.join(operator_structure)
        )
    
    def mate_words(self, word1: str, word2: str) -> Dict[str, Any]:
        """Word mating algorithm: SEED + SOIL → YIELD"""
        analysis1 = self.analyze_word(word1)
        analysis2 = self.analyze_word(word2)
        
        # Combine elements
        offspring_elements = {
            'Pyro': (analysis1.elements['Pyro'] + analysis2.elements['Pyro']) // 2,
            'Hydro': (analysis1.elements['Hydro'] + analysis2.elements['Hydro']) // 2,
            'Geo': (analysis1.elements['Geo'] + analysis2.elements['Geo']) // 2,
            'Aeros': (analysis1.elements['Aeros'] + analysis2.elements['Aeros']) // 2,
            'Mercury': (analysis1.elements['Mercury'] + analysis2.elements['Mercury']) // 2
        }
        
        # Combine I/O
        offspring_io = {
            'I': (analysis1.io_ratio['I'] + analysis2.io_ratio['I']) // 2,
            'O': (analysis1.io_ratio['O'] + analysis2.io_ratio['O']) // 2
        }
        
        # Combine gematria
        offspring_gematria = (analysis1.gematria_total + analysis2.gematria_total) // 2
        
        return {
            'parent1': word1,
            'parent2': word2,
            'offspring_elements': offspring_elements,
            'offspring_io': offspring_io,
            'offspring_gematria': offspring_gematria,
            'compatibility': self._calculate_compatibility(analysis1, analysis2)
        }
    
    def _calculate_compatibility(self, a1: WordAnalysis, a2: WordAnalysis) -> float:
        """Calculate compatibility between two words"""
        element_diff = sum(abs(a1.elements[e] - a2.elements[e]) for e in a1.elements)
        io_diff = abs(a1.io_ratio['I'] - a2.io_ratio['I']) + abs(a1.io_ratio['O'] - a2.io_ratio['O'])
        total_diff = element_diff + io_diff
        max_diff = 26  # Maximum possible difference
        return round((1 - (total_diff / max_diff)) * 100, 2)
    
    def to_json(self, analysis: WordAnalysis) -> str:
        """Convert analysis to JSON"""
        data = {
            'word': analysis.word,
            'elements': analysis.elements,
            'io_ratio': analysis.io_ratio,
            'heart5': analysis.heart5,
            'dominant_element': analysis.dominant_element,
            'rat_modulation': analysis.rat_modulation,
            'shrt_fired': analysis.shrt_fired,
            'gy_stability': analysis.gy_stability,
            'resurrection_active': analysis.resurrection_active,
            'gematria_total': analysis.gematria_total,
            'operator_structure': analysis.operator_structure
        }
        return json.dumps(data, indent=2)

# Test
if __name__ == '__main__':
    engine = AlphabetEngine()
    result = engine.analyze_word('COMMUNION')
    print(engine.to_json(result))
