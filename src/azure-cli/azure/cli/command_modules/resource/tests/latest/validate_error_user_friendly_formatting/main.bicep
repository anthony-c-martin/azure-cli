resource foo 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: 'foo'
  location: 'eastus'
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}
