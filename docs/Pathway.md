# Pathway


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**organism** | **str** |  | 
**source** | **str** |  | 
**source_url** | **str** |  | 
**id_version** | **str** |  | 
**is_in_disease** | **bool** |  | 
**name_aliases** | **List[str]** |  | 
**is_top_level_pathway** | **bool** |  | 
**disease_ontology_terms** | **List[str]** |  | 
**go_biological_process** | **str** |  | 
**var_class** | **str** |  | 
**method** | **str** |  | 
**label** | **str** |  | 
**files_filesets** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.pathway import Pathway

# TODO update the JSON string below
json = "{}"
# create an instance of Pathway from a JSON string
pathway_instance = Pathway.from_json(json)
# print the JSON string representation of the object
print(Pathway.to_json())

# convert the object into a dict
pathway_dict = pathway_instance.to_dict()
# create an instance of Pathway from a dict
pathway_from_dict = Pathway.from_dict(pathway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


