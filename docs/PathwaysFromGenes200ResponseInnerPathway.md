# PathwaysFromGenes200ResponseInnerPathway


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
from igvf_catalog_client.models.pathways_from_genes200_response_inner_pathway import PathwaysFromGenes200ResponseInnerPathway

# TODO update the JSON string below
json = "{}"
# create an instance of PathwaysFromGenes200ResponseInnerPathway from a JSON string
pathways_from_genes200_response_inner_pathway_instance = PathwaysFromGenes200ResponseInnerPathway.from_json(json)
# print the JSON string representation of the object
print(PathwaysFromGenes200ResponseInnerPathway.to_json())

# convert the object into a dict
pathways_from_genes200_response_inner_pathway_dict = pathways_from_genes200_response_inner_pathway_instance.to_dict()
# create an instance of PathwaysFromGenes200ResponseInnerPathway from a dict
pathways_from_genes200_response_inner_pathway_from_dict = PathwaysFromGenes200ResponseInnerPathway.from_dict(pathways_from_genes200_response_inner_pathway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


