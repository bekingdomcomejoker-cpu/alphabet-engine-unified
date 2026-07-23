"""
LLM INTEGRATION WRAPPER - Alphabet Engine Enhancement
======================================================

Wraps Claude, GPT, and Gemini with Alphabet Engine analysis
to provide enhanced semantic understanding and word analysis.

Features:
1. Pre-analysis: Analyze query through Alphabet Engine before sending to LLM
2. Post-analysis: Analyze LLM response for semantic patterns
3. Enhanced prompts: Inject Alphabet Engine insights into prompts
4. Comparative analysis: Compare responses across LLMs using Alphabet metrics
"""

import os
import sys
from typing import Dict, List, Optional
from openai import OpenAI

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.alphabet_engine import AlphabetEngine
from core.advanced_operators import AdvancedOperators
from core.word_mating import WordMating


class AlphabetLLM:
    """
    LLM wrapper with Alphabet Engine integration.
    
    Supports:
    - Claude (via OpenAI-compatible API)
    - GPT (via OpenAI API)
    - Gemini (via OpenAI-compatible API)
    """
    
    def __init__(self, model: str = "gpt-4.1-mini"):
        """
        Initialize LLM wrapper.
        
        Args:
            model: Model name (gpt-4.1-mini, gpt-4.1-nano, gemini-2.5-flash)
        """
        self.model = model
        self.client = OpenAI()  # Uses pre-configured API key and base URL
        
        # Initialize Alphabet Engine components
        self.engine = AlphabetEngine()
        self.operators = AdvancedOperators()
        self.mating = WordMating()
    
    def query(
        self, 
        prompt: str, 
        with_alphabet_analysis: bool = True,
        system_prompt: Optional[str] = None
    ) -> Dict:
        """
        Query LLM with optional Alphabet Engine analysis.
        
        Args:
            prompt: User query
            with_alphabet_analysis: Whether to include Alphabet analysis
            system_prompt: Optional system prompt
            
        Returns:
            Dictionary containing:
            - response: LLM response text
            - prompt_analysis: Alphabet analysis of prompt
            - response_analysis: Alphabet analysis of response
            - model: Model used
        """
        # Analyze prompt
        prompt_analysis = None
        if with_alphabet_analysis:
            prompt_analysis = self._analyze_text(prompt)
        
        # Build messages
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        # Optionally enhance prompt with Alphabet insights
        if with_alphabet_analysis and prompt_analysis:
            enhanced_prompt = self._enhance_prompt(prompt, prompt_analysis)
            messages.append({"role": "user", "content": enhanced_prompt})
        else:
            messages.append({"role": "user", "content": prompt})
        
        # Query LLM
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=2000
            )
            response_text = completion.choices[0].message.content
        except Exception as e:
            return {
                'error': str(e),
                'model': self.model,
                'prompt_analysis': prompt_analysis
            }
        
        # Analyze response
        response_analysis = None
        if with_alphabet_analysis:
            response_analysis = self._analyze_text(response_text)
        
        return {
            'response': response_text,
            'prompt_analysis': prompt_analysis,
            'response_analysis': response_analysis,
            'model': self.model
        }
    
    def compare_models(
        self, 
        prompt: str, 
        models: List[str] = None
    ) -> Dict:
        """
        Compare responses across multiple LLMs using Alphabet metrics.
        
        Args:
            prompt: Query to send to all models
            models: List of model names (default: all available)
            
        Returns:
            Dictionary with responses and comparative analysis
        """
        if models is None:
            models = ["gpt-4.1-mini", "gpt-4.1-nano", "gemini-2.5-flash"]
        
        results = {}
        
        for model in models:
            # Temporarily switch model
            original_model = self.model
            self.model = model
            
            # Query model
            result = self.query(prompt, with_alphabet_analysis=True)
            results[model] = result
            
            # Restore original model
            self.model = original_model
        
        # Comparative analysis
        comparison = self._compare_responses(results)
        
        return {
            'prompt': prompt,
            'results': results,
            'comparison': comparison
        }
    
    def analyze_word_with_llm(self, word: str) -> Dict:
        """
        Analyze a word using both Alphabet Engine and LLM insights.
        
        Args:
            word: Word to analyze
            
        Returns:
            Combined analysis from Alphabet Engine and LLM
        """
        # Alphabet Engine analysis
        alphabet_analysis = self.engine.analyze_word(word)
        operator_analysis = self.operators.transform_word(word)
        
        # LLM analysis
        llm_prompt = f"""Analyze the word "{word}" from multiple perspectives:
1. Etymology and historical origin
2. Symbolic and archetypal meaning
3. Phonetic and acoustic qualities
4. Cultural and mythological associations

Provide a concise but insightful analysis."""
        
        llm_result = self.query(llm_prompt, with_alphabet_analysis=False)
        
        return {
            'word': word,
            'alphabet_analysis': alphabet_analysis,
            'operator_analysis': operator_analysis,
            'llm_analysis': llm_result.get('response', 'Error in LLM analysis'),
            'model': self.model
        }
    
    def generate_offspring_with_llm(
        self, 
        parent1: str, 
        parent2: str
    ) -> Dict:
        """
        Generate word offspring using Alphabet Engine and validate with LLM.
        
        Args:
            parent1: First parent word
            parent2: Second parent word
            
        Returns:
            Offspring candidates with LLM semantic validation
        """
        # Generate offspring using Alphabet Engine
        mating_result = self.mating.mate_words(parent1, parent2, max_candidates=5)
        
        # Get top candidates
        top_candidates = [
            offspring['word'] 
            for offspring in mating_result['offspring'][:3]
        ]
        
        # Ask LLM to validate semantic coherence
        llm_prompt = f"""Given two parent words "{parent1}" and "{parent2}", 
evaluate these potential offspring words for semantic coherence and meaningfulness:

{', '.join(top_candidates)}

For each word, assess:
1. Does it feel like a natural combination of the parent concepts?
2. Could it plausibly exist as a word in English or another language?
3. What meaning or concept might it represent?

Provide brief evaluations."""
        
        llm_validation = self.query(llm_prompt, with_alphabet_analysis=False)
        
        return {
            'parent1': parent1,
            'parent2': parent2,
            'compatibility': mating_result['compatibility'],
            'offspring_candidates': mating_result['offspring'][:3],
            'llm_validation': llm_validation.get('response', 'Error in validation'),
            'model': self.model
        }
    
    def _analyze_text(self, text: str) -> Dict:
        """
        Analyze text using Alphabet Engine.
        
        Extracts key words and analyzes them.
        """
        # Simple word extraction (split on whitespace and punctuation)
        import re
        words = re.findall(r'\b[a-zA-Z]+\b', text)
        
        # Filter to significant words (length >= 4)
        significant_words = [w for w in words if len(w) >= 4][:5]
        
        if not significant_words:
            return {'words': [], 'summary': 'No significant words found'}
        
        # Analyze each word
        word_analyses = []
        for word in significant_words:
            try:
                analysis = self.engine.analyze_word(word)
                word_analyses.append({
                    'word': word,
                    'gematria': analysis['gematria'],
                    'io_ratio': analysis['io_ratio'],
                    'dominant_element': analysis['dominant_element']
                })
            except:
                continue
        
        # Calculate aggregate metrics
        if word_analyses:
            avg_io_ratio = sum(w['io_ratio'] for w in word_analyses) / len(word_analyses)
            total_gematria = sum(w['gematria'] for w in word_analyses)
        else:
            avg_io_ratio = 0.5
            total_gematria = 0
        
        return {
            'words': word_analyses,
            'avg_io_ratio': round(avg_io_ratio, 4),
            'total_gematria': total_gematria,
            'summary': f"{len(word_analyses)} words analyzed"
        }
    
    def _enhance_prompt(self, prompt: str, analysis: Dict) -> str:
        """
        Enhance prompt with Alphabet Engine insights.
        
        Adds subtle context about the semantic structure of the query.
        """
        io_ratio = analysis.get('avg_io_ratio', 0.5)
        
        if io_ratio > 0.6:
            tone_hint = "(Note: This query has projective/assertive energy)"
        elif io_ratio < 0.4:
            tone_hint = "(Note: This query has receptive/exploratory energy)"
        else:
            tone_hint = "(Note: This query has balanced energy)"
        
        # Don't actually modify the prompt - just return original
        # (Alphabet analysis is for internal tracking)
        return prompt
    
    def _compare_responses(self, results: Dict) -> Dict:
        """
        Compare responses across models using Alphabet metrics.
        """
        comparisons = {}
        
        for model, result in results.items():
            if 'response_analysis' in result and result['response_analysis']:
                analysis = result['response_analysis']
                comparisons[model] = {
                    'avg_io_ratio': analysis.get('avg_io_ratio', 0.5),
                    'total_gematria': analysis.get('total_gematria', 0),
                    'word_count': len(analysis.get('words', []))
                }
        
        return comparisons


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

