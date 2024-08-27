param name string

resource foo 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: name
  location: 'eastus'
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}
