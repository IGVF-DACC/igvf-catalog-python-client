# OntologyTermTransitiveClosure200ResponseVerticesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** |  | 
**term_id** | **str** |  | 
**name** | **str** |  | 
**synonyms** | **List[str]** |  | 
**description** | **str** |  | 
**source** | **str** |  | 
**subontology** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.ontology_term_transitive_closure200_response_vertices_value import OntologyTermTransitiveClosure200ResponseVerticesValue

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyTermTransitiveClosure200ResponseVerticesValue from a JSON string
ontology_term_transitive_closure200_response_vertices_value_instance = OntologyTermTransitiveClosure200ResponseVerticesValue.from_json(json)
# print the JSON string representation of the object
print(OntologyTermTransitiveClosure200ResponseVerticesValue.to_json())

# convert the object into a dict
ontology_term_transitive_closure200_response_vertices_value_dict = ontology_term_transitive_closure200_response_vertices_value_instance.to_dict()
# create an instance of OntologyTermTransitiveClosure200ResponseVerticesValue from a dict
ontology_term_transitive_closure200_response_vertices_value_from_dict = OntologyTermTransitiveClosure200ResponseVerticesValue.from_dict(ontology_term_transitive_closure200_response_vertices_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


