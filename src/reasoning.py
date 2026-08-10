from google import genai
from google.genai import types
import os

class VoiceMatchReasoning:
    def __init__(self):
        # Automatically picks up GEMINI_API_KEY from the environment
        self.client = genai.Client()

    def analyze_ambiguous_match(self, target_name, match_score, audio_metadata):
        """
        Uses Gemini with a thinking configuration to reason through 
        borderline or ambiguous voice recognition scores.
        """
        prompt = f"""
        Analyze the following biometric voice recognition result and determine if it's a false positive or environmental distortion:
        - Target Identity: {target_name}
        - Cosine Similarity Score: {match_score}
        - Audio Characteristics: {audio_metadata}
        
        Provide a step-by-step reasoning breakdown and a final confidence recommendation.
        """

        response = self.client.models.generate_content(
            model="gemini-2.5-flash", # Or gemini-3.x models
            contents=prompt,
            config=types.GenerateContentConfig(
                # Enable thinking configuration with a token budget
                thinking_config=types.ThinkingConfig(
                    thinking_budget=2048,  # Allocates tokens specifically for internal reasoning steps
                ),
                temperature=0.2
            ),
        )

        return response.text

if __name__ == "__main__":
    reasoner = VoiceMatchReasoning()
    # Example evaluation call
    # print(reasoner.analyze_ambiguous_match("Athlete_A", 0.31, "High background crowd noise, 2-second clip"))
