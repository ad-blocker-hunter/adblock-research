# Analysis of overlays-v6.07.js

This document provides an analysis of the `overlays-v6.07.js` script from Smarter Click (intent.ly).

## Overview

This script is responsible for managing and displaying various types of overlays on a client's website. These overlays can be pop-ups, banners, side panels, or full-screen takeovers. The script contains a wide range of triggers, targeting rules, and engagement tracking functionalities. It is a sophisticated piece of code designed to maximize user engagement and conversion, often through intrusive means.

## Core Functionality

The script's main object is `$smcO5`. It orchestrates the entire process of loading, configuring, triggering, and displaying overlays.

### 1. Overlay Triggers

The script can trigger overlays based on a vast array of user behaviors and conditions. This is the primary mechanism for deciding *when* to show an overlay. Key triggers include:

*   **Exit Intent (`heatmapping`, `page_close`):** This is a major feature. The script monitors mouse movement to detect when a user is about to leave the page (e.g., moving the mouse towards the close button). It can detect this through `mouseout` events on the document.
*   **Timer (`timer`):** An overlay can be displayed after a specific amount of time has passed since the page loaded.
*   **Page Scroll (`scroll_speed`, `viewed_element`):**
    *   It can trigger an overlay based on how fast the user is scrolling up or down the page.
    *   It can also trigger when a user has viewed a specific element (defined by a CSS selector) for a certain duration.
*   **Page Count (`page_count`):** Displays an overlay after the user has visited a specific number of pages in their session.
*   **Back Button Detection (`back_button_display`):** The script uses multiple techniques (including manipulating browser history with `history.pushState`) to detect when the user clicks the back button, allowing it to trigger an overlay at that moment.
*   **Tab Inactivity (`in_active_tab`, `tab_switch`):**
    *   If the user switches to another tab and leaves the page inactive for a period, the script can change the page's title (favicon) to a custom message to draw them back.
    *   It can also trigger a `confirm()` dialog box or an overlay when the user switches away from the tab.
*   **Input Activation (`input_activate`):** An overlay can be shown or canceled based on what a user types into a specific form field (e.g., an email input). It can use regex to match the input.
*   **Copying Text (`copying_activate`):** Triggers an overlay if a user copies text from a specified element on the page.
*   **Phone Down Detection (`phone_down`):** On mobile devices, it uses the `deviceorientation` API to detect if the phone has been placed face-down or is stationary for a period, and can trigger an overlay based on this.
*   **Inactivity Timer (`inactivity_timer`):** If the user is inactive (no mouse or touch movement) for a set duration, an overlay is displayed.
*   **Geolocation (`closest_store`):** The script can request the user's geolocation to find the nearest physical store and display customized content or offers. It uses the `navigator.geolocation` API.

### 2. Overlay Types & Content

The script supports various overlay formats:

*   **Standard Modal:** A typical centered pop-up.
*   **Side Panel:** A panel that slides in from the left or right.
*   **Strip/Bar:** A banner at the top or bottom of the page.
*   **Dynamic Content:** The content of the overlays is highly dynamic. It can include:
    *   Forms (e.g., for email capture).
    *   Voucher codes (`clickToReveal`, `emailToReveal`).
    *   Redirect links.
    *   Dynamic product information from the user's basket (`dynamicBasket`).
    *   Product recommendations (`recomminder`).
    *   Video content.
    *   Push notification subscription prompts (`requestNotifications`).

### 3. Data Collection and Tracking

The script is deeply integrated with Smarter Click's tracking infrastructure.

*   **Engagement Tracking:** It logs every significant interaction with an overlay:
    *   `loaded`: When an overlay's configuration is loaded.
    *   `shown`: When an overlay is displayed to the user.
    *   `engaged`: When the user interacts with the overlay (clicks a button, fills a form).
    *   `closed`: When the overlay is closed.
*   **Form Data:** Any data submitted through forms in an overlay is sent to Smarter Click's servers (`ep.smct.co`).
*   **Cookie Management:** It sets persistent cookies (`smc_v4_{overlayId}`) to track the user's interaction history with overlays. This is used to decide whether to show an overlay again, based on rules like "don't show for X days after closing" or "don't show for Y days after engaging."
*   **Pixel Tracking:** It fires tracking pixels for various events, sending data back to the home servers.
*   **Dynamic Code Generation (`dc.smct.co`):** For unique voucher codes, it communicates with a "Dynamic Codes" service to reserve and decrypt single-use codes for the user, tracking their usage.

### 4. Privacy Concerns

*   **Aggressive Triggering:** The sheer number of triggers, especially exit-intent, back-button hijacking, and inactivity timers, can lead to a very intrusive user experience. The goal is to interrupt the user's journey to present an offer.
*   **Browser History Manipulation:** The use of `history.pushState` and `history.replaceState` to detect the back button is a form of history manipulation that can be confusing and frustrating for users.
*   **Extensive User Behavior Monitoring:** The script constantly monitors detailed user actions like scroll speed, mouse position, tab focus, device orientation, and form inputs. This is a significant amount of behavioral data being collected.
*   **Geolocation Request:** While it requires user permission, the `closest_store` feature prompts for the user's precise physical location.
*   **Persistent Tracking:** The use of long-lasting cookies ensures that users are tracked across sessions for extended periods (up to 525,600 minutes, or 1 year).

## Conclusion

`overlays-v6.07.js` is a powerful and complex script that provides Smarter Click's clients with a comprehensive toolkit for displaying targeted, behavior-driven overlays. While designed to increase conversions, its methods are often aggressive and raise significant privacy concerns due to the extensive monitoring of user behavior and the intrusive nature of its triggers. It is a prime example of the kind of script that ad and tracker blockers aim to neutralize to improve user experience and protect privacy.
