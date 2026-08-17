# OntologyTerm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** |  | 
**term_id** | **str** |  | 
**name** | **str** |  | 
**synonyms** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**subontology** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.ontology_term import OntologyTerm

# TODO update the JSON string below
json = "{}"
# create an instance of OntologyTerm from a JSON string
ontology_term_instance = OntologyTerm.from_json(json)
# print the JSON string representation of the object
print(OntologyTerm.to_json())

# convert the object into a dict
ontology_term_dict = ontology_term_instance.to_dict()
# create an instance of OntologyTerm from a dict
ontology_term_from_dict = OntologyTerm.from_dict(ontology_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


