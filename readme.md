# Magic Cheese Shop

## Running Tests

- Navigate to root directory
- Execute `pipenv shell`
- Execute `pytest magic_cheese_shop_test.py`

## Completing Exercise

- Do not alter item.py
- item.py may be extended
- add code to the `execute` function in magic_cheese_shop.py such that the first unit test is passed
- remove the `skip` decorator from the next unit test
- focus on passing as many unit tests as possible

## Excerise Thesis

- The owner of the magic cheese shop needs someone to design an inventory management system that takes into account the specific nature of the items that the magic cheese shop sells.
- The system will be executed at the end of each day.
- Every item will have a string `name`, which can be used to differentiate the item from other items.
- Every item will have an integer `days_until_expiration` which represents the number of days until that item expires.
- Every item will have an integer `quality` which represents the total quality score for that item.
- Special items will have unique behavior that is further defined in the unit tests.

## Considerations

- A candidate is not expected to fully complete the exercise.
- Refactoring and code quality are valued far more than number of tests passed.
- The minutes taken to pass each test can be an important metric to differentiate exceptional candidates.
