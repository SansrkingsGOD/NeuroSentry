# NeuroSentry
### EEG-Based AI Assistive System with Confidence-Based Intent Classification and Caregiver Alerts

## 1. Project Overview

NeuroSentry is a proposed EEG-based assistive system designed to explore how brain-signal analysis and machine learning can support communication of predefined user needs to caregivers.

The system is designed around EEG signal acquisition, signal preprocessing, intent classification, confidence-based validation, and caregiver notification. Its primary objective is to investigate a structured approach for recognizing predefined intent categories while reducing alerts generated from uncertain predictions.

## 2. Problem Statement

Individuals who experience difficulties with conventional communication may need assistance expressing their basic needs. Caregivers may not always be able to identify these needs immediately.

NeuroSentry explores whether EEG signal processing and machine learning can help recognize predefined user intents and communicate validated predictions to caregivers through an alert mechanism.

## 3. Project Objectives

- Acquire EEG signals using compatible EEG hardware.
- Preprocess signals to prepare them for analysis.
- Investigate suitable features for EEG-based intent classification.
- Develop a machine-learning pipeline for predefined intent categories.
- Implement confidence-based validation to reject uncertain predictions.
- Design a caregiver notification mechanism for validated predictions.
- Evaluate classification performance and alert reliability through testing.

## 4. Proposed System Workflow

### Step 1: EEG Signal Acquisition
Collect EEG signals using a compatible EEG acquisition device.

### Step 2: Signal Preprocessing
Prepare the acquired signals for analysis and reduce unwanted noise and artifacts.

### Step 3: Feature Extraction
Extract suitable signal features for the selected classification approach.

### Step 4: Intent Classification
Use a trained machine-learning model to classify the processed signals into supported intent categories.

### Step 5: Confidence-Based Validation
Compare the predicted class confidence with a configured threshold. Predictions that do not meet the threshold should be rejected or marked uncertain.

### Step 6: Caregiver Notification
Send an alert containing the accepted intent through the selected caregiver notification interface.

### Step 7: Performance Evaluation
Evaluate classification performance, uncertain predictions, false alerts, and notification reliability.

**Note:** EEG signals do not automatically reveal a person's thoughts or intentions. Recognizing specific intents requires an appropriate experimental protocol, suitable training data, and validation.

## 5. EEG Acquisition

The project design discussions have considered a Ganglion EEG board with the following specifications:

- **EEG channels:** 4
- **Sampling rate:** 200 Hz

The final hardware configuration, electrode placement, acquisition settings, and signal quality must be confirmed during implementation and testing.

## 6. Confidence-Based Validation

Confidence-based validation is intended to prevent uncertain model predictions from immediately triggering caregiver alerts.

The proposed decision process is:

- **Confidence meets the configured threshold:** Allow the prediction to proceed to the next validation stage.
- **Confidence falls below the threshold:** Reject the prediction or mark it as uncertain.

The threshold must be selected and evaluated using suitable validation data. A high confidence score does not, by itself, guarantee a correct prediction.

## 7. Caregiver Alert Mechanism

The proposed notification component communicates an accepted intent to a designated caregiver.

The implementation should address:

- Selection of the caregiver interface or notification channel.
- Alert content and presentation.
- Notification delivery failures.
- Prevention of unnecessary repeated alerts.
- Privacy and protection of user data.

The final notification technology will be documented after it has been selected and implemented.

## 8. Proposed System Components

| Component | Responsibility |
|---|---|
| EEG Acquisition Module | Collect signals from the selected EEG device. |
| Signal Preprocessing Module | Prepare signals for model input. |
| Feature Extraction Module | Generate features suitable for classification. |
| Machine-Learning Classifier | Predict a supported intent category. |
| Confidence Validation Module | Reject or flag uncertain predictions. |
| Caregiver Alert Module | Communicate accepted predictions to the caregiver. |
| Evaluation Module | Measure system performance using appropriate test data. |

## 9. Proposed Technology Stack

The final technology stack will be documented as implementation progresses.

Potential development areas include:

- Python for signal processing and machine learning.
- Compatible EEG acquisition software and device interfaces.
- Scientific computing and machine-learning libraries.
- A suitable caregiver notification interface.

## 10. Setup and Installation

### Prerequisites
- Python 3.10 or later
- Git
- A code editor such as Visual Studio Code

### Clone the Repository

```bash
git clone https://github.com/SansrkingsGOD/NeuroSentry.git
cd NeuroSentry
```

### Create a Virtual Environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

The software dependencies will be finalized when the signal-processing and machine-learning implementation is selected.

Once `requirements.txt` is available, install the dependencies using:

```bash
pip install -r requirements.txt
```

**Current status:** These are development setup instructions. The complete application is not yet confirmed to be implemented or executable.

## 11. Environment Variables

The current documentation does not require any environment variables.

If caregiver notifications, API integrations, or external services are added later, credentials must be stored in environment variables rather than committed to the repository.

Never publish passwords, API keys, access tokens, or personal health information.

## 12. Development Status

NeuroSentry is under development. The repository currently documents the proposed system architecture, component design, and development plan.

EEG acquisition, preprocessing, intent classification, confidence-based validation, and caregiver notification must be implemented and tested before the system can be considered operational.

## 13. Testing

Refer to `tests/test_cases.md` for the planned functional test cases and expected outcomes.

Refer to `data/README.md` for information about sample data and its intended use.

## 14. Technical Documentation

- `docs/system_architecture.md` — Proposed system architecture and workflow.
- `docs/component_diagram.md` — System components and their interactions.
- `docs/development_plan.md` — Planned development activities.

## 15. Safety and Limitations

NeuroSentry is a proposed assistive research project, not a clinically validated medical device. Predictions must not be treated as confirmed user intent without appropriate validation. The system is intended to support caregivers, not replace human supervision or professional medical care.

Specific libraries, model architectures, and notification services will be listed once they have been selected and tested.

