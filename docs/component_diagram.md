# NeuroSentry — Component Diagram and Design

## 1. Purpose

This document describes the proposed components of NeuroSentry and how they interact to support EEG-based classification of predefined intents and caregiver notification.

The design includes EEG acquisition, signal preprocessing, feature extraction, machine-learning classification, confidence-based validation, and caregiver notification.

**Development note:** This is a proposed component design. Actual hardware integration, model performance, and end-to-end operation must be verified through implementation and testing.

## 2. Component Diagram

```text
+--------------------------+
|       User / Subject     |
+------------+-------------+
             |
             | EEG signals
             v
+--------------------------+
| 1. EEG Acquisition       |
| Compatible EEG device    |
| Proposed: Ganglion       |
| 4 channels, 200 Hz       |
+------------+-------------+
             |
             | Raw EEG samples
             v
+--------------------------+
| 2. Signal Preprocessing  |
| Signal quality checks    |
| Filtering / segmentation|
+------------+-------------+
             |
             | Processed signal windows
             v
+--------------------------+
| 3. Feature Extraction    |
| Generate model features |
+------------+-------------+
             |
             | Feature vectors
             v
+--------------------------+
| 4. AI/ML Classifier      |
| Predict supported intent |
| category                 |
+------------+-------------+
             |
             | Prediction + confidence
             v
+--------------------------+
| 5. Confidence Validator  |
| Apply configured policy |
+------------+-------------+
             |
             v
       +-----+------+
       |            |
       v            v
+--------------+  +--------------------+
| Reject /     |  | Accepted Prediction|
| Mark Uncertain| +---------+----------+
+--------------+            |
                            | Validated intent
                            v
                 +------------------------+
                 | 6. Caregiver Alert     |
                 | Notification Interface|
                 +------------------------+
```

## 3. Component Responsibilities

### 3.1 EEG Acquisition Component

**Purpose:** Acquire EEG samples from the selected hardware.

**Input:** Electrical signals measured through the EEG electrodes.

**Output:** Digital EEG samples for downstream processing.

**Design considerations:**
- Confirm device compatibility and configuration.
- Verify channel availability and sampling rate.
- Check for missing, saturated, or poor-quality signals.
- Follow appropriate electrode placement and data-collection procedures.

A Ganglion board with four channels and a 200 Hz sampling rate has been considered during project discussions. The final configuration must be verified during implementation.

### 3.2 Signal Preprocessing Component

**Purpose:** Prepare the acquired EEG samples for analysis.

**Input:** Raw EEG samples.

**Output:** Processed signal segments suitable for feature extraction.

**Potential operations:**
- Signal quality assessment.
- Appropriate digital filtering.
- Artifact identification or handling.
- Segmentation into analysis windows.
- Handling of invalid or missing samples.

The exact preprocessing pipeline will be selected and evaluated using the actual acquisition setup.

### 3.3 Feature Extraction Component

**Purpose:** Convert processed EEG segments into features that can be supplied to the classifier.

**Input:** Preprocessed EEG segments.

**Output:** Feature vectors.

Feature selection depends on the chosen experimental protocol and model. The same feature definitions and processing parameters must be used consistently during training and inference.

### 3.4 AI/ML Classification Component

**Purpose:** Predict a supported intent category from the extracted features.

**Input:** Feature vectors.

**Output:** Predicted class and its associated confidence score, where supported by the selected model.

The classifier requires suitable training data and a defined labeling protocol. The model architecture and supported intent categories must be finalized and evaluated before deployment.

### 3.5 Confidence-Based Validation Component

**Purpose:** Determine whether a prediction satisfies the configured acceptance policy.

**Input:** Predicted class and confidence information.

**Output:** An accepted prediction or a rejected/uncertain result.

**Decision logic:**
- If the prediction satisfies the configured criteria, pass it to the next validation stage.
- If it does not satisfy those criteria, reject it or mark it uncertain.
- Do not automatically interpret confidence as proof of correctness.

The threshold and validation policy must be chosen using appropriate validation data and evaluated against false alerts and missed predictions.

### 3.6 Caregiver Alert Component

**Purpose:** Communicate an accepted intent to the designated caregiver.

**Input:** An accepted intent and any approved information needed for the alert.

**Output:** A notification through the interface selected for implementation.

**Design considerations:**
- Clear and understandable alert messages.
- Notification delivery status and error handling.
- Duplicate-alert control.
- Appropriate access control and data protection.

The notification channel has not been finalized in this document and must be recorded after implementation.

## 4. Component Interaction Sequence

1. The acquisition component collects EEG samples.
2. The preprocessing component checks and prepares the samples.
3. The feature extraction component produces the model input.
4. The classifier predicts a supported intent category.
5. The confidence validator evaluates the prediction.
6. Uncertain predictions are rejected or flagged.
7. Accepted predictions are passed to the caregiver alert component.
8. Testing records the results required to evaluate system performance.

## 5. Error Handling

The proposed design should address the following cases:

| Condition | Proposed response |
|---|---|
| Poor-quality EEG signal | Flag the signal and avoid making an unreliable prediction. |
| Missing or invalid samples | Reject the affected input window or handle it according to the validated processing policy. |
| Low-confidence prediction | Reject or mark the prediction uncertain. |
| Classifier failure | Record the error and avoid sending an unverified alert. |
| Notification delivery failure | Record the failure and apply the selected retry or recovery policy. |
| Repeated predictions | Apply an appropriate duplicate-alert policy after testing. |

## 6. Privacy and Safety

- Collect EEG data only under an appropriate consent and data-handling process.
- Avoid publishing identifiable or sensitive recordings.
- Restrict access to private data and notification configuration.
- Evaluate false positives and false negatives.
- Do not present a predicted intent as a confirmed thought or request.
- Keep human caregiving and appropriate clinical assessment separate from the prototype's predictions.

## 7. Implementation Status

This document describes the proposed component design. It does not imply that all components have been implemented, integrated, or validated.

The final hardware configuration, signal-processing methods, classifier, confidence threshold, notification channel, and measured performance will be documented as the corresponding work is completed and tested.
