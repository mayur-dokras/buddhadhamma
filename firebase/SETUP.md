# Home slider: connecting Firebase

The slider and its admin page (`/#admin`) work without a database, showing six starter cards.
To publish cards for every visitor, connect a free Firebase project (Spark plan, no card needed).

1. Go to console.firebase.google.com and create a project.
2. Build → Firestore Database → Create database (production mode).
3. Firestore → Rules: paste `firebase/firestore.rules`, put your Google email in place of `you@example.com`, Publish.
4. Build → Authentication → Get started → enable the Google provider.
5. Authentication → Settings → Authorized domains: add `mayur-dokras.github.io` and `buddhadhamma.in`.
6. Project settings → Your apps → Web app (</>) → copy the config.
7. Edit `feed_config.js` in the repo root:

```js
window.BD_FIREBASE={apiKey:"...",authDomain:"yourproject.firebaseapp.com",projectId:"yourproject",appId:"...",
  admins:["you@example.com"]};
```

8. Commit. After Pages deploys, open `/#admin`, sign in with Google, press "Add the starter cards" and edit from there.

The web config is not a secret; the Firestore rules are what keep editing limited to your account.
The admin list in `feed_config.js` only decides who sees the editor; the rules decide who can save.
