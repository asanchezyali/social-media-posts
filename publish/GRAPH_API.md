# Instagram Graph API — one-time setup

The default publisher uses Instagram's **official Content Publishing API**. It is
ToS-compliant and does not get blocked the way the private API (instagrapi) does.
The trade-off is a one-time setup that gives you two secrets for `.env`:

```
IG_USER_ID=17841400000000000        # your IG Business/Creator account id
IG_ACCESS_TOKEN=EAAG...             # long-lived token with content publishing
```

There are two products that both work with this tool (same endpoints, different
host). Pick one:

- **A. Instagram API with Instagram Login** (recommended, no Facebook Page) —
  host `graph.instagram.com`, `IG_USER_ID=me`. This is the flow with
  *Add accounts → Generate token → Webhooks*.
- **B. Instagram Graph API via Facebook Login** — host `graph.facebook.com`,
  needs a Facebook Page, numeric `IG_USER_ID`. Set
  `GRAPH_BASE_URL=https://graph.facebook.com/v21.0`.

---

## Route A — Instagram API with Instagram Login (recommended)

1. **Make @yalixyz Business/Creator** (IG app → Settings → *Account type and
   tools* → professional). Free.
2. **Create a Meta app** (developers.facebook.com/apps) and add the
   **Instagram** product → *"Instagram API with Instagram login"* / *API setup*.
3. **Add @yalixyz as an Instagram Tester** — API setup step **"1. Add accounts"**
   (a.k.a. "assign the Instagram Tester role"). Enter `yalixyz`, send the invite.
4. **Accept the invite as @yalixyz**: Instagram app → **Settings → Apps and
   websites → Tester invites → Accept** (or instagram.com → *Apps and websites*).
   > If you skip this you get **"Insufficient Developer Role"** when authorizing.
5. **Generate the token** — API setup step **"2. Generate token"** → log in as
   @yalixyz, approve `instagram_business_basic` + `instagram_business_content_publish`.
   Copy the token → `.env` as `IG_ACCESS_TOKEN`. Leave `IG_USER_ID=me`.
6. Done — the tool defaults to this route.

You can lengthen the token later (Instagram Login tokens are exchangeable for a
~60-day long-lived token via `GET graph.instagram.com/access_token?
grant_type=ig_exchange_token&client_secret=...&access_token=...`).

---

## Route B — Instagram Graph API via Facebook Login

Content publishing works for a **Business/Creator** account linked to a
**Facebook Page**. Set `GRAPH_BASE_URL=https://graph.facebook.com/v21.0`.

### Steps

1. **Make @yalixyz a Business/Creator account.**
   Instagram app → Settings → *Account type and tools* → *Switch to professional
   account* → Business (or Creator). Free.

2. **Link it to a Facebook Page.**
   Create a Facebook Page (facebook.com/pages/create) if you don't have one, then
   in the IG app: Settings → *Business tools and controls* → connect the Page.

3. **Create a Meta app.**
   Go to <https://developers.facebook.com/apps> → *Create app* → use case
   **"Other"** → type **Business**. Then add the **Instagram** product
   (Instagram Graph API / Instagram API with Instagram Login).

4. **Get a User access token with the right scopes.**
   Open the **Graph API Explorer** (<https://developers.facebook.com/tools/explorer>),
   pick your app, and *Generate access token* granting:
   `instagram_basic`, `instagram_content_publish`, `pages_show_list`,
   `pages_read_engagement`, `business_management`.
   (Publishing to *your own* account works in the app's Development mode — no App
   Review needed while you're the only user.)

5. **Find your IG Business account id (`IG_USER_ID`).**
   In the Graph API Explorer run:
   - `GET /me/accounts` → note your Page's `id`.
   - `GET /{page-id}?fields=instagram_business_account` → the returned
     `instagram_business_account.id` is your **IG_USER_ID**.

6. **Exchange for a long-lived token (~60 days).**
   ```
   GET https://graph.facebook.com/v21.0/oauth/access_token
       ?grant_type=fb_exchange_token
       &client_id={app-id}
       &client_secret={app-secret}
       &fb_exchange_token={short-lived-token}
   ```
   Put the returned token in `.env` as `IG_ACCESS_TOKEN`. (Re-run this before it
   expires; you can automate refresh later.)

## Publish

```
uv run publish post Instagram/MatematicasParaML/SistemasLineales            # dry run
uv run publish post Instagram/MatematicasParaML/SistemasLineales --publish   # go live
```

By default the slides are uploaded to **catbox.moe** to get the public URLs the
Graph API fetches. To host them yourself instead (e.g. via this public repo's
raw files, or your own site), set `IMAGE_BASE_URL` in `.env` and make the slide
files reachable at `"$IMAGE_BASE_URL/<path from repo root>"`.

## Notes / limits

- A carousel needs **2–10 images** (our posts qualify).
- Content publishing is rate-limited to **~50 posts / 24 h** per account.
- Captions ≤ 2200 chars (the tool checks this on the instagrapi path; keep the
  Graph caption within the same limit).
