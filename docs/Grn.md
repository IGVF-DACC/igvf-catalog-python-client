# Grn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_gene** | **str** |  | 
**genomic_element** | [**GenomicElement4**](GenomicElement4.md) |  | [optional] 
**regulator_gene** | **str** |  | [optional] 
**transcript** | [**GenesTranscriptsGenesTranscript**](GenesTranscriptsGenesTranscript.md) |  | [optional] 
**perturbation** | **str** |  | [optional] 
**var_class** | **str** |  | 
**method** | **str** |  | 
**source** | **str** |  | 
**biological_context** | **str** |  | 
**files_filesets** | **str** |  | 
**log2_fc** | **float** |  | [optional] 
**neg_log10_pvalue** | [**GenesFromGenomicElementsPValue**](GenesFromGenomicElementsPValue.md) |  | [optional] 
**neg_log10_pvalue_adj** | [**GenesFromGenomicElementsPValue**](GenesFromGenomicElementsPValue.md) |  | [optional] 
**significant** | **bool** |  | [optional] 
**p_value** | [**GenesFromGenomicElementsPValue**](GenesFromGenomicElementsPValue.md) |  | [optional] 
**p_value_adj** | [**GenesFromGenomicElementsPValue**](GenesFromGenomicElementsPValue.md) |  | [optional] 
**perturbation_efficiency_log2_fc** | **float** |  | [optional] 
**perturbation_efficiency_neg_log10_pvalue** | [**GenesFromGenomicElementsPValue**](GenesFromGenomicElementsPValue.md) |  | [optional] 
**perturbation_efficiency_neg_log10_pvalue_adj** | [**GenesFromGenomicElementsPValue**](GenesFromGenomicElementsPValue.md) |  | [optional] 
**perturbation_efficiency_significant** | **bool** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.grn import Grn

# TODO update the JSON string below
json = "{}"
# create an instance of Grn from a JSON string
grn_instance = Grn.from_json(json)
# print the JSON string representation of the object
print(Grn.to_json())

# convert the object into a dict
grn_dict = grn_instance.to_dict()
# create an instance of Grn from a dict
grn_from_dict = Grn.from_dict(grn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


