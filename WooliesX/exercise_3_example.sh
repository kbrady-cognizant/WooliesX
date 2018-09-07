curl -X POST --header 'Content-Type: application/json-patch+json' --header 'Accept: application/json' -d '{
  "products": [
    {
      "name": "string",
      "price": 6
    },
    {
      "name": "string",
      "price": 20
    }
  ],
  "specials": [
    {
      "quantities": [
        {
          "name": "string",
          "quantity": 10
        }
      ],
      "total": 10
    },
        {
      "quantities": [
        {
          "name": "string",
          "quantity": 10
        }
      ],
      "total": 200
    }
  ],
  "quantities": [
    {
      "name": "string",
      "quantity": 12
    }
  ]
}' 'https://mf4x0dcc99.execute-api.ap-southeast-2.amazonaws.com/default/trolleyCalculator'