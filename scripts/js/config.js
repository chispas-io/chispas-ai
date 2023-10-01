const ENTRIES = [
  "main.js",
]

module.exports = {
  entryPoints: ENTRIES.map((entry) => `chispas/javascripts/${entry}`),
  outdir: "chispas/javascripts/dist",
  bundle: true,
  loader: {".js": "jsx"},
}
