# Analysis of `tm-demo.smarterclick.co.uk.js`

This document provides an analysis of the script loaded from `https://smct.co/tm/?t=demo.smarterclick.co.uk`.

### Summary

This script is a configuration and loader for the main Intent.ly tracking functionality. It is not the full tracking script itself but sets up the environment for it by defining resource URLs, loading configuration data, and preparing to load the core tracking and overlay scripts.

---

### Key Components

#### 1. Resource URLs (`$smctResources`)
This object defines a large number of URLs for loading additional JavaScript files and for sending data to various endpoints.
*   **Core Logic:** It sets the stage to load the main tracking script from `https://js.smct.io/t/tag-v6.07.js` and the overlay logic from `https://js.smct.io/o/overlays-v6.07.js`.
*   **Endpoints:** It contains numerous endpoints for features like:
    *   `basket_backup_endpoint`: `https://ep.smct.co/bb-ep/`
    *   `insights_url`: `https://ep.smct.co/insights/`
    *   `url_track`: `https://ep.smct.co/ut/`
    *   `smarter_codes_endpoint`: `https://ep.smct.co/smcdz-ep/`

#### 2. Configuration Data (`$smctData`)
This object contains the specific settings for the `demo.smarterclick.co.uk` website.
*   **Base64 Encoded Rules:** A large part of the configuration is a Base64 encoded string. When decoded, this string reveals the rules that determine when and how to show overlays (pop-ups, banners, etc.). These rules can be based on the user's URL, location, referring site, and other factors.
*   **Dynamic Element Selectors:** It defines CSS selectors to find key e-commerce elements on the page, allowing the script to read their contents. Examples for this site include:
    *   **Basket Value:** `#cart-total`
    *   **Order ID:** `#order-id`
    *   **Confirmation Page:** URLs containing `/confirmed.php`

#### 3. Functionality and Behavior
*   **Dynamic Script Loading:** The script's primary job is to load other scripts. It includes logic to test for Content Security Policy (CSP) issues and dynamically choose between `smct.co` and `smct.io` domains for loading resources, likely for redundancy or to bypass certain network blocks.
*   **Custom Scripts:** It includes a section for custom JavaScript code to be run on the page. In this specific script, it contains:
    *   Logic to handle voucher code input on the demo site.
    *   A call to `Notification.requestPermission()`, which triggers the browser to ask the user for permission to show push notifications.
    *   Code that initializes and reads data from the device's `Gyroscope`.
    *   Functions for "claiming" and checking the availability of dynamic voucher codes from their servers.
    *   Basket tracking logic that listens for clicks on "add to cart" buttons and syncs the contents of the shopping cart with its own internal representation.
*   **Event Tracking:** The script sets up listeners for overlay events (`smc_overlay_loaded`, `smc_overlay_shown`, `smc_overlay_engaged`, `smc_overlay_closed`) and dispatches its own custom events (`intently_overlay_event`) that other scripts on the page could listen to.

---

### Potential Privacy and User Experience Concerns

*   **Device Motion and Orientation:** The script accesses `Gyroscope` data. While this can be used for interactive animations, it can also be a component of a device fingerprinting strategy to uniquely identify a user's device.
*   **Proactive Push Notification Request:** The script programmatically requests permission for push notifications without direct user interaction (like clicking a button to subscribe). This can be an intrusive and unwelcome request for many users.
*   **Extensive Tracking Infrastructure:** The sheer number of endpoints for tracking different user actions (page views, basket contents, engagement with overlays) indicates a comprehensive and detailed user tracking system.
*   **Basket Backup:** The "basket backup" feature implies that the contents of a user's shopping cart are being sent to and stored on Intent.ly's servers, which may happen without the user's explicit knowledge or consent.
