# NeuroSentry — System Architecture

## 1. Overview

NeuroSentry is a proposed EEG-based assistive system that explores the classification of predefined user intents and the delivery of validated predictions to a caregiver. The architecture is organized into signal acquisition, signal processing, intent classification, confidence-based validation, and caregiver notification layers.

This document describes the proposed design. Hardware integration, model selection, and end-to-end functionality must be verified during implementation.

## 2. Architectural Objectives

- Acquire EEG signals from a compatible device.
- Prepare the acquired signals for analysis.
- Classify signals into supported intent categories using a trained model.
- Reject or flag predictions that do not meet the configured confidence threshold.
- Notify a caregiver when a prediction passes the required validation stages.
- Support testing, monitoring, and performance evaluation.

## 3. High-Level Data Flow

```text
+-------------------------+
|       User / Subject    |
+------------+------------+
             |
             v
+-------------------------+
| EEG Acquisition Device  |
| Proposed: Ganglion      |
| 4 channels, 200 Hz      |
+------------+------------+
             |
             v
+-------------------------+
| Signal Preprocessing    |
| Filtering and quality   |
| checks, as appropriate  |
+------------+------------+
             |
             v
+-------------------------+
| Feature Extraction      |
| Features selected       |
| during model development|
+------------+------------+
             |
             v
+-------------------------+
| AI/ML Intent Classifier |
| Predicts supported      |
| intent category         |
+------------+------------+
             |
             v
+-------------------------+
| Confidence Validation   |
| Compare with configured |
| threshold               |
+------------+------------+
             |
       +-----+------+
       |            |
       v            v
+-------------+  +----------------+
| Uncertain / |  | Accepted       |
| Rejected    |  | Prediction     |
+-------------+  +-------+--------+
                         |
                         v
                +------------------+
                | Caregiver Alert  |
                | Notification     |
                +------------------+
```

**Note:** The diagram represents the proposed data flow. Exact filtering methods, features, classifier architecture, confidence threshold, and notification technology remain to be finalized and validated.

## 4. Architecture Components

### 4.1 EEG Acquisition Layer

This layer collects EEG data using a compatible EEG acquisition device. A Ganglion board with four channels and a sampling rate of 200 Hz has been considered during project discussions.

The final configuration must be confirmed through hardware testing, including electrode placement, signal quality, and device compatibility.

### 4.2 Signal Preprocessing Layer

The preprocessing layer prepares raw EEG signals for analysis. Depending on the selected acquisition setup and experimental protocol, it may include:

- Signal quality checks.
- Appropriate filtering.
- Artifact identification or handling.
- Segmentation into suitable analysis windows.
- Validation of missing or invalid samples.

The final processing pipeline must be selected and tested against the actual signals.

### 4.3 Feature Extraction Layer

This layer converts the preprocessed signal windows into features suitable for the selected classification model.

The features will be determined during experimentation. They must be calculated consistently during model training and inference.

### 4.4 AI/ML Classification Layer

The classifier predicts one of the intent categories supported by the experimental dataset and training procedure.

The model architecture, training dataset, labeling procedure, and evaluation metrics must be documented once selected. EEG-based intent recognition must not be assumed to work without appropriate data and validation.

### 4.5 Confidence-Based Validation Layer

This layer evaluates the classifier's prediction confidence against a configurable threshold.

- Predictions meeting the configured criteria may proceed to the next validation stage.
- Predictions below the threshold should be rejected or marked uncertain.
- A confidence score alone does not establish that a prediction is correct.

The threshold and decision policy must be evaluated using validation data and appropriate performance metrics.

### 4.6 Caregiver Notification Layer

This layer is responsible for communicating an accepted intent to the designated caregiver through the notification interface selected for implementation.

The implementation should address delivery failures, duplicate alerts, message clarity, access control, and protection of sensitive data.

### 4.7 Evaluation Layer

The system should be tested using appropriate data and predefined metrics, including:

- Classification accuracy and class-wise performance.
- False-positive and false-negative rates.
- Number of rejected or uncertain predictions.
- Notification delivery success and latency.
- End-to-end system reliability.

Results must be reported only after testing has been performed.

## 5. Proposed End-to-End Operation

1. Collect EEG signals using the configured acquisition device.
2. Check signal quality and preprocess valid signal segments.
3. Extract the features required by the trained model.
4. Generate a prediction for a supported intent category.
5. Apply confidence-based validation.
6. Reject or flag uncertain predictions.
7. Pass accepted predictions to the caregiver notification component.
8. Record appropriate test results while protecting sensitive information.

## 6. Reliability, Privacy, and Safety

- Obtain appropriate consent before collecting EEG data.
- Protect sensitive recordings and personal information.
- Avoid sending caregiver alerts for predictions that fail validation.
- Include suitable error handling for invalid signals and notification failures.
- Evaluate false alerts and missed predictions.
- Do not treat a model output as a confirmed statement of the user's intention.
- Do not position the prototype as a replacement for clinical assessment or human caregiving.

## 7. Current Development Status

This document records the proposed architecture for the restructured NeuroSentry project. It does not establish that the complete system has been implemented or validated.

The final hardware configuration, preprocessing pipeline, trained model, validation threshold, notification mechanism, and measured performance will be documented as they are implemented and tested.

## 8. Next Implementation Milestones

1. Confirm the EEG acquisition hardware and configuration.
2. Define the experimental protocol and supported intent categories.
3. Establish an appropriate data collection and labeling process.
4. Implement and test preprocessing and feature extraction.
5. Train and evaluate the classification model.
6. Implement confidence-based validation.
7. Integrate and test caregiver notifications.
8. Perform end-to-end testing and document measured results.
