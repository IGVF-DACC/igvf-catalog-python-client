# OntologyTermParents200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | [**OntologyTerm**](OntologyTerm.md) |  | 
**relationship_type** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.ontology_term_parents200_response_inner import OntologyTermParents200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyTermParents200ResponseInner from a JSON string
ontology_term_parents200_response_inner_instance = OntologyTermParents200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(OntologyTermParents200ResponseInner.to_json())

# convert the object into a dict
ontology_term_parents200_response_inner_dict = ontology_term_parents200_response_inner_instance.to_dict()
# create an instance of OntologyTermParents200ResponseInner from a dict
ontology_term_parents200_response_inner_from_dict = OntologyTermParents200ResponseInner.from_dict(ontology_term_parents200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


