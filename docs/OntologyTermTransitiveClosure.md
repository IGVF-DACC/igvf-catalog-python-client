# OntologyTermTransitiveClosure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vertices** | [**Dict[str, OntologyTermBasic]**](OntologyTermBasic.md) |  | 
**paths** | **List[List[Paths]]** |  | 

## Example

```python
from igvf_catalog_client.models.ontology_term_transitive_closure import OntologyTermTransitiveClosure

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyTermTransitiveClosure from a JSON string
ontology_term_transitive_closure_instance = OntologyTermTransitiveClosure.from_json(json)
# print the JSON string representation of the object
print(OntologyTermTransitiveClosure.to_json())

# convert the object into a dict
ontology_term_transitive_closure_dict = ontology_term_transitive_closure_instance.to_dict()
# create an instance of OntologyTermTransitiveClosure from a dict
ontology_term_transitive_closure_from_dict = OntologyTermTransitiveClosure.from_dict(ontology_term_transitive_closure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


