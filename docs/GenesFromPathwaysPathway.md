# GenesFromPathwaysPathway


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
from igvf_catalog_client.models.genes_from_pathways_pathway import GenesFromPathwaysPathway

# TODO update the JSON string below
json = "{}"
# create an instance of GenesFromPathwaysPathway from a JSON string
genes_from_pathways_pathway_instance = GenesFromPathwaysPathway.from_json(json)
# print the JSON string representation of the object
print(GenesFromPathwaysPathway.to_json())

# convert the object into a dict
genes_from_pathways_pathway_dict = genes_from_pathways_pathway_instance.to_dict()
# create an instance of GenesFromPathwaysPathway from a dict
genes_from_pathways_pathway_from_dict = GenesFromPathwaysPathway.from_dict(genes_from_pathways_pathway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


