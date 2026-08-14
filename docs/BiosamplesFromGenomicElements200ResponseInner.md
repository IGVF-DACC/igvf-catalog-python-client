# BiosamplesFromGenomicElements200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log2_fc** | **float** |  | 
**strand** | **str** |  | 
**neg_log10_pvalue** | **float** |  | 
**neg_log10_pvalue_adj** | **float** |  | 
**dna_count** | **float** |  | [optional] 
**rna_count** | **float** |  | [optional] 
**significant** | **bool** |  | [optional] 
**source** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**genomic_element** | [**BiosamplesFromGenomicElements200ResponseInnerGenomicElement**](BiosamplesFromGenomicElements200ResponseInnerGenomicElement.md) |  | [optional] 
**biosample** | [**DiseaseFromVariants200ResponseInnerDisease**](DiseaseFromVariants200ResponseInnerDisease.md) |  | [optional] 
**name** | **str** |  | 
**var_class** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.biosamples_from_genomic_elements200_response_inner import BiosamplesFromGenomicElements200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of BiosamplesFromGenomicElements200ResponseInner from a JSON string
biosamples_from_genomic_elements200_response_inner_instance = BiosamplesFromGenomicElements200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(BiosamplesFromGenomicElements200ResponseInner.to_json())

# convert the object into a dict
biosamples_from_genomic_elements200_response_inner_dict = biosamples_from_genomic_elements200_response_inner_instance.to_dict()
# create an instance of BiosamplesFromGenomicElements200ResponseInner from a dict
biosamples_from_genomic_elements200_response_inner_from_dict = BiosamplesFromGenomicElements200ResponseInner.from_dict(biosamples_from_genomic_elements200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


