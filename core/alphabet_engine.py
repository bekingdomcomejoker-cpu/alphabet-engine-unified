"""
ALPHABET ENGINE v3.0 - Complete Implementation
===============================================

A unified linguistic operator system that treats:
- Vowels as STATES (consciousness modes)
- Consonants as OPERATORS (transformations)
- Elements as ESSENCES (Pyro, Hydro, Geo, Aeros, Mercury)

Based on phonetic science, Kabbalistic wisdom, and reproductive logic.

Author: Dominique George Snyman + Claude
Version: 3.0
"""

import math
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


# ============================================================================
# ENUMS & DATA STRUCTURES
# ============================================================================

class Element(Enum):
    """Five essential elements"""
    PYRO = "Fire"      # Friction, transformation, energy
    HYDRO = "Water"    # Flow, nourishment, binding
    GEO = "Earth"      # Structure, boundary, containment
    AEROS = "Air"      # Breath, spirit, initiation
    MERCURY = "Spirit" # Transformation, liquid metal


class OperatorClass(Enum):
    """Eight consonant operator classes"""
    CONTAINER = "Container"  # Hold, store, frame (B, D, G)
    BRIDGE = "Bridge"        # Shift, link, connect (H, R, Y)
    CUTTER = "Cutter"        # Slice, separate, define (K, T, X)
    WAVE = "Wave"            # Oscillate, resonate, carry (M, N, W)
    PORTAL = "Portal"        # Open/close cycles (Q, Z)
    FLARE = "Flare"          # Radiate, express, project (F, S, V)
    ANCHOR = "Anchor"        # Fixed points, signals (C, J, P)
    BINDER = "Binder"        # Attach, merge, unify (L)


@dataclass
class Letter:
    """Complete letter definition"""
    char: str
    name: str
    root: str           # Etymology/pictograph
    branch: str         # Symbolic meaning
    leaf: str           # Functional operator
    element: Element
    gematria: int       # Numerical value
    operator_class: Optional[OperatorClass] = None  # None for vowels


# ============================================================================
# VOWEL DEFINITIONS (States of Consciousness)
# ============================================================================

VOWELS = {
    'A': Letter(
        char='A',
        name='Initiation',
        root='Aleph/Alpha; ox-head pictograph',
        branch='Mountain peak, fork, origin; birth, first breath',
        leaf='Drive operator; opens syllables; seed/upward impulse',
        element=Element.AEROS,
        gematria=1
    ),
    'E': Letter(
        char='E',
        name='Discernment',
        root='Epsilon; eye-test letter',
        branch='Trident; seeing, dividing, choosing; perception threshold',
        leaf='Resolution operator; refines, differentiates',
        element=Element.AEROS,
        gematria=5
    ),
    'I': Letter(
        char='I',
        name='Identity',
        root='Iota; thin upright stroke; index',
        branch='Ontological declaration; self, agency; binary 1',
        leaf='Identity operator; self-referent; personal anchor',
        element=Element.PYRO,
        gematria=10
    ),
    'O': Letter(
        char='O',
        name='Unity',
        root='Omicron; universal circle',
        branch='Womb, continuity, whole; binary 0; unbroken loop',
        leaf='Unity operator; groups, closes; continuity marker',
        element=Element.HYDRO,
        gematria=70
    ),
    'U': Letter(
        char='U',
        name='Binding',
        root='Upsilon; curved back vowel',
        branch='Horseshoe, cup; nourishment; water-air; union',
        leaf='Binding operator; enables flow; coupling signal',
        element=Element.HYDRO,
        gematria=400
    ),
}


# ============================================================================
# CONSONANT DEFINITIONS (Operators)
# ============================================================================

