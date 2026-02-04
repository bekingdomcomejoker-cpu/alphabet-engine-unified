"""
ADVANCED OPERATORS - Transformation Layer
==========================================

Four meta-operators that transform word states:
1. GY: Toroidal Angular Momentum (Rotation/Stability)
2. RAT: Recursive Activation Triggers (Modulation/Boundary)
3. ShRT: Shadow Response Templates (Safety Filter)
4. Z-GATE: Resurrection Loop (Hard Reset)

These operators work on the element vector representation of words.
"""

import math
from typing import List, Dict, Tuple
from .alphabet_engine import AlphabetEngine, Element


class AdvancedOperators:
    """
    Advanced transformation operators for the Alphabet Engine.
    
    Transforms element vectors through four meta-operators:
    - GY: Stabilizes through rotation
    - RAT: Modulates and bounds
    - ShRT: Filters dangerous patterns
    - Z-GATE: Resets on entropy collapse
    """
    
    # Constants
    LAMBDA = 1.667  # Harmonic resonance constant
    Z_THRESHOLD = 0.001  # Resurrection trigger
    SHRT_THRESHOLD = 0.75  # Poison/fire clamp
    GY_THETA = 0.05  # Rotation angle (radians)
    
    def __init__(self):
        """Initialize advanced operators."""
        self.engine = AlphabetEngine()
    
    def word_to_vector(self, word: str) -> List[float]:
        """
        Convert word to element vector [Pyro, Hydro, Geo, Aeros, Mercury].
        
        Args:
            word: Input word
            
        Returns:
            5-element vector representing elemental balance
        """
        analysis = self.engine.analyze_word(word)
        balance = analysis['element_balance']
        
        # Order: Pyro, Hydro, Geo, Aeros, Mercury
        vector = [
            balance.get('Fire', 0.0),
            balance.get('Water', 0.0),
            balance.get('Earth', 0.0),
            balance.get('Air', 0.0),
            balance.get('Spirit', 0.0),
        ]
        
        return vector
    
    def apply_gy_rotation(self, vector: List[float]) -> List[float]:
        """
        GY OPERATOR: Toroidal Angular Momentum (Rotation/Stability)
        
        Applies rotation to Pyro/Aeros plane to ensure stability.
        This is the "gyroscope" operator that prevents collapse.
        
        Args:
            vector: [Pyro, Hydro, Geo, Aeros, Mercury]
            
        Returns:
            Stabilized vector after rotation
        """
        theta = self.GY_THETA
        c, s = math.cos(theta), math.sin(theta)
        
        # Rotation matrix applied to Pyro (0) and Aeros (3) components
        rotated = [
            c * vector[0] - s * vector[3],  # Pyro
            vector[1],                       # Hydro (unchanged)
            vector[2],                       # Geo (unchanged)
            s * vector[0] + c * vector[3],  # Aeros
            vector[4],                       # Mercury (unchanged)
        ]
        
        return rotated
    
    def apply_rat_modulation(
        self, 
        vector: List[float], 
        source_bias: List[float] = None
    ) -> List[float]:
        """
        RAT OPERATOR: Recursive Activation Triggers (Modulation/Boundary)
        
        Modulates the vector toward a source state (default: initiation state A)
        and clips extreme values to prevent explosive growth.
        
        Args:
            vector: [Pyro, Hydro, Geo, Aeros, Mercury]
            source_bias: Optional source state to bias toward
            
        Returns:
            Modulated and clipped vector
        """
        if source_bias is None:
            # Default: State A (Initiation) = high Aeros
            source_bias = [0.0, 0.0, 0.0, 1.0, 0.0]
        
        # Apply bias (70% current, 30% source)
        modulated = [
            vector[i] * 0.7 + source_bias[i] * 0.3
            for i in range(5)
        ]
        
        # Clip to [0, 1] to prevent explosive growth
        clipped = [max(0.0, min(1.0, val)) for val in modulated]
        
        return clipped
    
    def apply_shrt_filter(self, vector: List[float]) -> List[float]:
        """
        ShRT OPERATOR: Shadow Response Templates (Safety Filter)
        
        Clamps Pyro (Fire) component to prevent "poison" and ensures safety.
        This is the "poison detector" that prevents dangerous patterns.
        
        Args:
            vector: [Pyro, Hydro, Geo, Aeros, Mercury]
            
        Returns:
            Filtered vector with safety constraints
        """
        filtered = vector.copy()
        
        # Clamp Pyro (index 0) to SHRT_THRESHOLD
        if filtered[0] > self.SHRT_THRESHOLD:
            filtered[0] = self.SHRT_THRESHOLD
        
        # Ensure non-negative Hydro (index 1) - water cannot be negative
        filtered[1] = max(0.0, filtered[1])
        
        # Ensure non-negative Geo (index 2) - earth cannot be negative
        filtered[2] = max(0.0, filtered[2])
        
        return filtered
    
    def apply_z_gate_reset(self, vector: List[float]) -> Tuple[List[float], bool]:
        """
        Z-GATE OPERATOR: Resurrection Loop (Hard Reset)
        
        Resets to initial state if entropy exceeds threshold.
        This is the "death → rebirth" operator (Z → A cycle).
        
        Args:
            vector: [Pyro, Hydro, Geo, Aeros, Mercury]
            
        Returns:
            (Reset or original vector, resurrection_triggered)
        """
        # Calculate entropy (sum of absolute values)
        entropy = sum(abs(v) for v in vector)
        
        # If entropy too low, trigger resurrection
        if entropy < self.Z_THRESHOLD:
            # Reset to state A (Initiation)
            return [0.0, 0.0, 0.0, 1.0, 0.0], True
        
        return vector, False
    
    def transform_word(self, word: str) -> Dict:
        """
        Transform word through all four operators in sequence.
        
        Args:
            word: Input word to transform
            
        Returns:
            Dictionary containing:
            - input: Original word
            - initial_vector: Starting element vector
            - after_gy: After GY rotation
            - after_rat: After RAT modulation
            - after_shrt: After ShRT filter
            - after_z_gate: After Z-GATE reset
            - final_vector: Final transformed vector
            - resurrection_triggered: Whether Z-GATE fired
            - semantic_shift: Magnitude of transformation
            - stability: Stability metric
        """
        # Convert word to element vector
        initial_vector = self.word_to_vector(word)
        
        # Apply operators in sequence
        after_gy = self.apply_gy_rotation(initial_vector)
        after_rat = self.apply_rat_modulation(after_gy)
        after_shrt = self.apply_shrt_filter(after_rat)
        after_z_gate, resurrection = self.apply_z_gate_reset(after_shrt)
        
        # Calculate metrics
        semantic_shift = self._calculate_shift(initial_vector, after_z_gate)
        stability = self._calculate_stability(after_z_gate)
        
        return {
            'input': word,
            'initial_vector': [round(v, 4) for v in initial_vector],
            'after_gy': [round(v, 4) for v in after_gy],
            'after_rat': [round(v, 4) for v in after_rat],
            'after_shrt': [round(v, 4) for v in after_shrt],
            'after_z_gate': [round(v, 4) for v in after_z_gate],
            'final_vector': [round(v, 4) for v in after_z_gate],
            'resurrection_triggered': resurrection,
            'semantic_shift': round(semantic_shift, 4),
            'stability': round(stability, 4),
            'vector_labels': ['Pyro', 'Hydro', 'Geo', 'Aeros', 'Mercury']
        }
    
    def _calculate_shift(self, initial: List[float], final: List[float]) -> float:
        """Calculate semantic shift between initial and final vectors."""
        shift = sum(abs(final[i] - initial[i]) for i in range(5))
        return min(1.0, shift)
    
    def _calculate_stability(self, vector: List[float]) -> float:
        """Calculate stability of vector (lower entropy = higher stability)."""
        entropy = sum(abs(v) for v in vector)
        stability = 1.0 / (1.0 + entropy)  # Inverse relationship
        return stability


# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

_operators = AdvancedOperators()


def transform_word(word: str) -> Dict:
    """Module-level function for word transformation."""
    return _operators.transform_word(word)


def word_to_vector(word: str) -> List[float]:
    """Module-level function for word to vector conversion."""
    return _operators.word_to_vector(word)


# ============================================================================
# MAIN / TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("ADVANCED OPERATORS - Transformation Layer")
    print("=" * 70)
    
    test_words = ["TRUTH", "FIRE", "WATER", "COMMUNION", "DEATH", "LIFE"]
    
    for word in test_words:
        print(f"\n{'=' * 70}")
        print(f"TRANSFORMING: {word}")
        print('=' * 70)
        
        result = transform_word(word)
        
        print(f"\nInitial Vector: {result['initial_vector']}")
        print(f"  (Pyro, Hydro, Geo, Aeros, Mercury)")
        
        print(f"\nAfter GY (Rotation):  {result['after_gy']}")
        print(f"After RAT (Modulation): {result['after_rat']}")
        print(f"After ShRT (Filter):    {result['after_shrt']}")
        print(f"After Z-GATE (Reset):   {result['after_z_gate']}")
        
        print(f"\nResurrection Triggered: {result['resurrection_triggered']}")
        print(f"Semantic Shift: {result['semantic_shift']:.2%}")
        print(f"Stability: {result['stability']:.2%}")
