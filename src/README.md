# NeuroSentry Source Code

## Purpose

This directory contains the source code for the NeuroSentry prototype.

NeuroSentry is a proposed EEG-based assistive system that investigates classifying predefined user intents and communicating validated predictions to a caregiver.

## Planned Components

1. **EEG Input:** Receives EEG recordings from a compatible acquisition device or a clearly identified sample dataset.
2. **Signal Preprocessing:** Prepares input signals for analysis.
3. **Intent Classification:** Applies a classification model to estimate predefined intent categories.
4. **Confidence Validation:** Rejects or flags predictions that do not meet the configured acceptance criteria.
5. **Caregiver Notification:** Communicates accepted predictions through the selected notification mechanism.

## Development Status

The components above describe the proposed design. They must not be considered implemented until corresponding code has been added and tested.

Initial development will use controlled sample inputs to test the software workflow. Sample-input results will not be treated as evidence of real EEG intent recognition.

## Planned Files

- `main.py` — Prototype entry point.
- `preprocessing.py` — Signal preprocessing functions.
- `classifier.py` — Intent classification interface.
- `validation.py` — Confidence-based prediction validation.
- `tests/` — Automated tests for supported functionality.

The final file structure may change as implementation progresses.
