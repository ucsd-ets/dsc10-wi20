test = {
  'name': 'q3_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.mean(left_end) > 75
          True
          >>> np.mean(left_end) < 90
          True
          >>> np.mean(right_end) > 150
          True
          >>> np.mean(right_end) < 170
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
