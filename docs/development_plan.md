# NeuroSentry — Development Plan

## 1. Purpose

This document defines the proposed development stages for NeuroSentry, an EEG-based assistive system designed to classify predefined user intents and provide validated predictions to a caregiver.

The plan covers hardware configuration, EEG data acquisition, signal processing, machine-learning development, confidence-based validation, caregiver notification, and system evaluation.

**Status:** This is a development plan. Tasks should be marked complete only after implementation and verification.

## 2. Development Phases

### Phase 1: Hardware and Environment Setup

**Objective:** Establish a suitable environment for EEG acquisition and software development.

Planned tasks:
- Confirm the selected EEG acquisition device and its compatibility.
- Verify the proposed four-channel, 200 Hz configuration if the Ganglion board is used.
- Review electrode placement and acquisition requirements.
- Set up the development environment and required software dependencies.
- Verify that the device can produce usable EEG recordings.

**Deliverable:** Documented hardware configuration and a verified acquisition setup.

### Phase 2: Data Collection and Experimental Protocol

**Objective:** Establish a suitable dataset for the supported intent categories.

Planned tasks:
- Define the intent categories to be investigated.
- Design a consistent data collection protocol.
- Define appropriate participant consent and privacy procedures.
- Record the experimental conditions and relevant acquisition settings.
- Label collected recordings using the defined protocol.
- Separate training, validation, and test data appropriately.

**Deliverable:** A documented data collection protocol and a suitably prepared dataset.

EEG data must not be assumed to represent a particular intent without a suitable experimental protocol and supporting evidence.

### Phase 3: Signal Preprocessing

**Objective:** Prepare EEG recordings for model development.

Planned tasks:
- Inspect signal quality.
- Investigate suitable filtering methods.
- Identify and handle artifacts where appropriate.
- Segment recordings into analysis windows.
- Check for missing, invalid, or unusable samples.
- Document the selected preprocessing parameters.

**Deliverable:** A tested preprocessing pipeline.

### Phase 4: Feature Extraction

**Objective:** Prepare suitable model inputs from the processed EEG signals.

Planned tasks:
- Investigate appropriate EEG feature representations.
- Implement the selected feature extraction method.
- Ensure consistent processing across training and inference.
- Evaluate feature quality using the available dataset.

**Deliverable:** A documented feature extraction pipeline.

### Phase 5: Machine-Learning Model Development

**Objective:** Investigate classification of the predefined intent categories.

Planned tasks:
- Select a suitable baseline classification approach.
- Train the model using the prepared training data.
- Evaluate the model using separate validation data.
- Measure class-wise performance and common errors.
- Record the selected model configuration and experimental results.

**Deliverable:** A trained and evaluated model, if supported by the experimental results.

The model architecture and final supported intent categories will be documented after they are selected and tested.

### Phase 6: Confidence-Based Validation

**Objective:** Reduce alerts caused by uncertain model predictions.

Planned tasks:
- Identify how prediction confidence will be obtained.
- Define a configurable acceptance threshold or validation policy.
- Evaluate the policy using validation data.
- Record accepted, rejected, and uncertain predictions.
- Measure the effect on false alerts and missed predictions.

**Deliverable:** A tested confidence-validation component and documented evaluation results.

Confidence scores must not be treated as proof that a prediction is correct.

### Phase 7: Caregiver Notification

**Objective:** Communicate accepted intent predictions to a designated caregiver.

Planned tasks:
- Select the notification interface or communication channel.
- Define the information included in an alert.
- Implement the notification workflow.
- Handle notification failures and repeated alerts.
- Verify delivery behavior during testing.
- Apply appropriate privacy and access controls.

**Deliverable:** A tested caregiver notification component.

The final notification technology remains to be selected and verified.

### Phase 8: System Integration

**Objective:** Integrate the individual components into one workflow.

Planned tasks:
- Connect EEG acquisition to preprocessing.
- Connect preprocessing and feature extraction to the classifier.
- Connect classification to confidence-based validation.
- Connect accepted predictions to caregiver notification.
- Add error handling between components.
- Verify that invalid or uncertain inputs do not trigger inappropriate alerts.

**Deliverable:** An integrated prototype, subject to successful implementation and testing.

### Phase 9: Testing and Evaluation

**Objective:** Evaluate the system using documented test procedures.

Planned tasks:
- Test signal preprocessing and invalid-input handling.
- Evaluate classification performance on held-out test data.
- Measure false positives, false negatives, and rejected predictions.
- Test notification delivery and failure handling.
- Measure end-to-end latency and reliability.
- Document limitations and observed failure cases.

**Deliverable:** Test cases, measured results, and an evaluation report.

No performance figures should be reported until they have been measured.

### Phase 10: Documentation and Demonstration

**Objective:** Prepare the project for technical review and demonstration.

Planned tasks:
- Document the final hardware and software configuration.
- Maintain system architecture and component documentation.
- Provide setup instructions and dependency information.
- Include sample test procedures and representative results where appropriate.
- Prepare a demonstration using verified functionality.
- Clearly state implemented features, limitations, and remaining work.

**Deliverable:** A documented prototype suitable for review, if the required implementation and testing are completed.

## 3. Proposed Milestone Tracker

| Milestone | Expected evidence | Status |
|---|---|---|
| M1: Hardware setup | Verified device configuration and acquisition test | Planned |
| M2: Dataset preparation | Documented collection and labeling protocol | Planned |
| M3: Signal processing | Tested preprocessing pipeline | Planned |
| M4: Feature extraction | Documented feature pipeline | Planned |
| M5: Model development | Training and evaluation results | Planned |
| M6: Confidence validation | Evaluated acceptance policy | Planned |
| M7: Caregiver notification | Notification test results | Planned |
| M8: System integration | End-to-end integration test | Planned |
| M9: Final evaluation | Test report with measured results | Planned |
| M10: Demonstration | Verified demonstration and setup guide | Planned |

Update the status of each milestone only when the corresponding work has been completed and verified.

## 4. Risks and Mitigation

| Risk | Proposed mitigation |
|---|---|
| Poor EEG signal quality | Verify electrode setup, inspect recordings, and define signal-quality checks. |
| Insufficient training data | Use a documented collection protocol and report dataset limitations. |
| Incorrect intent predictions | Evaluate class-wise performance and test on held-out data. |
| False caregiver alerts | Apply and evaluate confidence-based validation. |
| Missed valid intents | Measure false negatives and assess the validation policy. |
| Notification failures | Implement delivery checks and appropriate error handling. |
| Sensitive data exposure | Apply consent, access control, and secure data-handling practices. |

## 5. Development Principles

- Implement and verify each stage before marking it complete.
- Keep training, validation, and test data appropriately separated.
- Document software dependencies and configuration.
- Report measured results without inventing performance figures.
- Protect sensitive EEG recordings and participant information.
- Treat predictions as uncertain outputs that require appropriate validation.
- Do not claim clinical validation without suitable evidence.

## 6. Current Status

The repository currently contains project documentation describing the proposed system architecture, component responsibilities, and development plan.

The implementation status of individual hardware and software components must be recorded separately as development progresses.

---

**NeuroSentry — Development roadmap for an EEG-based assistive intent-classification and caregiver-alert prototype.**
