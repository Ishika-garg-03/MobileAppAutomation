Feature: Sign in
  @id:Playstore
  Scenario: signin when playstore launch
    Given Playstore is launched
    When Try to perform login actions
    Then User should be logged in
