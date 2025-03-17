Feature: Search category and add product to cart

  @id:addToCart
  Scenario: Add product to cart
    Given User is signed in on amazon application
    When Try to search category and add product to cart
    Then Product should be added to the cart