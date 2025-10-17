# Intent.ly (formerly Smarter Click)

## Company Overview

Intent.ly is a technology company focused on shopper journey optimization for e-commerce websites. The company was previously known as **Smarter Click**.

They provide a suite of tools and managed services designed to increase onsite conversions, customer engagement, and overall sales for online retailers.

## Services and Technology

Intent.ly's platform is described as a "performance-based shopper journey optimisation platform." Their core offerings include:

*   **Targeted Overlays:** These are dynamic, personalized messages shown to website visitors to encourage specific actions, such as completing a purchase or signing up for a newsletter.
*   **Email Remarketing:** Systems to capture and re-engage users who have left the site without converting.
*   **In-page Campaigns:** Promotional messages and campaigns embedded directly within the content of the site.
*   **Analytics and Insights:** They provide data and analytics on shopper behavior to help optimize campaigns.

## Business Model

Intent.ly operates on a performance-based model, often referred to as Cost Per Acquisition (CPA). This means clients are charged based on the conversions or sales generated through Intent.ly's services. They market themselves as a "managed SaaS" solution, providing not just the technology but also account management and expertise to run and optimize the campaigns.

## Integrations

The platform is designed to integrate with various e-commerce and marketing tools, including:
*   Affiliate Networks
*   Google Tag Manager
*   Shopify
*   Other API-based integrations

## Analysis Summary

Based on the analysis of the various JavaScript files and configuration, here is a summary of the findings regarding Intent.ly's tracking and overlay technology.

### Core Functionality

The system is composed of several key scripts:

1.  **Loader Script (`tm-demo.smarterclick.co.uk.js`):** This is the initial entry point. It loads the main configuration and dynamically injects the core tracking and overlay scripts into the page. It defines endpoints for data collection and sets up site-specific configurations.
2.  **Core Tracking Engine (`tag-v6.07.js`):** This is the heart of the tracking system. It assigns a persistent unique ID to each user, performs device and browser fingerprinting, and continuously scans the webpage for data (like shopping cart value). It contains a powerful rule engine that matches user behavior against a list of rules to decide when to act.
3.  **Overlay Engine (`overlays-v6.07.js`):** This script is responsible for displaying all marketing interventions. It contains a vast library of triggers to decide *when* to show an overlay, including exit intent, scroll speed, inactivity, and even detecting when a user puts their phone down.
4.  **Configuration (`config-decoded.json`):** This is the "brain" that dictates the behavior of the other scripts. It contains the specific rules, overlay content, and data extraction definitions for a particular website.

### Key Behaviors and Privacy Concerns

*   **Persistent User Tracking:** Assigns a unique ID (`smc_uid`) to users, allowing for long-term, cross-session tracking of their browsing habits on any site using the service.
*   **Device Fingerprinting:** Collects a detailed profile of the user's device, including OS, browser, screen dimensions, and user agent, which can be used for identification even if cookies are cleared.
*   **Intrusive Overlay Triggers:** The system is designed to interrupt the user's journey at critical moments using aggressive techniques like:
    *   **Exit Intent:** Detecting when the mouse moves towards the close button.
    *   **Back-Button Hijacking:** Manipulating browser history to trigger an overlay when the user tries to go back.
    *   **Tab Inactivity:** Changing the page title or showing a prompt to lure the user back to an inactive tab.
    *   **Device Motion:** Using gyroscope and device orientation data, for example, to detect when a phone is placed face-down.
*   **Extensive Data Collection:** The scripts continuously monitor and collect a wide range of data, including:
    *   Shopping cart contents (value, items).
    *   User-submitted form data (e.g., email addresses).
    *   User's physical location via IP-based geolocation and `navigator.geolocation` requests.
    *   Interactions with the page, such as scroll speed and copied text.
*   **Behavioral Profiling:** The collected data is sent to Intent.ly's servers, including for "machine learning" purposes, to build detailed profiles of user shopping habits and predict future behavior.
*   **Resource Usage:** The constant page scanning and event monitoring can contribute to increased CPU usage and battery drain on user devices.

### Conclusion

The Intent.ly (Smarter Click) platform is a sophisticated and aggressive marketing tool designed to maximize e-commerce conversions. While effective from a marketing perspective, it achieves its goals through highly intrusive tracking, extensive data collection, and user experience patterns that many would consider annoying or a violation of privacy. The technology is a prime candidate for blocking by privacy-focused tools.
