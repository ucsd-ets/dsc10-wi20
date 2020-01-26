
test = {
  'name': 'q1_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
	>>> # should be a float
	>>> import numbers
	>>> isinstance(san_diego_free_beaches_with_parking, numbers.Integral)
	True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