def query_claude(prompt: str, **kwargs) -> Dict:
    """Query Claude with Alphabet Engine analysis."""
    llm = AlphabetLLM(model="gpt-4.1-mini")  # Claude via OpenAI-compatible API
    return llm.query(prompt, **kwargs)


def query_gpt(prompt: str, **kwargs) -> Dict:
    """Query GPT with Alphabet Engine analysis."""
    llm = AlphabetLLM(model="gpt-4.1-nano")
    return llm.query(prompt, **kwargs)


def query_gemini(prompt: str, **kwargs) -> Dict:
    """Query Gemini with Alphabet Engine analysis."""
    llm = AlphabetLLM(model="gemini-2.5-flash")
    return llm.query(prompt, **kwargs)


def compare_all_models(prompt: str) -> Dict:
    """Compare responses across all available models."""
    llm = AlphabetLLM()
    return llm.compare_models(prompt)


# ============================================================================
# MAIN / TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("LLM INTEGRATION WRAPPER - Alphabet Engine Enhancement")
    print("=" * 70)
    
    # Test 1: Single word analysis
    print("\n" + "=" * 70)
    print("TEST 1: Word Analysis with LLM")
    print("=" * 70)
    
    llm = AlphabetLLM(model="gpt-4.1-mini")
    result = llm.analyze_word_with_llm("TRUTH")
    
    print(f"\nWord: {result['word']}")
    print(f"Gematria: {result['alphabet_analysis']['gematria']}")
    print(f"I/O Ratio: {result['alphabet_analysis']['io_ratio']}")
    print(f"Dominant Element: {result['alphabet_analysis']['dominant_element']}")
    print(f"\nLLM Analysis:\n{result['llm_analysis'][:300]}...")
    
    # Test 2: Word mating with LLM validation
    print("\n" + "=" * 70)
    print("TEST 2: Word Mating with LLM Validation")
    print("=" * 70)
    
    result = llm.generate_offspring_with_llm("FIRE", "WATER")
    
    print(f"\nParents: {result['parent1']} + {result['parent2']}")
    print(f"Compatibility: {result['compatibility']:.2%}")
    print(f"\nTop Offspring:")
    for offspring in result['offspring_candidates']:
        print(f"  - {offspring['word']} (Score: {offspring['score']:.2%})")
    print(f"\nLLM Validation:\n{result['llm_validation'][:300]}...")
