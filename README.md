# VisioMetric Technical Test

## Introduction

You have been tasked with developing a new feature for a web application designed for surveillance officers to log the status of the surveillance cameras under their responsibility. The application serves a broad user base of officers.

Currently, the application relies on the client-side to determine the status of a camera. The frontend team has requested the addition of several backend endpoints to enable clients to update and log the status of the cameras directly.

### Requirement 1: Problem State Logging

A Camera's status is determined by the most recent log entry. I.e., if a camera's most recent CameraStatusLog entry is "Working", the camera is considered to be in a working state.

Clients (via a mobile or desktop app) should be capable of:

1. Marking a camera as being in a problem state (e.g., offline, incorrect position) by creating a corresponding log entry.
2. Logging when a camera returns to a working state, which resolves the existing problem log.

Considerations:

- To resolve a problem state, both a start and end time must be recorded in the log. If the end time is absent, the camera is deemed to be still in a problem state.
- Problem states must not overlap. If a camera is currently in a problem state, a new status log cannot be created until the existing one is resolved.
- The log must record the identity of the user who created it.

### Requirement 2: Camera Status Retrieval

Clients should be able to fetch a list of all cameras along with their latest status.

Example output:

```json
[
    {
        "id": 1,
        "name": "Camera E1",
        "group": "Entrance",
        "status": "Working"
    },
    {
        "id": 2,
        "name": "Camera E2",
        "group": "Entrance",
        "status": "Offline"
    }
]
```

### Requirement 3: Metrics Extraction

The security manager requires metrics on camera issues within specific time frames. Develop reusable code to determine:

- Which camera has experienced the most issues.
- Any cameras that have been offline for more than X minutes.
- The day with the highest number of issues logged.

### Coding Restrictions

You are encouraged to modify and extend this Django application to meet the above requirements. We value solutions that are straightforward, comprehensible, and maintainable. Please be prepared to justify your design and implementation choices.

### Time Limit

While there's no set time limit, we recommend spending approximately 2-3 hours on this test.
