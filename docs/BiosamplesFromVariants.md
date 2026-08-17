# BiosamplesFromVariants


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant** | [**BiosamplesFromVariantsVariant**](BiosamplesFromVariantsVariant.md) |  | [optional] 
**biosample** | [**BiosamplesFromGenomicElementsBiosample**](BiosamplesFromGenomicElementsBiosample.md) |  | [optional] 
**genomic_element** | [**BiosamplesFromVariantsGenomicElement**](BiosamplesFromVariantsGenomicElement.md) |  | [optional] 
**strand** | **str** |  | [optional] 
**log2_fc** | **float** |  | [optional] 
**dna_count_ref** | **float** |  | [optional] 
**dna_count_alt** | **float** |  | [optional] 
**rna_count_ref** | **float** |  | [optional] 
**rna_count_alt** | **float** |  | [optional] 
**post_prob_effect** | **float** |  | [optional] 
**ci_lower_95** | **float** |  | [optional] 
**ci_upper_95** | **float** |  | [optional] 
**significant** | **bool** |  | [optional] 
**neg_log10_pvalue** | **float** |  | [optional] 
**neg_log10_pvalue_adj** | **float** |  | [optional] 
**label** | **str** |  | 
**method** | **str** |  | 
**var_class** | **str** |  | [optional] 
**source** | **str** |  | 
**source_url** | **str** |  | 
**name** | **str** |  | 
**files_filesets** | **str** |  | [optional] 

## Example

```python
from igvf_catalog_client.models.biosamples_from_variants import BiosamplesFromVariants

# TODO update the JSON string below
json = "{}"
# create an instance of BiosamplesFromVariants from a JSON string
biosamples_from_variants_instance = BiosamplesFromVariants.from_json(json)
# print the JSON string representation of the object
print(BiosamplesFromVariants.to_json())

# convert the object into a dict
biosamples_from_variants_dict = biosamples_from_variants_instance.to_dict()
# create an instance of BiosamplesFromVariants from a dict
biosamples_from_variants_from_dict = BiosamplesFromVariants.from_dict(biosamples_from_variants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


