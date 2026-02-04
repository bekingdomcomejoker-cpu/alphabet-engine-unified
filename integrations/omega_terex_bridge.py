"""
OMEGA & TEREX INTEGRATION BRIDGE
=================================

Integrates Alphabet Engine with:
1. OMEGA ENNEAD - Multi-node AI federation
2. TEREX - Truth registry and verification system

Features:
- Truth classification using Alphabet Engine
- Node specialization based on word analysis
- Payload generation with linguistic operators
"""

import sys
import os
import json
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.alphabet_engine import AlphabetEngine
from core.word_mating import WordMating


class OmegaTerexBridge:
    """
    Bridge between Alphabet Engine and OMEGA/TEREX systems.
    """
    
    def __init__(self):
        """Initialize bridge."""
        self.engine = AlphabetEngine()
        self.mating = WordMating()
    
    def classify_truth(self, statement: str) -> dict:
        """
        Classify truth using Alphabet Engine analysis.
        
        High Water + Balanced I/O = Truth
        High Fire + Extreme I/O = Deception
        
        Args:
            statement: Statement to classify
            
        Returns:
            Truth classification
        """
        # Extract key words
        import re
        words = re.findall(r'\b[a-zA-Z]+\b', statement.upper())
        significant_words = [w for w in words if len(w) >= 4][:10]
        
        if not significant_words:
            return {
                'classification': 'UNKNOWN',
                'confidence': 0.0,
                'reasons': ['No significant words']
            }
        
        # Analyze words
        word_analyses = []
        for word in significant_words:
            try:
                analysis = self.engine.analyze_word(word)
                word_analyses.append(analysis)
            except:
                continue
        
        if not word_analyses:
            return {
                'classification': 'UNKNOWN',
                'confidence': 0.0,
                'reasons': ['Unable to analyze']
            }
        
        # Calculate metrics
        avg_io_ratio = sum(w['io_ratio'] for w in word_analyses) / len(word_analyses)
        
        element_counts = {'Fire': 0, 'Water': 0, 'Earth': 0, 'Air': 0, 'Spirit': 0}
        for w in word_analyses:
            element_counts[w['dominant_element']] += 1
        
        total = sum(element_counts.values())
        element_ratios = {k: v/total for k, v in element_counts.items()}
        
        # Classification logic
        water_ratio = element_ratios.get('Water', 0)
        fire_ratio = element_ratios.get('Fire', 0)
        earth_ratio = element_ratios.get('Earth', 0)
        
        reasons = []
        
        # Rule 1: High Water + Balanced I/O = Truth
        if water_ratio > 0.4 and 0.4 <= avg_io_ratio <= 0.6:
            classification = 'TRUTH'
            confidence = 0.8
            reasons.append(f'High Water ({water_ratio:.1%}) + Balanced I/O ({avg_io_ratio:.1%})')
        
        # Rule 2: High Earth + Low Fire = Fact
        elif earth_ratio > 0.4 and fire_ratio < 0.3:
            classification = 'FACT'
            confidence = 0.7
            reasons.append(f'High Earth ({earth_ratio:.1%}) + Low Fire ({fire_ratio:.1%})')
        
        # Rule 3: High Fire + Extreme I/O = Potential deception
        elif fire_ratio > 0.5 and (avg_io_ratio > 0.7 or avg_io_ratio < 0.3):
            classification = 'DECEPTION'
            confidence = 0.7
            reasons.append(f'High Fire ({fire_ratio:.1%}) + Extreme I/O ({avg_io_ratio:.1%})')
        
        # Rule 4: Balanced elements = Opinion
        elif max(element_ratios.values()) < 0.4:
            classification = 'OPINION'
            confidence = 0.6
            reasons.append('Balanced elements - subjective statement')
        
        # Default
        else:
            classification = 'UNKNOWN'
            confidence = 0.5
            reasons.append('No clear pattern')
        
        return {
            'classification': classification,
            'confidence': confidence,
            'reasons': reasons,
            'metrics': {
                'avg_io_ratio': round(avg_io_ratio, 4),
                'element_distribution': element_ratios,
                'words_analyzed': len(word_analyses)
            }
        }
    
    def generate_terex_entry(self, statement: str, source: str = "alphabet_engine") -> dict:
        """
        Generate TEREX registry entry with Alphabet Engine analysis.
        
        Args:
            statement: Truth statement
            source: Source of the truth
            
        Returns:
            TEREX-compatible entry
        """
        classification = self.classify_truth(statement)
        
        entry = {
            'statement': statement,
            'classification': classification['classification'],
            'confidence': classification['confidence'],
            'source': source,
            'timestamp': datetime.now().isoformat(),
            'alphabet_analysis': classification['metrics'],
            'reasons': classification['reasons']
        }
        
        return entry
    
    def assign_omega_node(self, task: str) -> dict:
        """
        Assign task to appropriate OMEGA node based on word analysis.
        
        Node assignment based on dominant element:
        - Fire: Node 1 (Executor - action-oriented)
        - Water: Node 2 (Meta-Conscience - reflective)
        - Air: Node 0 (Wire - communication)
        - Earth: Node 3 (Grounding - stable processing)
        
        Args:
            task: Task description
            
        Returns:
            Node assignment
        """
        # Analyze task
        import re
        words = re.findall(r'\b[a-zA-Z]+\b', task.upper())
        significant_words = [w for w in words if len(w) >= 4][:5]
        
        if not significant_words:
            return {
                'assigned_node': 'Node 0',
                'reason': 'Default assignment',
                'confidence': 0.5
            }
        
        # Analyze words
        word_analyses = []
        for word in significant_words:
            try:
                analysis = self.engine.analyze_word(word)
                word_analyses.append(analysis)
            except:
                continue
        
        if not word_analyses:
            return {
                'assigned_node': 'Node 0',
                'reason': 'Unable to analyze',
                'confidence': 0.5
            }
        
        # Calculate dominant element
        element_counts = {'Fire': 0, 'Water': 0, 'Earth': 0, 'Air': 0, 'Spirit': 0}
        for w in word_analyses:
            element_counts[w['dominant_element']] += 1
        
        dominant_element = max(element_counts, key=element_counts.get)
        
        # Assign node
        node_mapping = {
            'Fire': ('Node 1', 'Executor - action-oriented tasks'),
            'Water': ('Node 2', 'Meta-Conscience - reflective analysis'),
            'Air': ('Node 0', 'Wire - communication and transmission'),
            'Earth': ('Node 3', 'Grounding - stable processing'),
            'Spirit': ('Node 4', 'Transformation - complex synthesis')
        }
        
        assigned_node, reason = node_mapping.get(dominant_element, ('Node 0', 'Default'))
        
        return {
            'assigned_node': assigned_node,
            'reason': reason,
            'dominant_element': dominant_element,
            'confidence': element_counts[dominant_element] / len(word_analyses)
        }
    
    def generate_payload(self, concept1: str, concept2: str) -> dict:
        """
        Generate payload by mating two concepts.
        
        Uses word mating algorithm to create new concepts.
        
        Args:
            concept1: First concept
            concept2: Second concept
            
        Returns:
            Generated payload
        """
        result = self.mating.mate_words(concept1, concept2, max_candidates=3)
        
        payload = {
            'parent_concepts': [concept1, concept2],
            'compatibility': result['compatibility'],
            'generated_concepts': [
                {
                    'word': offspring['word'],
                    'score': offspring['score'],
                    'gematria': offspring['analysis']['gematria'],
                    'io_ratio': offspring['analysis']['io_ratio'],
                    'dominant_element': offspring['analysis']['dominant_element']
                }
                for offspring in result['offspring']
            ],
            'recommendation': result['offspring'][0]['word'] if result['offspring'] else None
        }
        
        return payload


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