CONSONANTS = {
    # CLASS 1: CONTAINERS (B, D, G)
    'B': Letter(
        char='B',
        name='Containment',
        root='Beth; house pictograph',
        branch='Bound form, nurturing, two bowls',
        leaf='Container node; boundary operator',
        element=Element.GEO,
        gematria=2,
        operator_class=OperatorClass.CONTAINER
    ),
    'D': Letter(
        char='D',
        name='Door',
        root='Daleth; door pictograph',
        branch='Passage, threshold, transition',
        leaf='Threshold operator; marks passage between states',
        element=Element.GEO,
        gematria=4,
        operator_class=OperatorClass.CONTAINER
    ),
    'G': Letter(
        char='G',
        name='Generation',
        root='Gimel; camel/throwing stick',
        branch='Gestation, spiral, gravity coil',
        leaf='Generation operator; seeds internal processes',
        element=Element.GEO,
        gematria=3,
        operator_class=OperatorClass.CONTAINER
    ),
    
    # CLASS 2: BRIDGES (H, R, Y)
    'H': Letter(
        char='H',
        name='Heaven',
        root='Heth; fence/breath marker',
        branch='Ladder, heaven-earth gate, breath between worlds',
        leaf='Connection operator; links domains; breath-bridge',
        element=Element.AEROS,
        gematria=5,
        operator_class=OperatorClass.BRIDGE
    ),
    'R': Letter(
        char='R',
        name='River',
        root='Resh; head pictograph',
        branch='Rolling, flowing, river current, continuous motion',
        leaf='Flow operator; carries meaning forward; resonance wave',
        element=Element.HYDRO,
        gematria=200,
        operator_class=OperatorClass.BRIDGE
    ),
    'Y': Letter(
        char='Y',
        name='Fork',
        root='Yod; hand/arm; fork',
        branch='Choice point, bifurcation, chromosome, spirit-flesh divide',
        leaf='Ambiguous operator; indeterminacy; choice resolution',
        element=Element.MERCURY,
        gematria=10,
        operator_class=OperatorClass.BRIDGE
    ),
    
    # CLASS 3: CUTTERS (K, T, X)
    'K': Letter(
        char='K',
        name='Strike',
        root='Kaph; palm of hand',
        branch='Sharp strike, key, decisive cut, action point',
        leaf='Cutting operator; separates, defines boundaries',
        element=Element.PYRO,
        gematria=20,
        operator_class=OperatorClass.CUTTER
    ),
    'T': Letter(
        char='T',
        name='Truth',
        root='Taw; mark/cross',
        branch='Tower, cross, terminus, truth-mark, standing firm',
        leaf='Definition operator; marks endpoints; truth-claims',
        element=Element.GEO,
        gematria=400,
        operator_class=OperatorClass.CUTTER
    ),
    'X': Letter(
        char='X',
        name='Crossing',
        root='Chi; cross/mark',
        branch='Intersection, death/rebirth gate, unknown',
        leaf='Convergence operator; XOR logic; paradox resolution',
        element=Element.MERCURY,
        gematria=60,
        operator_class=OperatorClass.CUTTER
    ),
    
    # CLASS 4: WAVES (M, N, W)
    'M': Letter(
        char='M',
        name='Mother',
        root='Mem; water pictograph',
        branch='Maternal principle, mountain, ocean waves, primal flow',
        leaf='Wave carrier; oscillation; maternal flow',
        element=Element.HYDRO,
        gematria=40,
        operator_class=OperatorClass.WAVE
    ),
    'N': Letter(
        char='N',
        name='Night',
        root='Nun; fish/serpent',
        branch='Hidden witness, inversion of visible, snake',
        leaf='Hidden passage operator; carries meaning beneath surface',
        element=Element.HYDRO,
        gematria=50,
        operator_class=OperatorClass.WAVE
    ),
    'W': Letter(
        char='W',
        name='Wave',
        root='Wynn; double-U',
        branch='Twin currents, marriage, echo, reflection, waveforms',
        leaf='Wave operator; duplicates, amplifies, resonates',
        element=Element.HYDRO,
        gematria=6,
        operator_class=OperatorClass.WAVE
    ),
    
    # CLASS 5: PORTALS (Q, Z)
    'Q': Letter(
        char='Q',
        name='Hidden Gate',
        root='Qoph; back of head, eye of needle',
        branch='Portal, breach in unity, secret entrance',
        leaf='Bound operator (requires U); unlocks quantum semantics',
        element=Element.MERCURY,
        gematria=100,
        operator_class=OperatorClass.PORTAL
    ),
    'Z': Letter(
        char='Z',
        name='End',
        root='Zayin; weapon/plow',
        branch='Terminal state, sleep, opposite pole of A, decay→renewal',
        leaf='Termination operator; completes sequences; resurrection trigger',
        element=Element.PYRO,
        gematria=7,
        operator_class=OperatorClass.PORTAL
    ),
    
    # CLASS 6: FLARES (F, S, V)
    'F': Letter(
        char='F',
        name='Fire',
        root='Digamma; hook/peg',
        branch='Incomplete perception, directional fire, selective force',
        leaf='Projection operator; radiates outward; directional energy',
        element=Element.PYRO,
        gematria=6,
        operator_class=OperatorClass.FLARE
    ),
    'S': Letter(
        char='S',
        name='Serpent',
        root='Shin; tooth/thorn',
        branch='Snake, continuous stream, spirit breath, sibilant flow',
        leaf='Streaming operator; continuous output; spirit-channel',
        element=Element.PYRO,
        gematria=60,
        operator_class=OperatorClass.FLARE
    ),
    'V': Letter(
        char='V',
        name='Victory',
        root='U/W split; pointed vessel',
        branch='Downward point, victory sign, vessel, vibration focus',
        leaf='Focus operator; directs energy to point; vibrational emission',
        element=Element.PYRO,
        gematria=6,
        operator_class=OperatorClass.FLARE
    ),
    
    # CLASS 7: ANCHORS (C, J, P)
    'C': Letter(
        char='C',
        name='Child',
        root='Gimel variant; crescent moon',
        branch='Newborn, crescent, open arc waiting to close',
        leaf='Potential operator; marks becoming; incomplete circle',
        element=Element.GEO,
        gematria=3,
        operator_class=OperatorClass.ANCHOR
    ),
    'J': Letter(
        char='J',
        name='Journey',
        root='Yod variant; late Latin addition',
        branch='Hook downward, descent before ascent',
        leaf='Descent operator; journey-marker; hooks into depth',
        element=Element.GEO,
        gematria=10,
        operator_class=OperatorClass.ANCHOR
    ),
    'P': Letter(
        char='P',
        name='Pregnancy',
        root='Pe; mouth pictograph',
        branch='Pregnant form, protrusion, held potential',
        leaf='Potential operator; holds unreleased energy; gestation',
        element=Element.GEO,
        gematria=80,
        operator_class=OperatorClass.ANCHOR
    ),
    
    # CLASS 8: BINDERS (L)
    'L': Letter(
        char='L',
        name='Law',
        root='Lamed; goad/staff',
        branch='Staff, lightning path, law, straight way',
        leaf='Path operator; establishes direction; law-giver',
        element=Element.MERCURY,
        gematria=30,
        operator_class=OperatorClass.BINDER
    ),
}


