# DiseasesFromGenes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmids** | **List[str]** |  | [optional] 
**term_name** | **str** |  | [optional] 
**gene_symbol** | **str** |  | [optional] 
**association_type** | **str** |  | [optional] 
**association_status** | **str** |  | [optional] 
**sgc_id** | **str** |  | [optional] 
**hgnc** | **str** |  | [optional] 
**classification** | **str** |  | [optional] 
**moi_id** | **str** |  | [optional] 
**moi_name** | **str** |  | [optional] 
**submitter** | **str** |  | [optional] 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**gene** | [**DiseasesFromGenesGene**](DiseasesFromGenesGene.md) |  | [optional] 
**disease** | [**BiosamplesFromGenomicElementsBiosample**](BiosamplesFromGenomicElementsBiosample.md) |  | [optional] 
**inheritance_mode** | **str** |  | [optional] 
**variants** | [**List[VariantMinimal]**](VariantMinimal.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from igvf_catalog_client.models.diseases_from_genes import DiseasesFromGenes

# TODO update the JSON string below
json = "{}"
# create an instance of DiseasesFromGenes from a JSON string
diseases_from_genes_instance = DiseasesFromGenes.from_json(json)
# print the JSON string representation of the object
print(DiseasesFromGenes.to_json())

# convert the object into a dict
diseases_from_genes_dict = diseases_from_genes_instance.to_dict()
# create an instance of DiseasesFromGenes from a dict
diseases_from_genes_from_dict = DiseasesFromGenes.from_dict(diseases_from_genes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


