# OntologyTermTransitiveClosure200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vertices** | [**Dict[str, OntologyTermTransitiveClosure200ResponseVerticesValue]**](OntologyTermTransitiveClosure200ResponseVerticesValue.md) |  | 
**paths** | **List[List[OntologyTermTransitiveClosure200ResponsePathsInnerInner]]** |  | 

## Example

```python
from igvf_catalog_client.models.ontology_term_transitive_closure200_response import OntologyTermTransitiveClosure200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyTermTransitiveClosure200Response from a JSON string
ontology_term_transitive_closure200_response_instance = OntologyTermTransitiveClosure200Response.from_json(json)
# print the JSON string representation of the object
print(OntologyTermTransitiveClosure200Response.to_json())

# convert the object into a dict
ontology_term_transitive_closure200_response_dict = ontology_term_transitive_closure200_response_instance.to_dict()
# create an instance of OntologyTermTransitiveClosure200Response from a dict
ontology_term_transitive_closure200_response_from_dict = OntologyTermTransitiveClosure200Response.from_dict(ontology_term_transitive_closure200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