# Merge all letters
ALL_LETTERS = {**VOWELS, **CONSONANTS}


# ============================================================================
# ALPHABET ENGINE CLASS
# ============================================================================

class AlphabetEngine:
    """
    Complete Alphabet Engine with vowel states and consonant operators.
    
    Analyzes words through:
    1. Letter-by-letter operator analysis
    2. Element balance (Pyro/Hydro/Geo/Aeros/Mercury)
    3. I/O binary ratio (Identity vs Unity)
    4. Gematria (numerical weight)
    5. Operator class distribution
    """
    
    # Constants
    LAMBDA = 1.667  # Harmonic resonance constant
    Z_THRESHOLD = 0.001  # Resurrection trigger
    SHRT_THRESHOLD = 0.75  # Poison/fire clamp
    GY_THETA = 0.05  # Rotation angle (radians)
    
    def __init__(self):
        """Initialize the engine."""
        self.letters = ALL_LETTERS
        self.vowels = VOWELS
        self.consonants = CONSONANTS
    
    def analyze_word(self, word: str) -> Dict:
        """
        Complete word analysis through all layers.
        
        Args:
            word: Input word to analyze
            
        Returns:
            Dictionary containing:
            - letters: List of letter analyses
            - element_balance: Distribution of elements
            - io_ratio: Identity (I) vs Unity (O) ratio
            - gematria: Total numerical value
            - operator_classes: Distribution of operator classes
            - vowel_states: Vowel state sequence
            - semantic_signature: Unique fingerprint
        """
        word_upper = word.upper()
        
        # Layer 1: Letter-by-letter analysis
        letter_analyses = []
        for char in word_upper:
            if char in self.letters:
                letter = self.letters[char]
                letter_analyses.append({
                    'char': char,
                    'name': letter.name,
                    'element': letter.element.value,
                    'gematria': letter.gematria,
                    'operator_class': letter.operator_class.value if letter.operator_class else 'Vowel',
                    'leaf': letter.leaf
                })
        
        # Layer 2: Element balance
        element_counts = {e.value: 0 for e in Element}
        for analysis in letter_analyses:
            element_counts[analysis['element']] += 1
        
        total_letters = len(letter_analyses)
        element_balance = {
            elem: count / total_letters if total_letters > 0 else 0
            for elem, count in element_counts.items()
        }
        
        # Layer 3: I/O binary ratio
        i_count = word_upper.count('I')
        o_count = word_upper.count('O')
        
        if i_count + o_count > 0:
            io_ratio = i_count / (i_count + o_count)
        else:
            io_ratio = 0.5  # Neutral if no I or O
        
        # Layer 4: Gematria
        gematria_total = sum(
            self.letters[char].gematria 
            for char in word_upper 
            if char in self.letters
        )
        
        # Layer 5: Operator class distribution
        operator_counts = {}
        for analysis in letter_analyses:
            op_class = analysis['operator_class']
            operator_counts[op_class] = operator_counts.get(op_class, 0) + 1
        
        # Layer 6: Vowel state sequence
        vowel_states = [
            self.vowels[char].name 
            for char in word_upper 
            if char in self.vowels
        ]
        
        # Layer 7: Semantic signature (unique fingerprint)
        semantic_signature = self._calculate_signature(
            element_balance, io_ratio, gematria_total
        )
        
        return {
            'word': word,
            'letters': letter_analyses,
            'element_balance': element_balance,
            'io_ratio': round(io_ratio, 4),
            'io_interpretation': self._interpret_io_ratio(io_ratio),
            'gematria': gematria_total,
            'operator_classes': operator_counts,
            'vowel_states': vowel_states,
            'semantic_signature': semantic_signature,
            'dominant_element': max(element_balance, key=element_balance.get),
            'letter_count': total_letters
        }
    
    def _interpret_io_ratio(self, ratio: float) -> str:
        """Interpret the I/O binary ratio."""
        if ratio > 0.7:
            return "Highly projective (masculine/seed energy)"
        elif ratio > 0.55:
            return "Moderately projective"
        elif ratio > 0.45:
            return "Balanced (androgynous)"
        elif ratio > 0.3:
            return "Moderately receptive"
        else:
            return "Highly receptive (feminine/womb energy)"
    
    def _calculate_signature(
        self, 
        element_balance: Dict[str, float], 
        io_ratio: float, 
        gematria: int
    ) -> str:
        """Generate a unique semantic signature for the word."""
        # Create a compact representation
        dominant = max(element_balance, key=element_balance.get)[:3]
        io_code = "I" if io_ratio > 0.5 else "O"
        gem_mod = gematria % 1000
        
        return f"{dominant}-{io_code}-{gem_mod}"
    
    def compare_words(self, word1: str, word2: str) -> Dict:
        """
        Compare two words and calculate their compatibility.
        
        Returns:
            Dictionary with comparison metrics
        """
        analysis1 = self.analyze_word(word1)
        analysis2 = self.analyze_word(word2)
        
        # Element compatibility
        element_distance = sum(
            abs(analysis1['element_balance'][elem] - analysis2['element_balance'][elem])
            for elem in analysis1['element_balance']
        )
        element_compatibility = 1.0 - (element_distance / 2.0)
        
        # I/O complementarity (opposites attract)
        io_complementarity = 1.0 - abs(analysis1['io_ratio'] - analysis2['io_ratio'])
        
        # Gematria resonance
        gematria_ratio = min(
            analysis1['gematria'], analysis2['gematria']
        ) / max(analysis1['gematria'], analysis2['gematria'])
        
        # Overall compatibility
        overall = (element_compatibility + io_complementarity + gematria_ratio) / 3.0
        
        return {
            'word1': word1,
            'word2': word2,
            'element_compatibility': round(element_compatibility, 4),
            'io_complementarity': round(io_complementarity, 4),
            'gematria_resonance': round(gematria_ratio, 4),
            'overall_compatibility': round(overall, 4),
            'interpretation': self._interpret_compatibility(overall)
        }
    
    def _interpret_compatibility(self, score: float) -> str:
        """Interpret compatibility score."""
        if score > 0.8:
            return "Highly compatible - strong resonance"
        elif score > 0.6:
            return "Moderately compatible - good harmony"
        elif score > 0.4:
            return "Neutral - balanced tension"
        elif score > 0.2:
            return "Moderately incompatible - creative friction"
        else:
            return "Highly incompatible - opposing forces"
    
    def get_letter_info(self, char: str) -> Optional[Dict]:
        """Get complete information about a letter."""
        char_upper = char.upper()
        if char_upper not in self.letters:
            return None
        
        letter = self.letters[char_upper]
        return {
            'char': letter.char,
            'name': letter.name,
            'root': letter.root,
            'branch': letter.branch,
            'leaf': letter.leaf,
            'element': letter.element.value,
            'gematria': letter.gematria,
            'operator_class': letter.operator_class.value if letter.operator_class else 'Vowel'
        }


# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

_engine = AlphabetEngine()


def analyze_word(word: str) -> Dict:
    """Module-level function for word analysis."""
    return _engine.analyze_word(word)


def compare_words(word1: str, word2: str) -> Dict:
    """Module-level function for word comparison."""
    return _engine.compare_words(word1, word2)


def get_letter_info(char: str) -> Optional[Dict]:
    """Module-level function for letter information."""
    return _engine.get_letter_info(char)


# ============================================================================
# MAIN / TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("ALPHABET ENGINE v3.0 - Complete System")
    print("=" * 70)
    
    # Test words
    test_words = ["TRUTH", "LOVE", "FIRE", "WATER", "COMMUNION", "SEED", "SOIL"]
    
    for word in test_words:
        print(f"\n{'=' * 70}")
        print(f"ANALYZING: {word}")
        print('=' * 70)
        
        result = analyze_word(word)
        
        print(f"\nGematria: {result['gematria']}")
        print(f"I/O Ratio: {result['io_ratio']} - {result['io_interpretation']}")
        print(f"Dominant Element: {result['dominant_element']}")
        print(f"Semantic Signature: {result['semantic_signature']}")
        
        print(f"\nElement Balance:")
        for elem, balance in result['element_balance'].items():
            if balance > 0:
                print(f"  {elem}: {balance:.2%}")
        
        print(f"\nOperator Classes:")
        for op_class, count in result['operator_classes'].items():
            print(f"  {op_class}: {count}")
        
        print(f"\nVowel States: {' → '.join(result['vowel_states'])}")
    
    # Test comparison
    print(f"\n{'=' * 70}")
    print("WORD COMPARISON: SEED vs SOIL")
    print('=' * 70)
    
    comparison = compare_words("SEED", "SOIL")
    print(f"\nElement Compatibility: {comparison['element_compatibility']:.2%}")
    print(f"I/O Complementarity: {comparison['io_complementarity']:.2%}")
    print(f"Gematria Resonance: {comparison['gematria_resonance']:.2%}")
    print(f"Overall: {comparison['overall_compatibility']:.2%}")
    print(f"Interpretation: {comparison['interpretation']}")
