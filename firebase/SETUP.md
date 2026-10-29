# Accounts, enrolment and the admin page

The site connects to the Firebase project set in `feed_config.js`.

## One-time setup in the Firebase console
1. Firestore Database: created in production mode (asia-south1).
2. Firestore → Rules: paste `firebase/firestore.rules` and Publish. Paste again whenever this file changes.
3. Authentication → Sign-in method: Email/Password enabled.
4. Authentication → Settings → Authorized domains: `mayur-dokras.github.io` (add your own domain later).

## Make yourself admin
1. On the site, Join for updates with your email and a password, and open the verification link.
2. Firebase console → Authentication → Users: copy your User UID.
3. Firestore → Start collection `admins` → Document ID = your UID → field `role` (string) = `admin` → Save.
4. Reload the site. The account menu now shows Admin, and `/#admin` lets you edit the slider,
   publish courses, approve experts and download the members list.

## How it works
- Members and experts sign up with email and password and must open the verification link before they can continue.
- Experts create courses and add YouTube lessons (one per line: `title | link`). Courses go live when an admin publishes them.
- Learners enrol after signing in. Lessons unlock only for enrolled learners.
