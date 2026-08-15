"""Clean up openapi_spec.json before code generation.

- Remove unwanted endpoints (health, autocomplete)
- Fix spec errors (e.g. missing array items schema on /llm-query)
"""

import json
import os

PATHS_TO_REMOVE = ["/health", "/autocomplete"]

spec_path = os.path.join(os.path.dirname(__file__), "..", "openapi_spec.json")

with open(spec_path) as f:
    spec = json.load(f)

# Remove unwanted paths
for path in PATHS_TO_REMOVE:
    if path in spec.get("paths", {}):
        del spec["paths"][path]
        print(f"Removed {path}")
    else:
        print(f"Not found (skipping): {path}")

# Fix /llm-query: aql_result array is missing "items"
llm_query = spec.get("paths", {}).get("/llm-query", {})
aql_result = (
    llm_query
    .get("post", {})
    .get("responses", {})
    .get("200", {})
    .get("content", {})
    .get("application/json", {})
    .get("schema", {})
    .get("properties", {})
    .get("aql_result", {})
)
if aql_result.get("type") == "array" and "items" not in aql_result:
    aql_result["items"] = {}
    print("Fixed /llm-query: added missing items schema to aql_result array")

with open(spec_path, "w") as f:
    json.dump(spec, f, indent=2)
    f.write("\n")

print("Done.")
