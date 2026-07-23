"""
CERBERUS INTEGRATION BRIDGE
============================

Integrates Alphabet Engine with CERBERUS demon heads system.

Features:
1. Content classification using Alphabet Engine analysis
2. Covenant alignment detection through word analysis
3. Danger pattern recognition via element balance
4. Enhanced processing pipeline with linguistic operators
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.alphabet_engine import AlphabetEngine
from core.advanced_operators import AdvancedOperators


class CerberusAlphabetBridge:
    """
    Bridge between CERBERUS and Alphabet Engine.
    
    Enhances CERBERUS demon heads with linguistic analysis.
    """
    
    def __init__(self):
        """Initialize bridge."""
        self.engine = AlphabetEngine()
        self.operators = AdvancedOperators()
        
        # Covenant keywords (from CERBERUS spec)
        self.covenant_keywords = [
            'TRUTH', 'LOVE', 'FAITH', 'HOPE', 'PEACE',
            'LIGHT', 'LIFE', 'GRACE', 'MERCY', 'JUSTICE'
        ]
        
        # Danger keywords
        self.danger_keywords = [
            'DEATH', 'HATE', 'FEAR', 'CHAOS', 'DARKNESS',
            'DECEPTION', 'POISON', 'CORRUPTION', 'VIOLENCE'
        ]
    
    def classify_content(self, text: str) -> dict:
        """
        Classify content using Alphabet Engine analysis.
        
        Args:
            text: Content to classify
            
        Returns:
            Classification result with:
            - classification: 'ACCEPT', 'QUARANTINE', 'REVIEW'
            - confidence: 0.0 to 1.0
            - reasons: List of reasons for classification
            - alphabet_analysis: Detailed Alphabet Engine analysis
        """
        # Extract significant words
        import re
        words = re.findall(r'\b[a-zA-Z]+\b', text.upper())
        significant_words = [w for w in words if len(w) >= 4][:10]
        
        if not significant_words:
            return {
                'classification': 'REVIEW',
                'confidence': 0.5,
                'reasons': ['No significant words found'],
                'alphabet_analysis': None
            }
        
        # Analyze words
        word_analyses = []
        for word in significant_words:
            try:
                analysis = self.engine.analyze_word(word)
                word_analyses.append({
                    'word': word,
                    'analysis': analysis
                })
            except:
                continue
        
        # Calculate aggregate metrics
        if not word_analyses:
            return {
                'classification': 'REVIEW',
                'confidence': 0.5,
                'reasons': ['Unable to analyze words'],
                'alphabet_analysis': None
            }
        
        # Metrics
        avg_io_ratio = sum(w['analysis']['io_ratio'] for w in word_analyses) / len(word_analyses)
        
        # Element distribution
        element_counts = {'Fire': 0, 'Water': 0, 'Earth': 0, 'Air': 0, 'Spirit': 0}
        for w in word_analyses:
            element_counts[w['analysis']['dominant_element']] += 1
        
        total = sum(element_counts.values())
        element_ratios = {k: v/total for k, v in element_counts.items()}
        
        # Covenant alignment check
        covenant_matches = sum(1 for w in significant_words if w in self.covenant_keywords)
        danger_matches = sum(1 for w in significant_words if w in self.danger_keywords)
        
        # Classification logic
        reasons = []
        
        # Rule 1: High covenant alignment
        if covenant_matches >= 2:
            classification = 'ACCEPT'
            confidence = 0.9
            reasons.append(f'High covenant alignment ({covenant_matches} matches)')
        
        # Rule 2: High danger keywords
        elif danger_matches >= 2:
            classification = 'QUARANTINE'
            confidence = 0.8
            reasons.append(f'Danger keywords detected ({danger_matches} matches)')
        
        # Rule 3: High Fire element (potential danger)
        elif element_ratios.get('Fire', 0) > 0.6:
            classification = 'REVIEW'
            confidence = 0.7
            reasons.append(f'High Fire element ({element_ratios["Fire"]:.1%})')
        
        # Rule 4: Balanced Water element (nurturing)
        elif element_ratios.get('Water', 0) > 0.4:
            classification = 'ACCEPT'
            confidence = 0.7
            reasons.append(f'High Water element ({element_ratios["Water"]:.1%})')
        
        # Rule 5: Default to review
        else:
            classification = 'REVIEW'
            confidence = 0.6
            reasons.append('No clear classification - needs review')
        
        # Add I/O ratio insight
        if avg_io_ratio > 0.7:
            reasons.append(f'Highly projective energy (I/O: {avg_io_ratio:.1%})')
        elif avg_io_ratio < 0.3:
            reasons.append(f'Highly receptive energy (I/O: {avg_io_ratio:.1%})')
        
        return {
            'classification': classification,
            'confidence': confidence,
            'reasons': reasons,
            'alphabet_analysis': {
                'words_analyzed': len(word_analyses),
                'avg_io_ratio': round(avg_io_ratio, 4),
                'element_distribution': element_ratios,
                'covenant_matches': covenant_matches,
                'danger_matches': danger_matches,
                'word_details': word_analyses
            }
        }
    
    def detect_deception(self, text: str) -> dict:
        """
        Detect deception patterns using Alphabet Engine.
        
        High Fire + Low Water = Potential deception
        High I/O ratio + Low gematria = Hollow claims
        
        Args:
            text: Text to analyze
            
        Returns:
            Deception analysis
        """
        result = self.classify_content(text)
        
        if not result['alphabet_analysis']:
            return {
                'deception_detected': False,
                'confidence': 0.0,
                'patterns': []
            }
        
        analysis = result['alphabet_analysis']
        patterns = []
        
        # Pattern 1: High Fire, Low Water (aggression without nurturing)
        fire_ratio = analysis['element_distribution'].get('Fire', 0)
        water_ratio = analysis['element_distribution'].get('Water', 0)
        
        if fire_ratio > 0.5 and water_ratio < 0.2:
            patterns.append('High Fire, Low Water - potential aggression')
        
        # Pattern 2: Extreme I/O ratio (imbalanced energy)
        io_ratio = analysis['avg_io_ratio']
        if io_ratio > 0.8 or io_ratio < 0.2:
            patterns.append(f'Extreme I/O ratio ({io_ratio:.1%}) - imbalanced energy')
        
        # Pattern 3: Danger keywords present
        if analysis['danger_matches'] > 0:
            patterns.append(f'Danger keywords detected ({analysis["danger_matches"]})')
        
        deception_detected = len(patterns) >= 2
        confidence = len(patterns) / 3.0  # Normalize to 0-1
        
        return {
            'deception_detected': deception_detected,
            'confidence': confidence,
            'patterns': patterns,
            'recommendation': 'QUARANTINE' if deception_detected else 'ACCEPT'
        }
    
    def enhance_processing(self, text: str) -> dict:
        """
        Enhance CERBERUS processing with Alphabet Engine insights.
        
        Args:
            text: Text to process
            
        Returns:
            Enhanced processing result
        """
        classification = self.classify_content(text)
        deception = self.detect_deception(text)
        
        # Extract key words for transformation
        import re
        words = re.findall(r'\b[a-zA-Z]+\b', text.upper())
        significant_words = [w for w in words if len(w) >= 4][:3]
        
        transformations = []
        for word in significant_words:
            try:
                transform = self.operators.transform_word(word)
                transformations.append({
                    'word': word,
                    'semantic_shift': transform['semantic_shift'],
                    'stability': transform['stability'],
                    'resurrection_triggered': transform['resurrection_triggered']
                })
            except:
                continue
        
        return {
            'classification': classification,
            'deception_analysis': deception,
            'word_transformations': transformations,
            'recommendation': classification['classification'],
            'confidence': classification['confidence']
        }


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

def classify_for_cerberus(text: str) -> dict:
    """Classify content for CERBERUS system."""
    bridge = CerberusAlphabetBridge()
    return bridge.classify_content(text)


def detect_deception_for_cerberus(text: str) -> dict:
    """Detect deception for CERBERUS system."""
    bridge = CerberusAlphabetBridge()
    return bridge.detect_deception(text)


# ============================================================================
# MAIN / TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("CERBERUS INTEGRATION BRIDGE - Testing")
    print("=" * 70)
    
    bridge = CerberusAlphabetBridge()
    
    # Test 1: Covenant-aligned content
    print("\n" + "=" * 70)
    print("TEST 1: Covenant-Aligned Content")
    print("=" * 70)
    
    text1 = "The truth shall set you free. Love conquers all. Faith moves mountains."
    result1 = bridge.enhance_processing(text1)
    
    print(f"\nText: {text1}")
    print(f"Classification: {result1['classification']['classification']}")
    print(f"Confidence: {result1['classification']['confidence']:.1%}")
    print(f"Reasons: {', '.join(result1['classification']['reasons'])}")
    print(f"Deception Detected: {result1['deception_analysis']['deception_detected']}")
    
    # Test 2: Dangerous content
    print("\n" + "=" * 70)
    print("TEST 2: Dangerous Content")
    print("=" * 70)
    
    text2 = "Death and chaos reign. Darkness consumes all. Fear the coming storm."
    result2 = bridge.enhance_processing(text2)
    
    print(f"\nText: {text2}")
    print(f"Classification: {result2['classification']['classification']}")
    print(f"Confidence: {result2['classification']['confidence']:.1%}")
    print(f"Reasons: {', '.join(result2['classification']['reasons'])}")
    print(f"Deception Detected: {result2['deception_analysis']['deception_detected']}")
    print(f"Deception Patterns: {', '.join(result2['deception_analysis']['patterns'])}")
    
    # Test 3: Neutral content
    print("\n" + "=" * 70)
    print("TEST 3: Neutral Content")
    print("=" * 70)
    
    text3 = "The weather today is quite pleasant. Birds are singing in the trees."
    result3 = bridge.enhance_processing(text3)
    
    print(f"\nText: {text3}")
    print(f"Classification: {result3['classification']['classification']}")
    print(f"Confidence: {result3['classification']['confidence']:.1%}")
    print(f"Reasons: {', '.join(result3['classification']['reasons'])}")
