import sys
sys.path.insert(0, '/home/ubuntu/alphabet-engine/core')
from alphabet_engine import AlphabetEngine
import json
from typing import Dict, Any

class ClaudeIntegration:
    def __init__(self):
        self.engine = AlphabetEngine()
    def analyze_linguistic_task(self, query: str) -> Dict[str, Any]:
        words = [w for w in query.split() if len(w) > 2]
        results = [{'word': w, 'analysis': self.engine.analyze_word(w).__dict__} for w in words[:5]]
        return {'query': query, 'analyses': results}

class GPTIntegration:
    def __init__(self):
        self.engine = AlphabetEngine()
    def analyze_creative_generation(self, seed: str) -> Dict[str, Any]:
        return self.engine.mate_words(seed, 'SPIRIT')

class GeminiIntegration:
    def __init__(self):
        self.engine = AlphabetEngine()
    def analyze_multimodal(self, text: str) -> Dict[str, Any]:
        analysis = self.engine.analyze_word(text)
        return {'text': text, 'gematria': analysis.gematria_total, 'elements': analysis.elements}

class BenchmarkSuite:
    def __init__(self):
        self.engine = AlphabetEngine()
    def run_all(self) -> Dict[str, Any]:
        tests = ['COMMUNION', 'KINGDOM', 'TRUTH', 'LOVE', 'SPIRIT', 'GABRIEL', 'MICHAEL', 'JESUS']
        return {'benchmarks': [{'word': w, 'gematria': self.engine.analyze_word(w).gematria_total} for w in tests]}

if __name__ == '__main__':
    suite = BenchmarkSuite()
    print(json.dumps(suite.run_all(), indent=2, default=str))
