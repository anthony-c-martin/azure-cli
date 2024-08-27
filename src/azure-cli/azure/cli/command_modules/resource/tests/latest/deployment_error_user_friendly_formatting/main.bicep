module bar 'bar.bicep' = {
  name: 'bar'
}

module foo 'foo.bicep' = {
  name: 'foo'
  params: {
    name: bar.outputs.name
  }
}
