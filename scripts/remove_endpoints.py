"""Remove unwanted endpoints from openapi_spec.json before code generation."""

import json
import os

PATHS_TO_REMOVE = ["/health", "/autocomplete", "/llm-query"]

spec_path = os.path.join(os.path.dirname(__file__), "..", "openapi_spec.json")

with open(spec_path) as f:
    spec = json.load(f)

for path in PATHS_TO_REMOVE:
    if path in spec.get("paths", {}):
        del spec["paths"][path]
        print(f"Removed {path}")
    else:
        print(f"Not found (skipping): {path}")

with open(spec_path, "w") as f:
    json.dump(spec, f, indent=2)
    f.write("\n")

print("Done.")
