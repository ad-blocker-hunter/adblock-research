# Analysis of `config-decoded.json`

This document provides an analysis of the decoded configuration file for the `intent.ly` (Smarter Click) tracking scripts running on `demo.smarterclick.co.uk`.

## Overview

This JSON file contains the master configuration for the entire tracking and overlay system. It dictates which rules are active, what triggers them, which overlays are displayed, and how various plugins behave. It's the "brain" of the operation.

## Key Sections

### 1. `config` - Global Settings

This section defines global behavior for the tag.

*   `jQueryForceLoad`: `0` - It won't force-load its own version of jQuery if one is already present.
*   `ignoreHash`: `1` - URL hashes (`#`) are ignored when matching URLs for rules.
*   `encodeCookies`: `1` - Cookie values are encoded.
*   `dynamicElements`: This is a crucial part. It defines how the script should find and extract key pieces of data from the page. For the demo site, it's configured to find:
    *   `BasketValue`: Using the CSS selector `#cart-total`.
    *   `ConfirmationPage`: By checking if the URL contains `/confirmed.php`.
    *   `OrderId`: Using the CSS selector `#order-id`.
    *   `Currency`, `BasketCount`, `ObjectKey`: These are configured to read from custom JavaScript functions (`readCustomVarOrFunc`), showing the system's flexibility.
*   `webpush_key`: `BJXh...` - A public key for web push notifications, indicating they use this functionality.

### 2. `rulesList` - The Rule Engine

This is the most important section. It's an array of "rules," where each rule defines a scenario for triggering an overlay. The script iterates through this list, and the first rule that matches the user's context (URL, device, etc.) is executed.

Here are some example rules from the list:

*   **Rule: "Phone Down Test"**
    *   **Triggers:** This rule is generic and applies to all pages and visitors.
    *   **Action:** It will show overlay with ID `29572` on desktop, mobile, and tablet. This overlay is likely configured with the "Phone Down" trigger we saw in `overlays-v6.07.js`.

*   **Rule: "Remail Consent Overlays (Desktop and Mobile)"**
    *   **Triggers:** This rule is active only when the URL contains `/cart.php` or `/checkout.php`.
    *   **Action:** Shows overlay `8008` on desktop and `8009` on mobile/tablet. This is a classic cart abandonment prevention strategy.

*   **Rule: "Click To Reveal"**
    *   **Triggers:** Activates when the URL contains `click-to-reveal`.
    *   **Action:** Shows overlay `35` on desktop. This is for demonstrating a "click to get the code" feature.

*   **Rule: "v5.12 - Request Notifications"**
    *   **Triggers:** Activates when the URL contains `request-notifications` and the user has not already accepted or denied push notifications (`"notificationsAccepted": "not_set"`).
    *   **Action:** Shows overlay `6874` to prompt the user to subscribe to push notifications.

*   **Rule: "BB Referrer Test"**
    *   **Triggers:** This rule activates if the user's referring URL matches a specific pattern (ID `372`, which corresponds to the cookie `smc_bbeid`). This is likely a test for tracking users coming from a specific campaign or affiliate.
    *   **Action:** Shows overlay `2774`.

The list is extensive and contains many demo rules that are activated by specific query parameters in the URL (e.g., `?envolve`, `?refer`, `?social`), allowing their sales team to demonstrate different overlay types to potential clients.

### 3. `plugins` - Additional Functionalities

This section configures other scripts that can be loaded.

*   `autoInsert`: This plugin can automatically insert a value (likely a voucher code) into a form field. Here, it's configured to target the input `#promocode` on `cart.php`.
*   `tracking`: Configures conversion tracking. It uses the `dynamicElements` we saw earlier (`ConfirmationPage`, `BasketValue`, `OrderId`) to identify when a conversion happens and record its value.
*   `basketBackup`: Has an ID of `55`. This likely corresponds to a configuration for the `basket_backup_script` mentioned in the loader, used to save and restore a user's shopping cart.
*   `smarterCodes`: Has an ID of `152`. This is for the Smarter Codes feature, which probably involves advanced voucher code logic.
*   `notifications`: Defines the path to the service worker (`/assets/js/service-worker.js`) used for push notifications.

## Conclusion

The `config-decoded.json` file provides a clear blueprint of how `intent.ly` operates on this demo site. It reveals a powerful and highly flexible rule engine that allows them to target users with specific overlays based on a wide variety of conditions, including URL, device, location, and referral source.

The configuration confirms that the primary purpose is to drive engagement and conversions through overlays, with a heavy focus on cart abandonment, email capture, and push notification subscriptions. The presence of numerous demo rules triggered by URL parameters shows that this is a showcase of their capabilities for potential customers.