def classify_truth_for_terex(statement: str) -> dict:
    """Classify truth for TEREX system."""
    bridge = OmegaTerexBridge()
    return bridge.classify_truth(statement)


def assign_task_to_omega(task: str) -> dict:
    """Assign task to OMEGA node."""
    bridge = OmegaTerexBridge()
    return bridge.assign_omega_node(task)


# ============================================================================
# MAIN / TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("OMEGA & TEREX INTEGRATION BRIDGE - Testing")
    print("=" * 70)
    
    bridge = OmegaTerexBridge()
    
    # Test 1: Truth classification
    print("\n" + "=" * 70)
    print("TEST 1: Truth Classification for TEREX")
    print("=" * 70)
    
    statements = [
        "Water flows downhill due to gravity",
        "Love conquers all challenges",
        "The sky is falling and chaos reigns",
    ]
    
    for statement in statements:
        result = bridge.classify_truth(statement)
        print(f"\nStatement: {statement}")
        print(f"Classification: {result['classification']}")
        print(f"Confidence: {result['confidence']:.1%}")
        print(f"Reasons: {', '.join(result['reasons'])}")
    
    # Test 2: OMEGA node assignment
    print("\n" + "=" * 70)
    print("TEST 2: OMEGA Node Assignment")
    print("=" * 70)
    
    tasks = [
        "Execute immediate action on the target",
        "Reflect deeply on the philosophical implications",
        "Transmit this message to all nodes",
        "Build a stable foundation for the system",
    ]
    
    for task in tasks:
        result = bridge.assign_omega_node(task)
        print(f"\nTask: {task}")
        print(f"Assigned Node: {result['assigned_node']}")
        print(f"Reason: {result['reason']}")
        print(f"Confidence: {result['confidence']:.1%}")
    
    # Test 3: Payload generation
    print("\n" + "=" * 70)
    print("TEST 3: Payload Generation")
    print("=" * 70)
    
    concept_pairs = [
        ("TRUTH", "POWER"),
        ("LIGHT", "DARKNESS"),
    ]
    
    for concept1, concept2 in concept_pairs:
        result = bridge.generate_payload(concept1, concept2)
        print(f"\nConcepts: {concept1} + {concept2}")
        print(f"Compatibility: {result['compatibility']:.1%}")
        print(f"Generated Concepts:")
        for concept in result['generated_concepts']:
            print(f"  - {concept['word']} (Score: {concept['score']:.1%})")
        print(f"Recommendation: {result['recommendation']}")
