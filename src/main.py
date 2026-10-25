"""
NeuroSentry - Initial Software Prototype

Demonstrates a simulated intent-classification workflow:
sample input -> classification -> confidence validation -> alert simulation.

This prototype does NOT process real EEG signals or infer actual human intent.
"""

from dataclasses import dataclass


CONFIDENCE_THRESHOLD = 0.75


@dataclass
class Prediction:
    intent: str
    confidence: float


def classify_sample(sample: dict) -> Prediction:
    """
    Simulated classifier for software workflow testing only.

    The sample represents a predefined test case, not measured EEG.
    Replace this function with a properly trained and evaluated model
    before attempting real EEG intent classification.
    """
    return Prediction(
        intent=sample["intent"],
        confidence=float(sample["confidence"]),
    )


def validate_prediction(prediction: Prediction) -> bool:
    """Accept predictions that meet the configured threshold."""
    if not 0.0 <= prediction.confidence <= 1.0:
        return False

    return prediction.confidence >= CONFIDENCE_THRESHOLD


def notify_caregiver(intent: str) -> None:
    """Simulate a caregiver alert; no real message is sent."""
    print(f"[ALERT SIMULATION] Proposed user intent: {intent}")
    print("[INFO] No actual caregiver notification was sent.")


def process_sample(sample: dict) -> None:
    """Run one sample through the simulated workflow."""
    print("\n--- NeuroSentry Prototype ---")

    try:
        prediction = classify_sample(sample)
    except (KeyError, TypeError, ValueError) as error:
        print(f"[ERROR] Invalid sample: {error}")
        return

    if not prediction.intent.strip():
        print("[REJECTED] Intent label is empty.")
        return

    print(f"Predicted intent: {prediction.intent}")
    print(f"Simulated confidence: {prediction.confidence:.2f}")

    if validate_prediction(prediction):
        print("[ACCEPTED] Prediction passed the threshold.")
        notify_caregiver(prediction.intent)
    else:
        print("[REJECTED] Prediction did not pass validation.")
        print("[INFO] No alert simulation was triggered.")


def main() -> None:
    # Illustrative test cases only; these are not EEG recordings.
    test_samples = [
        {"intent": "water", "confidence": 0.92},
        {"intent": "assistance", "confidence": 0.61},
        {"intent": "rest", "confidence": 0.81},
    ]

    print("NeuroSentry - Simulated Workflow Test")
    print(f"Confidence threshold: {CONFIDENCE_THRESHOLD:.2f}")

    for sample in test_samples:
        process_sample(sample)

    print("\nSimulation completed.")
    print("This result does not validate real EEG intent recognition.")


if __name__ == "__main__":
    main()
