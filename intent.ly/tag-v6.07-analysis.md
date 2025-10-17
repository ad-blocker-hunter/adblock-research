# Analysis of `tag-v6.07.js`

This document provides an analysis of the `tag-v6.07.js` script, which is the core tracking and overlay engine for the Intent.ly (formerly Smarter Click) service.

### Summary

This script is a comprehensive user tracking and behavior analysis engine. Its primary purpose is to monitor user activity on a website, match that activity against a set of predefined rules, and trigger marketing interventions (overlays) to influence user behavior, typically to prevent them from leaving the site or to encourage a purchase.

---

### Core Functionalities

#### 1. Data Storage and User Identification

*   **Persistent User ID (`smc_uid`):** The script assigns a unique and persistent ID to each user, stored in cookies or local storage. This allows Intent.ly to track the same user across multiple sessions and potentially across different websites using their service.
*   **Cookie and Local Storage Management:** It features a robust system for storing data on the user's device. It creates numerous data points, including:
    *   `smct_session`: Tracks the current session, including start time, last active time, and time spent on the page.
    *   `smc_spv`, `smc_tpv`: Counts session page views and total page views, respectively.
    *   `smc_r`: Stores the referring domain.
    *   `smct_last_ov`: Keeps a history of the last few overlays shown to the user.
*   **Local Storage Migration:** The script includes logic to migrate its data from cookies to the browser's local storage, which can be more persistent and hold more data.

#### 2. Device and Browser Fingerprinting

*   The script performs detailed device detection to create a profile of the user's system.
*   **Data Points Collected:**
    *   Operating System (e.g., Windows 10, iOS, Android)
    *   Browser (e.g., Chrome, Safari, Firefox)
    *   Device Type (desktop, mobile, tablet)
    *   Screen dimensions and browser viewport size.
    *   User agent string.
    *   Presence of touch capabilities (`ontouchstart`).

#### 3. Continuous Page Scanning and Data Extraction

*   **Dynamic Data Keys:** The script is configured to continuously scan the page for specific pieces of information ("Dynamic Keys"). This is highly customizable.
*   **Data Extraction Methods:**
    *   Reading text or HTML from elements specified by CSS selectors.
    *   Getting the value of form inputs.
    *   Searching the page's JavaScript `dataLayer` object, which is a standard for analytics tools.
    *   Checking for the presence of specific text anywhere in the page's HTML.
    *   Checking for specific strings in the current URL.
*   **E-commerce Focus:** It is specifically configured to look for e-commerce data, such as basket value, order ID, product details, and confirmation page identifiers.

#### 4. Rule Engine and Overlay Triggering

*   This is the script's central logic. It runs in a loop (every 100-300ms), comparing all the data it has collected against a `rulesList`.
*   **Rule Conditions:** A rule can be triggered based on a combination of many factors, including:
    *   **URL Matching:** Is the user on a specific page (e.g., the checkout)?
    *   **Referrer Matching:** Did the user come from a specific site (e.g., a partner blog)?
    *   **Location:** Is the user in a specific country?
    *   **User State:** Is the user new or returning? Have they viewed more than a certain number of pages?
    *   **Basket Contents:** Is the basket value over a certain amount?
    *   **Time-based:** Only show an overlay during a specific date/time range.
*   When a rule's conditions are met, the script triggers the loading of a specific overlay.

#### 5. Event and Pixel Tracking

*   **Behavioral Tracking:** The script sends data back to Intent.ly's servers at key moments. This is often referred to as "pixel tracking."
*   **Tracked Events:**
    *   When an overlay is shown, engaged with, or closed.
    *   When a user completes a purchase (a "goal" or "conversion").
    *   "Machine Learning" events that send a bundle of data about the user's session, likely for building predictive models.
*   **IP-based Geolocation:** The script makes calls to an external service (`ipl.smct.co`) to get the user's approximate geographical location based on their IP address.

---

### Potential Privacy and User Experience Concerns

*   **Extensive Fingerprinting:** The detailed collection of device and browser information is a form of fingerprinting, which can be used to identify users even if they clear their cookies.
*   **Persistent Cross-Session Tracking:** The use of a persistent `smc_uid` allows for long-term tracking of an individual's browsing habits on any site using this script.
*   **Intrusive Data Collection:** The script has the ability to read a wide array of information from the page, including the contents of the shopping basket. This data is then sent to third-party servers.
*   **Behavioral Profiling:** The "machine learning" component explicitly sends behavioral data for analysis, contributing to a detailed profile of the user's shopping habits and preferences.
*   **Resource Usage:** The script runs in a constant loop, repeatedly scanning the page. While it appears to have some optimizations (e.g., pausing when the tab is not active), this can still contribute to CPU usage and battery drain on the user's device.
