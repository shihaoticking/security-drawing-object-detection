# Senior AI/ML Engineer - Take Home Assignment

## Introduction

As a Senior Software Engineer specialized in AI/ML (Computer Vision domain), we expect you to be able to solve ambiguous problems with effective and well thought out solutions, even if you need to solve the problem with new or unfamiliar technologies.

This is an open-ended challenge to test your:
- Technical depth
- Technical experience
- Problem-solving skills
- Adaptability
- Effective communication

### Time Commitment
- Expected time: 2-4 hours
- Additional time is optional and not penalized
- Focus on planning and prioritizing MVP features

### Project Goals
The goal is not to build a full production-ready product, but rather to demonstrate your ability to:
- Take initial steps in project development
- Think and reason about the path from zero to production
- Consider legacy maintenance
- Build using your understanding of Senior Engineer expectations

## Context

Security drawings are detailed plans that outline the security features of a building or facility. These drawings contain the placement of physical security devices like:
- Security cameras
- Alarm systems
- Access control points
- Other security measures

## Goal

Build a prototype that performs object detection on images using computer vision techniques to:
1. Correctly identify doors in security drawings
2. Plot boundary boxes
3. Output results in a structured JSON format detailing detected objects and their locations

## Requirements

### Hard Requirements (MVP Minimum)
1. The MVP must be functional and runnable
2. Code documentation focusing on context (why) rather than implementation details
   - Example: "This uses X because of this particular edge case which might cause race conditions"
   - Not: "The next line uses X"
3. Clear setup and run instructions
4. Documented development assumptions

### Constraints
1. Cannot use existing frameworks/libraries that implement core features completely
   - Example: Cannot use a library that fully achieves the goal and just build a UI wrapper
   - However, frameworks/libraries for non-core features (like YOLO) are allowed
2. No external SaaS APIs/services integration
   - Must run completely locally on your device

## Evaluation Criteria

### 1. Problem-Solving and Planning
- Ability to foresee potential use cases and obstacles
- MVP doesn't need to handle every edge case
- Must document potential obstacles/edge cases in:
  - Code comments
  - Documentation
  - Interview discussion

### 2. Technical Depth
- Ability to work at a deeper technical level than product integration
- Capability to build with lower-level technology if needed
- Understanding of standard libraries and lower-level primitives

### 3. Communication Skills
- Clear and effective communication
- Ability to explain concepts to both technical and non-technical audiences

## Additional Notes

1. Language preference: Python (though any language is acceptable)
2. Be prepared for:
   - Making changes
   - Implementing new features
   - Answering technical questions about your decisions during the follow-up interview
