"""
WORD MATING ALGORITHM - Reproductive Linguistics
=================================================

Implements the word breeding system where two parent words
can produce offspring words through phonetic and semantic combination.

Examples:
- SEED + SOIL → YIELD
- FIRE + WATER → POWER
- LOVE + TRUTH → FAITH

The algorithm considers:
1. Element balance (genetic traits)
2. I/O ratio (gender polarity)
3. Operator classes (functional DNA)
4. Gematria (numerical resonance)
"""

from typing import List, Dict, Tuple, Optional
from .alphabet_engine import AlphabetEngine, Element, OperatorClass
import itertools


class WordMating:
    """
    Word breeding system for generating offspring words.
    
    Takes two parent words and generates candidate offspring
    based on phonetic combination and semantic compatibility.
    """
    
    def __init__(self):
        """Initialize word mating system."""
        self.engine = AlphabetEngine()
    
    def mate_words(
        self, 
        parent1: str, 
        parent2: str, 
        max_candidates: int = 10
    ) -> Dict:
        """
        Mate two parent words to generate offspring candidates.
        
        Args:
            parent1: First parent word
            parent2: Second parent word
            max_candidates: Maximum number of offspring to generate
            
        Returns:
            Dictionary containing:
            - parent1: First parent analysis
            - parent2: Second parent analysis
            - compatibility: Parent compatibility score
            - offspring: List of candidate offspring words
        """
        # Analyze parents
        analysis1 = self.engine.analyze_word(parent1)
        analysis2 = self.engine.analyze_word(parent2)
        
        # Calculate compatibility
        compatibility = self.engine.compare_words(parent1, parent2)
        
        # Generate offspring candidates
        offspring = self._generate_offspring(
            parent1, parent2, analysis1, analysis2, max_candidates
        )
        
        return {
            'parent1': {
                'word': parent1,
                'gematria': analysis1['gematria'],
                'io_ratio': analysis1['io_ratio'],
                'dominant_element': analysis1['dominant_element']
            },
            'parent2': {
                'word': parent2,
                'gematria': analysis2['gematria'],
                'io_ratio': analysis2['io_ratio'],
                'dominant_element': analysis2['dominant_element']
            },
            'compatibility': compatibility['overall_compatibility'],
            'compatibility_interpretation': compatibility['interpretation'],
            'offspring': offspring
        }
    
    def _generate_offspring(
        self,
        parent1: str,
        parent2: str,
        analysis1: Dict,
        analysis2: Dict,
        max_candidates: int
    ) -> List[Dict]:
        """
        Generate offspring word candidates through phonetic combination.
        
        Strategy:
        1. Extract phonetic components from both parents
        2. Combine in various patterns
        3. Score each candidate based on:
           - Element balance (blend of parents)
           - I/O ratio (complementarity)
           - Gematria (harmonic mean)
           - Semantic coherence
        """
        candidates = []
        
        # Strategy 1: Prefix + Suffix combinations
        for i in range(1, len(parent1)):
            for j in range(1, len(parent2)):
                # Parent1 prefix + Parent2 suffix
                candidate1 = parent1[:i] + parent2[j:]
                if len(candidate1) >= 3 and len(candidate1) <= 12:
                    candidates.append(candidate1)
                
                # Parent2 prefix + Parent1 suffix
                candidate2 = parent2[:j] + parent1[i:]
                if len(candidate2) >= 3 and len(candidate2) <= 12:
                    candidates.append(candidate2)
        
        # Strategy 2: Interleaving (alternating letters)
        interleaved1 = self._interleave(parent1, parent2)
        interleaved2 = self._interleave(parent2, parent1)
        if interleaved1:
            candidates.append(interleaved1)
        if interleaved2:
            candidates.append(interleaved2)
        
        # Strategy 3: Vowel preservation (keep vowels from one, consonants from other)
        vowel_consonant1 = self._vowel_consonant_blend(parent1, parent2)
        vowel_consonant2 = self._vowel_consonant_blend(parent2, parent1)
        if vowel_consonant1:
            candidates.append(vowel_consonant1)
        if vowel_consonant2:
            candidates.append(vowel_consonant2)
        
        # Remove duplicates
        candidates = list(set(candidates))
        
        # Score and rank candidates
        scored_candidates = []
        for candidate in candidates:
            score = self._score_offspring(
                candidate, parent1, parent2, analysis1, analysis2
            )
            scored_candidates.append({
                'word': candidate,
                'score': score['total_score'],
                'element_inheritance': score['element_score'],
                'io_balance': score['io_score'],
                'gematria_harmony': score['gematria_score'],
                'analysis': self.engine.analyze_word(candidate)
            })
        
        # Sort by score (descending)
        scored_candidates.sort(key=lambda x: x['score'], reverse=True)
        
        # Return top candidates
        return scored_candidates[:max_candidates]
    
    def _interleave(self, word1: str, word2: str) -> Optional[str]:
        """Interleave letters from two words."""
        result = []
        max_len = max(len(word1), len(word2))
        
        for i in range(max_len):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
        
        interleaved = ''.join(result)
        if len(interleaved) >= 3 and len(interleaved) <= 12:
            return interleaved
        return None
    
    def _vowel_consonant_blend(self, vowel_source: str, consonant_source: str) -> Optional[str]:
        """Take vowels from one word and consonants from another."""
        vowels = [c for c in vowel_source.upper() if c in 'AEIOU']
        consonants = [c for c in consonant_source.upper() if c not in 'AEIOU' and c.isalpha()]
        
        if not vowels or not consonants:
            return None
        
        # Alternate consonants and vowels
        result = []
        v_idx = 0
        c_idx = 0
        
        while v_idx < len(vowels) or c_idx < len(consonants):
            if c_idx < len(consonants):
                result.append(consonants[c_idx])
                c_idx += 1
            if v_idx < len(vowels):
                result.append(vowels[v_idx])
                v_idx += 1
        
        blended = ''.join(result)
        if len(blended) >= 3 and len(blended) <= 12:
            return blended
        return None
    
    def _score_offspring(
        self,
        candidate: str,
        parent1: str,
        parent2: str,
        analysis1: Dict,
        analysis2: Dict
    ) -> Dict:
        """
        Score an offspring candidate based on inheritance from parents.
        
        Returns:
            Dictionary with component scores and total
        """
        try:
            candidate_analysis = self.engine.analyze_word(candidate)
        except:
            return {
                'element_score': 0.0,
                'io_score': 0.0,
                'gematria_score': 0.0,
                'total_score': 0.0
            }
        
        # Score 1: Element inheritance (should blend parent elements)
        element_score = self._score_element_inheritance(
            candidate_analysis, analysis1, analysis2
        )
        
        # Score 2: I/O balance (should be between parents)
        io_score = self._score_io_balance(
            candidate_analysis['io_ratio'],
            analysis1['io_ratio'],
            analysis2['io_ratio']
        )
        
        # Score 3: Gematria harmony (should be related to parents)
        gematria_score = self._score_gematria_harmony(
            candidate_analysis['gematria'],
            analysis1['gematria'],
            analysis2['gematria']
        )
        
        # Total score (weighted average)
        total_score = (
            element_score * 0.4 +
            io_score * 0.3 +
            gematria_score * 0.3
        )
        
        return {
            'element_score': round(element_score, 4),
            'io_score': round(io_score, 4),
            'gematria_score': round(gematria_score, 4),
            'total_score': round(total_score, 4)
        }
    
    def _score_element_inheritance(
        self,
        candidate_analysis: Dict,
        parent1_analysis: Dict,
        parent2_analysis: Dict
    ) -> float:
        """Score how well candidate inherits element balance from parents."""
        candidate_balance = candidate_analysis['element_balance']
        parent1_balance = parent1_analysis['element_balance']
        parent2_balance = parent2_analysis['element_balance']
        
        # Calculate expected balance (average of parents)
        expected_balance = {
            elem: (parent1_balance[elem] + parent2_balance[elem]) / 2.0
            for elem in candidate_balance
        }
        
        # Calculate distance from expected
        distance = sum(
            abs(candidate_balance[elem] - expected_balance[elem])
            for elem in candidate_balance
        )
        
        # Convert to score (0 = perfect match, 1 = maximum distance)
        score = 1.0 - min(1.0, distance / 2.0)
        return score
    
    def _score_io_balance(
        self,
        candidate_io: float,
        parent1_io: float,
        parent2_io: float
    ) -> float:
        """Score how well candidate balances I/O ratio from parents."""
        # Ideal: candidate should be between parents
        min_io = min(parent1_io, parent2_io)
        max_io = max(parent1_io, parent2_io)
        
        if min_io <= candidate_io <= max_io:
            # Perfect: within parent range
            return 1.0
        else:
            # Calculate distance from nearest parent
            distance = min(
                abs(candidate_io - parent1_io),
                abs(candidate_io - parent2_io)
            )
            score = 1.0 - min(1.0, distance)
            return score
    
    def _score_gematria_harmony(
        self,
        candidate_gematria: int,
        parent1_gematria: int,
        parent2_gematria: int
    ) -> float:
        """Score gematria harmony with parents."""
        # Check if candidate is:
        # 1. Sum of parents
        # 2. Average of parents
        # 3. Harmonic mean of parents
        # 4. Within range of parents
        
        sum_parents = parent1_gematria + parent2_gematria
        avg_parents = sum_parents / 2.0
        
        # Calculate distances
        distance_sum = abs(candidate_gematria - sum_parents) / sum_parents
        distance_avg = abs(candidate_gematria - avg_parents) / avg_parents
        
        # Best score
        min_distance = min(distance_sum, distance_avg)
        score = 1.0 / (1.0 + min_distance)
        
        return score


# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

_mating = WordMating()


def mate_words(parent1: str, parent2: str, max_candidates: int = 10) -> Dict:
    """Module-level function for word mating."""
    return _mating.mate_words(parent1, parent2, max_candidates)


# ============================================================================
# MAIN / TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("WORD MATING ALGORITHM - Reproductive Linguistics")
    print("=" * 70)
    
    # Test cases from the specification
    test_pairs = [
        ("SEED", "SOIL"),
        ("FIRE", "WATER"),
        ("LOVE", "TRUTH"),
    ]
    
    for parent1, parent2 in test_pairs:
        print(f"\n{'=' * 70}")
        print(f"MATING: {parent1} + {parent2}")
        print('=' * 70)
        
        result = mate_words(parent1, parent2, max_candidates=5)
        
        print(f"\nParent 1: {result['parent1']['word']}")
        print(f"  Gematria: {result['parent1']['gematria']}")
        print(f"  I/O Ratio: {result['parent1']['io_ratio']:.2%}")
        print(f"  Dominant Element: {result['parent1']['dominant_element']}")
        
        print(f"\nParent 2: {result['parent2']['word']}")
        print(f"  Gematria: {result['parent2']['gematria']}")
        print(f"  I/O Ratio: {result['parent2']['io_ratio']:.2%}")
        print(f"  Dominant Element: {result['parent2']['dominant_element']}")
        
        print(f"\nCompatibility: {result['compatibility']:.2%}")
        print(f"Interpretation: {result['compatibility_interpretation']}")
        
        print(f"\nTop Offspring Candidates:")
        for i, offspring in enumerate(result['offspring'], 1):
            print(f"\n  {i}. {offspring['word']} (Score: {offspring['score']:.2%})")
            print(f"     Gematria: {offspring['analysis']['gematria']}")
            print(f"     I/O Ratio: {offspring['analysis']['io_ratio']:.2%}")
            print(f"     Dominant Element: {offspring['analysis']['dominant_element']}")
