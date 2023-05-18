Feature: Shopping Journey
  Users with different permissions should be able to
  shop and checkout successfully

  Background: The common step(s) is recorded here
    Given I am on the sauce demo page

  @smoke
  Scenario: A standard user should be able to checkout successfully
    When I insert the standard username
    And I insert the password
    And I click the "login button"
    Then I should see the product list page
    When I add an Item to cart
    And I click the "cart icon"
    Then I should see the item in the cart
    And I logout

  @datatable
  Scenario: A user should be able to checkout successfully
    When I insert the standard username
    And I insert the password
    And I click the "login button"
    Then I should see the following on the product page
      | Items     |
      | Products  |
      | Swag Labs |
    When I add an Item to cart
    And I click the "cart icon"
    Then I should see the item in the cart
    And I logout

  @smoke
  Scenario: A glitch user should be able to checkout successfully
    When I insert the glitch username
    And I insert the password
    And I click the "login button"
    Then I should see the product list page
    When I remove an Item from cart
    And I click the "cart icon"
    Then I should not see the item in the cart
    And I logout

  @regression
  Scenario Outline: User types should be able to login and perform actions
    When I insert the "<username>"
    And I insert the password
    And I click the "login button"
    Then I should see the product list page
    When I "<action>" item
    And I click the "cart icon"
    Then I should see the "<result>"
    And I logout

    Examples:
      | username                | action | result       |
      | standard_user           | add    | item in cart |
      | performance_glitch_user | remove | empty cart   |