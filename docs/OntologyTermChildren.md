# OntologyTermChildren


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | [**OntologyTerm**](OntologyTerm.md) |  | 
**relationship_type** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.ontology_term_children import OntologyTermChildren

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyTermChildren from a JSON string
ontology_term_children_instance = OntologyTermChildren.from_json(json)
# print the JSON string representation of the object
print(OntologyTermChildren.to_json())

# convert the object into a dict
ontology_term_children_dict = ontology_term_children_instance.to_dict()
# create an instance of OntologyTermChildren from a dict
ontology_term_children_from_dict = OntologyTermChildren.from_dict(ontology_term_children_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


