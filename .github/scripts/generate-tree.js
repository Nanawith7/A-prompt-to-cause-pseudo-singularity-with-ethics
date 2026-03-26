const fs = require("fs");
const path = require("path");
const yaml = require("js-yaml");

const ROOT = "docs/hypotheses";

function walk(dir) {
  const result = {};

  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      result[entry.name] = walk(full);
    } else if (entry.isFile() && entry.name.endsWith(".md")) {
      const url = full.replace("docs/", "").replace(".md", ".html");
      const title = entry.name.replace(".md", "").replace(/_/g, " ");

      if (!result._files) result._files = [];
      result._files.push({ title, url });
    }
  }

  return result;
}

const tree = walk(ROOT);

const yamlText = yaml.dump(tree, { lineWidth: -1 });

fs.writeFileSync("_data/tree.yml", yamlText);

console.log("Generated _data/tree.yml");
