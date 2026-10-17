// Check published formulas with the site's KaTeX version, without a browser.
"use strict";
const fs = require("node:fs");
const [formulasPath, modulePath] = process.argv.slice(2);
if (!formulasPath || !modulePath) {
  throw new Error("Usage: node check_knowledge_math.cjs formulas.json /path/to/katex");
}
const katex = require(modulePath);
if (katex.version !== "0.16.46") {
  throw new Error(`Expected KaTeX 0.16.46, got ${katex.version}`);
}
const formulas = JSON.parse(fs.readFileSync(formulasPath, "utf8"));
const seen = new Set();
for (const formula of formulas) {
  const key = JSON.stringify([formula.tex, formula.display]);
  if (seen.has(key)) continue;
  try {
    katex.renderToString(formula.tex, {
      displayMode: formula.display,
      throwOnError: true,
      strict: "ignore", // Allow Chinese text; TeX parsing errors still throw.
      trust: false,
      maxExpand: 1000,
    });
  } catch (error) {
    throw new Error(`${formula.page}: ${error.message}`);
  }
  seen.add(key);
}
process.stdout.write(JSON.stringify({
  renderer: "KaTeX",
  version: katex.version,
  occurrences_checked: formulas.length,
  distinct_formulas_checked: seen.size,
  browser_used: false,
}) + "\n");
