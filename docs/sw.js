// Service worker: saves the key on the device so it works with no signal.
// Bump VERSION whenever you publish new data or code, so phones fetch the update.
const VERSION = "core-v13";
const CORE = [
  "./",
  "index.html",
  "manifest.webmanifest",
  "data/species.json",
  "data/packs.json",
  "icons/icon-192.png",
  "icons/icon-512.png",
];

self.addEventListener("install", (e) => {
  // cache: "reload" skips the browser's HTTP cache, so a new version never saves a stale copy of the page.
  e.waitUntil(caches.open(VERSION).then((c) => c.addAll(CORE.map((u) => new Request(u, { cache: "reload" })))).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (e) => {
  // Remove old copies of the core files; photo packs ("photos-…") are kept.
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k.startsWith("core-") && k !== VERSION).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);

  // Species data and the page: try the network first so updates arrive, fall back to the saved copy offline.
  if (url.origin === location.origin && (url.pathname.endsWith("species.json") || req.mode === "navigate")) {
    e.respondWith(
      fetch(req, { cache: "no-cache" })
        .then((res) => { const copy = res.clone(); caches.open(VERSION).then((c) => c.put(req, copy)); return res; })
        .catch(() => caches.match(req).then((r) => r || caches.match("index.html")))
    );
    return;
  }

  // Everything else (icons, fonts, photos): use the saved copy if there is one.
  e.respondWith(
    caches.match(req).then((hit) => hit || fetch(req).then((res) => {
      if (res.ok && (url.origin === location.origin || url.hostname.endsWith("gstatic.com") || url.hostname.endsWith("googleapis.com"))) {
        const copy = res.clone(); caches.open(VERSION).then((c) => c.put(req, copy));
      }
      return res;
    }))
  );
});
